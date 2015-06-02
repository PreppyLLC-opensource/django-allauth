from django.conf.urls import patterns, url
from django.views.generic import RedirectView

from . import views

urlpatterns = patterns(
    "",
    url(r"^signup/$",
        views.SignupView.as_view(template_name="allauth/registration_form.html"),
        name="account_signup"),
    url(r"^login/$",
        views.LoginView.as_view(template_name="allauth/login.html"), name="account_login"),
    url(r"^logout/$", views.logout, name="account_logout"),

    url(r"^password/change/$",
        views.PasswordChangeView.as_view(template_name='allauth/password_change.html'),
        name="account_change_password"),
    url(r"^password/change/complete$",
        views.PasswordChangeView.as_view(template_name='allauth/password_change_done.html'),
        name="account_change_password_complete"),
    url(r"^password/set/$", views.password_set, name="account_set_password"),

    url(r"^inactive/$", views.account_inactive, name="account_inactive"),

    # E-mail
    url(r"^email/$", views.email, name="account_email"),
    url(r"^confirm-email/$",
        views.EmailVerificationSentView.as_view(template_name='allauth/registration_complete.html'),
        name="account_email_verification_sent"),
    url(r"^confirm-email/complete/$",
        views.TemplateView.as_view(template_name='allauth/activation_complete.html'),
        name="activation_complete"),
    url(r"^confirm-email/(?P<key>\w+)/$", views.confirm_email,
        name="account_confirm_email"),
    # Handle old redirects
    url(r"^confirm_email/(?P<key>\w+)/$",
        RedirectView.as_view(url='/accounts/confirm-email/%(key)s/',
                             permanent=True)),

    # password reset
    url(r"^password/reset/$",
        views.PasswordResetView.as_view(template_name='allauth/password_reset_form.html'),
        name="account_reset_password"),
    url(r"^password/reset/done/$",
        views.PasswordResetDoneView.as_view(template_name="allauth/password_reset_done.html"),
        name="account_reset_password_done"),
    url(r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
        views.PasswordResetFromKeyView.as_view(template_name="allauth/password_reset_from_key.html"),
        name="account_reset_password_from_key"),
    url(r"^password/reset/key/done/$",
        views.PasswordResetFromKeyDoneView.as_view(template_name="allauth/password_reset_from_key_done.html"),
        name="account_reset_password_from_key_done"),
)
