from django.urls import path

from . import views

urlpatterns = [
    # Email
    path('email/', views.UserEmailListCreateAPIView.as_view()),
    path('email/<str:pk>', views.UserEmailRetrieveUpdateDestroyAPIView.as_view()),

    # Phone
    path('phone/', views.UserPhoneListCreateAPIView.as_view()),
    path('phone/<str:pk>', views.UserPhoneRetrieveUpdateDestroyAPIView.as_view()),

    # back-account
    path('bank-account/', views.UserBankAccountListCreateAPIView.as_view()),
    path('bank-account/<str:pk>', views.UserBankAccountRetrieveUpdateDestroyAPIView.as_view()),

    # back-cart
    path('bank-cart/', views.UserBankCartListCreateAPIView.as_view()),
    path('bank-cart/<str:pk>', views.UserBankCartRetrieveUpdateDestroyAPIView.as_view()),

    # User product
    path('product/', views.UserProductListCreateAPIView.as_view()),
    path('product/<str:pk>', views.UserProductRetrieveUpdateDestroyAPIView.as_view()),

    # User image
    path('image/', views.UserImageListCreateAPIView.as_view()),
    path('image/<str:pk>', views.UserImageRetrieveUpdateDestroyAPIView.as_view()),

    # User video
    path('video/', views.UserVideoListCreateAPIView.as_view()),
    path('video/<str:pk>', views.UserVideoRetrieveUpdateDestroyAPIView.as_view()),

    path('social/<str:pk>', views.UserSocialRetrieveUpdateDestroyAPIView.as_view()),
    path('social/', views.UserSocialListCreateAPIView.as_view()),

    path('qr-code/<str:pk>', views.UserQRCodeRetrieve.as_view()),

    path('social-category/', views.SocialCategoryListApiView.as_view()),
    path('social-category/<str:pk>', views.SocialCategoryRetrieveApiView.as_view()),

    # messanger category
    path('messanger-category/', views.MessangerCategoryListApiView.as_view()),
    path('messanger-category/<str:pk>', views.MessangerCategoryRetrieveApiView.as_view()),

    path('messanger/<str:pk>', views.UserMessangerRetrieveUpdateDestroyAPIView.as_view()),
    path('messanger/', views.UserMessangerListCreateAPIView.as_view()),

]
