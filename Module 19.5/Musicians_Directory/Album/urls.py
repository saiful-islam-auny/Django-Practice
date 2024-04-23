from django.urls import path,include
from . import views

urlpatterns = [
    path('add/',views.AddAlbumCreateView.as_view(),name="add_album"),
    # path('edit/<int:id>',views.edit_album,name='edit_album'),
    path('edit/<int:id>',views.EditAlbumView.as_view(),name='edit_album'),
    
    # path('delete/<int:id>', views.delete_album, name=' delete_album'),
    path('delete/<int:id>', views.DeleteAlbumView.as_view(), name=' delete_album'),
]