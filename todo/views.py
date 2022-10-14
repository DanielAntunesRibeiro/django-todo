from django.http import HttpResponseRedirect
from django.shortcuts import render
from todo.models import Item

def TodoAppView(request):
    all_items = Item.objects.all()
    print(all_items)
    return render(request, 'todolist.html', {'all_items': all_items, 'ACTION_URL': '/todo/'})

def AddTodo(request):
    new_item = Item(content=request.POST['content'])
    if request.POST['content'].strip() != '':
        new_item.save()
    return HttpResponseRedirect('/')

# Delete Todo:

# Edit Todo:
def EditTodo(resquest, item_id):
    all_itens = Item.objects.all()
    item_id_edit = Item.objects.get(id=item_id)
    return render(request, 'todolist.html', {'edit_item': item_to_edit, 'all_itens': all_itens})
# Update Todo Item:
def UpdateTodoItem(request, item_id):
    item_to_update = Item.objects.get(id=item_id)
    item_to_update.content = request.POST['content']
    item_to_update.save()
    return HttpResponseRedirect('/')
