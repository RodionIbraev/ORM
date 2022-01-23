from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')

def show_catalog(request):
    sort_1 = request.GET.getlist('sort')
    arg_sort = {
        'name': 'name',
        'max_price': '-price',
        'min_price': 'price'
    }
    if sort_1:
        response = [obj for obj in Phone.objects.all().order_by(arg_sort[sort_1[0]])]
    else:
        response = [obj for obj in Phone.objects.all()]
    template = 'catalog.html'
    context = {
        'phones': response
    }
    return render(request, template, context)


def show_product(request, slug):
    name = ' '.join(slug.split('-'))
    template = 'product.html'
    context = {
        'phone': Phone.objects.filter(name=name)[0]
    }
    return render(request, template, context)