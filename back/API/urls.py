from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('registration/', views.RegistrationAPIView.as_view(), name='registration'),
    path('orders/', views.OrderAPIView.as_view({'get': 'list'}), name='orders' ),
    path('successOrder/', views.SuccessOrderAPIView.as_view({'get': 'list'}), name='success_order'),
    path('services/', views.ServicesAPIView.as_view(), name='services' ),
    path('details/', views.DetailAPIView.as_view(), name='details'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/verify/', TokenVerifyView.as_view(), name='token_verify'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)