from django.urls import path
from . import views
urlpatterns = [
    path('', views.getroute),
    path('notes/', views.getnotes),
    path('create/', views.createnote),
    path('notes/<str:pk>', views.getnote),
    path('notes/<str:pk>/edit', views.editnote),
    path('notes/<str:pk>/delete', views.deletenote)

]
