from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('create_entry/',views.create_entry,name='create_entry'),
    path('read_entry/',views.read_entry,name='read_entry'),
    path('update_entry/<int:id>/',views.update_entry,name='update_entry'),
    path('delete_entry/<int:id>/',views.delete_entry,name='delete_entry'),
    ]