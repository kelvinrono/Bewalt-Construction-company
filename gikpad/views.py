from django.shortcuts import render,redirect
from .forms import ClientForm,RegisterForm
from .models import Clientrequest
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    return render(request, 'index.html')
def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    context = {
        'form':form,
    }
    return render(request, 'registration/register.html', context)


def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contacts(request):
    if request.method == 'POST':
        form=ClientForm(request.POST,request.FILES)
        if form.is_valid():
            request = form.save(commit=False)
            request.save()
            # messages.success(request, "Data inserted successfully")

            return redirect('contacts')
    else:
        # messages.warning(request, "Data was not inserted")
        form=ClientForm()
    params={
        'form':form
    }

    return render(request, 'contacts.html',params)

@login_required(login_url='/accounts/login/')
def advance(request):
    requests=Clientrequest.objects.all()

    return render(request, 'advance.html',{"requests": requests})
