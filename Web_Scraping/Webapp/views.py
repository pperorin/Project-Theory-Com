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

bananaMouse = []
bananaKB = []
notGoodName = ["Micropack Wireless Mouse + Keyboard KM-203W Black (TH/EN)","Rapoo Bluetooth and Wireless Mouse + Keyboard 8000M (TH/EN) (EO)","Rapoo Wireless Mouse + Keyboard 1800S Black (TH/EN) (EO)"]
colorLis = ["BLACK","BLUE","WHITE","GREEN","RED","YELLOW", "GREY", "PINK", "PURPLE"] # unuse

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
    temp = []
    mouseInDB = Mouse.objects.all()
    mouse_serializer=MouseSerializer(mouseInDB,many=True)
    a = obj["RegularName"]
    for i in mouse_serializer.data:
        temp.append(i["RegularName"])
    if a in temp:
        m = Mouse.objects.get(RegularName=a)
        mOld = MouseSerializer(m)
        ## Add Price from Banana
        if obj["Banana"] != "0" and mOld.data["Banana"] == "0":
            obj["Ihavecpu"] = mOld.data["Ihavecpu"]
        ## Add Price from Ihavecpu
        elif obj["Ihavecpu"] != "0" and mOld.data["Ihavecpu"] == "0":
            obj["Banana"] = mOld.data["Banana"]
        ## Update Price of Banana
        elif obj["Banana"] != "0" and mOld["Banana"] != 0:
            obj["Ihavecpu"] = mOld.data["Ihavecpu"]
        ## Update Price of Ihavecpu
        elif obj["Ihavecpu"] != "0" and mOld["Ihavecpu"] != 0:
            obj["Banana"] = mOld.data["Banana"]
        moS = MouseSerializer(m,data=obj)
        if moS.is_valid():
            moS.save()
            return True
        else:
            return False
    else:
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
    temp = []
    kbInDB = Keyboard.objects.all()
    keyboard_serializer=KeyboardSerializer(kbInDB,many=True)
    a = obj["RegularName"]
    for i in keyboard_serializer.data:
        temp.append(i["RegularName"])
    if a in temp:
        k = Keyboard.objects.get(RegularName=a)
        kOld = KeyboardSerializer(k)
        ## Add Price from Banana
        if obj["Banana"] != "0" and kOld.data["Banana"] == "0":
            obj["Ihavecpu"] = kOld.data["Ihavecpu"]
        ## Add Price from Ihavecpu
        elif obj["Ihavecpu"] != "0" and kOld.data["Ihavecpu"] == "0":
            obj["Banana"] = kOld.data["Banana"]
        ## Update Price of Banana
        elif obj["Banana"] != "0" and kOld["Banana"] != 0:
            obj["Ihavecpu"] = kOld.data["Ihavecpu"]
        ## Update Price of Ihavecpu
        elif obj["Ihavecpu"] != "0" and kOld["Ihavecpu"] != 0:
            obj["Banana"] = kOld.data["Banana"]
        koS = KeyboardSerializer(k,data=obj)
        if koS.is_valid():
            koS.save()
            return True
        else:
            return False
    else:
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





@csrf_exempt
def addMouseFromBanana(request):
    lis = webScrap.Banana("mouse")
    temp =""
    for i in lis:
        dat = {
            "Name": i["name"],
            "Brand": i["brand"],
            "PictureLink": i["img_url"],
            "Detail": i["description"],
            "Banana": i["bananaPrice"],
            "Ihavecpu": "0",
            "RegularName": temp, 
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

        isAdded = False
        for idx,j in enumerate(a):
            c = i["Brand"]
            col = i["Color"]
            x = re.findall("[0-9]+",j)
            if x != []:
                isAdded = True
                strt = c + " " + j + " " + col
                strup = strt.upper()
                i["RegularName"] = strup
        if isAdded == False:
            getjoinstr = ' '.join(a)
            getupstr = getjoinstr.upper()
            i["RegularName"] = getupstr
        if mouseAdd(i) == False:
            JsonResponse("Failed To Add",safe=False)
    return JsonResponse("Complete",safe=False)

@csrf_exempt
def addMouseFromIHav(request):
    colLis = ["BLACK","WHITE","GREY","PINK"]
    lis = webScrap.ihavecpu("mouse")
    col = "None"
    temp = ""
    reg = "None"
    datLis = []
    for i in lis:
        a = i["name"]
        a = a.replace("(",'')
        a = a.replace(")",'')
        a = a.replace("-",'')
        a = a.replace("G PRO X",'GPROX')
        a = a.replace("G PRO","GPRO")
        a = a.split()
        for idx,j in enumerate(a):
            x = re.findall("[0-9]+",j)
            if j in colLis:
               col = j
            if x != []:
                reg = j
        if reg == "None":
            temp = ' '.join(a)
        else:
            if col == "None":
                temp = i["brand"] + " " + reg
            else:
                temp = i["brand"] + " " + reg + " " + col
  
        dat = {
            "Name": i["name"],
            "Brand": i["brand"],
            "PictureLink": i["img_url"],
            "Detail": i["description"],
            "Banana": "0",
            "Ihavecpu": i["price"],
            "RegularName": temp
        }
        temp = ""
        col = "None"
        reg = "None"
        if mouseAdd(dat) == False:
            return JsonResponse("Failed",safe=False)
        datLis.append(dat)
    return JsonResponse(datLis,safe=False)


@csrf_exempt
def addKBFromBanana(requset):
    reg = "None"
    lis = webScrap.Banana("keyboard")
    temp =""
    for i in lis:
        dat = {
            "Name": i["name"],
            "Brand": i["brand"],
            "PictureLink": i["img_url"],
            "Detail": i["description"],
            "Banana": i["bananaPrice"],
            "Ihavecpu": "0",
            "RegularName": temp, 
            "Color": i["feature"]["Color"]
        }
        bananaKB.append(dat)
    for i in bananaKB:
        a = i["Name"]
        a = a.replace("(Red Switch)",'Red Switch')
        a = a.replace("(Blue Switch)",'Blue Switch')
        tp = a.split()
        newStr = []
        for j in tp:
            if "(" in j:
                pass
            if "คีย์บอร์ดไร้สาย" in j:
                pass
            if "คีย์บอร์ด" in j:
                pass
            else:
                newStr.append(j)
        a = " ".join(newStr)
        a = a.replace("-",'')
        a = a.replace("/",' ')
        a = a.replace("EN",'')
        a = a.replace("TH",'')
        a = a.replace("EO",'')
        a = a.replace("G PRO",'GPRO')
        i["Name"] = a
        a = a.split()

        for j in a:
            x = re.findall("[0-9]+",j)
            if x != []:
                reg = j
        if reg == "None":
            temp = ' '.join(a)
            temp = temp.upper()
            i["RegularName"] = temp
        else:
            temp = i["Brand"] + " " + reg + " " + i["Color"]
            temp = temp.upper()
            i["RegularName"] = temp
        temp = ""
        reg = "None"
        if keyAdd(i) == False:
            return JsonResponse("Failed",safe=False)
    return JsonResponse(bananaKB,safe=False)






















# def testHi(requset):
#     for i in range(10,100,10):
#         dat = {
#             "Name": "test",
#             "Brand": "test",
#             "PictureLink": "test",
#             "Detail": "test",
#             "Banana": str(i),
#             "Ihavecpu": "0",
#             "RegularName": "test" + " " + str(i)
#         }
#         if mouseAdd(dat) == False:
#             return JsonResponse("Failed Test",safe=False)
#         dat1 = {
#             "Name": "test",
#             "Brand": "test",
#             "PictureLink": "test",
#             "Detail": "test",
#             "Banana": "0",
#             "Ihavecpu": str(i),
#             "RegularName": "test" + " " + str(i)
#         }
#         if mouseAdd(dat1) == False:
#             return JsonResponse("Faled Test",safe=False)
#         dat2 = {
#             "Name": "test",
#             "Brand": "test",
#             "PictureLink": "test",
#             "Detail": "test",
#             "Banana": "0",
#             "Ihavecpu": str(i+10),
#             "RegularName": "test" + " " + str(i)
#         }
#         if mouseAdd(dat2) == False:
#             return JsonResponse("Failed Test",safe=False)
#     return JsonResponse("Cool",safe=False)
