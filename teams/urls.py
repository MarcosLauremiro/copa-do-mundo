from django.urls import path
from .views import TeamsView, TeamsViewDetail


urlpatterns = [
    path('teams/', TeamsView.as_view()),
    path('teams/<team_id>/', TeamsViewDetail.as_view())
]
