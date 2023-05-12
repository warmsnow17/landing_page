import os

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from .forms import LeadForm

MAIL_CLIENT = os.getenv('MAIL_CLIENT')


from django.shortcuts import render, redirect
from django.views import View
from .forms import LeadForm


class CombinedView(View):
    def get(self, request, *args, **kwargs):
        form = LeadForm()
        if request.path == '/contact/':
            template = 'app/contact.html'
            context = {
                'form': form,
                'title': 'Написать мне'
            }
        else:
            template = 'app/home.html'
            context = {
                'form': form,
            }
        return render(request, template, context)

    def post(self, request, *args, **kwargs):
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')

        if request.path == '/contact/':
            template = 'app/contact.html'
            context = {
                'form': form,
                'title': 'Написать мне'
            }
        else:
            template = 'app/home.html'
            context = {
                'form': form,
            }
        return render(request, template, context)


class SuccessView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/success.html', context={
            'title': 'Спасибо'
        })

