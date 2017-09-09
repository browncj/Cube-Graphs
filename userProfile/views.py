from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def index(request):
    return render(request, 'userProfile/userProfile.html', {})


@login_required(login_url='/login')
def update_mail(request):
    if request.method == 'POST':
        validate_email(request.POST['email'])
        request.user.email = request.POST['email']
        request.user.save()
        return redirect('/profile')

    return render(request, 'userProfile/updateMail.html', {})
