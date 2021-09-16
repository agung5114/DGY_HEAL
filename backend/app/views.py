# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template

@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'profil.html' )
    return HttpResponse(html_template.render(context, request))

# @login_required(login_url="/login/")
# def pages(request):
#     context = {}
#     # All resource paths end in .html.
#     # Pick out the html file name from the url. And load that template.
#     try:
        
#         load_template      = request.path.split('/')[-1]
#         context['segment'] = load_template
        
#         html_template = loader.get_template( load_template )
#         return HttpResponse(html_template.render(context, request))
        
#     except template.TemplateDoesNotExist:

#         html_template = loader.get_template( 'page-404.html' )
#         return HttpResponse(html_template.render(context, request))

#     except:
    
#         html_template = loader.get_template( 'page-500.html' )
#         return HttpResponse(html_template.render(context, request))

# @login_required(login_url="/login/")
# def nasional(request):
#     return render(request,'nasional.html')

# # @login_required(login_url="/login/")
# def regional(request):
#     return render(request,'regional.html')

# # @login_required(login_url="/login/")
# def analytics(request):
#     return render(request,'analytics.html')
@login_required(login_url="/login/")    
def makan(request):
    return render(request,'makan.html')

@login_required(login_url="/login/")
def olahraga(request):
    return render(request,'olahraga.html')

@login_required(login_url="/login/")
def obat(request):
    return render(request,'obat.html')
    
# def verdict(request):
#     return render(request,'verdict.html')
    
# def ratio(request):
#     return render(request,'ratio.html')
    
# def cluster(request):
#     return render(request,'cluster.html')