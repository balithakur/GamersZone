from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [
    path("", views.landingpage, name='landpage'),
    path("home", views.home, name='home'),
    path("createaccount", views.signup, name='signup'),
    path("thankyoupage", views.thank, name='thankyou'),
    path("tournamentpage", views.tournament, name='tournament'),
    path("aboutus", views.aboutus, name='aboutus'),
    path("login", views.loginn, name='login'),
    path("profile", views.profile, name='profile'),
    path("contact", views.contact, name='contact'), 
    path("ffdata", views.ffdata, name='ffdata'),
    path("pubgdata", views.pubgdata, name='pubgdata'),
    path("coddata", views.callofdutydata, name='coddata'),
    path("payment", views.payment, name='payment'),
    path("order", views.handlerequest, name='order'),
]
