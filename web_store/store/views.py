from django.shortcuts import render, get_object_or_404, redirect
from .models import storeItem, stockItem

# Create your views here.
def home_page(request):
    """This function takes user to homepage 

    :param request: Client request
    :return: rendered html
    """
    items = storeItem.objects
    return render(request, 'store_templates/home_page.html', {'items': items})

def stock_page(request, storeItem_id):
    """This function takes user to the stock page

    :param request: Client request
    :param storeItem_id: store item id
    :return: rendered html
    """
    brand = get_object_or_404(storeItem, pk=storeItem_id)
    items = stockItem.objects.all()
    return render(request, 'store_templates/stock_page.html', {'brand': brand, 'items': items})

def confirmation_page(request, stockItem_id):
    """This function takes user to the order confirmation page

    :param request: Client request
    :param storeItem_id: stock id
    :return: rendered html
    """
    item = get_object_or_404(stockItem, pk=stockItem_id)
    return render(request, 'store_templates/confirmation_page.html', {'item': item})


def successful_reg_page(request):
    """This function takes user to successful registration page 

    :param request: Client request
    :return: rendered html
    """
    return render(request, 'store_templates/successful_reg.html', {})


def successful_order(request):
    """This function takes user to successful order page 

    :param request: Client request
    :return: rendered html
    """
    return render(request, 'store_templates/successful_order.html', {})
