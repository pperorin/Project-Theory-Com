from django.urls import re_path as url
from Webapp import views

urlpatterns=[
    url(r'^mouse$',views.mouseApi),
    url(r'^mouse/(?P<id>[0-9]+)$',views.mouseApi),

    url(r'^keyboard$',views.keyboardApi),
    url(r'^keyboard/(?P<id>[0-9]+)$',views.keyboardApi),
    
    url(r'^headgear$', views.headGearApi),
    url(r'^headgear/(?P<id>[0-9]+)$', views.headGearApi),

    url(r'^bananaMouse$', views.addMouseFromBanana),

    url(r'^ihaveCPUMouse$', views.addMouseFromIHav),

    url(r'^bananaKB$', views.addKBFromBanana)
    # url(r'^testHi',views.testHi)
]


