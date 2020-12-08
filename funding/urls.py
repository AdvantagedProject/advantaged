from django.urls import path, re_path
from funding import views as my_view
from django.contrib.auth import views as auth_views

app_name = 'funding'

urlpatterns = [
    path('t1/', my_view.test),
    path('login/', auth_views.LoginView.as_view(template_name='funding/login.html')),
    path('passchange/', auth_views.PasswordChangeView.as_view(template_name='funding/passchange.html')),
    path('logout/', my_view.logout),
    path('signup/', my_view.signup),
    path('create/', my_view.funding_create, name="funding_create"),
    path('detail/<int:pk>/', my_view.funding_detail, name="funding_detail"),
]

# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']