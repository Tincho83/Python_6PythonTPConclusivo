from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import TipoDoc, Categoria, Pedido, DetallePedido
from .forms import CategoriaForm, TipoDocForm, PedidoForm
from django.contrib.auth.decorators import login_required
from decimal import Decimal, ROUND_HALF_UP


# *** Categoria ***
@login_required
def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'app_operaciones/categoria_list.html', {'categorias': categorias})

@login_required
def categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoría registrada.")            
            return redirect('app_operaciones:categoria_listar')
    else:
        form = CategoriaForm()    
    return render(request, 'app_operaciones/categoria_form.html', {'form': form})

@login_required
def categoria_editar(request, pk):
    cat = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=cat)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoría actualizada.")
            return redirect('app_operaciones:categoria_listar')
    else:
        form = CategoriaForm(instance=cat)
    return render(request, 'app_operaciones/categoria_form.html', {'form': form})

@login_required
def categoria_eliminar(request, pk):
    cat = get_object_or_404(Categoria, pk=pk)
    cat.delete()
    messages.success(request, "Categoría eliminada.")
    return redirect('app_operaciones:categoria_listar')
# *** Categoria ***


# *** Tipo Doc ***
@login_required
def tipodoc_list(request):
    tiposdoc = TipoDoc.objects.all()
    return render(request, 'app_operaciones/tipodoc_list.html', {'tiposdoc': tiposdoc})

@login_required
def tipodoc(request):
    if request.method == "POST":
        form = TipoDocForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tipo de documento registrado.")
            #return redirect('app_ecommerce:index')
            return redirect('app_operaciones:tipodoc_listar')
    else:
        form = TipoDocForm()    
    return render(request, 'app_operaciones/tipodoc_form.html', {'form': form})

@login_required
def tipodoc_editar(request, pk):
    td = get_object_or_404(TipoDoc, pk=pk)
    if request.method == "POST":
        form = TipoDocForm(request.POST, instance=td)
        if form.is_valid():
            form.save()
            messages.success(request, "Tipo de documento actualizado.")
            return redirect('app_operaciones:tipodoc_listar')
    else:
        form = TipoDocForm(instance=td)
    return render(request, 'app_operaciones/tipodoc_form.html', {'form': form})

@login_required
def tipodoc_eliminar(request, pk):
    td = get_object_or_404(TipoDoc, pk=pk)
    td.delete()
    messages.success(request, "Tipo de documento eliminado.")
    return redirect('app_operaciones:tipodoc_listar')
# *** Tipo Doc ***

# *** Pedido ***
@login_required
def pedido_list(request):
    pedidos = Pedido.objects.all().order_by('-fecha_pedido')
    return render(request, 'app_operaciones/pedido_list.html', {'pedidos': pedidos})

@login_required
def pedido(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            # inicializamos total
            pedido.total = Decimal('0.00')
            pedido.save()  # primero guardamos el pedido para tener ID

            productos = form.cleaned_data['producto']  # QuerySet de productos            
            cantidades = request.POST.getlist('cantidad')  # si hay input separado por cantidad

            for i, producto in enumerate(productos):
                cantidad = int(cantidades[i]) if i < len(cantidades) else 1
                print(f"cantidades: {request.POST.getlist('cantidad')}")
                print(f"cantidades: {cantidades}")
                print(f"cantidades: {cantidad}")                
                precio = Decimal(str(producto.precio))                
                subtotal = (precio * Decimal(cantidad)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                pedido.total += subtotal

                # guardamos en DetallePedido
                from .models import DetallePedido
                DetallePedido.objects.create(
                    pedido=pedido,
                    producto=producto,
                    cantidad=cantidad,
                    subtotal=subtotal
                )

            pedido.total = pedido.total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

            pedido.save()  # actualizamos total
            messages.success(request, f"Pedido #{pedido.id} registrado correctamente.")
            return redirect('app_operaciones:pedido_crear')
    else:
        form = PedidoForm()

    return render(request, 'app_operaciones/pedido_form.html', {'form': form})

@login_required
def pedido_editar(request, pk):
    pedido_obj = get_object_or_404(Pedido, pk=pk)
    if request.method == "POST":
        form = PedidoForm(request.POST, instance=pedido_obj)
        if form.is_valid():
            pedido = form.save(commit=False)
            # recalcular total
            total = 0
            for detalle in pedido.detallepedido_set.all():
                total += detalle.subtotal
            pedido.total = total
            pedido.save()
            messages.success(request, f"Pedido #{pedido.cod_ped} actualizado.")
            return redirect('app_operaciones:pedido_listar')
    else:
        form = PedidoForm(instance=pedido_obj)
    return render(request, 'app_operaciones/pedido_form.html', {'form': form})

@login_required
def pedido_eliminar(request, pk):
    pedido_obj = get_object_or_404(Pedido, pk=pk)
    pedido_obj.delete()
    messages.success(request, f"Pedido #{pedido_obj.cod_ped} eliminado.")
    return redirect('app_operaciones:pedido_listar')
# *** Pedido ***




