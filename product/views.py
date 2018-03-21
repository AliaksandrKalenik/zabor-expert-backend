from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from product import models as mx


@csrf_exempt
def home(request):
    hits = mx.Product.objects.filter(is_favorite=False).order_by('priority_order').all()
    context = {'hits': hits}
    return render(request, 'index.html', context)


def contacts(request):
    context = {}
    return render(request, 'contact.html', context)
