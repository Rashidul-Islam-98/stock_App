from django.shortcuts import render, redirect
from stocks.models import Stock
from .forms import StockForm

def stock_list(request):
    stocks = Stock.objects.all()
    return render(request, 'stocks/stock_list.html', {'stocks': stocks})

def create_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock_list')
    else:
        form = StockForm()
    return render(request, 'stocks/create_stock.html', {'form': form})

def edit_stock(request, stock_id):
    stock = Stock.objects.get(id=stock_id)
    if request.method == 'POST':
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect('stock_list')
    else:
        form = StockForm(instance=stock)
    return render(request, 'stocks/edit_stock.html', {'form': form, 'stock': stock})

def delete_stock(request, stock_id):
    stock = Stock.objects.get(id=stock_id)
    if request.method == 'POST':
        stock.delete()
        return redirect('stock_list')
    return render(request, 'stocks/delete_stock.html', {'stock': stock})
