from django.urls import path
from .views import MemberListAPI

urlpatterns = [
    path('api/members/', MemberListAPI.as_view(), name='member-list-api'),
]
