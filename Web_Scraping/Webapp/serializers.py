from rest_framework import serializers
from Webapp.models import Mouse,Keyboard,HeadGear

class MouseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mouse
        fields=('MouseId','Name','Brand','PictureLink','Detail','Banana','PowerB','Jib')

class KeyboardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Keyboard
        fields=('KeyboardId','Name','Brand','PictureLink','Detail','Banana','PowerB','Jib')

class HeadGearSerializer(serializers.ModelSerializer):
    class Meta:
        model=HeadGear
        field=('HeadGearId','Name','Brand','PictureLink','Detail','Banana','PowerB','Jib')