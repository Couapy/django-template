from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, render
from django.shortcuts import reverse

from .forms import ProfileForm, UserForm


def index(request):
    return HttpResponseRedirect(reverse('account:profile'))

@login_required
def profile(request):
    """Profile view."""
    profile_form = ProfileForm(
        request.POST or None,
        request.FILES or None,
        instance=request.user.profile,
    )
    success = None

    if request.method == "POST":
        if profile_form.is_valid():
            profile_form.save()
            # To avoid the image link break
            profile_form = ProfileForm(instance=request.user.profile)
            success = True

    context = {
        'profile_form': profile_form,
        'success': success,
        'url': 'profile',
    }
    return render(request, 'account/profile.html', context)


@login_required
def user(request):
    """User view."""
    user_form = UserForm(
        request.POST or None,
        instance=request.user,
    )
    success = None

    if request.method == "POST":
        if user_form.is_valid():
            user_form.save()
            success = True

    context = {
        'user_form': user_form,
        'success': success,
        'url': 'user',
    }
    return render(request, 'account/user.html', context)


def login(request):
    """Login view."""
    return render(request, 'account/login.html', {})


@login_required
def logout(request):
    """Logout view."""
    auth.logout(request)
    return HttpResponseRedirect('/')


@login_required
def delete(request):
    """Delete user account."""
    request.user.delete()
    return HttpResponseRedirect('/')
