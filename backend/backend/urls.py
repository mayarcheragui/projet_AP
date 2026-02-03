from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Internal Apps views
from apps.users.views import RegisterView, LogoutView, LoginView
from apps.habits.views import TaskViewSet, JournalViewSet
from apps.goals.views import GoalViewSet, UserAnalyticsView
from apps.notifications.views import NotificationViewSet

# Swagger
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

# router handle GET, POST, PUT, DELETE automatically
router = DefaultRouter()

router.register(r'habits/tasks', TaskViewSet, basename='tasks')
router.register(r'habits/journals', JournalViewSet, basename='journals')
router.register(r'goals', GoalViewSet, basename='goals')
router.register(r'notifications', NotificationViewSet, basename='notifications')

urlpatterns = [
    # Admin interface
    path('admin/', admin.site.urls),

    # Authentication Endpoints
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/login/', LoginView.as_view()),
    path('api/auth/logout/', LogoutView.as_view()),
    path('accounts/', include('allauth.urls')), # Routes Google : /accounts/google/login/

    # router URLs
    path('api/', include(router.urls)),

    # Swagger
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),


    # Other URLs
    path('api/analytics/', UserAnalyticsView.as_view(), name='user-analytics'),
]
