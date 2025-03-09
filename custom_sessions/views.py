from django.http import HttpResponse
from django.shortcuts import render


def create_session(request):
    request.session["key1"] = "value1"
    return HttpResponse(f'created session: {request.session["key1"]}')


def read_session(request):
    print(request.session["key1"])
    return HttpResponse(f'{request.session["key1"]}')


def delete_session(request):
    session = request.session["key1"]
    del request.session["key1"]
    request.session.modified = True
    print(f"SESSION: {request.session["key1"]}")
    return HttpResponse(f"{session}")
