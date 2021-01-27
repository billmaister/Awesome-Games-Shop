from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm, DevRegisterForm
from .models import Profile, DevProfile
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token_generator import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage


def pre_register(request):
    return render(request, 'users/register_start.html')


def register(request, user_type):
    is_dev = user_type=='developer'
    if request.method == 'POST':
        form = DevRegisterForm(request.POST) if is_dev else UserRegisterForm(request.POST)

        if form.is_valid():

            user = form.save()
            # Set user as inactive before verification link is clicked
            user.is_active = False
            user.save()
            if is_dev:
                profile = DevProfile.objects.create(user=user, is_dev=is_dev, seller_id=form.data['seller_id'], secret_key=form.data['secret_key'] )
            else:
                profile = Profile.objects.create(user=user, is_dev=is_dev)
            profile.save()
            current_site = get_current_site(request)
            email_subject = 'Activate Your Account'
            message = render_to_string('users/activate_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()
            return render(request, 'users/send_email.html')
    else:
        form = DevRegisterForm if is_dev else UserRegisterForm()

    return render(request, 'users/register.html', { 'form': form })


def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, 'django.contrib.auth.backends.ModelBackend')
        return render(request, 'users/activation_succ.html')
    else:
        return HttpResponse('Activation link is invalid!')
