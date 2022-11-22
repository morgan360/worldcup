from django.urls import path
from .views import HomePageView, AboutPageView, FantasyView, form_page

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
    path("form/", form_page, name="form"),
    path("fantasy_list/", FantasyView.as_view(), name="fantasy"),
]
