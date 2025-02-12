# gRPC Demo
gRPC is a modern open-source remote procedure call (RPC) framework developed by Google that enables communication between applications in a fast, efficient, and scalable way. It uses Protocol Buffers (protobufs) for data serialization, which are more efficient than traditional text-based formats like JSON or XML. gRPC is widely used for microservices communication and offers a range of features, such as authentication, load balancing, and bidirectional streaming.

This is very simple Greeter gRPC service. Feel free to clone and explore :)

### Set UP
1. Create Virtual Env: `python3 -m venv myenv`
2. Activate it: source `myenv/bin/activate`
3. Install grpc libraries: `pip install grpcio grpcio-tools`

### Generate Code from .proto file:
```python
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. greeter.proto
```

### Finally Run Server and Client
```python
python3 greeter_server.py
python3 greeter_client.py
```