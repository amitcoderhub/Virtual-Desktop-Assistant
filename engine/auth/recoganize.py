# from sys import flags
# import time
# import cv2
# import pyautogui as p


# def AuthenticateFace():

#     flag = ""
#     # Local Binary Patterns Histograms
#     recognizer = cv2.face.LBPHFaceRecognizer_create()

#     recognizer.read('engine\\auth\\trainer\\trainer.yml')  # load trained model
#     cascadePath = "engine\\auth\\haarcascade_frontalface_default .xml"
#     # initializing haar cascade for object detection approach
#     faceCascade = cv2.CascadeClassifier(cascadePath)

#     font = cv2.FONT_HERSHEY_SIMPLEX  # denotes the font type


#     id = 2  # number of persons you want to Recognize


#     names = ['', 'Amit', 'sumit']  # names, leave first empty bcz counter starts from 0


#     cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # cv2.CAP_DSHOW to remove warning
#     cam.set(3, 640)  # set video FrameWidht
#     cam.set(4, 480)  # set video FrameHeight

#     # Define min window size to be recognized as a face
#     minW = 0.1*cam.get(3)
#     minH = 0.1*cam.get(4)

#     # flag = True

#     while True:

#         ret, img = cam.read()  # read the frames using the above created object

#         # The function converts an input image from one color space to another
#         converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#         faces = faceCascade.detectMultiScale(
#             converted_image,
#             scaleFactor=1.2,
#             minNeighbors=5,
#             minSize=(int(minW), int(minH)),
#         )

#         for(x, y, w, h) in faces:

#             # used to draw a rectangle on any image
#             cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

#             # to predict on every single image
#             id, accuracy = recognizer.predict(converted_image[y:y+h, x:x+w])

#             # Check if accuracy is less them 100 ==> "0" is perfect match
#             if (accuracy < 100):
#                 id = names[id]
#                 accuracy = "  {0}%".format(round(100 - accuracy))
#                 flag = 1
#             else:
#                 id = "unknown"
#                 accuracy = "  {0}%".format(round(100 - accuracy))
#                 flag = 0

#             cv2.putText(img, str(id), (x+5, y-5), font, 1, (255, 255, 255), 2)
#             cv2.putText(img, str(accuracy), (x+5, y+h-5),
#                         font, 1, (255, 255, 0), 1)

#         cv2.imshow('camera', img)

#         k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
#         if k == 27:
#             break
#         if flag == 1:
#             break
            

#     # Do a bit of cleanup
    
#     cam.release()
#     cv2.destroyAllWindows()
#     return flag
# AuthenticateFace()






import cv2
import pyautogui as p

def AuthenticateFace():
    flag = ""
    
    # Initialize the LBPH face recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    # Load the trained model
    recognizer.read('engine\\auth\\trainer\\trainer.yml')
    
    # Path to the Haar Cascade file
    cascadePath = "engine\\auth\\haarcascade_frontalface_default .xml"
    
    # Initialize Haar Cascade for face detection
    faceCascade = cv2.CascadeClassifier(cascadePath)

    font = cv2.FONT_HERSHEY_SIMPLEX  # Font type for text

    # Number of persons you want to recognize (not really used here)
    id = 2  

    # Names corresponding to IDs (leave the first one empty because index starts at 0)
    names = ['', 'Amit', 'Sumit']

    # Initialize webcam
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Use cv2.CAP_DSHOW to suppress warnings
    cam.set(3, 640)  # Set video frame width
    cam.set(4, 480)  # Set video frame height

    # Define min window size to be recognized as a face
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    while True:
        ret, img = cam.read()  # Read the frames from the webcam

        # Convert the frame to grayscale
        converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = faceCascade.detectMultiScale(
            converted_image,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )

        for (x, y, w, h) in faces:
            # Draw a rectangle around the detected face
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Predict the ID of the face
            id, accuracy = recognizer.predict(converted_image[y:y+h, x:x+w])

            # Check if the accuracy is acceptable
            if accuracy < 100:
                id = names[id]
                accuracy_text = "  {0}%".format(round(100 - accuracy))
                flag = 1
            else:
                id = "unknown"
                accuracy_text = "  {0}%".format(round(100 - accuracy))
                flag = 0

            # Display the ID and accuracy on the frame
            cv2.putText(img, str(id), (x+5, y-5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(accuracy_text), (x+5, y+h-5),
                        font, 1, (255, 255, 0), 1)

        # Show the frame with the drawings
        cv2.imshow('camera', img)

        # Exit on 'ESC' key press
        k = cv2.waitKey(10) & 0xff
        if k == 27:
            break
        if flag == 1:
            break

    # Cleanup resources
    cam.release()
    cv2.destroyAllWindows()
    return flag

# Call the function
# AuthenticateFace()


