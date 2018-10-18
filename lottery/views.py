from django.shortcuts import render
from django.contrib import messages

from lottery.forms import PersonForm


def register(request):
    """User registration for the raffle."""
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Email adicionado')
        else:
            messages.error(request,
                           'Corrija os erros apontados e tente novamente')

    return render(request, 'lottery/register.html')
