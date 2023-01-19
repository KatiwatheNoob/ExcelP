from django.shortcuts import render
import pandas as pd


def index(request):
    return render(request, 'index.html')

def fetch(request):
    if request.method == 'POST':
        file = request.FILES['file']
        df = pd.read_excel(file)
        context = {'tables': [df.to_html(classes='data')], 'titles': df.columns.values}
        return render(request, 'fetch.html', context)
