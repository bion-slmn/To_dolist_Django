from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import TodoForm
from .models import Todo
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
    
        if form.is_valid():
            form.save()
            messages.info(request, "item created !!!")
            return redirect('todo')
    item_list = Todo.objects.order_by('-date')

    form = TodoForm()
    print(item_list)

    page = {
            'forms': form,
            'list': item_list,
            'title': 'TODo list',
            }
    return render(request, 'todo/index.html', page)

def remove(request, item_id):
    obj = get_object_or_404(Todo, pk=item_id)
    obj.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')
