from django.shortcuts import render


def register(request):
    """User registration for the raffle."""
    return render(request, 'lottery/register.html')
