from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List


# Create your views here.
def home_page(request):
    # if request.method == 'POST':
    #     new_item_text = request.POST.get('item_text', '')
    #     Item.objects.create(text=new_item_text)
    #     return redirect('/lists/the_only_list/')

    return render(request, 'home_page.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})


def new_list(request):
    list_ = List()
    list_.save()

    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/the_only_list/')

