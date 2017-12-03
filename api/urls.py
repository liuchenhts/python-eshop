from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from .views import ProductViewSet


app_name = 'api'

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    url(r'^docs/',  get_swagger_view()),
]
urlpatterns += router.urls
