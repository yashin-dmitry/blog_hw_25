from django.shortcuts import render, get_object_or_404
from .models import Product, MyModel
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import ProductForm

# Представления для MyModel
class MyModelCreateView(CreateView):
    model = MyModel
    fields = ['name', 'description']
    template_name = 'main/mymodel_form.html'
    success_url = reverse_lazy('main:mymodel_list')

class MyModelListView(ListView):
    model = MyModel
    template_name = 'main/mymodel_list.html'
    context_object_name = 'mymodels'

class MyModelDetailView(DetailView):
    model = MyModel
    template_name = 'main/mymodel_detail.html'
    context_object_name = 'mymodel'

class MyModelUpdateView(UpdateView):
    model = MyModel
    fields = ['name', 'description']
    template_name = 'main/mymodel_form.html'
    success_url = reverse_lazy('main:mymodel_list')

class MyModelDeleteView(DeleteView):
    model = MyModel
    template_name = 'main/mymodel_confirm_delete.html'
    success_url = reverse_lazy('main:mymodel_list')

# Представления для Product
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'main/product_form.html'
    success_url = reverse_lazy('main:product_list')

class ProductListView(ListView):
    model = Product
    template_name = 'main/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_detail.html'
    context_object_name = 'product'

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'main/product_form.html'
    success_url = reverse_lazy('main:product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'main/product_confirm_delete.html'
    success_url = reverse_lazy('main:product_list')

def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'main/index.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'main/product_detail.html', context)
