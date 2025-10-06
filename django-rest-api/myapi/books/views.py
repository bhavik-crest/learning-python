#from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

# class BookViewSet(viewsets.ModelViewSet):
    # Example viewset for managing books
    # queryset = Book.objects.all()
    # serializer_class = BookSerializer

# Example without viewset
class AuthorAPIView(APIView):
    def get(self, request):
            authors = Author.objects.all()
            serializer = AuthorSerializer(authors, many=True)
            return Response(serializer.data)

class BookAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)