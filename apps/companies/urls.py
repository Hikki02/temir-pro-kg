from django.urls import path

from . import views

urlpatterns = [
    path('company/', views.UserCompanyCreateListAPIView.as_view()),
    path('company/<str:pk>', views.UserCompanyRetrieveUpdateDestroyAPIView.as_view()),
]
