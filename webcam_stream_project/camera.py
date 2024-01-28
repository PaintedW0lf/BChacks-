# import cv2

# class VideoCamera(object):
#     def __init__(self):
#         self.video = cv2.VideoCapture(0)
#         self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#     def __del__(self):
#         self.video.release()

#     def get_frame(self):
#         ret, frame = self.video.read()

#         # Convert the frame to grayscale for face detection
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#         # Detect faces in the frame
#         faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

#         # Draw rectangles around the detected faces
#         for (x, y, w, h) in faces:
#             cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

#         # DO WHAT YOU WANT WITH TENSORFLOW / KERAS AND OPENCV

#         ret, jpeg = cv2.imencode('.jpg', frame)

#         return jpeg.tobytes()
import cv2

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def __del__(self):
        self.video.release()

    def detect_faces(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        return frame

    def get_frame(self):
        success, frame = self.video.read()
        
        if not success:
            return None, []

        # Perform face detection
        frame_with_faces = self.detect_faces(frame)

        # Encode the frame as JPEG
        ret, jpeg = cv2.imencode('.jpg', frame_with_faces)

        # Convert the frame to bytes
        frame_bytes = jpeg.tobytes()

        return frame_bytes, []
