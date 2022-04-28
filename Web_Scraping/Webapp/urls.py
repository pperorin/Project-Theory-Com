from django.urls import re_path as url
from Webapp import views

urlpatterns=[
    url(r'^mouse$',views.mouseApi),
    url(r'^AddMouse$',views.addMouse),
    url(r'^mouse/(?P<id>[0-9]+)$',views.mouseApi),


    url(r'^keyboard$',views.keyboardApi),
    url(r'^AddKeyBoard$',views.addKeyBoard),
    url(r'^keyboard/(?P<id>[0-9]+)$',views.keyboardApi),
    
    url(r'^headgear$', views.headGearApi),
    url(r'^AddHeadGear$',views.addHeadGear),
    url(r'^headgear/(?P<id>[0-9]+)$', views.headGearApi),



]


