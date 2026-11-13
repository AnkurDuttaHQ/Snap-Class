
import dlib
import face_recognition_models
from sklearn.svm import SVC
import numpy as np
import streamlit as st

from src.database.db import get_all_students


# --------------------------------
# Load Dlib Models
# --------------------------------

@st.cache_resource
def load_dlib_models():

    detector = dlib.get_frontal_face_detector()

    sp = dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location()
    )

    facerec = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )

    return detector, sp, facerec


# --------------------------------
# Generate Face Embeddings
# --------------------------------

def get_face_embeddings(image_np):

    detector, sp, facerec = load_dlib_models()

    # Ensure correct image format
    image_np = np.ascontiguousarray(image_np, dtype=np.uint8)

    faces = detector(image_np, 1)

    encodings = []

    for face in faces:

        shape = sp(image_np, face)

        face_descriptor = facerec.compute_face_descriptor(
            image_np,
            shape,
            1
        )

        encodings.append(np.array(face_descriptor, dtype=np.float64))

    return encodings


# --------------------------------
# Train SVM Classifier
# --------------------------------

@st.cache_resource
def get_trained_model():

    X = []
    Y = []

    student_db = get_all_students()

    if not student_db:
        return None

    for student in student_db:

        embeddings = student.get("face_login")

        if embeddings is None:
            continue

        embedding = np.asarray(embeddings, dtype=np.float64)

        if embedding.shape != (128,):
            continue

        student_id = student.get("student_id")

        if student_id is None:
            continue

        X.append(embedding)
        Y.append(student_id)

    if len(X) == 0:
        return None

    X = np.asarray(X)
    Y = np.asarray(Y)

    clf = None

    # SVM requires at least two different classes
    if len(np.unique(Y)) >= 2:

        clf = SVC(
            kernel="linear",
            probability=True,
            class_weight="balanced"
        )

        clf.fit(X, Y)

    return {
        "clf": clf,
        "X": X,
        "Y": Y
    }


# --------------------------------
# Refresh Classifier
# --------------------------------

def trained_classifier():

    get_trained_model.clear()

    model_data = get_trained_model()

    return model_data is not None


# --------------------------------
# Predict Attendance
# --------------------------------

def predict_attendence(class_image_np):

    embeddings = get_face_embeddings(class_image_np)

    detected_students = {}

    model_data = get_trained_model()

    if model_data is None:
        return detected_students, [], len(embeddings)

    X_train = model_data["X"]
    Y_train = model_data["Y"]

    all_students = list(np.unique(Y_train))

    # Initial conservative threshold.
    # Calibrate using genuine and impostor face images.
    similarity_threshold = 0.45

    # Minimum distance difference between two different identities.
    ambiguity_margin = 0.05

    for embedding in embeddings:

        embedding = np.asarray(
            embedding,
            dtype=np.float64
        )

        distances = np.linalg.norm(
            X_train - embedding,
            axis=1
        )

        # Best match
        best_index = int(np.argmin(distances))
        best_match_score = float(distances[best_index])

        predicted_id = Y_train[best_index]

        # Reject if the closest face is too different
        if best_match_score > similarity_threshold:
            print("Face rejected. Distance:", best_match_score)
            continue

        # Find the closest match belonging to another student
        other_student_distances = distances[
            Y_train != predicted_id
        ]

        if len(other_student_distances) > 0:

            second_best_score = float(
                np.min(other_student_distances)
            )

            # Reject ambiguous identity matches
            if second_best_score - best_match_score < ambiguity_margin:
                print("Ambiguous face match. Rejected.")
                continue

        detected_students[predicted_id] = True

        print("Face accepted:", predicted_id)
        print("Distance:", best_match_score)

    return detected_students, all_students, len(embeddings)
