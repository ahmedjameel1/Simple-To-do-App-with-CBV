from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('routes/', views.GetRoutes.as_view(), name='routes'),
    path('tasks/', views.TaskList.as_view(), name='api-tasks'),
    path('task/<int:pk>/', views.TaskDetails.as_view(), name='api-task'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
