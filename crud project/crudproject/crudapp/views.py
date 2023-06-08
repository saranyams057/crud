from django.shortcuts import get_object_or_404, render,redirect
from django.shortcuts import render
from .forms import CrudForm
from .models import Crud
from django.contrib import messages
from django.views.generic import ListView
def index(request):
    # crud = Crud.objects.all()
    # if request.method == 'POST':
    #     form = CrudForm(request.POST)
    #     if form.is_valid():
    #         form.save() 
    #         form = CrudForm()
    #         # Save the form data to the database
    # else:
    #     form = CrudForm()
    # return render(request, 'index.html', {'form': form,'crud':crud})
    if request.method == 'POST':
        slno = request.POST.get('slno', '')
        itemname = request.POST.get('itemname','')
        description = request.POST.get('description', '')
        crud = Crud(slno = slno,itemname = itemname,description = description)
        crud.save()
        messages.success(request, "Data saved Succesfully")
        return redirect('/')
    crud1 = Crud.objects.all()
    return render(request,'index1.html', {'crud1':crud1})

# def update(request,id):
#     crud = Crud.objects.get(id=id)
#     f=CrudForm(request.POST or None,instance=crud)
#     if f.is_valid():
#         f.save()
#         messages.success(request, "Data updated Succesfully")
#         return redirect('/')
#     return render(request,'update.html',{'f':f,'crud':crud})

def update(request, id):
    contact1 = Crud.objects.all()
    contact = Crud.objects.get(id=id)

    if request.method == 'POST':
        slno = request.POST.get('slno', '')
        itemname = request.POST.get('itemname', '')
        description = request.POST.get('description', '')

        contact.slno = slno
        contact.itemname = itemname
        contact.description = description
        contact.save()
        messages.success(request, "Data updated Succesfully")
        return redirect('/')
    
    return render(request, 'update.html', {'contact1': contact1, 'contact': contact})


def delete(request,crudid):
    crud=Crud.objects.get(id=crudid)
    if request.method =='POST':
        crud.delete()
        return redirect('/')

    return render(request,'delete.html')


class Itemlistview(ListView):
    model=Crud
    template_name='temp.html'
    