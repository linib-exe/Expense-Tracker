from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import EntryForm

# Create your views here.
def home(request):
    return HttpResponse("You are in Home")

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
    pass

def delete_entry(request,id):
    pass