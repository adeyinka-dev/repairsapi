from .views import RepairListView
from django.urls import path, include

urlpatterns = [
    path("", RepairListView.as_view(), name="home"),
]
