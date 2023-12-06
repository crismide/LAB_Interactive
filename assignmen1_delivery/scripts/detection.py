import csv
import cv2
from feat import Detector
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import os
import numpy as np

images_folder = '../processed/images'
detector = Detector()
emotion_labels = ["Anger", "Disgust", "Fear", "Happiness", "Sadness", "Surprise", "Neutral"]

csv_file_path = '../processed/aus.csv'

with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    header_row = ['file', 'FaceIndex', 'AU01', 'AU02','AU03', 'AU04', 'AU05', 'AU06', 'AU07', 'AU09', 'AU10', 'AU12', 'AU14', 'AU15', 'AU17', 'AU20', 'AU23', 'AU24', 'AU25', 'AU26', 'AU28', 'AU43']
    csv_writer.writerow(header_row)

    for filename in os.listdir(images_folder):
        file_path = os.path.join(images_folder, filename)
        frame = cv2.imread(file_path)

        detected_faces = detector.detect_faces(frame)
        detected_landmarks = detector.detect_landmarks(frame, detected_faces)
        detected_emotions = detector.detect_emotions(frame, detected_faces, detected_landmarks)
        au_activations = detector.detect_aus(frame, detected_landmarks)

        num_faces = len(detected_emotions[0])

        for i in range(num_faces):
            face = detected_faces[0][i]
            emotions = detected_emotions[0][i]
            au_activation = au_activations[0][i]

            # adding line in csv
            row_data = [filename, i + 1] + list(au_activation)
            csv_writer.writerow(row_data)

            # calculating emotions
            max_emotion_index = np.argmax(emotions)
            max_emotion_label = emotion_labels[max_emotion_index]

            # calculating face for the square
            x1 = face[0]
            y1 = face[1]
            x2 = face[2]
            y2 = face[3]
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, max_emotion_label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        base_filename = os.path.splitext(os.path.basename(file_path))[0]
        path = images_folder+"/"+base_filename+".jpg"
        cv2.imwrite(path,frame)