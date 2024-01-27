# import http.server
# import socketserver

# # Choose a port (e.g., 8000)
# port = 8000

# # Define the handler to use for incoming requests
# handler = http.server.SimpleHTTPRequestHandler

# # Create a TCP server with the specified port and handler
# httpd = socketserver.TCPServer(("", port), handler)

# print(f"Serving on port {port}")
# print(f"http://localhost:{port}")

# # Start the server
# httpd.serve_forever()

# import cv2
# camera = cv2.VideoCapture(0)  # Use 0 for the default camera, you can change it if you have multiple cameras.

# def generate_frames():
#     while True:
#         success, frame = camera.read()
#         if not success:
#             break
#         else:
#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# import http.server
# import socketserver
# import cv2
# import threading
# from io import BytesIO
# from PIL import Image

# class VideoStreamHandler(http.server.BaseHTTPRequestHandler):
#     def do_GET(self):
#         if self.path == '/video_feed.jpg':
#             self.send_response(200)
#             self.send_header('Content-type', 'image/jpeg')
#             self.end_headers()

#             # Read a frame from the webcam
#             success, frame = camera.read()
#             if success:
#                 # Convert the OpenCV frame to JPEG format
#                 _, buffer = cv2.imencode('.jpg', frame)
#                 img_bytes = BytesIO(buffer).getvalue()
#                 self.wfile.write(img_bytes)
#             else:
#                 self.send_error(500, 'Error reading frame from the camera')
#         elif self.path == '/':
#             self.send_response(200)
#             self.send_header('Content-type', 'index/html')
#             self.end_headers()

#             # Read the HTML file and send it as the response
#             with open('index.html', 'rb') as file:
#                 self.wfile.write(file.read())
#         else:
#             self.send_error(404, 'File not found')

# def start_server():
#     with socketserver.TCPServer(("", 8000), VideoStreamHandler) as httpd:
#         print("Serving on port 8000")
#         httpd.serve_forever()

# # Start the webcam
# camera = cv2.VideoCapture(0)

# # Start the HTTP server in a separate thread
# server_thread = threading.Thread(target=start_server)
# server_thread.start()

# # Open the default web browser
# import webbrowser
# webbrowser.open('http://localhost:8000')



#Import necessary libraries
from flask import Flask, render_template, Response
import cv2
#Initialize the Flask app
app = Flask(__name__)

camera = cv2.VideoCapture(0)
'''
for ip camera use - rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' 
for local webcam use cv2.VideoCapture(0)
'''

def gen_frames():  
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
            

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)


