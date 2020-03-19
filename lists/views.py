from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from .forms import EMPTY_ITEM_ERROR, ExistingListItemForm, ItemForm, NewListForm
from .models import Item, List

User = get_user_model()


# Create your views here.
def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_)
    return render(request, 'list.html', {'list': list_, 'form': form, 'error': EMPTY_ITEM_ERROR})

def new_list(request):
    form = NewListForm(data=request.POST)
    if form.is_valid():
        list_ = form.save(owner=request.user)
        return redirect(list_)
    return render(request, 'home.html', {'form' : form, 'error': EMPTY_ITEM_ERROR})

def my_lists(request, email):
    owner = User.objects.get(email=email)
    return render(request, 'my_lists.html', {'owner': owner})

def send_share_email(request, list_id):
    email = request.POST['share']
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)
    print('Shared with email')
    return render(request, 'list.html', {'list': list_, 'form': form, 'error': EMPTY_ITEM_ERROR})