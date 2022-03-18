from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Webapp.models import Mouse,Keyboard,HeadGear
from Webapp.serializers import MouseSerializer,KeyboardSerializer,HeadGearSerializer

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
        mouse=Mouse.objects.get(MouseId=mouse_data['MouseId'])
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
def keyboardApi(request,id=0):
    if request.method=='GET':
        keyboard = Keyboard.objects.all()
        keyboard_serializer=KeyboardSerializer(keyboard,many=True)
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
        keyboard=Keyboard.objects.get(KeyboardId=keyboard_data['KeyboardId'])
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