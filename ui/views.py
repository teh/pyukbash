from django.shortcuts import render, redirect
from django import forms

from .models import Quote

class QuoteForm(forms.Form):
    quote = forms.CharField(widget=forms.Textarea)

def landing(request):
    last_10 = Quote.objects.order_by('-created')[:10]
    return render(request, 'landing.html', {
        'last_10': last_10,
    })

def submit(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            Quote.objects.create(text=form.cleaned_data['quote'])
            return redirect('landing')

    else:
        form = QuoteForm()

    return render(request, 'submit.html', {
        'form': form,
    })
