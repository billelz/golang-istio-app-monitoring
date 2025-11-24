import grpc
import library_pb2
import library_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = library_pb2_grpc.LibraryServiceStub(channel)

    # Send a GetBookRequest instead of BookRequest
    response = stub.GetBook(library_pb2.GetBookRequest(id=1))

    # Response contains a "book" field
    book = response.book
    print(f"📘 Book received:")
    print(f"   ID: {book.id}")
    print(f"   Title: {book.title}")
    print(f"   Author: {book.author}")
    print(f"   ISBN: {book.isbn}")
    print(f"   Year: {book.publication_year}")
    print(f"   Genre: {book.genre}")

if __name__ == '__main__':
    run()
