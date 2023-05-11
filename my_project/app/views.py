from django.shortcuts import render, redirect
from .forms import LeadForm


def landing_page(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = LeadForm()
    return render(request, 'app/landing_page.html', {'form': form})


def thank_you(request):
    return render(request, 'app/thank_you.html')
