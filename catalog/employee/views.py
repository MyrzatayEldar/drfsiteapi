from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .forms import *
from .models import *
from .serializers import *
from django.contrib.auth import authenticate, login


class EmployeeApiView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd.get('username'), password=cd.get('password'))
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('main')
    else:
        form = LoginForm()
    return render(request, 'employee/login.html', {'form': form})


@login_required(login_url='/')
def main(request):
    user_list = Employee.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'employee/main.html', {'users': users})


@login_required(login_url='/')
def create_emp(request):
    if request.method == 'POST':
        form = EmployeeCreateForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('main')
    else:
        form = EmployeeCreateForm
    return render(request, 'employee/create_emp.html', {'form': form})
