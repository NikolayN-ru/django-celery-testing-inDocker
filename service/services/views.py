from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from service.serializers import SubscriptionSerializer
from services.models import Subscription


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all().prefetch_related('client__user')
    serializer_class = SubscriptionSerializer
    