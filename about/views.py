from django.shortcuts import render
from django.shortcuts import redirect

from about.forms import FeedbackForm

def index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'message': 'Your feedback has been recorded.'}
        else:
            context = {'message': 'Invalid form data'}
        return render(request, 'about/about.html', context)

    form = FeedbackForm()
    context = {'form': form}
    return render(request, 'about/about.html', context)
