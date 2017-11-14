"""
Define some views to help authenticate and test authentication.
"""
from django.conf.urls import url, include
from rest_framework_jwt.views import refresh_jwt_token
from authentication import views

urlpatterns = [
    url(r'^test$', views.test_auth),
    url(r'^token$', views.TokenViewSet.as_view()),
    url(r'^', include('rest_auth.urls')),
    url(r'^registration/', include('rest_auth.registration.urls')),
    url(r'^refresh-token', refresh_jwt_token),
]
