from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('product', views.ProductView)
router.register('model', views.ModelView)
router.register('pre_product', views.PreProductView)

urlpatterns = [
    path('', include(router.urls), name='product'),
    path('', include(router.urls), name='model'),
    path('', include(router.urls), name='pre_product'),
]
