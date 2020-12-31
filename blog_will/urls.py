from django.urls import path
from .views import Blog_willListCreate, Blog_willRetrieveUpdateDestroy

urlpatterns = [
  path('', Blog_willListCreate.as_view(), name='blog_will_list_create'),
  path('<int:pk>/', Blog_willRetrieveUpdateDestroy.as_view(), name='blog_will_retrieve_update_destroy'),
  
]