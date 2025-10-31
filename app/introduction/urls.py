from django.urls import path
from app.introduction.views import introView, historyView, departmentView

urlpatterns = [
    path("", introView, name="intro"),
    path("history/", historyView, name="history"),
    path("department/", departmentView, name="department")
]
