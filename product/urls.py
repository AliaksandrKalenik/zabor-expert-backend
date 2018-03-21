from django.conf.urls import url
from product import views as vw


urlpatterns = [
    url(r'^$', view=vw.home, name="home"),
    url(r'^contact$', view=vw.contacts, name="contact"),
]
