from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, render

from .forms import ProfileForm


@login_required
def profile(request):
    """Profile view."""
    profile_form = ProfileForm(
        request.POST or None,
        request.FILES or None,
        instance=request.user.profile,
    )
    success = None

    if profile_form.is_valid():
        profile_form.save()
        success = True

    context = {
        'profile_form': profile_form,
        'success': success,
    }
    return render(request, 'account/profile.html', context)


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
