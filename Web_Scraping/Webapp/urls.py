from django.urls import re_path as url
from Webapp import views

urlpatterns=[
    url(r'^mouse$',views.mouseApi),
    url(r'^mouse/([0-9]+)$',views.mouseApi),

    url(r'^keyboard$',views.keyboardApi),
    url(r'^keyboard/([0-9]+)$',views.keyboardApi),
]