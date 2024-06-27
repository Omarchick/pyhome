from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Entity
from .forms import EntityForm

@login_required
def entity_list(request):
    entities = Entity.objects.filter(user=request.user)
    return render(request, 'app/entity_list.html', {'entities': entities})

@login_required
def entity_detail(request, pk):
    entity = get_object_or_404(Entity, pk=pk)
    return render(request, 'app/entity_detail.html', {'entity': entity})

@login_required
def entity_create(request):
    if request.method == 'POST':
        form = EntityForm(request.POST)
        if form.is_valid():
            entity = form.save(commit=False)
            entity.user = request.user
            entity.save()
            return redirect('entity_list')
    else:
        form = EntityForm()
    return render(request, 'app/entity_form.html', {'form': form})

@login_required
def entity_edit(request, pk):
    entity = get_object_or_404(Entity, pk=pk)
    if request.method == 'POST':
        form = EntityForm(request.POST, instance=entity)
        if form.is_valid():
            form.save()
            return redirect('entity_list')
    else:
        form = EntityForm(instance=entity)
    return render(request, 'app/entity_form.html', {'form': form})

@login_required
def entity_delete(request, pk):
    entity = get_object_or_404(Entity, pk=pk)
    if request.method == 'POST':
        entity.delete()
        return redirect('entity_list')
    return render(request, 'app/entity_confirm_delete.html', {'entity': entity})

from django.db.models import Count

@login_required
def analytics(request):
    entities_count = Entity.objects.filter(user=request.user).count()
    return render(request, 'app/analytics.html', {'entities_count': entities_count})

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('entity_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
