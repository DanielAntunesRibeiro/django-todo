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
def DeleteTodo(_, item_id):
    item_to_delete = Item.objects.get(id=item_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/')

# Edit Todo:

# Update Todo Item:
