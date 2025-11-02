from .models import ContadorVisitas

def contador_visitas_context(request):
    contador, _ = ContadorVisitas.objects.get_or_create(pk=1)
    return {'contador_visitas': contador.total}

