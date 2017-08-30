from django.shortcuts import render, redirect
from django.core.validators import validate_email


def index(request):
    if not request.user.is_authenticated():
        return redirect('/login')

    return render(request, 'userProfile/userProfile.html', {})


def update_mail(request):
    if request.method == 'POST':
        validate_email(request.POST['email'])
        request.user.email = request.POST['email']
        request.user.save()
        return redirect('/profile')

    return render(request, 'userProfile/updateMail.html', {})
