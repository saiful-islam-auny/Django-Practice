from django.urls import path,include
from . import views

urlpatterns = [
    path('add/',views.add_musician,name="add_musician"),
    path('edit_musician/<int:id>',views.edit_musician,name='edit_musician')
]