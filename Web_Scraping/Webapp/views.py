from ast import pattern
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
import re

from django.core.files.storage import default_storage

# Create your views here.



@csrf_exempt
def mouseApi(request,id=0):
    if request.method=='GET':
        if id == 0:
            mouse = Mouse.objects.all()
            mouse_serializer=MouseSerializer(mouse,many=True)
            for i in mouse_serializer.data:
                mouseLis.append(dict(i))
            # for i in mouseLis:
            #     a = i["Brand"]
            #     ls1 = list(mouseBrandList.keys())
            #     if a in ls1:
            #         mouseBrandList[a] += 1
            #     else:
            #         temp = {a:1}
            #         mouseBrandList.update(temp)
            # print(mouseBrandList)
            for i in mouseLis:
                a = i["Name"]
                a = a.replace("(",'')
                a = a.replace(")",'')
                a = a.replace("-",'')
                insenGPRO = re.compile(re.escape('G PRO'), re.IGNORECASE)
                a = insenGPRO.sub('GPRO', a)
                a = a.split()
                mouseName.append(a)
            print(mouseName)
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
    mouse_data = obj
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
def keyAdd(obj):
    keyboard_data = obj
    keyboard_serializer=KeyboardSerializer(data=keyboard_data)
    if keyboard_serializer.is_valid():
        keyboard_serializer.save()
        return True
    return False

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



mouseBrandList = {}
mouseBrandBananaList = []
mouseLis = []
mouseName = []
bananaMouse = []
bananaMouseName = []
regName = []
notGoodName = ["Micropack Wireless Mouse + Keyboard KM-203W Black (TH/EN)","Rapoo Bluetooth and Wireless Mouse + Keyboard 8000M (TH/EN) (EO)","Rapoo Wireless Mouse + Keyboard 1800S Black (TH/EN) (EO)"]
colorLis = ["BLACK","BLUE","WHITE","GREEN","RED","YELLOW"]





@csrf_exempt
def hiBanana(request):
    # patt = re.compile("[0-9]+")
    lis = webScrap.Banana("mouse")
    for i in lis:
        dat = {
            "Name": i["name"],
            "Brand": i["brand"],
            "PictureLink": i["img_url"],
            "Detail": i["description"],
            "Banana": i["bananaPrice"],
            "Ihavecpu": "0",
            "Color": i["feature"]["Color"]
        }
        if dat["Name"] in notGoodName:
            pass
        else:
            bananaMouse.append(dat)
    for i in bananaMouse:
        thaiWord = re.compile(re.escape('เมาส์ไร้สาย'), re.IGNORECASE)
        a = i["Name"]
        if ("เมาส์ไร้สาย" in a) and ("Wireless" not in a):
            a = a.replace("เมาส์ไร้สาย","Wireless")
        if "[email protected]" in a:
            a = a.replace("[email protected]",'')
        if "เพื่อสุขภาพ" in a:
            a = a.replace("เพื่อสุขภาพ",'')
        a = a.replace("(",'')
        a = a.replace(")",'')
        a = a.replace("-",'')
        a = a.replace("EO",'')
        a = thaiWord.sub('',a)
        a = a.split()
        # if keyAdd(dat) == False:
        #     return JsonResponse("Failed to Upload",safe=False)
        
        isAdded = False
        for idx,j in enumerate(a):
            c = i["Brand"]
            col = i["Color"]
            x = re.findall("[0-9]+",j)
            if x != []:
                isAdded = True
                if len(x[0]) < 3:
                    if idx-1 >= 0:
                        strt = c + " " + a[idx-1] + " " + j + " " + col
                        regName.append(strt)
                else:
                    regName.append(c+" "+j+" "+col)
        if not isAdded:
            regName.append(' '.join(a))

    print(regName)
    print(len(regName), len(bananaMouse))
    return JsonResponse(lis,safe=False)

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
        if mouseAdd(dat) == False:
            return JsonResponse("Failed",safe=False)
    return JsonResponse("All done",safe=False)

