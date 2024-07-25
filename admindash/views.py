from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import UserProfile, Order, BannedIP, ActivityLog, API, PanelRate, OrderPanelConfig


@login_required
def user_list(request):
    users = UserProfile.objects.all()
    return render(request, 'templates/user_list.html', {'users': users})

@login_required
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'templates/order_list.html', {'orders': orders})

def overview(request):
    return render(request, 'templates/overview.html')

@login_required
def ip_banning(request):
    banned_ips = BannedIP.objects.all()
    logs = ActivityLog.objects.all()
    context = {
        'banned_ips': banned_ips,
        'logs': logs,
    }
    return render(request, 'templates/Ip_Banning.html', context)

@login_required
def api_management(request):
    apis = API.objects.all()
    return render(request, 'templates/api_management.html', {'apis': apis})

@login_required
def toggle_api_status(request, api_id):
    api = get_object_or_404(API, id=api_id)
    api.status = not api.status
    api.save()
    return redirect('admindash:api_management')

@login_required
def delete_api(request, api_id):
    api = get_object_or_404(API, id=api_id)
    api.delete()
    return redirect('admindash:api_management')

@login_required
def add_duplicate_api(request):
    if request.method == 'POST':
        domain = request.POST['domain']
        status = request.POST.get('status', False)
        API.objects.create(domain=domain, status=status)
        return redirect('admindash:api_management')
    return render(request, 'templates/api_management.html')

@login_required
def panel_rate_management(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('rate_'):
                user_id = key.split('_')[1]
                try:
                    user = User.objects.get(pk=user_id)
                    rate, created = PanelRate.objects.get_or_create(user=user)
                    rate.rate = value
                    rate.save()
                except User.DoesNotExist:
                    continue  # Skip if the user does not exist
        return redirect('admindash:panel_rate_management')

    users = User.objects.all()
    return render(request, 'templates/panel_rate_management.html', {'users': users})

@login_required
def order_panel_configuration(request):
    if request.method == 'POST':
        default_features = request.POST.get('default_features') == 'on'
        maintenance_mode = request.POST.get('maintenance_mode') == 'on'
        custom_message = request.POST.get('custom_message')

        config, created = OrderPanelConfig.objects.get_or_create(id=1)  # Assuming there's only one config
        config.default_features = default_features
        config.maintenance_mode = maintenance_mode
        config.custom_message = custom_message
        config.save()

        return redirect('admindash:order_panel_configuration')

    config = OrderPanelConfig.objects.first()
    return render(request, 'templates/order_panel_configuration.html', {'config': config})

from rest_framework import viewsets
from .models import UserProfile, Order, BannedIP, ActivityLog, API, PanelRate, OrderPanelConfig
from .serializers import (
    UserProfileSerializer,
    OrderSerializer,
    BannedIPSerializer,
    ActivityLogSerializer,
    APISerializer,
    PanelRateSerializer,
    OrderPanelConfigSerializer
)

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class BannedIPViewSet(viewsets.ModelViewSet):
    queryset = BannedIP.objects.all()
    serializer_class = BannedIPSerializer

class ActivityLogViewSet(viewsets.ModelViewSet):
    queryset = ActivityLog.objects.all()
    serializer_class = ActivityLogSerializer

class APIViewSet(viewsets.ModelViewSet):
    queryset = API.objects.all()
    serializer_class = APISerializer

class PanelRateViewSet(viewsets.ModelViewSet):
    queryset = PanelRate.objects.all()
    serializer_class = PanelRateSerializer

class OrderPanelConfigViewSet(viewsets.ModelViewSet):
    queryset = OrderPanelConfig.objects.all()
    serializer_class = OrderPanelConfigSerializer

