# clubs/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'clubs'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Add other URL patterns
]
# clubs/urls.py
from django.urls import path
from . import views

app_name = 'clubs'

urlpatterns = [
    path('api/clubs/', views.ClubList.as_view(), name='club-list'),
    path('api/clubs/<int:pk>/', views.ClubDetail.as_view(), name='club-detail'),
    path('api/requests/', views.MembershipRequestList.as_view(), name='request-list'),
    # Define URLs for Task and Announcement models
]
