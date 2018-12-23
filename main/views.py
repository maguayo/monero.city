# -*- coding: utf-8 -*-
from django.shortcuts import render
from main.forms import ListingForm
from main.models import Listing
from django.http import *
import os


def home(request):
    listings = Listing.objects.all()
    dictionary = {
        'page_title': 'Monero.city - Use Moneroin your city',
        'body_class': 'home',
        'listings': listings
    }
    return render(request, 'home.html', dictionary)



def contribute(request):
    dictionary = {
        'page_title': 'Monero.city - Use Moneroin your city',
        'body_class': 'contribute',
    }
    return render(request, 'contribute.html', dictionary)


def explore(request):
    dictionary = {
        'page_title': 'Monero.city - Use Moneroin your city',
        'body_class': 'explore',
    }
    return render(request, 'explore.html', dictionary)



def listings(request):
    listings = Listing.objects.all()
    dictionary = {
        'page_title': 'Monero.city - Use Moneroin your city',
        'body_class': 'listings',
        'listings': listings
    }
    return render(request, 'listings.html', dictionary)



def add_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = Listing()
            listing.name = form.cleaned_data["name"]
            listing.email = form.cleaned_data["email"]
            listing.phone = form.cleaned_data["phone"]
            listing.website = form.cleaned_data["website"]
            listing.map_lat = form.cleaned_data["latitude"]
            listing.map_long = form.cleaned_data["longitude"]
            listing.address = form.cleaned_data["address"]
            listing.city = form.cleaned_data["city"]
            listing.zip_code = form.cleaned_data["zip_code"]
            listing.country = form.cleaned_data["country"]
            listing.save()
    else:
        form = ListingForm()

    dictionary = {
        'page_title': 'Monero.city - Use Moneroin your city',
        'body_class': 'add_listing', 
        'form': form
    }
    return render(request, 'listing-add.html', dictionary)
