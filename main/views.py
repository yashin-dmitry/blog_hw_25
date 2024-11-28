from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, permission_required
from .models import Product, MyModel
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
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'main/product_form.html'
    success_url = reverse_lazy('main:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ProductListView(ListView):
    model = Product
    template_name = 'main/product_list.html'
    context_object_name = 'products'

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'main/product_detail.html'
    context_object_name = 'product'

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'main/product_form.html'
    success_url = reverse_lazy('main:product_list')

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner or self.request.user.has_perm('your_app.change_product')

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'main/product_confirm_delete.html'
    success_url = reverse_lazy('main:product_list')

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner or self.request.user.has_perm('main.delete_product')

@login_required
@permission_required('main.can_unpublish_product', raise_exception=True)
def unpublish_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.is_published = False
    product.save()
    return redirect('main:product_list')

def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'main/index.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'main/product_detail.html', context)

def register():
    return None
