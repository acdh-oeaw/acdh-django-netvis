from django.urls import path

from . import views

urlpatterns = [
    path('my-text/<int:pk>/', views.MyTextDetailViewSimple.as_view(), name='mytext_simple'),
    path('m/<int:pk>/', views.MyTextDetailView.as_view(), name='mytext'),
    path('', views.IndexView.as_view(), name="index")
]
