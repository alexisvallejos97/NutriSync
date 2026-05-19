# core/signals.py
# Signal para crear el PerfilNutricionista automáticamente al crear un User.
# Garantiza que nunca exista un User sin su perfil correspondiente.

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import PerfilNutricionista


@receiver(post_save, sender=User)
def crear_perfil_nutricionista(sender, instance, created, **kwargs):
    """
    Crea automáticamente el PerfilNutricionista cuando se crea un nuevo User.
    Usamos get_or_create para evitar duplicados en caso de saves múltiples.
    El nombre_completo se inicializa con el nombre del User si está disponible.
    """
    if created:
        nombre = f"{instance.first_name} {instance.last_name}".strip()
        PerfilNutricionista.objects.get_or_create(
            usuario=instance,
            defaults={"nombre_completo": nombre or instance.username},
        )
