from re import I
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import requests
from Webapp.models import Mouse,Keyboard,HeadGear
from Webapp.serializers import MouseSerializer,KeyboardSerializer,HeadGearSerializer
from Web_Scraping import views as webScrap
import json

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def mouseApi(request,id=0):
    if request.method=='GET':
        if id == 0:
            mouse = Mouse.objects.all()
            mouse_serializer=MouseSerializer(mouse,many=True)
            return JsonResponse(mouse_serializer.data,safe=False)
        else:
            mouse = Mouse.objects.get(MouseId=id)
            mouse_serializer=MouseSerializer(mouse)
            return JsonResponse(mouse_serializer.data,safe=False)
    elif request.method=='POST':
        mouse_data=JSONParser().parse(request)
        mouse_serializer=MouseSerializer(data=mouse_data)
        if mouse_serializer.is_valid():
            mouse_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        mouse_data=JSONParser().parse(request)
        mouse=Mouse.objects.get(MouseId=id)
        mouse_serializer=MouseSerializer(mouse,data=mouse_data)
        if mouse_serializer.is_valid():
            mouse_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        mouse=Mouse.objects.get(MouseId=id)
        mouse.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def mouseAdd(obj):
    mouse_data= obj
    print(mouse_data)
    mouse_serializer = MouseSerializer(data=mouse_data)
    if mouse_serializer.is_valid():
        mouse_serializer.save()
        return True
    return False


@csrf_exempt
def keyboardApi(request,id=0):
    if request.method=='GET':
        if id == 0:
            keyboard = Keyboard.objects.all()
            keyboard_serializer=KeyboardSerializer(keyboard,many=True)
            return JsonResponse(keyboard_serializer.data,safe=False)
        else:
            keyboard = Keyboard.objects.get(KeyboardId=id)
            keyboard_serializer = KeyboardSerializer(keyboard)
            return JsonResponse(keyboard_serializer.data,safe=False)
    elif request.method=='POST':
        keyboard_data=JSONParser().parse(request)
        keyboard_serializer=KeyboardSerializer(data=keyboard_data)
        if keyboard_serializer.is_valid():
            keyboard_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        keyboard_data=JSONParser().parse(request)
        keyboard=Keyboard.objects.get(KeyboardId=id)
        keyboard_serializer=KeyboardSerializer(keyboard,data=keyboard_data)
        if keyboard_serializer.is_valid():
            keyboard_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        keyboard=Keyboard.objects.get(KeyboardId=id)
        keyboard.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def headGearApi(request, id=0):
    if request.method=='GET':
        if id == 0:
            headGear = HeadGear.objects.all()
            headGear_serializer = HeadGearSerializer(headGear,many=True)
            return JsonResponse(headGear_serializer.data,safe=False)
        else:
            headGear = HeadGear.objects.get(HeadGearId=id)
            headGear_serializer = HeadGearSerializer(headGear)
            return JsonResponse(headGear_serializer.data,safe=False)
    elif request.method=='POST':
        headGear_data=JSONParser().parse(request)
        headGear_serializer=HeadGearSerializer(data=headGear_data)
        if headGear_serializer.is_valid():
            headGear_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        headGear_data=JSONParser().parse(request)
        headGear=HeadGear.objects.get(HeadGearId=id)
        headGear_serializer = HeadGearSerializer(headGear,data=headGear_data)
        if headGear_serializer.is_valid():
            headGear_serializer.save()
            return JsonResponse(f'Update {headGear_data} Successfully',safe=False)
        return JsonResponse(f'Failed to Update {headGear_data}')
    elif request.method=='DELETE':
        headGear=HeadGear.objects.get(HeadGearId=id)
        headGear.delete()
        return JsonResponse(f'Deleted {headGear} Successfully',safe=False)

@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)

@csrf_exempt
def catchTest(dataT):
    i = 0
    api = "http://127.0.0.1:8000/mouse"
    while i < len(dataT):
        if requests.post(api, json=dataT[i]):
            i += 1
        else:
            break
    if i == len(dataT):
        return True
    else:
        return False


@csrf_exempt
def hiBanana(request):
    lis = webScrap.Banana("mouse")
    i = 0
    for i in range(5):
        dat = {
            "Name": lis[i]["name"],
            "Brand": lis[i]["brand"],
            "PictureLink": lis[i]["link"],
            "Detail": lis[i]["description"],
            "Banana": "1",
            "Ihavecpu": "0"
        }
        print(dat)
        if mouseAdd(dat) == False:
            return JsonResponse("Failed to Upload",safe=False)
    return JsonResponse("All done",safe=False)

@csrf_exempt
def hiIHCPU(request):
    lis = webScrap.ihavecpu("mouse")
    for i in lis:
        dat = {
            "Name": i["name"],
            "Brand": i["brand"],
            "PictureLink": i["img_url"],
            "Detail": i["description"],
            "Banana": "0",
            "Ihavecpu": i["price"]
        }
        j = json.dumps(dat,ensure_ascii=False).encode('utf8')
        if mouseAdd(j.decode()) == False:
            return JsonResponse("Failed",safe=False)
    return JsonResponse("All done",safe=False)

    