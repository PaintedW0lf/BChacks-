# import base64
# import cv2

# class VideoCamera(object):
#     def __init__(self):
#         self.video = cv2.VideoCapture(0)

#         # Load YOLO model
#         self.net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
#         with open("yolov3.txt", "r") as f:
#             self.classes = f.read().strip().split('\n')

#     def __del__(self):
#         self.video.release()

#     def yolo_face_detection(self, frame):
#         height, width, _ = frame.shape
#         blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
#         self.net.setInput(blob)
#         outs = self.net.forward(self.net.getUnconnectedOutLayersNames())

#         class_ids = []
#         confidences = []
#         boxes = []

#         for out in outs:
#             for detection in out:
#                 scores = detection[5:]
#                 class_id = np.argmax(scores)
#                 confidence = scores[class_id]
#                 if confidence > 0.5 and class_id == 0:  # Assuming class_id 0 is a person
#                     center_x = int(detection[0] * width)
#                     center_y = int(detection[1] * height)
#                     w = int(detection[2] * width)
#                     h = int(detection[3] * height)
#                     x = int(center_x - w / 2)
#                     y = int(center_y - h / 2)

#                     class_ids.append(class_id)
#                     confidences.append(float(confidence))
#                     boxes.append([x, y, w, h])

#         # Perform non-maximum suppression
#         indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

#         detected_faces = []
#         for i in indices:
#             i = i[0]
#             x, y, w, h = boxes[i]
#             face_roi = frame[y:y+h, x:x+w]
#             ret, jpeg = cv2.imencode('.jpg', face_roi)
#             face_url = 'data:image/jpeg;base64,' + base64.b64encode(jpeg.tobytes()).decode('utf-8')
#             detected_faces.append(face_url)

#             # Draw a rectangle around the detected face
#             cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

#         return frame, detected_faces

#     def get_frame(self):
#         ret, frame = self.video.read()

#         # Perform YOLO face detection
#         frame, detected_faces = self.yolo_face_detection(frame)

#         ret, jpeg = cv2.imencode('.jpg', frame)

#         return jpeg.tobytes(), detected_faces
