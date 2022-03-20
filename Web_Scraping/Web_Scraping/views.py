from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from Webapp import views as webapp



lis = []
data = {"Name":20,"Brand":"20"}
lis.append(data)
nub = data["Name"]
for i in range(1,5):
    dic = {"Name":nub+i,"Brand":nub+i}
    lis.append(dic)
    



def helloFromWebScr(request):
    return JsonResponse("Hello",safe=False)

@csrf_exempt
def throwTest(request):
    res = webapp.catchTest(lis)
    if res == True:
        return JsonResponse("Added",safe=False)
    else:
        return JsonResponse("Failed to Added",safe=False)