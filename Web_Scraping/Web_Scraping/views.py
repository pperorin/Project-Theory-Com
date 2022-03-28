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
    return JsonResponse("Hello", safe=False)


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
        return description.text

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
    elif(device == "keyboard"):
        url = "https://www.bnn.in.th/th/p/it-accessories/mouse-and-keyboards/keyboard-and-numpad?in_stock=true&page="
    elif(device == "headphone"):
        url = "https://www.bnn.in.th/th/p/home-entertainment/headphone?in_stock=true&page="
    
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
            "name": name[i].string[1:-1],
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
