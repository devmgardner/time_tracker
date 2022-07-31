from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def clock(request):
    return render(request, 'clock/clock.html')