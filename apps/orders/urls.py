from django.urls import path
from . import views

from rest_framework.routers import SimpleRouter

urlpatterns = [
    path('cart/', views.OrderItemView.as_view(), name="cart"),
    path('cart/<int:pk>/', views.OrderItmeRetrieve.as_view()),
    path('cart/delete/<int:pk>/', views.OrderItemDelView.as_view()),
    path('cart/add_one/<int:pk>/', views.OrderItemAddOneView.as_view()),
    path('cart/reduce_one/<int:pk>/', views.OrderItemReduceOneView.as_view()),
    path('cart/post/', views.OrderItemPostView.as_view(), name='Post метод для корзины')
]

router = SimpleRouter()
router.register('cart/add', views.OrderItemAddView, basename='order')

urlpatterns += router.urls
