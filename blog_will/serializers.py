from .models import Blog_will
from rest_framework.serializers import ModelSerializer

class Blog_willSerializer(ModelSerializer):
  class Meta:
    model = Blog_will
    fields = ('id', 'name','purchaser','description')