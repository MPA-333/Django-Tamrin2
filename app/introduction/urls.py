from django.urls import path
from app.introduction.views import introView, historyView, departmentView, museumView

urlpatterns = [
    path("", introView, name="intro"),
    path("history/", historyView, name="history"),
    path("department/", departmentView, name="department"),
    path("department/museum/", museumView, name="museum")
]
