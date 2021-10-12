from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import pandas as pd

# Create your views here.
def BytsLinksol(request):
    gsheet_id = '1JfZE3m-C_VEIfrdvJ97b5GjXXyTo6MVcfGxguRxhgbw'
    sheet_name = 'Sheet1'
    gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheet_id, sheet_name)

    df = pd.read_csv(gsheet_url)
    today_link = df.iloc[-1,:]['Meet Link']

    return redirect(today_link)
