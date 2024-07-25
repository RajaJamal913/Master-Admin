from rest_framework import serializers
from .models import UserProfile, Order, BannedIP, ActivityLog, API, PanelRate, OrderPanelConfig

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class BannedIPSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannedIP
        fields = '__all__'

class ActivityLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityLog
        fields = '__all__'

class APISerializer(serializers.ModelSerializer):
    class Meta:
        model = API
        fields = '__all__'

class PanelRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PanelRate
        fields = '__all__'

class OrderPanelConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPanelConfig
        fields = '__all__'
