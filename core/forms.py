# core/forms.py
# Formulario para editar el perfil profesional del nutricionista.

from django import forms
from .models import PerfilNutricionista


class PerfilNutricionistaForm(forms.ModelForm):
    """Formulario para que el nutricionista edite sus datos profesionales."""

    class Meta:
        model = PerfilNutricionista
        fields = [
            "nombre_completo",
            "especialidad",
            "telefono",
            "email_profesional",
            "numero_colegiatura",
            "direccion_consultorio",
        ]
        widgets = {
            # Aplicamos clases Tailwind para mantener consistencia visual
            "nombre_completo": forms.TextInput(
                attrs={
                    "class": "w-full border border-slate-200 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-teal-500 text-slate-800",
                    "placeholder": "Nombre completo",
                }
            ),
            "especialidad": forms.TextInput(
                attrs={
                    "class": "w-full border border-slate-200 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-teal-500 text-slate-800",
                    "placeholder": "Ej: Nutrición clínica, deportiva...",
                }
            ),
            "telefono": forms.TextInput(
                attrs={
                    "class": "w-full border border-slate-200 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-teal-500 text-slate-800",
                    "placeholder": "+51 999 000 000",
                }
            ),
            "email_profesional": forms.EmailInput(
                attrs={
                    "class": "w-full border border-slate-200 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-teal-500 text-slate-800",
                    "placeholder": "correo@ejemplo.com",
                }
            ),
            "numero_colegiatura": forms.TextInput(
                attrs={
                    "class": "w-full border border-slate-200 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-teal-500 text-slate-800",
                    "placeholder": "CNP-00000",
                }
            ),
            "direccion_consultorio": forms.Textarea(
                attrs={
                    "class": "w-full border border-slate-200 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-teal-500 text-slate-800",
                    "rows": 3,
                    "placeholder": "Dirección del consultorio",
                }
            ),
        }
