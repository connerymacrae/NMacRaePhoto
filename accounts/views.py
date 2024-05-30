from django.shortcuts import render, redirect
from django.contrib.auth import login
from accounts.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, UserManager


def register(request):
    if request.method != 'POST':
        form = UserRegisterForm()
    else:
        form = UserRegisterForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('photomanager:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)


@login_required
def profile(request):
    return render(request, 'registration/profile.html')


# def profile(request):
#     username = User.objects.username()
#     useremail = User.objects.email()
#     photographer = getattr(request.user, 'photgrapher', None)
#     context = {'username': username, 'useremail': useremail, 'photographer': photographer}
#     return render(request, 'registration/profile.html', context=context)
