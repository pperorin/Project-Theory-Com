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
    return JsonResponse(Banana("mouse"), safe=False)


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
        info = table.find_all("td")
        for i in range(0, len(info), 2):
            feature[info[i].text[1:-1]] = info[i+1].text[1:-1]
            # print(info[i].text[1:-1],info[i+1].text[1:-1])
        return feature

    if device == "mouse":
        url = "https://www.bnn.in.th/th/p/it-accessories/mouse-and-keyboards/mouse-1?in_stock=true&page="
        # url = "https://www.bnn.in.th/th/p/it-accessories/mouse-and-keyboards/mouse-1?page="
    elif(device == "keyboard"):
        url = "https://www.bnn.in.th/th/p/it-accessories/mouse-and-keyboards/keyboard-and-numpad?in_stock=true&page="
        # url = "https://www.bnn.in.th/th/p/it-accessories/mouse-and-keyboards/keyboard-and-numpad?page="
    elif(device == "headphone"):
        url = "https://www.bnn.in.th/th/p/home-entertainment/headphone?in_stock=true&page="
        # url = "https://www.bnn.in.th/th/p/home-entertainment/headphone?page="

    # find the number of pages
    res = requests.get(url + "1")
    res.encoding = "utf-8"
    soup = BeautifulSoup(res.text, 'html.parser')
    page = soup.find_all("button", {"class": "vmq-pagination-link"})
    numberOfPage = int(page[-1].text[1:-1])
    print("Number of pages : ", numberOfPage)

    datas = []
    for numPage in range(1, numberOfPage+1):
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
    if page == []:
        numberOfPage = 1
    else:
        numberOfPage = int(page[-1].text)

    datas = []

    for numPage in range(numberOfPage + 1):
        res = requests.get(url+str(numPage))
        soup = BeautifulSoup(res.text, 'html.parser')

        allDevice = soup.find(
            "div", {"class": "productsArea tsk-dataview thumbnailArea size-250r frame-000"})
        device = allDevice.find_all(
            "div", {"class": "productArea productItem"})
        for i in range(len(device)):
            name = device[i].find("a", {"class": "gadgetThumbnail"}).get(
                "title").split(" ")
            brand = name[1]
            realname = ""
            for i in range(2, len(name)):
                realname += name[i] + " "
            link = device[i].find(
                "a", {"class": "gadgetThumbnail"}).get("href")
            price = device[i].find(
                "div", {"class": "product_price has_currency_unit"}).text
            image_url = device[i].find("img").get("data-src")
            obj = {
                "name": realname,
                "brand": brand,
                "price": price[:-7],
                "img_url": image_url,
                "description": getDescription(link)
            }
            datas.append(obj)
    return datas
    
