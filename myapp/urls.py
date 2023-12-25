from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home.html", views.home, name="home"),
    path("data_analysis.html", views.data_analysis, name="data_analysis"),
    path("machine_learning.html", views.machine_learning, name="machine_learning"),
    path("breast_cancer.html", views.breast_cancer, name="breast_cancer"),
    path("austin_hpi.html", views.austin_hpi, name="austin_hpi"),
    path("contact.html", views.contact, name="contact"),
    path("game_projects.html", views.game_projects, name="game_projects"),
    path("about_me.html", views.about_me, name="about_me"),
]