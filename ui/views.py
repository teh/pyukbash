from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.db import IntegrityError
from django.contrib import messages

from .models import Quote, VoteRecord

class QuoteForm(forms.Form):
    quote = forms.CharField(widget=forms.Textarea)

def landing(request):
    last_10 = Quote.objects.order_by('-created')[:10]
    return render(request, 'landing.html', {
        'last_10': last_10,
        'request': request,
    })

def submit(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            Quote.objects.create(text=form.cleaned_data['quote'])
            messages.add_message(request, messages.INFO, "Quote submitted.")
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
    try:
        VoteRecord.objects.create(
            quote=quote,
            ip4=request.META['REMOTE_ADDR'],
            vote=-1 if updown == 'down' else +1,
        )
    except IntegrityError:
        messages.add_message(request, messages.ERROR, "Already voted on this qoute.")
        return redirect('landing')
    
    if updown == 'up':
        quote.up += 1
    else:
        quote.down += 1
    quote.save()
    messages.add_message(request, messages.INFO, "Voted.")
    return redirect('landing')
