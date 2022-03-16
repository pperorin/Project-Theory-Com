from rest_framework import serializers
from Webapp.models import Mouse,Keyboard

class MouseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mouse
        fields=('MouseId','MouseName')

class KeyboardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Keyboard
        fields=('KeyboardId','KeyboardName')