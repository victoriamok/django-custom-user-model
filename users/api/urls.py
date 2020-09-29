from django.conf.urls import url
from django.urls import path, include

from users.api.views import (
    UserCreateAPIView,
    UserLoginAPIView,
    #   CreateUserView
    ChangePasswordView)

urlpatterns = [
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^register/$', UserCreateAPIView.as_view(), name='signup'),
    url(r'^change-password/$', ChangePasswordView.as_view(), name='change-password'),
]

# router = routers.DefaultRouter()
# router.register(r'createuser', CreateUserView)
#
# urlpatterns = [
#     # path('', include(router.urls)),
#     path('signup/', CreateUserView.as_view(), name='signup'),
# ]
