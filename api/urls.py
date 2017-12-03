from django.conf.urls import url
from rest_framework import routers
from .views import ProductViewSet


app_name = 'api'
router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
urlpatterns = router.urls
