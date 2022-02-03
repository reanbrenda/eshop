from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Products
from store.models.orders import Order
from store.middlewares.auth import auth_middleware
from django.views.generic import ListView
from django.core.paginator import Paginator


class ItemSearchView(ListView):
    model = Products
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        context = super(ItemSearchView, self).get_context_data(**kwargs)
        query = self.request.GET.get('q')
        products = Products.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )
        context['products'] = products
        return context