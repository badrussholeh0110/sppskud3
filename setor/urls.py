from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import loginview
urlpatterns = [
    path('',views.home, name='home'),
    path('petugas/',views.petugas, name='petugas'),
    path('Tpetugas/',views.Tpetugas, name='Tpetugas'),
    path('Upetugas/<str:pk>',views.Upetugas, name='Upetugas'),
    path('Hpetugas/<str:pk>',views.Hpetugas, name='Hpetugas'),
    path('Uuser/<str:pk>',views.uuser, name='Uuser'),
    path('Uuuser/',views.uuuser, name='Uuuser'),
    path('Uuuseradmin/',views.uuseradmin, name='Uuseradmin'),
    path('Uuuseradmin1/',views.uuseradmin1, name='Uuseradmin1'),

    path('unit/',views.unit, name='unit'),
    path('Tunit/',views.Tunit, name='Tunit'),
    path('Uunit/<str:pk>',views.Uunit, name='Uunit'),
    path('Hunit/<str:pk>',views.Hunit, name='Hunit'),

    path('peternak/',views.peternak, name='peternak'),
    path('Tpeternak/',views.Tpeternak, name='Tpeternak'),
    path('Upeternak/<str:pk>',views.Upeternak, name='Upeternak'),
    path('Hpeternak/<str:pk>',views.Hpeternak, name='Hpeternak'),
    path('peternakunit/<str:pk>',views.peternakunit, name='peternakunit'),
    path('Uuserpeternak/<str:pk>',views.uuser, name='Uuserpeternak'),

    path('harga/',views.harga, name='harga'),
    path('Tharga/',views.Tharga, name='Tharga'),
    path('Uharga/<str:pk>',views.Uharga, name='Uharga'),
    path('Hharga/<str:pk>',views.Hharga, name='Hharga'),

    path('setoran/',views.setoran, name='setoran'),
    path('Tsetoran/',views.Tsetoran, name='Tsetoran'),
    path('Usetoran/<str:pk>',views.Usetoran, name='Usetoran'),
    path('Hsetoran/<str:pk>',views.Hsetoran, name='Hsetoran'),

    path('setoran1/',views.setoran1, name='setoran1'),
    path('Tsetoran1/',views.Tsetoran1, name='Tsetoran1'),
    path('Usetoran1/<str:pk>',views.Usetoran1, name='Usetoran1'),
    path('Hsetoran1/<str:pk>',views.Hsetoran1, name='Hsetoran1'),

    
    path('setoran2/',views.setoran2, name='setoran2'),

    # path('masuk/', loginView.as_view(), name='masuk'),
    path('login/',views.loginPage, name='login'),
    path('logout/',views.logoutPage, name='logout'),

    path('cetak/', views.pdflap, name="cetak"),
    path('cetak1/', views.pdflap1, name="cetak1"),
    path('cetak2/', views.pdflap2, name="cetak2"),
    path('cetakpeter/<str:pk>', views.pdfpeter, name="cetakpeter"),
    path('lihathasil/<str:pk>', views.lihathasil, name="lihathasil"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="data/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="data/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="data/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="data/password_reset_done.html"), name="password_reset_complete"),


]