from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from accounts.forms import UserRegistrationForm, UserLoginForm, UserAccountForm
from django.contrib.auth.decorators import login_required


def register(request):
    """
    Render the registration page
    """
    # First check if user is logged in. If True, redirect to the profile page
    if request.user.is_authenticated:
        return redirect(reverse('profile'))

    # If method is POST, register user.
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                messages.success(request, "You have successfully registered")
                return redirect(reverse('profile'))

            else:
                messages.error(request, "unable to sign you up at this time")

    # If method is get, render blank registration page
    else:
        form = UserRegistrationForm()

    args = {'form': form}
    args.update(csrf(request))

    return render(request, 'accounts/register.html', args)


@login_required(login_url='/account/login/')
def profile(request):
    """
    Render the profile page and load/save UserAccountForm.
    """
    if request.method == 'POST':
        form = UserAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your details have been updated")
            return redirect(reverse('profile'))
        else:
            messages.error(request, "We've been unable to update your details")
    else:
        form = UserAccountForm(instance=request.user)

    args = {
        'form': form,
        'my_courses': request.user.module_set.all()
    }

    args.update(csrf(request))
    return render(request, 'accounts/profile.html', args)


def login(request):
    """
    Render the login page
    """
    # First check if user is logged in. If True, redirect to the profile page
    if request.user.is_authenticated:
        return redirect(reverse('profile'))

    # If method is POST, log user in
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your email or password was not recognised")

    # If method is GET, render empty Login form
    else:
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'accounts/login.html', args)


@login_required(login_url='/account/login/')
def logout(request):
    """
    Log user out and redirect to Homepage
    """
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))
