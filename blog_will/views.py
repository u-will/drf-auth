from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Blog_will
from .serializers import Blog_willSerializer
from .permission import IsPurchaserOrReadOnly

class Blog_willListCreate(ListCreateAPIView):
    queryset = Blog_will.objects.all()
    serializer_class = Blog_willSerializer

class Blog_willRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):

  queryset = Blog_will.objects.all()
  serializer_class = Blog_willSerializer

  permission_classes = (IsPurchaserOrReadOnly,)