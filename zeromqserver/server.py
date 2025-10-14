import zmq
import signal
import sys

def signal_handler(sig, frame):
    print("\nShutting down server...")
    socket.close()
    context.term()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:2222")

socket.setsockopt(zmq.RCVTIMEO, 1000)

print("Server is running on port 2222...")

while True:
    try:
        message = socket.recv_string()
        print(f"Received from client: {message}")

        socket.send_string("Hello from server!")
    except zmq.Again:
        continue
    except zmq.ZMQError as e:
        print(f"ZMQ Error: {e}")
        break
