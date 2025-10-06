from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from .views import BookViewSet
from .views import AuthorAPIView, BookAPIView

router = DefaultRouter()
#router.register(r'books', BookViewSet)
#router.register(r'books', BookAPIView)

urlpatterns = [
    path('authors/', AuthorAPIView.as_view()),
    path('books/', BookAPIView.as_view()),
    path('', include(router.urls)),
]