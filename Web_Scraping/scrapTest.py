# web scarping
from bs4 import BeautifulSoup
from pip import main
import requests
import csv
import json

# regular expression
import re

notGoodName = ["Micropack Wireless Mouse + Keyboard KM-203W Black (TH/EN)","Rapoo Bluetooth and Wireless Mouse + Keyboard 8000M (TH/EN) (EO)","Rapoo Wireless Mouse + Keyboard 1800S Black (TH/EN) (EO)"]
colorLis = ["BLACK","BLUE","WHITE","GREEN","RED","YELLOW", "GREY", "PINK", "PURPLE"]



def Banana(device):
    def getDescription(link):
        res = requests.get(link)
        res.encoding = "utf-8"
        soup = BeautifulSoup(res.text, 'html.parser')
        description = soup.find(
            "div", {"class": "product-short-description html-content"})
        if description.text != None:
            return description.text
        else:
            return "ไม่มีข้อมูล"

    def getFeature(link):
        feature = {}
        res = requests.get(link)
        res.encoding = "utf-8"
        soup = BeautifulSoup(res.text, 'html.parser')
        table = soup.find(
            "table", {"class": "product-detail-specification-table table -striped"})
        if table != None:
            info = table.find_all("td")
            for j in range(0, len(info), 2):
                feature[info[j].text[1:-1]] = info[j+1].text[1:-1]
            if feature:
                return feature
            return "ไม่มีข้อมูล"
        else:
            return "ไม่มีข้อมูล"

    if device == "mouse":
        url = "https://www.bnn.in.th/th/p/gaming-gear/pc-gaming-accessories/gaming-mouse?page="
    elif(device == "keyboard"):
        url = "https://www.bnn.in.th/th/p/gaming-gear/pc-gaming-accessories/gaming-keyboard?page="
    elif(device == "headphone"):
        url = "https://www.bnn.in.th/th/p/gaming-gear/pc-gaming-accessories/gaming-headphone?page="

    # find the number of pages
    res = requests.get(url + "1")
    res.encoding = "utf-8"
    soup = BeautifulSoup(res.text, 'html.parser')
    page = soup.find_all("button", {"class": "vmq-pagination-link"})
    numberOfPage = int(page[-1].text[1:-1])

    datas = []
    for numPage in range(1, numberOfPage+1):
        print("Now page is: ", numPage)
        # res = requests.get(url+str(numPage))
        res = requests.get(url+str(numPage))
        # res = requests.get(url[input]+str(1))
        res.encoding = "utf-8"
        soup = BeautifulSoup(res.text, 'html.parser')

        name = soup.find_all("div", {"class": "product-name"})
        brand = soup.find_all("div", {"class": "product-label-brand"})
        price = soup.find_all("div", {"class": "product-price"})
        link = soup.find_all("a", {"class": "product-item"})
        img_url = soup.find_all("img", {"class": "image"})

        for i in range(len(name)):
            obj = {
                "name": name[i].text[1:-1],
                "brand": brand[i].string[1:-1],
                "link": "https://www.bnn.in.th"+link[i].get("href"),
                "bananaPrice": price[i].string[2:-1],
                "img_url": img_url[i].get("src")
            }
            obj["description"] = getDescription(obj["link"])
            obj["feature"] = getFeature(obj["link"])
            datas.append(obj)
    return datas


def ihavecpu(device):
    def getDescription(link):
        res = requests.get(link)
        soup = BeautifulSoup(res.text, 'html.parser')
        location = soup.find("tr", {"class": "descTR"})
        description = location.find("td", {"class": "bodyTD"})
        return description.text

    if(device == "mouse"):
        url = "https://www.ihavecpu.com/category/251/gaming-gear-%E0%B8%AD%E0%B8%B8%E0%B8%9B%E0%B8%81%E0%B8%A3%E0%B8%93%E0%B9%8C%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%84%E0%B8%99%E0%B9%80%E0%B8%A5%E0%B9%88%E0%B8%99%E0%B9%80%E0%B8%81%E0%B8%A1/mouse-%E0%B9%80%E0%B8%A1%E0%B8%B2%E0%B8%AA%E0%B9%8C?tskp="
    elif(device == "keyboard"):
        url = "https://www.ihavecpu.com/category/250/gaming-gear-%E0%B8%AD%E0%B8%B8%E0%B8%9B%E0%B8%81%E0%B8%A3%E0%B8%93%E0%B9%8C%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%84%E0%B8%99%E0%B9%80%E0%B8%A5%E0%B9%88%E0%B8%99%E0%B9%80%E0%B8%81%E0%B8%A1/keyboard-%E0%B8%84%E0%B8%B5%E0%B8%A2%E0%B9%8C%E0%B8%9A%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B8%94?tskp="
    elif(device == "headphone"):
        url = "https://www.ihavecpu.com/category/249/gaming-gear-%E0%B8%AD%E0%B8%B8%E0%B8%9B%E0%B8%81%E0%B8%A3%E0%B8%93%E0%B9%8C%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%84%E0%B8%99%E0%B9%80%E0%B8%A5%E0%B9%88%E0%B8%99%E0%B9%80%E0%B8%81%E0%B8%A1/gaming-headset-%E0%B8%AB%E0%B8%B9%E0%B8%9F%E0%B8%B1%E0%B8%87?tskp="

    res = requests.get(url)
    res.encoding = "utf-8"
    soup = BeautifulSoup(res.text, 'html.parser')
    page = soup.find_all("div", {"class": "numberBox"})
    datas = []
    if page == []:
        print("1 Page Case")
        res = requests.get(url+str(1))
        soup = BeautifulSoup(res.text, 'html.parser')

        allCard = soup.find(
            "div", {"class": "productsArea tsk-dataview thumbnailArea size-250r frame-000"})
        card = allCard.find_all(
            "div", {"class": "productArea productItem"})

        for i in range(len(card)):
            device = card[i].find_all("a", {"class": "gadgetThumbnail"})
            # name
            patternName = "\"name\":.*\"price"
            name = re.findall(patternName, device[0].get("gaeepd"))
            # brand
            brand = re.split("\s", name[0][8:-8])[1]
            # price
            patternPrice = "price\":.*,\"category"
            price = re.findall(patternPrice, device[0].get("gaeepd"))
            # link
            link = device[0].get("href")
            # image
            imageLink = device[0].find("img").get("data-src")
            # description
            description = getDescription(link)

            obj = {
                "name": name[0][8:-8],
                "brand": brand,
                "price": int(price[0][8:-14]),
                "img_url": imageLink,
                "description": description
            }
            datas.append(obj)
        return datas
    else:
        numberOfPage = int(page[-1].text)
        for numPage in range(1, numberOfPage + 1):
            print("Now page is: ", numPage)
            res = requests.get(url+str(numPage))
            soup = BeautifulSoup(res.text, 'html.parser')

            allCard = soup.find(
                "div", {"class": "productsArea tsk-dataview thumbnailArea size-250r frame-000"})
            card = allCard.find_all(
                "div", {"class": "productArea productItem"})

            for i in range(len(card)):
                device = card[i].find_all("a", {"class": "gadgetThumbnail"})
                # name
                patternName = "\"name\":.*\"price"
                name = re.findall(patternName, device[0].get("gaeepd"))
                # brand
                brand = re.split("\s", name[0][8:-8])[1]
                # price
                patternPrice = "price\":.*,\"category"
                price = re.findall(patternPrice, device[0].get("gaeepd"))
                # link
                link = device[0].get("href")
                # image
                imageLink = device[0].find("img").get("data-src")
                # description
                description = getDescription(link)

                obj = {
                    "name": name[0][8:-8],
                    "brand": brand,
                    "price": int(price[0][8:-14]),
                    "img_url": imageLink,
                    "description": description
                }
                datas.append(obj)
        return datas






def addMouseFromBanana():
    lis = Banana("mouse")
    temp =""
    bananaMouse = []
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

    return bananaMouse

################################ add IhaveCPU Mouse ##########################
def addMouseFromIHav():
    colLis = ["BLACK","WHITE","GREY","PINK","LILAC","BLUE"]
    lis = ihavecpu("mouse")
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
        datLis.append(dat)
        
    return datLis

def addKBFromBanana():
    # get all keyboard from Banana
    lis = Banana("keyboard")

    # lisName = list()
    bananaKB = list()
    removeWords = [" Gaming Keyboard Mechanical", " Gaming Keyboard", " Mechanical", " Gateron", " (Red Switch)", " (Hot-swappable)", " (Optical SW)", " Mini RGB", " RGB", "."]

    for item in lis:

        itemSerial = ""
        regularTemp = ""
        nameTemp = item["name"]

        # Renaming Item
        for removeWord in removeWords:
            nameTemp = nameTemp.replace(removeWord, "")
        nameTemp = nameTemp.replace("G Pro X", "GPROX")
        nameTemp = nameTemp.replace("G Pro", "GPRO")

        # Filter Item Serial for RegularName
        for namePart in nameTemp.split():
            if (re.findall("[0-9]+", namePart)) != []:
                if len(namePart) <= 2:
                    continue
                itemSerial = namePart
                break
            elif (re.findall("GPROX", namePart)) != []:
                itemSerial = namePart
                break
            elif (re.findall("GPRO", namePart)) != []:
                itemSerial = namePart
                break
            elif (re.findall("Laite", namePart)) != []:
                itemSerial = "CYNOSA LITE ESSENTIAL"
                break
        
        if itemSerial != "":
            regularTemp = item["brand"] + " " + itemSerial
        else:
            regularTemp = nameTemp

        # Create data format
        dat = {
            "Name": item["name"],
            "Brand": item["brand"],
            "PictureLink": item["img_url"],
            "Detail": item["description"],
            "Banana": item["bananaPrice"],
            "Ihavecpu": "0",
            "RegularName": regularTemp
            # "Color": i["feature"]["Color"]
        }
        bananaKB.append(dat)
        
    return bananaKB

def addKBFromIHaveCpu():
    # get all keyboard from IHaveCPU
    lis = ihavecpu("keyboard")

    # filter only needed info and add into ihaveCpuKey
    ihavecpuKeyboard = []
    nameList = []
    removeWords = ["-", "/ ", "(EN/TH)", "[TH/EN]", "[EN/TH]",  "(EN)", "TH/EN", "(RGB LED)", "(MEMBRANE) ", "GAMING ", "KEYBOARD "]
    # switchType = ["PRO ","BLUE SWITCH", "RED SWITCH", "CLICKY", "TACTILE", "NX BLUE", "NX BROWN"]

    lisRegName = list()

    for item in lis:
        
        # renaming for "RugularName"
        regularTemp = ""
        nameTemp = ""
        itemSerial = ""
        # itemType = ""
        if item["name"] not in nameList:
            # for checking duplicate
            nameList.append(item["name"])
            nameTemp = item["name"]
            for word in removeWords:
                nameTemp = nameTemp.replace(word, "")
            nameTemp = nameTemp.replace("G PRO X", "GPROX")
            nameTemp = nameTemp.replace("G PRO", "GPRO")
            for namePart in nameTemp.split():
                if re.findall("[0-9]+", namePart) != []:
                    itemSerial = namePart
                    break
                elif re.findall("STRIX", namePart) != []:
                    itemSerial = namePart
                    break
                elif re.findall("GPROX", namePart) != []:
                    itemSerial = namePart
                    break
                elif re.findall("GPRO", namePart) != []:
                    itemSerial = namePart
                    break
            # for word in switchType:
            #     if re.findall(word, nameTemp) != []:
            #         itemType = word

            regularTemp = item["brand"]
            if itemSerial != "":
                regularTemp += item["brand"] + " " + itemSerial
                # if itemType != "":
                #     regularTemp += " " + itemType
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
            print(dataDict["RegularName"]+" step 5")
            ihavecpuKeyboard.append(dataDict)
            lisRegName.append(dataDict["RegularName"])

    return ihavecpuKeyboard

def addHeadGearBanana():
    # get all headgear from Banana
    lis = Banana("headphone")
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

    return bananaHeadGear

def addHeadGearIHaveCpu():
    # get all headgear from IHaveCPU
    lis = ihavecpu("headphone")

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

    return ihavecpuHeadGear


# mouseIHav = addMouseFromIHav()
# mouseBanana = addMouseFromBanana()
kbIHav = addKBFromIHaveCpu()
kbBanana = addKBFromBanana()
hgIhav = addHeadGearIHaveCpu()
hgBanana = addHeadGearBanana()

# for i in mouseBanana:
#     i = json.dumps(i)
#     req = requests.post("https://theorybackend.herokuapp.com/AddMouse", i)
#     print(req)
# print("Complete Mouse Banana")
# for i in mouseIHav:
#     i = json.dumps(i)
#     req = requests.post("https://theorybackend.herokuapp.com/AddMouse", i)
#     print(req)
# print("Complete Mouse Ihave")
for i in kbBanana:
    i = json.dumps(i)
    req = requests.post("https://theorybackend.herokuapp.com/AddKeyBoard", i)
    print(req)
print("Complete KB Banana")
for i in kbIHav:
    i = json.dumps(i)
    req = requests.post("https://theorybackend.herokuapp.com/AddKeyBoard", i)
    print(req)
print("Complete KB Ihave")
for i in hgBanana:
    i = json.dumps(i)
    req = requests.post("https://theorybackend.herokuapp.com/AddHeadGear", i)
    print(req)
print("Complete HG Banana")
for i in hgIhav:
    i = json.dumps(i)
    req = requests.post("https://theorybackend.herokuapp.com/AddHeadGear", i)
    print(req)
print("Complete HG Ihave")


    
    

