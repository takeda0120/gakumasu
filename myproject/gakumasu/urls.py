from django.urls import path
from . import views
app_name = "gakumasu"
urlpatterns = [
    path("", views.index, name = "index"),
]