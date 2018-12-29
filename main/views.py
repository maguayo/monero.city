# -*- coding: utf-8 -*-
from django.shortcuts import render
from main.forms import ListingForm
from main.models import Listing, Category
from django.http import *
import os


def home(request):
    listings = Listing.objects.all()
    dictionary = {
        'page_title': 'Monero.city - Use Moneroin your city',
        'body_class': 'page-home big-map',
        'listings': listings
    }
    return render(request, 'home.html', dictionary)



def contribute(request):
    dictionary = {
        'page_title': 'Monero.city - Use Moneroin your city',
        'body_class': 'page-contribute',
    }
    return render(request, 'contribute.html', dictionary)


def explore(request):
    dictionary = {
        'page_title': 'Monero.city - Use Moneroin your city',
        'body_class': 'page-explore',
    }
    return render(request, 'explore.html', dictionary)



def map(request):
    listings = Listing.objects.all()
    dictionary = {
        'page_title': 'Monero.city - Use Moneroin your city',
        'body_class': 'page-map big-map',
        'listings': listings
    }
    return render(request, 'map.html', dictionary)



def listings(request, category=None):

    listings = Listing.objects.filter(approved=True)

    try:
        category_obj = Category.objects.get(slug=category)
        listings = listings.filter(categories=category_obj)
    except Exception:
        category_obj = None

    dictionary = {
        'page_title': 'Monero.city - Use Moneroin your city',
        'body_class': 'page-listings',
        'listings': listings,
        'category_obj': category_obj
    }
    return render(request, 'listings.html', dictionary)




def listings_online(request, category=None):
    listings = Listing.objects.filter(approved=True)

    try:
        category_obj = Category.objects.get(slug="online")
    except Exception:
        category_obj = None

    dictionary = {
        'page_title': 'Monero.city - Use Moneroin your city',
        'body_class': 'page-listings listing-no-map',
        'listings': listings,
        'category_obj': category_obj
    }
    return render(request, 'listings-no-map.html', dictionary)



def add_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = Listing()
            listing.name = form.cleaned_data["name"]
            listing.email = form.cleaned_data["email"]
            listing.image = form.cleaned_data["image"]
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
