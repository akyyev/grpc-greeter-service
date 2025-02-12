import grpc
import greeter_pb2
import greeter_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')  # Connect to the server
    stub = greeter_pb2_grpc.GreeterStub(channel)
    
    # Make a request to the server
    response = stub.SayHello(greeter_pb2.HelloRequest(name='John Doe'))
    
    # Print the server's response
    print(f"Server says: {response.message}")

if __name__ == '__main__':
    run()
