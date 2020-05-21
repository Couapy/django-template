from django.contrib import auth
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (AdminPasswordChangeForm,
                                       PasswordChangeForm)
from django.shortcuts import HttpResponseRedirect, render, reverse
from django.template import Template, Context
from django.template.loader import render_to_string
from social_django.models import UserSocialAuth

from .forms import LoginForm, ProfileForm, UserForm


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
    }
    return render(request, 'account/profile.html', context)


@login_required
def user(request):
    """User view."""
    user_form = UserForm(
        data=request.POST or None,
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
    }
    return render(request, 'account/user.html', context)


@login_required
def password(request):
    """Password view."""
    if request.user.has_usable_password():
        form = PasswordChangeForm
    else:
        form = AdminPasswordChangeForm

    if request.method == 'POST':
        password_form = form(request.user, request.POST)
        if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request, password_form.user)
            return HttpResponseRedirect(
                reverse('account:password') + "?success=1"
            )
    else:
        password_form = form(request.user)

    context = {
        'password_form': password_form,
        'success': "success" in request.GET,
    }
    return render(request, 'account/password.html', context)


@login_required
def connections(request):
    """Connections view."""
    user = request.user
    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    providers = [
        {
            "provider": "google-oauth2",
            "name": "Google",
            "link": None,
            "username": None,
        },
        {
            "provider": "github",
            "name": "Github",
            "link": "https://github.com/{{ data.login }}",
            "username": "{{ data.login }}",
        },
        {
            "provider": "twitter",
            "name": "Twitter",
            "link": "https://twitter.com/{{ data.access_token.screen_name }}/",
            "username": "@{{ data.access_token.screen_name }}",
        },
        {
            "provider": "facebook",
            "name": "Facebook",
            "link": "https://facebook.com/{{ data.id }}/",
            "username": "{{ data.id }}",
        },
    ]

    services = []

    for provider in providers:
        try:
            login = user.social_auth.get(provider=provider['provider'])
        except UserSocialAuth.DoesNotExist:
            login = None
        if login is not None:
            if provider['link'] is not None:
                template = Template(provider['link'])
                context = Context({'data': login.extra_data})
                link = template.render(context)
            else:
                link = None
            if provider['username'] is not None:
                template = Template(provider['username'])
                context = Context({'data': login.extra_data})
                username = template.render(context)
            else:
                username = None
        else:
            link = None
            username = None
        services.append({
            "provider": provider["provider"],
            "name": provider["name"],
            "login": login is not None,
            "link": link,
            "username": username,
        })

    context = {
        "services": services,
        'can_disconnect': can_disconnect
    }
    return render(request, 'account/connections.html', context)


def login(request):
    """Login view."""
    login_form = LoginForm(
        data=request.POST or None,
    )
    error = ''
    if request.method == "POST":
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(
                username=username,
                password=password
            )
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return HttpResponseRedirect(reverse('account:index'))
                else:
                    error = 'account disabled'
            else:
                error = 'invalid login'
    context = {
        'login_form': login_form,
        'error': error,
    }
    return render(request, 'account/login.html', context)


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
