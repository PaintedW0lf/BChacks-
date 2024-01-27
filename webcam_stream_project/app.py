import http.server
import socketserver

# Choose a port (e.g., 8000)
port = 8000

# Define the handler to use for incoming requests
handler = http.server.SimpleHTTPRequestHandler

# Create a TCP server with the specified port and handler
httpd = socketserver.TCPServer(("", port), handler)

print(f"Serving on port {port}")
print(f"http://localhost:{port}")

# Start the server
httpd.serve_forever()

import cv2
camera = cv2.VideoCapture(0)  # Use 0 for the default camera, you can change it if you have multiple cameras.

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')