from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from Webapp import views as webapp

# web scarping
from bs4 import BeautifulSoup
import requests
import csv

# regular expression
import re

# lis = []
# data = {"Name":20,"Brand":"20"}
# lis.append(data)
# nub = data["Name"]
# for i in range(1,5):
#     dic = {"Name":nub+i,"Brand":nub+i}
#     lis.append(dic)


def helloFromWebScr(request):
    # return JsonResponse("Hello", safe=False)
    return JsonResponse(Banana("headphone"), safe=False)

def helloBanana(request):
    return JsonResponse(Banana("mouse"), safe=False)

def helloIhaveCPU(request):
    return JsonResponse(ihavecpu("keyboard"), safe=False)

@csrf_exempt
def throwTest(request):
    res = webapp.catchTest(lis)
    if res == True:
        return JsonResponse("Added", safe=False)
    else:
        return JsonResponse("Failed to Added", safe=False)

# use like Banana("mouse") , Banana("keyboard") , Banana("headphone")


def Banana(device):
    def getDescription(link):
        res = requests.get(link)
        res.encoding = "utf-8"
        soup = BeautifulSoup(res.text, 'html.parser')
        description = soup.find(
            "div", {"class": "product-short-description html-content"})
        # print(description)
        # print(description.text)
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
                # print(info[j].text[1:-1],info[j+1].text[1:-1])
            if feature:
                return feature
            return "ไม่มีข้อมูล"
        else:
            return "ไม่มีข้อมูล"

    if device == "mouse":
        url = "https://www.bnn.in.th/th/p/gaming-gear/pc-gaming-accessories/gaming-mouse?page="
        # url = "https://www.bnn.in.th/th/p/it-accessories/mouse-and-keyboards/mouse-1?page="
    elif(device == "keyboard"):
        url = "https://www.bnn.in.th/th/p/gaming-gear/pc-gaming-accessories/gaming-keyboard?page="
        # url = "https://www.bnn.in.th/th/p/it-accessories/mouse-and-keyboards/keyboard-and-numpad?page="
    elif(device == "headphone"):
        url = "https://www.bnn.in.th/th/p/gaming-gear/pc-gaming-accessories/gaming-headphone?page="
        # url = "https://www.bnn.in.th/th/p/home-entertainment/headphone?page="

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
        # link = soup.find_all("a", {"class": "product-item"}).get("href")
        # productInfo = soup.find_all("div", {"class": "product-short-attribute"})
        img_url = soup.find_all("img", {"class": "image"})

        for i in range(len(name)):
            # # use regular expression for get just name model
            # model = re.findall("Mouse .*", name[i].string[1:-1])
            # if(len(model) > 0):
            #     model = model[0][6:]
            # else:
            #     model = re.findall(
            #         brand[i].string[1:-1] + " .*", name[i].string[1:-1])
            #     # model = model[0][len(brand[i].string[1:-1])+1:]
            # print(model)
            obj = {
                "name": name[i].text[1:-1],
                "brand": brand[i].string[1:-1],
                "link": "https://www.bnn.in.th"+link[i].get("href"),
                # "productInfo": productInfo[i].string[1:-1],
                "bananaPrice": price[i].string[2:-1],
                "img_url": img_url[i].get("src")
            }
            # description
            obj["description"] = getDescription(obj["link"])
            # feature
            obj["feature"] = getFeature(obj["link"])
            datas.append(obj)
            # print(obj)
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
