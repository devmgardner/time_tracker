from django.shortcuts import render

# Create your views here.

def clock(request):
    return render(request, 'clock/clock.html')

