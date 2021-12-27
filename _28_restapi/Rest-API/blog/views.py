from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)

from .models import Blog
from .serializers import BlogSerializer


class PostView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class SinglePostView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
