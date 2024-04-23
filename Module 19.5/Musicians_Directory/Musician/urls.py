from django.urls import path,include
from . import views

urlpatterns = [
    path('add/',views.AddMusicianCreateView.as_view(),name="add_musician"),
    path('edit_musician/<int:id>',views.EditmusicianView.as_view(),name='edit_musician')
]