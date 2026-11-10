
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

    all_students = []

    if model_data is None:

        return detected_students, all_students, len(embeddings)

    clf = model_data["clf"]

    X_train = model_data["X"]

    Y_train = model_data["Y"]

    all_students = list(np.unique(Y_train))

    for embedding in embeddings:

        embedding = np.asarray(embedding, dtype=np.float64)

        # Find nearest registered face
        distances = np.linalg.norm(
            X_train - embedding,
            axis=1
        )

        best_index = int(np.argmin(distances))

        best_match_score = float(distances[best_index])

        predicted_id = Y_train[best_index]

        # If multiple students are registered,
        # also use the SVM prediction
        if clf is not None:

            svm_prediction = clf.predict([embedding])[0]

            if svm_prediction == predicted_id:
                predicted_id = svm_prediction

        # Initial threshold; calibrate using your own validation images
        similarity_threshold = 0.6

        if best_match_score <= similarity_threshold:

            detected_students[predicted_id] = True

    return detected_students, all_students, len(embeddings)
