# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import *
import os


def home(request):
    dictionary = {
        'page_title': 'Monero.city - Use Moneroin your city',
        'body_class': 'home', 
    }
    return render(request, 'home.html', dictionary)


def add_listing(request):
    dictionary = {
        'page_title': 'Monero.city - Use Moneroin your city',
        'body_class': 'add_listing', 
    }
    return render(request, 'listing-add.html', dictionary)
