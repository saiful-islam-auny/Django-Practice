from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:roll>', views.delete_student, name="delete_student"),
    path('add/', views.add_student, name="add_student"),
    path('djangoform/', views.example_form_view, name='django_form'), 

]
