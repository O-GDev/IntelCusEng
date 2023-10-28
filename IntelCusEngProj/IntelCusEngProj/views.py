from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib import messages
from IntelCusApp.serializers import MainTableSerializer
from IntelCusApp.models import MainTable
from IntelCusApp.simplifyerror import error_simplification
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from IntelCusApp import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.db.models import Sum

@login_required
def admin_dashboard(request):
    user_list = MainTable.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 5)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    labels = []
    datas = []

    queryset = MainTable.objects.values('response_code').annotate(country_population=Sum('account_number')).order_by('-threshold')
    for entry in queryset:
        labels.append(entry['response_code'])
        
    return render(request, 'admin_dashboard.html', { 'data': data,'labels': labels,'datas':datas})


class MainView(APIView):    
    def post(self, request, *args, **kwargs):
        serializer = MainTableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_code = request.data['response_code']
            simplified = error_simplification(response_code)
            return Response(simplified.data)
        return Response(serializer.errors)
    
def admin_login(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        #  Authenticate
        user = authenticate(request, username=username, password = password )
        if user is not None:
            login(request, user)
            messages.success(request,"You have successfully logged in!")
            return redirect('admin_dashboard')
        else:
            messages.success(request, "There was an error logging in!")
            return redirect('admin_login')
    else:
        return render(request, 'admin_login.html', {})  
    
   
def signout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out...")
    return redirect('admin_login')