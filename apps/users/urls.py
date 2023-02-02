from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    path('registration/', views.UserCreate.as_view()),
    path('login/', views.UserLoginView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('save-contact/<str:pk>', views.UserSaveContact.as_view()),
    path('user-update/<str:pk>', views.UserRetrieveUpdateAPIView.as_view()),
    path('user-retrieve/<str:pk>', views.UserRetrieveAPIView.as_view()),

    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    path('save-contact/counts/', views.SaveContactCountListAPiView.as_view()),
    path('save-contact/count/', views.SaveContactCountCreateAPIView.as_view()),
    path('save-contact/count/<str:pk>/', views.SaveContactCountRetrieveAPIView.as_view()),

]
