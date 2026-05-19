# core/context_processors.py
# Inyecta el PerfilNutricionista en el contexto de todos los templates.
# Esto evita pasarlo manualmente desde cada vista — el sidebar siempre tiene acceso al perfil.

from .models import PerfilNutricionista


def perfil_nutricionista(request):
    """
    Agrega el perfil del nutricionista autenticado al contexto global de templates.
    Si el usuario no está autenticado o no tiene perfil, retorna None sin romper la app.
    """
    if request.user.is_authenticated:
        try:
            return {"perfil": request.user.perfil}
        except PerfilNutricionista.DoesNotExist:
            return {"perfil": None}
    return {"perfil": None}
