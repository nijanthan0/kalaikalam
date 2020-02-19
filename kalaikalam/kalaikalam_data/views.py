# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd

data = pd.read_json('/home/nijanthanrajachandran/Downloads/kalaikalam-prelims-final.json')
data = data.drop(columns=['StudentNo', 'Email', 'IsRegistered', 'Pincode', 'UpdatedOn', 'Phone'])


# Create your views here.
def home(request):
    val = request.POST
    if val:
        val = val.get('username')
        print(data)
        single = data.groupby('UniqueId')
        # single = pd.DataFrame(single)
        single_data = single.get_group(val).to_dict('list')
        context = {
            'data': single_data
        }
        return render(request, 'details.html', context)

    return render(request, 'home.html')


# def display_detail(request, value):


