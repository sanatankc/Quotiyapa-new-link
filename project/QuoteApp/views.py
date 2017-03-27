from django.shortcuts import render
from django.shortcuts import redirect
from .models import Quotes
from .form import Quotes_form
from django.contrib.auth.models import User
from django.http import Http404

# Create your views here.
def home(request):
    """
    return views at / url
    """
    if not request.user.is_authenticated():
        return redirect('/login')
    quotes = Quotes.objects.all()
    user = request.user
    return render(request, "home.html", {"quotes": quotes, "user": user})

def user_profile(request, username):
    """
    views for user profile
    """
    try:
        user = User.objects.get(username= username).username
    except User.DoesNotExist:
        raise Http404
    return render(request, "user_profile.html", {"username" : user})

def add_quote(request):
    if not request.user.is_authenticated():
        return redirect('/login')

    form_class = Quotes_form
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            quote = form.cleaned_data['quotes']
            author = form.cleaned_data['author']
            user = request.user
            obj = Quotes.objects.create(quotes=quote, author=author, user=user)
            return redirect('home')
    else:
        form = form_class()
    return render(request, 'add_quote.html',
    {'form':form,

    })