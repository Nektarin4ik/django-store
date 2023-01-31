from django.contrib.auth.decorators import login_required
from django.db.models.query import QuerySet
from django.shortcuts import HttpResponseRedirect, render
from django.views import View
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from users.models import User

from .models import Basket, Product, ProductCategory

# class Index(View):
#
#     def get(self, request):
#         return render(request, 'index.html')

class IndexView(TemplateView):
    template_name = 'index.html'


# def ProductsListView(request, **kwargs):
#     category_id = kwargs.get('category_id')
def ProductsListView(request, **kwargs):
    category_id = kwargs.get('category_id')
    page = request.GET.get('page')
    if category_id:
        queryset = Product.objects.filter(category=category_id)
    else:
        queryset = Product.objects.all()
    paginator = Paginator(queryset, 3)
    # page = request.GET.get('page')
    # if not page:
    #     paginator = Paginator(Product.objects.all(), 3)
    # else:
    #     paginator = Paginator(queryset, 3)

    # page = request.GET.get('page')
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        objects = paginator.page(paginator.num_pages)
    # if not page:
    #     objects = Product.objects.all()

    context = {'objects': objects,
               'categories': ProductCategory.objects.all()}

    # Add previous and next page links to context
    if objects.has_previous():
        context['previous_page_url'] = '?page={}'.format(objects.previous_page_number())
    if objects.has_next():
        context['next_page_url'] = '?page={}'.format(objects.next_page_number())

    return render(request, 'products.html', context)
# class ProductsListView(ListView):
#
#     model = Product
#     template_name = 'products.html'
#     paginate_by = 3
#
#     def get_queryset(self):
#         queryset = super(ProductsListView, self).get_queryset()
#         category_id = self.kwargs.get('category_id')
#         # if category_id == None:
#         #     category_id = 3
#         return queryset.filter(category_id=category_id) if category_id else queryset
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super(ProductsListView, self).get_context_data()
#         context['categories'] = ProductCategory.objects.all()
#         return context




# class BasketCreateView(CreateView):
#
#     model = Basket
#
#     def post(self, request, *args, **kwargs):
#         product=Product.obkects.get(id=)


@login_required
def basket_add(request, product_id):
    current_page = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(current_page)

@login_required
def basket_delete(request, basket_id):
    current_page = request.META.get('HTTP_REFERER')
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(current_page)





# class Products(ListView):
#     model = Product
#     template_name = 'products.html'
#     paginate_by = 3
#
#     def get_queryset(self):
#         queryset = super(Products, self).get_queryset()
#         category_id = self.kwargs.get('category_id')
#         return queryset.filter(category_id=category_id) if category_id else queryset
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super(Products, self).get_context_data()
#         context['categories'] = ProductCategory.objects.all()
#         return context


# class Poisk(ListView):
#     model = Karta_tovara
#     template_name = "testmptt/kategorii.html"
#     context_object_name = "vub_tov"
#     paginate_by = 1
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["q"] = f"tovar__icontains={self.request.GET.get('tovar__icontains')}&" + f"kat_tov={self.request.GET.get('kat_tov')}&" + f"cena_tov__lt={self.request.GET.get('cena_tov__lt')}&"+ f"cena_tov__gt={self.request.GET.get('cena_tov__gt')}&"+ f"sort={self.request.GET.get('sort')}&"
#         return context
#
#     def get_queryset(self):
#         zapros1 = self.request.GET.get
#         sort1 = ['cena_tov', '-cena_tov', 'tovar', '-tovar' ]
#         print(self.request.GET.get('sort'))
#         print(str(sort1[int(self.request.GET.get('sort'))]))
#         lookups = {
#             f: zapros1(f) for f in ('tovar__icontains', 'kat_tov', 'cena_tov__lt', 'cena_tov__gt') if zapros1(f)
#         }
#         return Karta_tovara.objects.filter(**lookups).order_by(str(sort1[int(self.request.GET.get('sort'))]))

class Products(View):

    def get(self, request, category_id=None, page=1):
        context = {
            'categories': ProductCategory.objects.all(),
                    }
        if category_id:
            products = Product.objects.filter(category_id=category_id)
            # context.update({'products': Product.objects.filter(category_id=category_id)})
        else:
            products = Product.objects.all()
            # a = None
            # # a = request.GET.get
            # # print('category_id', a)
            # if a:
            #     products = Product.objects.filter(category_id=a)
            # else:
            #     products = Product.objects.all()
            # context.update({'products': Product.objects.all()})
        paginator = Paginator(products, 3)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)
        products_paginator = paginator.page(page)
        context.update({'products': products_paginator})
        return render(request, 'products.html', context)


# class Basket_add(View):
#
#
#     def get(self, request, product_id):
#         current_page = request.META.get('HTTP_REFERER')
#         product = Product.objects.get(id=product_id)
#         baskets = Basket.objects.filter(user=request.user, product=product)
#         if not baskets.exists():
#             Basket.objects.create(user=request.user, product=product, quantity=1)
#             return HttpResponseRedirect(current_page)
#
#         else:
#             basket = baskets.first()
#             basket.quantity += 1
#             basket.save()
#             return HttpResponseRedirect(current_page)
#
#
# class Basket_delete(View):
#
#     def get(self, request, id):
#         basket = Basket.objects.get(id=id)
#         basket.delete()
#         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



