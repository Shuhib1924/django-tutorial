from django.http import HttpResponse
from django.shortcuts import render


def set1(request):
    response = HttpResponse("SET")
    response.set_cookie("key1", "value1")
    response.set_cookie("key2", "value2")
    return response


def get1(request):
    return HttpResponse(f"<h1>get cookie</h1><div>{request.COOKIES['key2']}</div>")


def delete1(request):
    response = HttpResponse(
        f"<h1>delete cookie</h1> <div>{request.COOKIES['key1']}</div>"
    )
    response.delete_cookie("key1")
    return response
