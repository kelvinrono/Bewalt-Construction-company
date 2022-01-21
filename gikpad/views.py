from django.shortcuts import render,redirect
from .forms import ClientForm,RegisterForm
from .models import gallery
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .email import send_welcome_email,send_director_email



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

def projects(request):
    
    projects=gallery.objects.all()

    context={
        'projects':projects
    }
    return render(request, 'projects.html', context)

def contacts(request):
    if request.method == 'POST':
        form=ClientForm(request.POST,request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            # recipient = ClientForm(name = name,email =email)
            # recipient.save()
            request = form.save(commit=False)
            name = request.name
            email = request.email
            admin_name='Director'
           
            send_welcome_email(name,email)
            send_director_email(admin_name)
                 

            request.save()
            # messages.success(request, f'Your request has been received. Check your Email!')

            return redirect('contacts')
    else:
        # messages.warning(request, f'Data was not inserted')
        form=ClientForm()
    params={
        'form':form
    }

    return render(request, 'contacts.html',params)

@login_required(login_url='/accounts/login/')
def advance(request):
    requests=Clientrequest.objects.all()

    return render(request, 'advance.html',{"requests": requests})

