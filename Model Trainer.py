# import cv2
# import numpy as np
# import os

# # Load the Haar Cascade face classifier
# face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# # Load the training data from the 'samples' directory
# folder_path = 'samples'
# training_data = []
# labels = []

# for filename in os.listdir(folder_path):
#     if filename.endswith('.jpg'):
#         img_path = os.path.join(folder_path, filename)
#         img = cv2.imread(img_path)
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         faces = face_classifier.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
#         for (x, y, w, h) in faces:
#             face_roi = gray[y:y + h, x:x + w]
#             training_data.append(face_roi)
#             labels.append(int(filename.split('.')[1]))

# # Train the model using the training data and labels
# face_recognizer = cv2.face.LBPHFaceRecognizer_create()
# face_recognizer.train(training_data, np.array(labels))

# # Save the trained model to a file
# face_recognizer.save('trained_model.yml')

# print('Model trained and saved successfully.')



import cv2
import numpy as np
from PIL import Image #pillow package
import os

path = 'samples' # Path for samples already taken

recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#Haar Cascade classifier is an effective object detection approach


def Images_And_Labels(path): # function to fetch the images and labels

    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []

    for imagePath in imagePaths: # to iterate particular image path

        gray_img = Image.open(imagePath).convert('L') # convert it to grayscale
        img_arr = np.array(gray_img,'uint8') #creating an array

        id = int(os.path.splitext(os.path.basename(imagePath))[0])
        faces = detector.detectMultiScale(img_arr)

        for (x,y,w,h) in faces:
            faceSamples.append(img_arr[y:y+h,x:x+w])
            ids.append(id)

    return faceSamples,ids

print ("Training faces. It will take a few seconds. Wait ...")

faces,ids = Images_And_Labels(path)
recognizer.train(faces, np.array(ids))

recognizer.write('trainer/trainer.yml')  # Save the trained model as trainer.yml

print("Model trained, Now we can recognize your face.")