from django.core.files.storage import default_storage
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from rest_framework.parsers import JSONParser

from Webapp.serializers import MouseSerializer,KeyboardSerializer,HeadGearSerializer
from Webapp.models import Mouse,Keyboard,HeadGear

from Web_Scraping import views as webScrap

import re
import requests

notGoodName = ["Micropack Wireless Mouse + Keyboard KM-203W Black (TH/EN)","Rapoo Bluetooth and Wireless Mouse + Keyboard 8000M (TH/EN) (EO)","Rapoo Wireless Mouse + Keyboard 1800S Black (TH/EN) (EO)"]
colorLis = ["BLACK","BLUE","WHITE","GREEN","RED","YELLOW", "GREY", "PINK", "PURPLE"]

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
def getMouse():
    mouse = Mouse.objects.all()
    mouse_sea = MouseSerializer(mouse,many=True)
    return mouse_sea.data

@csrf_exempt
def getKey():
    key = Keyboard.objects.all()
    key_sea = KeyboardSerializer(key,many=True)
    return key_sea.data

@csrf_exempt
def getHeadG():
    headG = HeadGear.objects.all()
    headG_sea = HeadGearSerializer(headG,many=True)
    return headG_sea.data


@csrf_exempt
def addMouse(request):
    temp = []
    mouseInDb = getMouse()
    mouse = JSONParser().parse(request)
    if mouseInDb == {}:
        mouse_serializer=MouseSerializer(data=request)
        if mouse_serializer.is_valid():
            mouse_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add 1",safe=False)  
    else:
        for i in mouseInDb:
            temp.append(i["RegularName"])
        a = mouse["RegularName"]
        ihav = mouse["Ihavecpu"]
        bana = mouse["Banana"]
        if a in temp:
            getData = Mouse.objects.get(RegularName=a)
            oldMouse = MouseSerializer(getData)
            if ihav != 0:
                mouse["Banana"] = oldMouse.data["Banana"]
            elif bana != 0:
                mouse["Ihavecpu"] = oldMouse.data["Ihavecpu"]
            updateMouse = MouseSerializer(getData,data=mouse)
            if updateMouse.is_valid():
                updateMouse.save()
                return JsonResponse("Added Successfully",safe=False)
            else:
                return JsonResponse("Failed to Add 2",safe=False)
        else:
            mouse_serializer=MouseSerializer(data=mouse)
            if mouse_serializer.is_valid():
                mouse_serializer.save()
                return JsonResponse("Added Successfully",safe=False)
            return JsonResponse("Failed to Add 4",safe=False)          

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
def addKeyBoard(request):
    temp = []
    keyInDb = getKey()
    kb = JSONParser().parse(request)
    if keyInDb == {}:
        keyboard_serializer=KeyboardSerializer(data=request)
        if keyboard_serializer.is_valid():
            keyboard_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add 1",safe=False)  
    else:
        for i in keyInDb:
            temp.append(i["RegularName"])
        a = kb["RegularName"]
        ihav = kb["Ihavecpu"]
        bana = kb["Banana"]
        if a in temp:
            getData = Keyboard.objects.get(RegularName=a)
            oldKB = KeyboardSerializer(getData)
            if ihav != 0:
                kb["Banana"] = oldKB.data["Banana"]
            elif bana != 0:
                kb["Ihavecpu"] = oldKB.data["Ihavecpu"]
            updateKB = KeyboardSerializer(getData,data=kb)
            if updateKB.is_valid():
                updateKB.save()
                return JsonResponse("Added Successfully",safe=False)
            else:
                return JsonResponse("Failed to Add 2",safe=False)
        else:
            keyboard_serializer=KeyboardSerializer(data=kb)
            if keyboard_serializer.is_valid():
                keyboard_serializer.save()
                return JsonResponse("Added Successfully",safe=False)
            return JsonResponse("Failed to Add 4",safe=False)

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
            return JsonResponse(f'Updated Successfully',safe=False)
        return JsonResponse(f'Failed to Update')
    elif request.method=='DELETE':
        headGear=HeadGear.objects.get(HeadGearId=id)
        headGear.delete()
        return JsonResponse(f'Deleted Successfully',safe=False)

@csrf_exempt
def addHeadGear(request):
    temp = []
    headInDb = getHeadG()
    hg = JSONParser().parse(request)
    if headInDb == {}:
        headGear_serializer = HeadGearSerializer(data=request)
        if headGear_serializer.is_valid():
            headGear_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add 1",safe=False)  
    else:
        for i in headInDb:
            temp.append(i["RegularName"])
        a = hg["RegularName"]
        ihav = hg["Ihavecpu"]
        bana = hg["Banana"]
        if a in temp:
            getData = HeadGear.objects.get(RegularName=a)
            oldHG = HeadGearSerializer(getData)
            if ihav != 0:
                hg["Banana"] = oldHG.data["Banana"]
            elif bana != 0:
                hg["Ihavecpu"] = oldHG.data["Ihavecpu"]
            updateHG = HeadGearSerializer(getData,data=hg)
            if updateHG.is_valid():
                updateHG.save()
                return JsonResponse("Added Successfully",safe=False)
            else:
                return JsonResponse("Failed to Add 2",safe=False)
        else:
            headGear_serializer = HeadGearSerializer(data=hg)
            if headGear_serializer.is_valid():
                headGear_serializer.save()
                return JsonResponse("Added Successfully",safe=False)
            return JsonResponse("Failed to Add 4",safe=False)

@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)
