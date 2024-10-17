
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Laboratorio
from .forms import LaboratorioForm


def inicio(request):
    return render(request, 'laboratorio/inicio.html')

class LaboratorioListView(View):
    def get(self, request):
        laboratorios = Laboratorio.objects.all()
        return render(request, 'laboratorio/laboratorio_list.html', {'laboratorios': laboratorios})


class LaboratorioCreateView(View):
    def get(self, request):
        form = LaboratorioForm()
        return render(request, 'laboratorio/laboratorio_form.html', {'form': form})

    def post(self, request):
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('laboratorio:list')
        return render(request, 'laboratorio/laboratorio_form.html', {'form': form})

class LaboratorioUpdateView(View):
    def get(self, request, pk):
        laboratorio = get_object_or_404(Laboratorio, pk=pk)
        form = LaboratorioForm(instance=laboratorio)
        return render(request, 'laboratorio/laboratorio_form.html', {'form': form})

    def post(self, request, pk):
        laboratorio = get_object_or_404(Laboratorio, pk=pk)
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('laboratorio:list')
        return render(request, 'laboratorio/laboratorio_form.html', {'form': form})

class LaboratorioDeleteView(View):
    def get(self, request, pk):
        laboratorio = get_object_or_404(Laboratorio, pk=pk)
        return render(request, 'laboratorio/laboratorio_confirm_delete.html', {'laboratorio': laboratorio})

    def post(self, request, pk):
        laboratorio = get_object_or_404(Laboratorio, pk=pk)
        laboratorio.delete()
        return redirect('laboratorio:list')

