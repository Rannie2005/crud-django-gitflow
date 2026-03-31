from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notas.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]


urlpatterns += [
    path('reset-password/', 
        auth_views.PasswordResetView.as_view(template_name='notas/reset_password.html'),
        name='password_reset'),
    path('reset-password/enviado/', 
        auth_views.PasswordResetDoneView.as_view(template_name='notas/reset_password_done.html'),
        name='password_reset_done'),
    path('reset-password/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name='notas/reset_password_confirm.html'),
        name='password_reset_confirm'),
    path('reset-password/completo/', 
        auth_views.PasswordResetCompleteView.as_view(template_name='notas/reset_password_complete.html'),
        name='password_reset_complete'),
]