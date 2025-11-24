import grpc
from concurrent import futures
import time
from prometheus_client import start_http_server, Counter

import library_pb2
import library_pb2_grpc

# Prometheus metric
REQUEST_COUNTER = Counter('grpc_requests_total', 'Total number of gRPC requests')

class LibraryService(library_pb2_grpc.LibraryServiceServicer):

    def GetBook(self, request, context):
        REQUEST_COUNTER.inc()
        # Create a mock book response
        book = library_pb2.Book(
            id=request.id,
            title=f"Book #{request.id}",
            author="Author X",
            isbn="1234567890",
            publication_year=2024,
            genre="Fiction"
        )
        return library_pb2.GetBookResponse(book=book)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    library_pb2_grpc.add_LibraryServiceServicer_to_server(LibraryService(), server)
    server.add_insecure_port('[::]:50051')

    start_http_server(8000)
    print("✅ Server running on port 50051 (Prometheus on :8000)")
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        print("Server stopped.")
        server.stop(0)

if __name__ == '__main__':
    serve()
