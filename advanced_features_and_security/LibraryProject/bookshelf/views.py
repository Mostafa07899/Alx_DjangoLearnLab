from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Article


# Create your views here.

@permission_required('myapp.can_view', raise_exception=True)
def view_items(request):
    # Logic for viewing items
    return render(request, 'view_items.html')

@permission_required('myapp.can_edit', raise_exception=True)
def edit_item(request, pk):
    # Logic for editing an item
    return render(request, 'edit_item.html')