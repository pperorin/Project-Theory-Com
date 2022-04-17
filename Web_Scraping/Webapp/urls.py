from django.urls import re_path as url
from Webapp import views

urlpatterns=[
    url(r'^mouse$',views.mouseApi),
    url(r'^mouse/(?P<id>[0-9]+)$',views.mouseApi),

    url(r'^keyboard$',views.keyboardApi),
    url(r'^keyboard/(?P<id>[0-9]+)$',views.keyboardApi),
    
    url(r'^headgear$', views.headGearApi),
    url(r'^headgear/(?P<id>[0-9]+)$', views.headGearApi),

    # Add Mouse to database
    url(r'^bananaMouse$', views.addMouseFromBanana),
    url(r'^ihaveCPUMouse$', views.addMouseFromIHav),
    
    # Add Keyboard to database
    url(r'^bananaKB$', views.addKBFromBanana),
    url(r'^ihavecpuKB$', views.addKBFromIHaveCpu),

    # Add HeadGear to database
    url(r'^bananaHeadGear$', views.addHeadGearBanana),
    url(r'^ihavecpuHeadGear$', views.addHeadGearIHaveCpu)

    # for testing functions
    # url(r'^testRenamingIHaveCpuKeyboard$', views.testRenamingIHaveCpuKeyboard)
    # url(r'^testRenamingBNNHeadGear$', views.testRenamingBNNHeadGear),
    # url(r'^testRenamingIHaveCpuHeadGear$', views.testRenamingIHaveCpuHeadGear)
    # # url(r'^testHi',views.testHi)
]


