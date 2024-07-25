from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    overview,
    user_list,
    order_list,
    ip_banning,
    api_management,
    toggle_api_status,
    delete_api,
    add_duplicate_api,
    panel_rate_management,
    order_panel_configuration,
    UserProfileViewSet,
    OrderViewSet,
    BannedIPViewSet,
    ActivityLogViewSet,
    APIViewSet,
    PanelRateViewSet,
    OrderPanelConfigViewSet
)

app_name = 'admindash'

router = DefaultRouter()
router.register(r'userprofiles', UserProfileViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'bannedips', BannedIPViewSet)
router.register(r'activitylogs', ActivityLogViewSet)
router.register(r'apis', APIViewSet)
router.register(r'panelrates', PanelRateViewSet)
router.register(r'orderpanelconfigs', OrderPanelConfigViewSet)

urlpatterns = [
    path('', overview, name='overview'),
    path('user_list/', user_list, name='users'),
    path('order_list/', order_list, name='orders'),
    path('ip_banning/', ip_banning, name='ip_banning'),
    path('api_management/', api_management, name='api_management'),
    path('api_management/toggle/<int:api_id>/', toggle_api_status, name='toggle_api_status'),
    path('api_management/delete/<int:api_id>/', delete_api, name='delete_api'),
    path('api_management/add/', add_duplicate_api, name='add_duplicate_api'),
    path('panel-rate-management/', panel_rate_management, name='panel_rate_management'),
    path('order-panel-configuration/', order_panel_configuration, name='order_panel_configuration'),
    path('', include(router.urls)),  # Ensure this is included
]
