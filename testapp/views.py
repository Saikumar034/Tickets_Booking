from django.shortcuts import render,redirect
from django.contrib.auth.forms import User
from testapp.forms import createForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def login(request):
    return redirect('homes')


def register(request):
    form=createForm()
    if request.method=='POST':
            form=createForm(request.POST)
            if form.is_valid():
                user=form.save()
                user.set_password(user.password)
                user.save()
                return redirect('homes')
    return render(request, 'testapp/registration.html', {'form': form})


def home(request):
    return render(request,'testapp/home.html')

def contact(request):
    return render(request,'testapp/contact.html')




