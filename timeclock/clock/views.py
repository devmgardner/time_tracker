from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def clock(request):
    if request.method == 'POST':
        queryDict = dict(request.POST)
        user = {}
        user['name'] = queryDict['name']
    return render(request, 'clock.html', {'user':user})