import os
import cv2
import numpy as np

def collect_dataset(data_path):
    face_images = []
    labels = []
    label_map = {}

    for label, name in enumerate(os.listdir(data_path)):
        label_map[label] = name
        person_dir = os.path.join(data_path, name)
        for image_file in os.listdir(person_dir):
            image_path = os.path.join(person_dir, image_file)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            face_images.append(image)
            labels.append(label)

    return face_images, labels, label_map

def train_lbph_model(data_path, model_save_path):
    face_images, labels, label_map = collect_dataset(data_path)

    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.train(face_images, np.array(labels))

    face_recognizer.save(model_save_path)

    print("Training completed. Model saved to:", model_save_path)

if __name__ == "__main__":
    data_path = "C:\project\jarvis\samples"  # Replace with the path to your dataset directory
    model_save_path = "trained_model2.yml"  # Replace with the desired path to save the trained model

    train_lbph_model(data_path, model_save_path)