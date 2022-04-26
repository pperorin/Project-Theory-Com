from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.http.response import JsonResponse

from rest_framework.parsers import JSONParser

from Webapp.serializers import MouseSerializer,KeyboardSerializer,HeadGearSerializer
from Webapp.models import Mouse,Keyboard,HeadGear
from Web_Scraping import views as webScrap

import re
import requests

# Create your views here.
bananaMouse = []
bananaKB = []

notGoodName = ["Micropack Wireless Mouse + Keyboard KM-203W Black (TH/EN)","Rapoo Bluetooth and Wireless Mouse + Keyboard 8000M (TH/EN) (EO)","Rapoo Wireless Mouse + Keyboard 1800S Black (TH/EN) (EO)"]
colorLis = ["BLACK","BLUE","WHITE","GREEN","RED","YELLOW", "GREY", "PINK", "PURPLE"]
keyBoardColor = []

def hellofromIhaveCPU(request):
    return JsonResponse("Hi there", safe=False)


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


def priceMap(merchandiseType, regularList, merchandise):
    temp = []
    for i in regularList.data:
        temp.append(i["RegularName"])
    if merchandise["RegularName"] in temp:
        if merchandiseType == 1:
            getData = Mouse.objects.get(RegularName=merchandise["RegularName"])
            oldData = MouseSerializer(getData)
        elif merchandiseType == 2:
            getData = Keyboard.objects.get(RegularName=merchandise["RegularName"])
            oldData = KeyboardSerializer(getData)
        elif merchandiseType == 3:
            getData = HeadGear.objects.get(RegularName=merchandise["RegularName"])
            oldData = KeyboardSerializer(getData)
        if merchandise["Ihavecpu"] != "0":
            merchandise["Banana"] = oldData.data["Banana"]
        elif merchandise["Banana"] != "0":
            merchandise["Ihavecpu"] = oldData.data["Ihavecpu"]
        if merchandiseType == 1:
            newData = MouseSerializer(getData, data = merchandise)
        elif merchandiseType == 2:
            newData = KeyboardSerializer(getData, data = merchandise)
        elif merchandiseType == 3:
            newData = HeadGearSerializer(getData, data = merchandise)
        return newData
    else:
        if merchandiseType == 1:
            newData = MouseSerializer(data = merchandise)
        elif merchandiseType == 2:
            newData = KeyboardSerializer(data = merchandise)
        elif merchandiseType == 3:
            newData = HeadGearSerializer(data = merchandise)
        return newData
        

@csrf_exempt
def mouseAdd(obj):
    mouseInDB = Mouse.objects.all()
    mouse_serializer=MouseSerializer(mouseInDB,many=True)
    newMouseData = priceMap(1, mouse_serializer, obj)
    if newMouseData.is_valid():
        newMouseData.save()
        return True
    else:
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
    kbInDB = Keyboard.objects.all()
    keyboard_serializer=KeyboardSerializer(kbInDB,many=True)
    newKeyBoardData = priceMap(2, keyboard_serializer, obj)
    if newKeyBoardData.is_valid():
        newKeyBoardData.save()
        return True
    else:
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
            return JsonResponse(f'Updated Successfully',safe=False)
        return JsonResponse(f'Failed to Update')
    elif request.method=='DELETE':
        headGear=HeadGear.objects.get(HeadGearId=id)
        headGear.delete()
        return JsonResponse(f'Deleted Successfully',safe=False)

@csrf_exempt
def headgearAdd(obj):
    headgearInDB = HeadGear.objects.all()
    headGear_serializer=HeadGearSerializer(headgearInDB, many=True)
    newHeadGearData = priceMap(3, headGear_serializer, obj)
    if newHeadGearData.is_valid():
        newHeadGearData.save()
        return True
    else:
        return False

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

################################### add Banana mouse ############################
@csrf_exempt
def addMouseFromBanana(request):
    lis = webScrap.Banana("mouse")
    temp =""
    for i in lis:
        if i["feature"]:
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
        else:
            dat = {
                "Name": i["name"],
                "Brand": i["brand"],
                "PictureLink": i["img_url"],
                "Detail": i["description"],
                "Banana": i["bananaPrice"],
                "Ihavecpu": "0",
                "RegularName": temp, 
                "Color": "None"
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
                if col != "None":
                    strt = c + " " + j + " " + col
                else:
                    strt = c + " " + j
                strup = strt.upper()
                i["RegularName"] = strup
        if isAdded == False:
            getjoinstr = ' '.join(a)
            getupstr = getjoinstr.upper()
            i["RegularName"] = getupstr
        if mouseAdd(i) == False:
            JsonResponse("Failed To Add",safe=False)
    return JsonResponse(bananaMouse,safe=False)

################################ add IHaveCPU Mouse ##########################

# add IhaveCPU mouse
@csrf_exempt
def addMouseFromIHav(request):
    colLis = ["BLACK","WHITE","GREY","PINK","LILAC","BLUE"]
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

################################ add Keyboard ##########################

@csrf_exempt
def addKBFromBanana(requset):
    reg = "None"
    lis = webScrap.Banana("keyboard")
    temp = ""
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
        lis=[]
        for m in a.split():
            lis.append(m)
        for j in lis:
            if "(" in j:
                lis.pop(lis.index(j))
            elif "คีย์บอร์ดไร้สาย" in j:
                lis.pop(lis.index(j))
            elif "คีย์บอร์ด" in j:
                lis.pop(lis.index(j))
        a = " ".join(lis)
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
        if i["Color"] in keyBoardColor:
            pass
        else:
            keyBoardColor.append(i["Color"])
        if keyAdd(i) == False:
            return JsonResponse("Failed",safe=False)
    
    return JsonResponse(bananaKB,safe=False)

################################ IHaveCPU Keyboard ##########################
@csrf_exempt
def addKBFromIHaveCpu(request):
    # get all keyboard from IHaveCPU
    lis = webScrap.ihavecpu("keyboard")

    # filter only needed info and add into ihaveCpuKey
    ihavecpuKeyboard = []
    nameList = []
    removeWords = ["-", "/ ", "(EN/TH)", "[TH/EN]", "[EN/TH]",  "(EN)", "TH/EN", "(RGB LED)", "(MEMBRANE) ", "GAMING ", "KEYBOARD "]
    switchType = ["PRO ","BLUE SWITCH", "RED SWITCH", "CLICKY", "TACTILE", "NX BLUE", "NX BROWN"]

    for item in lis:
        
        # renaming for "RugularName"
        regularTemp = ""
        nameTemp = ""
        itemSerial = ""
        itemType = ""
        if item["name"] not in nameList:
            # for checking duplicate
            nameList.append(item["name"])

            nameTemp = item["name"]
            for word in removeWords:
                nameTemp = nameTemp.replace(word, "")
            nameTemp = nameTemp.replace("G PRO", "GPRO")

            for namePart in nameTemp.split():
                if re.findall("[0-9]+", namePart) != []:
                    itemSerial = namePart
                    break
                if re.findall("STRIX", namePart) != []:
                    itemSerial = namePart
                    break
                if re.findall("GPRO", namePart) != []:
                    itemSerial = namePart
                    break
            
            for word in switchType:
                if re.findall(word, nameTemp) != []:
                    itemType = word

            regularTemp = item["brand"]
            if itemSerial != "" or itemType != "":
                regularTemp += " " + itemSerial
                if itemType != "":
                    regularTemp += " " + itemType
            else:
                regularTemp += " " + nameTemp

            # create data format
            dataDict = {
                    "Name": (item["name"]).strip(),
                    "Brand": item["brand"],
                    "PictureLink": item["img_url"],
                    "Detail": item["description"],
                    "Banana": "0",
                    "Ihavecpu": item["price"],
                    "RegularName": regularTemp.strip()
                    }
            ihavecpuKeyboard.append(dataDict)

        # add to database 
        if keyAdd(dataDict) == False:
            return JsonResponse("Failed",safe=False)
    return JsonResponse(ihavecpuKeyboard, safe=False)

# @csrf_exempt
# def testRenamingIHaveCpuKeyboard(request):
#     lis = [
#     "OUTEMU MK-61 ",
#     "OUTEMU MK-02 MECHANICAL BLUE SWITCH ",
#     "OUTEMU MK-03 MECHANICAL RED SWITCH ",
#     "OUTEMU MK-04 MECHANICAL GREY BLUE SWITCH ",
#     "XANOVA PULSAR XK400 BLUE SWITCH ",
#     "X YDK-AK-900 GAMING KEYBOARD ",
#     "GK-72 RGB MECHANICAL ",
#     "OUTEMU MK-02 PRO ",
#     "ROG STRIX SCOPE NX TKL MOONLIGHT WHITE (ROG NX BROWN)(EN/TH) ",
#     "ROG STRIX SCOPE NX TKL (ROG NX BLUE)(EN/TH) ",
#     "G PRO RGB MECHANICAL GAMING [GX BLUE CLICKY SWITCH] ",
#     "X33 ALISTAR [BLUE SWITCH] BLACK ",
#     "X33 ALISTAR [BLUE SWITCH] PURPLE / YELLOW ",
#     "X33 ALISTAR [RED SWITCH] YELLOW / WHITE ",
#     "CHALLENGER PRIME ",
#     "G413 CARBON GAMING MECHANICAL ROMER-G TACTILE ",
#     "CYNOSA LITE ESSENTIAL ",
#     "G512 CARBON [GX BLUE CLICKY SWITCH] [TH/EN] ",
#     "VIGOR GK30 GAMING ",
#     "KG8702 OSIRIS ",
#     "G213 PRODIGY (MEMBRANE) (RGB LED) (EN/TH) ",
#     "G PRO X [GX BLUE CLICKY ] (RGB LED) (EN) ",
#     "VIGOR GK60 MECHANICAL CHERRY RED SWITCH ",
#     "G913 LIGHTSPEED WIRELESS RGB [GL CLICKY SWITCH] TH/EN ",
#     "VIGOR GK50 LOW PROFILE US GAMING [EN/TH] ",
#     "GAMING KEYBOARD ORNATA CHROMA (EN/TH) "
#     ]

#     removeWords = ["-", "/ ", "(EN/TH)", "[TH/EN]", "[EN/TH]",  "(EN)", "TH/EN" ,"(RGB LED)", "(MEMBRANE)"]
#     for i in range(len(lis)):
#         for word in removeWords:
#             lis[i] = lis[i].replace(word, "")
#         lis[i] = lis[i].replace("G PRO", "GPRO")

#         lis[i] = lis[i].strip()
#         # print(lis[i])
#     return JsonResponse(lis, safe=False)


############################### HeadGear Banana #############################
@csrf_exempt
def addHeadGearBanana(request):
    # get all headgear from Banana
    lis = webScrap.Banana("headphone")
    bananaHeadGear = []
    # nameList = []

    # filter only needed info and add to bananaHeadGear
    for item in lis:

        # renaming for "RugularName"
        regularName = item["name"]
        removeWords = ["-", "ฟังสปอร์ต", "หูฟังไร้สาย", "หูฟังเกมมิ่ง", "หูฟังใส่ออกกำลังกาย", "หูฟัง", "หู", "รุ่น ", "In-Ear", "InEar", "In Ear", "Earbud", "Gaming Headset", 
        "Headphones", "Headphone", "Heaphone", "Headset", "with Mic.", "True Wireless", "Wireless", "(RMA2105)", "(EPM1)","(EPT25)","(14274)", "(RMA215)", "(RMA210)", "Bluetooth", "Stereo"]        
        for word in removeWords:
            if word in regularName:
                regularName = regularName.replace(word, "")
                regularName = regularName.replace("  ", " ")
        regularName = regularName.replace("G PRO", "GPRO")
        # nameList.append(regularName)

        # data format
        dataDict = {
            "Name": item["name"].strip(),
            "Brand": item["brand"],
            "Color": item["feature"]["Color"],
            "Banana": item["bananaPrice"],
            "Ihavecpu": "0",
            "PictureLink": item["img_url"],
            "Detail": item["description"],
            "RegularName": (regularName.strip()).upper()
        }
        bananaHeadGear.append(dataDict)

        # add to database
        if headgearAdd(dataDict) == False:
            print("Cannot add --> ", item["name"])

    return JsonResponse(bananaHeadGear, safe=False)

# @csrf_exempt
# def testRenamingBNNHeadGear(request):
#     currentHeadGearName = ['Sony Pulse 3D Wireless Headset PS5- Midnight Black', 'Samsung Galaxy Buds2', 'Samsung Galaxy Buds Pro Phantom Violet', 'Samsung Galaxy Buds Pro Phantom Silver', 'Samsung Galaxy Buds Pro Phantom Black', 'OPPO Enco Buds', 'OPPO Enco X', '1 More In-Ear Wireless TWS Comfo Buds Pro Black', '1 More In-Ear Wireless TWS Comfo Buds Pro White', '1 More In-Ear Wireless TWS Colour Buds Black', 'Aftershokz Wireless Headphone Openmove', 'Aftershokz Xtrainerz Sapphire', 'Anitech Headphone with Mic. AK39', 'Anitech Headphone with Mic. AK75', 'Audio Technica Headphone In-Ear Sport10', 'Audio Technica Headphone Professional Monitor Series M20X', 'Audio Technica In Ear with Mic. Wireless CLR100BT', 'AUKEY EP-M1 True Wireless Earbuds Black (EP-M1)', 'AUKEY EP-T25 True Wireless Earbuds Black (EP-T25)', 'AUKEY True Wireless Earbuds White (EP-T25)', 'B&O In-Ear Wireless TWS E8', 'B&O In-Ear Wireless TWS E8 3RD GEN', 'B&O In-Ear Wireless TWS E8 3RD GEN Sport', 'Black Shark Lucifer T1', 'Blue Box Earbud Wireless TWS AP-01', 'Blue Box Headphone TWS APG01', 'Blue Box Headphone TWS BB Pro', 'Blue Box Headphone Wireless ED-01', 'Blue Box Headphone Wireless H2', 'Blue Box In-Ear Wireless EE001', 'Blue Box In-Ear with Mic. BN-X50', 'Blue Box In-Ear with Mic. MS-212', 'Blue Box In-Ear with Mic. SH1', 'Blue Box Inear Wireless TWS AP PRO White', 'Defunc Earbud TWS\xa0True Basic', 'E&P Stereo Earphone EP-EE08', 'E&P Stereo Earphone EP-EE20 White/White', 'E&P Stereo Sport Bluetooth Headphone EP-BL06', 'Fantech Gaming Headset HG24 Specter II', 'Fantech Gaming Headset MH87 BLITZ', 'Fantech Gaming Headset Wh01 Wireless Black', 'Huawei In-Ear Wireless TWS Freebuds 4', 'IPIPOO In-Ear Wireless TWS TP-18', 'IPIPOO In-Ear Wireless TWS TP-9', 'IPIPOO In-Ear with Mic. Wireless IL-804', 'Jabra Bluetooth Headset Talk 15', 'Jabra Bluetooth Headset Talk 45 Black', 'Jabra Bluetooth Headset Talk 5 Black', 'Jabra Headset Elite 65T Copper Black', 'Jabra In-Ear Wireless TWS Elite 2', 'Jabra In-Ear Wireless TWS Elite 3', 'Jabra In-Ear Wireless TWS Elite 7 Active', 'Jabra In-Ear Wireless TWS Elite 7 PRO', 'Jabra In-Ear Wireless TWS Elite 75T Titanium Black', 'Jabra In-Ear Wireless TWS Elite 85T Grey', 'Jabra In-Ear Wireless TWS Elite Active 65T Copper Blue', 'Jabra In-Ear Wireless TWS Elite Active 65T Titanium Black', 'JBL Earbud TWS T225', 'JBL Earbud TWS T225 Ghost Edition Clear', 'JBL In Ear Endurance DIVE Waterproof Wireless with MP3 Player', 'JBL In Ear Endurance RUN Sweatproof Wired Sports Black', 'JBL In Ear Endurance RUN Sweatproof Wired Sports Red', 'JBL In Ear Endurance SPRINT Waterproof Wireless Black', 'JBL In Ear Endurance SPRINT Waterproof Wireless Red', 'JBL In-Ear Wireless TWS Endurance PEAK Black', 'JBL In-Ear Wireless TWS Endurance PEAK Blue', 'JBL In-Ear Wireless TWS Endurance PEAK II Black', 'JBL In-Ear Wireless TWS Endurance PEAK Red', 'JBL In-Ear Wireless TWS Live Black', 'JBL In-Ear Wireless TWS Live Blue', 'JBL In-Ear Wireless TWS Live Pink', 'JBL In-Ear Wireless TWS Under Armour Black', 'JBL In-Ear Wireless TWS Under Armour Red', 'JBL In-Ear with Mic. T110', 'JBL In-Ear with Mic. T110 Blue', 'JBL In-Ear with Mic. T110 White', 'JLAB Headphone Wireless Go Work Black', 'Jlab Headphone Wireless Rewind Retro Black', 'Jlab Headphone with Mic. Wireless Studio Pro Over Ear Black', 'Jlab In-Ear Wireless TWS Epic Air ANC Black', 'Jlab In-Ear Wireless TWS Epic Air Sport ANC Black', 'Jlab In-Ear Wireless TWS Go Air Black', 'Jlab In-Ear Wireless TWS Go Air Blue Black', 'Jlab In-Ear Wireless TWS Go Air Green Black', 'Jlab In-Ear Wireless TWS Jbuds Air Sport Black', 'Lenovo Gaming Headset IdeaPad  H100', 'Logitech Gaming Headset G PRO X Wireless', 'Logitech Gaming Headset G333 White', 'Logitech Gaming Headset G335 Wired', 'Logitech Gaming Headset G435 Lightspeed', 'Logitech Gaming Headset Pro X League of Legends Edition', 'Marshall In-Ear Wireless TWS Mode II Black', 'Marshall In-Ear with Mic. Mode EQ Black and Brass', 'Master and Dynamic In-Ear Wireless TWS MW07 GO Electric Blue', 'Master and Dynamic In-Ear Wireless TWS MW07 GO Flame Red', 'Master and Dynamic In-Ear Wireless TWS MW07 PLUS Black Pearl', 'Master and Dynamic In-Ear Wireless TWS MW07 PLUS Tortoise Shell', 'Master and Dynamic In-Ear Wireless TWS MW08 Black/Matte Black', 'Master and Dynamic In-Ear Wireless TWS MW08 Blue/Polished Graphite', 'Master and Dynamic In-Ear Wireless TWS MW08 White/Polished Silver', 'Monster In-Ear Wireless TWS Clarity 102 Airlinks', 'Motorola Bluetooth Headset HK255 Black', 'Motorola In-Ear Headphone Pace 125 Red', 'Motorola In-Ear Headphone Pace 200 Silver', 'Motorola In-Ear Pace 125 Black', 'Motorola In-Ear Pace 200 Gold', 'Motorola In-Ear Wireless Headset Verveloop 200 Black', 'Motorola In-Ear Wireless TWS Headset Verebuds 200 Sport Red', 'Motorola In-Ear Wireless TWS Headset Verebuds 200 Sport Royal Blue', 'Motorola In-Ear Wireless TWS Headset Verebuds 200 Sport Black', 'Motorola In-Ear Wireless TWS Vervebuds 100 Black', 'Motorola In-Ear Wireless TWS Vervebuds 100 White', 'Motorola In-Ear Wireless TWS Vervebuds 110 White', 'Motorola In-Ear Wireless TWS Vervebuds 400 Black', 'Nubwo Gaming Headset X80 Pro Wireless', 'Nubwo Gaming Headset X85 RGB', 'Nubwo Gaming Headset X98 Ping Edition', 'Onikuma Gaming Headset B60 Bluetooth Black', 'Onikuma Gaming Headset K10 Pro RGB Black', 'Onikuma Gaming Headset K20 RGB 7.1 Orange/Black', 'Onikuma Gaming Headset K9 3.5mm', 'Onikuma Gaming Headset K9 3.5mm (Special Edition Black)', 'Onikuma Gaming Headset K9 3.5mm (Special Edition Green)', 'Onikuma Gaming Headset K9 7.1 Power Honor Black', 'Onikuma Gaming Headset X11 RGB Limited Edition', 'Onikuma Gaming Headset X15 Pro RGB Black', 'Onikuma Gaming Headset X20 RGB 7.1 Black', 'Onikuma Gaming Headset X7 Pro 3.5 with RGB Black', 'QPLUS Braided Heaphone 3.5 Plug', 'QPLUS Braided Heaphone Type-C Plug', 'QPLUS Colorful Wired Headphone 3.5mm Blue', 'QPLUS Colorful Wired Headphone 3.5mm Grey', 'QPLUS Colorful Wired Headphone 3.5mm Pink', 'QPLUS Colorful Wired Headphone 3.5mm Yellow', 'QPLUS Earbud with Mic. SMT-16 Red', 'QPLUS Headphone QH002 Black', 'QPLUS Headphone Wireless ED-03', 'QPLUS In-Ear with Mic. K12 Black', 'QPLUS In-Ear with Mic. K12 White', 'QPLUS In-Ear with Mic. SF1', 'QPLUS In-Ear with Mic. STC-03 Black', 'QPLUS In-Ear with Mic. Wireless BT3 Black', 'QPLUS In-Ear with Mic. Wireless BT4 Black', 'QPLUS In-Ear with Mic. Wireless S5', 'QPLUS TWS BT12 White', 'QPLUS TWS Candy SQ-W6 Black', 'QPLUS TWS Candy SQ-W6 Mint', 'QPLUS TWS Candy SQ-W6 Pink', 'Razer Gaming Headset Barracuda X Wireless Black', 'Razer Gaming Headset Kraken V3 Hypersense', 'Razer Gaming Headset Opus X', 'Realme Buds Air 2', 'Realme Buds Air Pro (RMA210) White', 'Realme Buds Classic', 'Realme Buds Q (RMA215)', 'Rizz In-Ear With mic Model REM-1215C White', 'Rizz In-Ear With mic Model REM-1217C Black', 'Sennheiser Headphone TWS CX Plus TW Black', 'Sennheiser Headphone TWS CX Plus TW White', 'Sennheiser Headphone with Mic. Wireless TWS CX200TW', 'Sennheiser Headphone with Mic. Wireless TWSCX400TW1 White', 'Sennheiser In-Ear Wireless CX 150BT Black', 'SIGNO Gaming Headphone In-Ear SPACER EP-619 Black', 'Signo Gaming Headset 7.1 Striker HP-832', 'Signo Gaming Headset Bazzle HP-833 7.1 Black', 'Signo Gaming Headset Brexxon HP-830 7.1 Black', 'Skullcandy Headphone with Mic. Wireless TWS Dime Black Red', 'Skullcandy Headphone with Mic. Wireless TWS Indy EVO True Bleck', 'Skullcandy Headphone with Mic. Wireless TWS Sesh EVO Black Red', 'Sony Headphone with Mic. MDR ZX310AP Black', 'Sony Headphone with Mic. MDR ZX310AP Blue', 'Sony Headphone with Mic. MDR ZX310AP Red', 'Sony Headphone with Mic. Wireless TWS WF-1000XM3BME Silver', 'Sony Headphone with Mic. Wireless TWS WF-1000XM3BME Black', 'Sony Headphone with Mic. Wireless TWS WF-1000XM4', 'Sony Headphone with Mic. Wireless TWS WF-C500', 'Sony Headphone with Mic. Wireless TWS WF-SP800N/LME Blue', 'Sony Headphone with Mic. Wireless TWS WF-SP800N/WME White', 'Sony Headphone with Mic. Wireless WH-1000XM4BME Black', 'Sony Headphone with Mic. Wireless WH-1000XM4SME Silver', 'Sony In Ear with Mic. Wireless WI-SP510/DZ E Orange', 'Sony In Ear with Mic. Wireless WI-SP510/WZ E White', 'SteelSeries Gaming Headset Arctis 7 Plus Black', 'SteelSeries Gaming Headset Arctis 7P Plus Wireless White', 'Sudio Earbud Wireless TWS NIO', 'Sudio In-Ear Wireless TWS ETT Black', 'Sudio In-Ear Wireless TWS ETT Green', 'Sudio In-Ear Wireless TWS ETT Pink', 'Sudio In-Ear Wireless TWS ETT White', 'TECHPRO Earbud Headphone with Mic. 3.5mm Black', 'TECHPRO Earbud Headphone with Mic. 3.5mm White', 'TECHPRO Earbud with Mic. S12 Black', 'TECHPRO Headphone TWS Matellic Gray', 'TECHPRO Headphone TWS S1 Black', 'TECHPRO Headphone Wireless ED-02 Black', 'TECHPRO Headphones TH002-BK Black', 'TECHPRO In-Ear Wireless TE001 Black', 'TECHPRO In-Ear Wireless TE001 Blue', 'TECHPRO In-Ear Wireless TE001 Red', 'TECHPRO In-ear with Mic Type-C Wired Headphones', 'TECHPRO In-Ear with Mic. EL112 Black', 'TECHPRO In-Ear with Mic. EL112 Red', 'TECHPRO In-Ear with Mic. EL112 White', 'TECHPRO In-Ear with Mic. EL122 Silver', 'TECHPRO In-Ear with Mic. K14 Black', 'TECHPRO In-Ear with Mic. K14 White', 'TECHPRO In-Ear with Mic. Wireless BT2 Black', 'TheCoopidea In-Ear Wireless TWS Beans Air Ash', 'TheCoopidea In-Ear Wireless TWS Beans Air Sakura', 'TheCoopidea In-Ear Wireless TWS Beans Air Turquoise', 'TheCoopidea In-Ear Wireless TWS Sanrio Beans Little Twin Stars', 'TheCoopidea In-Ear Wireless TWS Sanrio Beans My Melody', 'Urbanears Earbud with Mic. Wireless Jakan Ash Grey', 'Urbanears Headphone with Mic. Wireless TWS Alby Charcoal Black', 'Urbanears Headphone with Mic. Wireless TWS Alby Dusty White', 'Urbanears Headphone with Mic. Wireless TWS Alby Teal Green', 'Urbanears Headphone with Mic. Wireless TWS Alby True Maroon', 'Urbanears Headphone with Mic. Wireless TWS Alby Ultra Violet', 'Urbanears Headphone with Mic. Wireless TWS Luma Charcoal Black', 
#     'Urbanears Headphone with Mic. Wireless TWS Luma Dustry White', 'Urbanears Headphone with Mic. Wireless TWS Luma Teal Green', 'Urbanears Headphone with Mic. Wireless TWS Luma True Maroon', 'Urbanears Headphone with Mic. Wireless TWS Luma Ultra Violet', 'Xiaomi Buds 3', 'Xiaomi Buds 3T Pro', 'Xiaomi In-Ear Headphones Basic Black', 'Xiaomi Mi FlipBuds Pro Black', 'Xiaomi Mi In-Ear Headphones Basic SL White (14274)', 'Xiaomi Mi True Wireless Earphones 2 Basic White', 'Xiaomi Redmi Buds 3 Lite', 'Xiaomi Redmi Buds 3 Pro', 'Xiaomi Redmi Buds 3 White', ' Blue Box BB001', ' QPLUS In-Ear with Mic. SF1', 'หู Shokz Openrun', 'หู Shokz Openrun Pro', ' Fantech Gaming Headset HG20 RGB Black', ' Shokz Openmove', ' B&O รุ่น BEOPLAY EQ', ' Beats Fit Pro', ' Beats Flex', ' Beats Powerbeats Pro', ' Beats Studio Buds', ' Fender Tour', ' Huawei Freebuds 4i True Wireless', ' Jabra Elite 4 Active', ' JBL Reflect Flow Pro', ' Jlab Go Air Pop', ' Motorola MOTO BUDS 085', ' Motorola Moto Buds 100', ' Realme Buds Air3 (RMA2105)']

#     nameList = []
    
#     for name in currentHeadGearName:
#         for word in removeWords:
#             if word in name:
#                 name = name.replace(word, "")
#                 name = name.replace("  ", " ")
#             name = name.strip()
#         name = name.replace("G PRO", "GPRO")
#         nameList.append(name)
    
#     print(nameList)
#     print("Length: " + str(len(nameList)))
#     return JsonResponse(nameList, safe=False)


############################# HeadGear IHaveCPU ########################
@csrf_exempt
def addHeadGearIHaveCpu(request):
    # get all headgear from IHaveCPU
    lis = webScrap.ihavecpu("headphone")

    # filter only needed info and to ihavecpuHeadGear
    removeWords = ["-", "BUFFY","LIGHTSPEED", "EARBUDS", "EARPHONES", "WIRELESS", "WIRELESS X", "(2.1)", "Virtual", "7.1", "(IN EAR)", "IN EAR", "INEAR", "USB", "SPACER", "OPEN ACOUSTIC ", 
    "TPYEC", "EARBUD", "GAMING", "Gaming", "MASTERPULSE", "EARPHONE", "& LILAC", "& RASPBERRY", "& NEON YELLOW", "LIGHTSYNC", "HEADSET", "Channels", "TRUE", "SURROUND", "SOUND"]
    # colors = ["BLACK", "WHITE", "BLUE", "RED", "OFFWHITE"]
    ihavecpuHeadGear = []
    nameList = []
    nameTemp = ""
    
    for item in lis:
        # renaming for "RegularName"
        regularTemp = ""
        nameTemp = item["name"]
        
        if item["name"] == "VH500 Virtual 7.1 Channels Gaming ":
            print("delete --> ", item["name"])
            continue

        if item["name"] not in nameList:
            nameList.append(item["name"])
            for word in removeWords:
                nameTemp = nameTemp.replace(word, "")
                nameTemp = nameTemp.replace("  ", " ")
            nameTemp = nameTemp.replace("G PRO", "GPRO")

            regularTemp = (item["brand"] + " " + nameTemp).strip()
            dataDict = {
                "Name": (item["name"]),
                "Brand": item["brand"],
                "PictureLink": item["img_url"],
                "Detail": item["description"],
                "Banana": "0",
                "Ihavecpu": item["price"],
                "RegularName": regularTemp
            }
            ihavecpuHeadGear.append(dataDict)
    
        # add to database
        if headgearAdd(dataDict) == False:
            print("Cannot add --> ", item["name"])
    return JsonResponse(ihavecpuHeadGear, safe=False)

# @csrf_exempt
# def testRenamingIHavHeadGear(request):
#     currentHeadGearName = [
    "OPEN ACOUSTIC GAME ONE BLACK ",
    "KRAKEN X BLACK ",
    "HAMMERHEAD PRO V2 ",
    "G333 BUFFY IN EAR WHITE ",
    "G333 BUFFY IN EAR BLACK ",
    "G435 LIGHTSPEED WIRELESS -BLACK & NEON YELLOW ",
    "G435 LIGHTSPEED WIRELESS - OFF-WHITE & LILAC ",
    "G435 LIGHTSPEED WIRELESS -BLUE & RASPBERRY ",
    "X CLOUD EARBUD EARPHONES - RED ",
    "ROG CETRA II (IN EAR) USB TPYE-C ",
    "X98 7.1 BLACK ",
    "G431 7.1 SURROUND SOUND ",
    "BLACKSHARK V2 PRO ",
    "MASTER MASTERPULSE MH630 ",
    "G PRO X WIRELESS LIGHTSPEED ",
    "HAMMERHEAD TRUE WIRELESS X - EARBUDS - BLACK ",
    "EP-619 SPACER IN-EAR GAMING EARPHONES ",
    "G PRO X GAMING BLACK - USB ",
    "G335 BLACK ",
    "G335 WHITE ",
    "ROG CETRA II CORE (IN EAR) ",
    "G633S 7.1 LIGHTSYNC BLACK ",
    "DS502 GAMING ",
    "G331 GAMING (2.1) ",
    "TYPE H8 GAMING HEADSET ",
    "VH500 Virtual 7.1 Channels Gaming "
# ]
#     return JsonResponse("", safe=False)


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