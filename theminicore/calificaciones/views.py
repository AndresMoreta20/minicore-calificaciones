from django.shortcuts import render, redirect
from django.views import View
from .models import Calificacion
from .forms import CalificacionForm, CalcularPromedioForm
from django.db.models import Avg, F, ExpressionWrapper, DecimalField, Q
from decimal import Decimal


def index(request):
    return render(request, 'index.html')

class IngresarCalificacionView(View):
    template_name = 'ingresar_calificacion.html'

    def get(self, request):
        form = CalificacionForm()
        calificaciones = Calificacion.objects.all()
        return render(request, self.template_name, {'form': form, 'calificaciones': calificaciones})

    def post(self, request):
        form = CalificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingresar_calificacion')
        else:
            calificaciones = Calificacion.objects.all()
            return render(request, self.template_name, {'form': form, 'calificaciones': calificaciones})
        
class CalcularPromedioView(View):
    template_name = 'calcular_promedio.html'

    def get(self, request):
        form = CalcularPromedioForm()
        estudiantes = []
        return render(request, self.template_name, {'form': form, 'estudiantes': estudiantes})

    def post(self, request):
        form = CalcularPromedioForm(request.POST)
        if form.is_valid():
            fecha_parcial1_inicio = form.cleaned_data['fecha_parcial1_inicio']
            fecha_parcial1_fin = form.cleaned_data['fecha_parcial1_fin']
            fecha_parcial2_inicio = form.cleaned_data['fecha_parcial2_inicio']
            fecha_parcial2_fin = form.cleaned_data['fecha_parcial2_fin']

            if fecha_parcial1_fin >= fecha_parcial2_inicio:
                error_message = "Los rangos de fechas no son válidos. Asegúrate de que no se mezclen."
                return render(request, self.template_name, {'form': form, 'error_message': error_message})

            # Calcular promedios por estudiante para el parcial 1 y el parcial 2
            calificaciones_parcial1 = Calificacion.objects.filter(fecha__range=(fecha_parcial1_inicio, fecha_parcial1_fin))
            calificaciones_parcial2 = Calificacion.objects.filter(fecha__range=(fecha_parcial2_inicio, fecha_parcial2_fin))

            estudiantes = []
            for estudiante in Calificacion.objects.values('nombre').distinct():
                nombre = estudiante['nombre']
                promedio_parcial1 = calificaciones_parcial1.filter(nombre=nombre).aggregate(promedio=Avg('nota'))['promedio'] or Decimal('0')
                promedio_parcial2 = calificaciones_parcial2.filter(nombre=nombre).aggregate(promedio=Avg('nota'))['promedio'] or Decimal('0')

                # Calcular la calificación necesaria para alcanzar un 6 en el último parcial
                calificacion_necesaria = (Decimal('6') - ((Decimal('0.25') * promedio_parcial1) + (Decimal('0.35') * promedio_parcial2))) * Decimal(5/2)
             

                estudiantes.append({
                    'nombre': nombre,
                    'promedio_parcial1': round(promedio_parcial1, 2),
                    'promedio_parcial2': round(promedio_parcial2, 2),
                    'calificacion_necesaria': round(calificacion_necesaria, 2),
                })

            return render(request, self.template_name, {'form': form, 'estudiantes': estudiantes})

        return render(request, self.template_name, {'form': form})