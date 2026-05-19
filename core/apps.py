# core/apps.py
# Configuración de la app 'core' con carga de signals al inicio.

from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"
    verbose_name = "Core — Autenticación y Perfil"

    def ready(self):
        # Importa signals para que se registren al iniciar la app.
        # Sin esto, los signals no se conectan y el PerfilNutricionista
        # no se crea automáticamente al crear un superusuario.
        import core.signals  # noqa: F401
