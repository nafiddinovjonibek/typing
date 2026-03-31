from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='index'),
    path('typing/<int:pk>/', views.typing_view, name='typing'),
    path('typing/<int:pk>/save/', views.save_result, name='save_result'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]
