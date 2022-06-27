#from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Servico, Contact
from .forms import ContactForm
from django.views.generic import ListView, DetailView

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect


# Create your views here.


class IndexView(ListView):
    template_name = 'crudapp/index.html'
    context_object_name = 'contact_list'
    
    def get_queryset(self):
        # return Contact.objects.all()
        return Contact.objects.filter(author=self.request.user)

class ContactDetailView(DetailView):
    model = Contact
    template_name = 'crudapp/contact-detail.html'

@login_required
def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            resp = form.save()
            return redirect('detail',resp.pk)
    form = ContactForm()
    return render(request,'crudapp/create.html',{'form': form})

@login_required
def edit(request, pk, template_name='crudapp/edit.html'):
    #contact = get_object_or_404(Contact, pk=pk)
    post = get_object_or_404(Contact, pk=pk)
    form = ContactForm(request.POST or None, instance=post)
    if form.is_valid():
        form.instance.author = request.user
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

def delete(request, pk, template_name='crudapp/confirm_delete.html'):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method=='POST':
        contact.delete()
        return redirect('index')
    return render(request, template_name, {'object':contact})


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
