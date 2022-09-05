from . import views
from django.urls import path

urlpatterns = [
   path("", views.DJList.as_view(), name="list"),
   path('musicdetail/<int:pk>/', views.DjDetailView.as_view(), name='dj_detail'),
]
