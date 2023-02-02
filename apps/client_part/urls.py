from django.urls import path

from .views import social_views, companies_views

urlpatterns = [
    # Email
    path('email/', social_views.UserEmailListAPIView.as_view()),
    path('email/<str:pk>', social_views.UserEmailRetrieveAPIView.as_view()),

    # Phone
    path('phone/', social_views.UserPhoneListAPIView.as_view()),
    path('phone/<str:pk>', social_views.UserPhoneRetrieveAPIView.as_view()),

    # back-account
    path('bank-account/', social_views.UserBankAccountListAPIView.as_view()),
    path('bank-account/<str:pk>', social_views.UserBankAccountRetrieveAPIView.as_view()),

    # back-cart
    path('bank-cart/', social_views.UserBankCartListAPIView.as_view()),
    path('bank-cart/<str:pk>', social_views.UserBankCartRetrieveAPIView.as_view()),

    # User product
    path('product/', social_views.UserProductListAPIView.as_view()),
    path('product/<str:pk>', social_views.UserProductRetrieveAPIView.as_view()),

    # User image
    path('image/', social_views.UserImageListAPIView.as_view()),
    path('image/<str:pk>', social_views.UserImageRetrieveAPIView.as_view()),

    # User video
    path('video/', social_views.UserVideoListAPIView.as_view()),
    path('video/<str:pk', social_views.UserVideoRetrieveAPIView.as_view()),

    # User social
    path('social/', social_views.UserSocialListAPIView.as_view()),
    path('social/<str:pk>', social_views.UserSocialRetrieveAPIView.as_view()),

    # User messanger
    path('messanger/', social_views.UserMessangerListAPIView.as_view()),
    path('social/<str:pk>', social_views.UserMessangerRetrieveAPIView.as_view()),

    # - - - - - - - - - - - - - - - - - - - COMPANIES VIEWS - - - - - - - - - - - - - - - - -

    path('company/', companies_views.UserCompanyListAPIView.as_view()),

    path('company/<str:pk>', companies_views.UserCompanyRetrieveAPIView.as_view()),

    path('qr-code/<str:pk>', social_views.UserQRCodeRetrieve.as_view()),
]
