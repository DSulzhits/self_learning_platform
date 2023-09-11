from django.urls import path
from users.apps import UsersConfig
from users.views import UserListAPIView, UserCreateAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.views.decorators.cache import never_cache

app_name = UsersConfig.name

urlpatterns = [
    # user urlpatterns
    path('', UserListAPIView.as_view(), name='users_list'),
    path('create/', never_cache(UserCreateAPIView.as_view()), name='user_create'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user_detail'),
    path('<int:pk>/update/', never_cache(UserUpdateAPIView.as_view()), name='user_update'),
    path('<int:pk>/delete/', never_cache(UserDestroyAPIView.as_view()), name='user_delete'),

    # token urlpatterns
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
