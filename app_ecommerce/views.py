from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Cliente, Producto, ContadorVisitas, Like
from .forms import ClienteForm, ProductoForm, PedidoForm, CategoriaForm, TipoDocForm
from app_operaciones.models import Pedido, Categoria, TipoDoc
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def index(request):
    # Contador de visitas unicas por sesion
    session_key = 'visitado'
    contador, _ = ContadorVisitas.objects.get_or_create(pk=1)

    if not request.session.get(session_key, False):
        contador.total += 1
        contador.save()
        request.session[session_key] = True

    # Mostramos los primeros 4 productos
    productos = Producto.objects.all()[:4]

    return render(request, 'app_ecommerce/index.html', {
        'productos': productos,
        'contador_visitas': contador.total
    })

class ProductoListView(ListView):
    model = Producto
    template_name = 'app_ecommerce/producto_list.html'
    context_object_name = 'productos'
    ordering = ['nombre']
    paginate_by = 12

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'app_ecommerce/producto_detail.html'
    context_object_name = 'producto'
    slug_field = "cod_prod"
    slug_url_kwarg = "cod_prod"

class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'app_ecommerce/producto_form.html'
    success_url = reverse_lazy('app_ecommerce:producto_listar')
    login_url = '/cuentas/login/'

    def form_valid(self, form):
        messages.success(self.request, "Producto creado correctamente.")
        return super().form_valid(form)

class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'app_ecommerce/producto_form.html'
    slug_field = 'cod_prod'
    slug_url_kwarg = 'cod_prod'
    context_object_name = 'producto' 
    success_url = reverse_lazy('app_ecommerce:producto_listar')
    login_url = '/cuentas/login/'

    def get_object(self, queryset=None):        
        cod_prod = self.kwargs.get(self.slug_url_kwarg)
        return get_object_or_404(Producto, cod_prod=cod_prod)

    def form_valid(self, form):
        messages.success(self.request, "Producto actualizado correctamente.")
        return super().form_valid(form)

class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'app_ecommerce/producto_confirm_delete.html'
    slug_field = 'cod_prod'
    slug_url_kwarg = 'cod_prod'
    success_url = reverse_lazy('app_ecommerce:producto_listar')
    login_url = '/cuentas/login/'

    def get_object(self, queryset=None):
        cod_prod = self.kwargs.get(self.slug_url_kwarg)
        return get_object_or_404(Producto, cod_prod=cod_prod)

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Producto eliminado.")
        return super().delete(request, *args, **kwargs)

def cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente registrado.")
            return redirect('app_ecommerce:index')
    else:
        form = ClienteForm()
    return render(request, 'app_ecommerce/cliente_form.html', {'form': form})


@login_required
def producto_crear(request):
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto guardado correctamente.")
            return redirect('app_ecommerce:producto_listar')
    else:
        form = ProductoForm()
    return render(request, 'app_ecommerce/producto_form.html', {'form': form})


def producto_listar(request):
    productos = Producto.objects.all().order_by('nombre')
    return render(request, 'app_ecommerce/producto_list.html', {'productos': productos})


def producto_detalle(request, cod_prod):
    producto = get_object_or_404(Producto, cod_prod=cod_prod)
    return render(request, 'app_ecommerce/producto_detail.html', {'producto': producto})


@login_required
def producto_editar(request, cod_prod):
    producto = get_object_or_404(Producto, cod_prod=cod_prod)
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto actualizado.")
            return redirect('app_ecommerce:producto_detalle', cod_prod=producto.cod_prod)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'app_ecommerce/producto_form.html', {'form': form, 'editar': True})


@login_required
def producto_eliminar(request, cod_prod):
    producto = get_object_or_404(Producto, cod_prod=cod_prod)
    if request.method == "POST":
        producto.delete()
        messages.success(request, "Producto eliminado.")
        return redirect('app_ecommerce:producto_listar')
    return render(request, 'app_ecommerce/producto_confirm_delete.html', {'producto': producto})

def buscar(request):
    query = request.GET.get('q', '')
    resultados = []
    if len(query) > 0:
        resultados = Producto.objects.filter(
            Q(nombre__icontains=query) | Q(descripcion__icontains=query)
        )
    else:
        resultados = Producto.objects.all().order_by("-precio")

    return render(request, 'app_ecommerce/buscar.html', {'resultados': resultados, 'query': query})

@login_required
def producto_like(request, cod_prod):    
    producto = get_object_or_404(Producto, cod_prod=cod_prod)
    like, created = Like.objects.get_or_create(user=request.user, producto=producto)
    if not created:
        like.delete()
    return redirect('app_ecommerce:producto_detalle', cod_prod=producto.cod_prod)
    
