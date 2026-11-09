import dlib
import face_recognition_models
from sklearn.svm import SVC
import numpy as np
import streamlit as st
from src.database.db import get_all_students

@st.cache_resource
def load_dlib_models():
    # It detects al the face 
    detector = dlib.get_frontal_face_detector()

    sp = dlib.shape_predictor( # Predictor needs a face recognition model
        face_recognition_models.pose_predictor_model_location()
    )

    facerec = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )
    return detector , sp , facerec

def get_face_embeddings(image_np):
    detector , sp , facerec = load_dlib_models()
    faces = detector(image_np , 1)
    encodings = []

    for face in faces:
        shape = sp(image_np,face)
        face_descriptor = facerec.compute_face_detector(image_np,shape,1)

        encodings.append(np.array(face_descriptor))
    return encodings

@st.cache_resource
def get_trained_model():
    X = []
    Y = []
    student_db = get_all_students()

    if not student_db:
        return None

    for student in student_db:
        embeddings = student.get("face_login")
        if embeddings:
            X.append(np.array(embeddings))
            Y.append(student.get("student_id"))

    if len(X) == 0:
        return 0

    clf = SVC(kernel="linear",probability=True,class_weight="balanced")

    try:
        clf.fit(X,Y)
    except ValueError:
        pass
        return{'clf':clf,'X':X,'Y':Y}

def trained_classifier():
    st.cache_resource.clear()
    model_data = get_trained_model()
    return bool(model_data)

def predict_attendence(class_image_np):
    embeddings = get_face_embeddings(class_image_np)

    detected_students = {}

    model_data = get_trained_model()

    if not model_data:
        return {} ,[] ,len(embeddings)
    clf = model_data["clf"]
    X_train = model_data["X"]
    Y_train = model_data["Y"]

    all_students = sorted(list(set(Y_train)))

    for embedding in embeddings:
        if len(all_students) >= 2:
            predicted_id = int(clf.predict([embedding])[0])
        else:
            predicted_id = int(all_students[0])

        student_embedding = X_train[Y_train.index(predicted_id)]

        best_match_score = np.linalg.norm(student_embedding - embedding)

        resemble_threshold = 0.6
        if  best_match_score <= resemble_threshold:
            detected_students[predicted_id]=True
    return detected_students, all_students , len(embedding)

