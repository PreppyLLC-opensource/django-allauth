from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url('^login/cancelled/$', views.login_cancelled, 
        name='socialaccount_login_cancelled'),
    url('^login/error/$', views.login_error, name='socialaccount_login_error'),
    url('^signup/$', views.SignupView.as_view(
        template_name = 'allauth/social_signup.html'), name='socialaccount_signup'),
    url('^connections/$', views.connections, name='socialaccount_connections'))
