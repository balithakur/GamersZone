from django.contrib import admin
from django.urls import path
from firstapp import views

#for sitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import path

from firstapp.sitemap import StaticViewSitemap
from . import views

sitemaps = {
    'static': StaticViewSitemap,
}
#end


urlpatterns = [
    path("", views.landingpage, name='index'),
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
    path("roomid", views.roomid, name='roomid'),
    #sitemap path
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
]