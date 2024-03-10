from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import EntryForm
from .models import Entry

# Create your views here.
def home(request):
    entries = Entry.objects.all()
    return render(request,'home.html',{'entries':entries})

def create_entry(request):
    form = EntryForm()
    if request.method == 'POST':
        form = EntryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'create_entry.html',{'form':form})

def read_entry(request):
    pass

def update_entry(request,id):
    entry = Entry.objects.get(id=id)
    form = EntryForm(instance=entry)
    if request.method == 'POST':
        form = EntryForm(request.POST,request.FILES,instance=entry)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request,'create_entry.html',{'form':form})

def delete_entry(request,id):
    entry = Entry.objects.get(id=id)
    entry.delete()
    return redirect('home')