from django.shortcuts import render
import json

def stock_list(request):
    with open('stock_market_data.json') as json_file:
        data = json.load(json_file)
    return render(request, 'stocks/stock_list.html', {'stocks': data})
