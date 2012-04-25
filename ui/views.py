from django.shortcuts import render, redirect, get_object_or_404
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

def quote_page(request, quote_id):
    quote = get_object_or_404(Quote, id=quote_id)
    return render(request, 'quote_page.html', {
        'quote': quote,
    })

def vote(request, quote_id, updown):
    quote = get_object_or_404(Quote, id=quote_id)
    if updown == 'up':
        quote.up += 1
    else:
        quote.down += 1
    quote.save()
    return redirect('landing')
