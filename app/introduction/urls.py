from django.urls import path
from app.introduction.views import introView, historyView

urlpatterns = [
    path("", introView, name="intro"),
    path("history/", historyView, name="history"),
]
