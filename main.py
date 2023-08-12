# import cv2

# image = cv2.imread("input_image.jpg")
# # face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# for (x, y, w, h) in faces:
#     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# cv2.imshow('Face Detection', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
