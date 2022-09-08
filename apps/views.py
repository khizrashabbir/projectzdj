from django.shortcuts import render, redirect
from .models import *
from .forms import SubjectForm
from django.http import JsonResponse, HttpResponse
from django.core import serializers
# Create your views here.


def index(request):
    context = {}
    context['studentMaster'] = StudentDetail.objects.all()
    return render(request, "apps/index.html", context)

def student(request):
    context = {}
    context['student'] = StudentMaster.objects.all()
    return render(request, "apps/index.html", context)


def postSubjectForm(request):
    if request.is_ajax and request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [ instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, status=400)
    return JsonResponse({"error": ""}, status=400)

def insert(request):
    if request.method == "POST":
        subject_name = request.POST.get('subjectname')
        subjectdescription = request.POST.get('subjectdescription')
        context = {
            'subject_name': subject_name,
            'subjectdescription': subjectdescription
        }
        return render(request, "apps/index.html", context)