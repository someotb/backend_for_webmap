import zmq
import signal
import sys
import json

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

        try:
            data = json.loads(message)
            print(json.dumps(data, indent=2))
        except json.JSONDecodeError:
            print("Receive NOT JSON")

        socket.send_string("Data receice OK")

    except zmq.Again:
        continue
    except zmq.ZMQError as e:
        print(f"ZMQ Error: {e}")
        break
