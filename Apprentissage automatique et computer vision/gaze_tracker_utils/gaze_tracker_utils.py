import numpy as np

def compte_actual_eye_gaze(landmarks, frame_width,frame_height):

    iris = landmarks[468]
    externe = landmarks[ 33]
    interne = landmarks[133]

    left_iris_center = np.array([iris.x *  frame_width, iris.y * frame_height])

    left_iris_externe = np.array([externe.x* frame_width,externe.y*frame_height])
    left_iris_interne = np.array([interne.x* frame_width,interne.y*frame_height])

    eye_axis= left_iris_interne - left_iris_externe
    eye_center = (left_iris_interne+left_iris_externe)/2
    gaze_offset = left_iris_center - eye_center

    norm =np.linalg.norm(eye_axis)
    gase_vec = gaze_offset/norm if norm > 1e-6 else np.zeros_like(gaze_offset)

    return eye_center, gase_vec
