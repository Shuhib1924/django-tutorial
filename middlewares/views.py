from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse

# from django.templates import TemplateResponse


def index(request):
    return render(request, "mdw.html")


def exception(request):
    raise Exception("exception from function")
    return HttpResponse("call from view function")


def templates(request):
    response = TemplateResponse(
        request, "mdw-templates.html", {"content": "content from view"}
    )
    return response
