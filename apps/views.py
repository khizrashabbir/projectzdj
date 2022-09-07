from django.shortcuts import render, redirect
from .models import *
from .forms import SubjectForm
from django.http import JsonResponse
from django.core import serializers
# Create your views here.


def index(request):
    context = {}
    context['studentMaster'] = StudentMaster.objects.all()
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
    SDetail = StudentDetail(firstname=request.POST['firstname'], lastname=request.POST['lastname'], address=request.POST['address'])
    SDetail.save()
    return redirect('/')