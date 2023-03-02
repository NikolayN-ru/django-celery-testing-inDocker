from django.contrib import admin
from django.urls import path
from rest_framework import routers
from services.views import SubscriptionView

urlpatterns = [
    path('admin/', admin.site.urls),
]

router = routers.DefaultRouter()
router.register(r'api/subscriptions', SubscriptionView)
# http://127.0.0.1:8000/api/subscriptions/?format=json

urlpatterns += router.urls