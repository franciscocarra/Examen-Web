from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework import routers
from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
router.register('tipoempleados', TipoEmpleadoViewset)
router.register('empleados', EmpleadoViewset)
router.register('generoempleados', GeneroViewset)

urlpatterns = [
    path('', index, name="index"),
    path('login', login, name="login"),
    path('category', category, name="category"),
    path('contact', contact, name="contact"),
    path('base', base, name="base"),
    path('noticia 1', noticia_1, name="noticia 1"),
    path('noticia 2', noticia_2, name="noticia 2"),
    path('noticia 3', noticia_3, name="noticia 3"),
    path('noticia 4', noticia_4, name="noticia 4"),
    path('noticia 5', noticia_5, name="noticia 5"),
    path('noticia 6', noticia_6, name="noticia 6"),
    path('noticia 7', noticia_7, name="noticia 7"),
    path('noticia 8', noticia_8, name="noticia 8"),
    path('noticia 9', noticia_9, name="noticia 9"),
    path('noticia 10', noticia_10, name="noticia 10"),
    path('noticia 11', noticia_11, name="noticia 11"),
    path('noticia 12', noticia_12, name="noticia 12"),
    path('noticia 13', noticia_13, name="noticia 13"),
    path('noticia 14', noticia_14, name="noticia 14"),
    path('noticia 15', noticia_15, name="noticia 15"),
    path('noticia 16', noticia_16, name="noticia 16"),
    path('noticia 17', noticia_17, name="noticia 17"),
    path('noticia 18', noticia_18, name="noticia 18"),
    path('noticia 19', noticia_19, name="noticia 19"),
    path('noticia 20', noticia_20, name="noticia 20"),
    path('noticia 21', noticia_21, name="noticia 21"),
    path('noticia 22', noticia_22, name="noticia 22"),
    path('noticia 23', noticia_23, name="noticia 23"),
    path('noticia 24', noticia_24, name="noticia 24"),
    path('noticia 25', noticia_25, name="noticia 25"),
    path('noticia 26', noticia_26, name="noticia 26"),
    path('noticia 27', noticia_27, name="noticia 27"),
    path('noticia 28', noticia_28, name="noticia 28"),
    path('noticia 29', noticia_29, name="noticia 29"),
    path('empleados/', empleados, name="empleados"),
    path('empleados/add/', empleadosadd, name="empleadosadd"),
    path('empleados/update/<id>', empleadosupdate, name="empleadosupdate"),
    path('empleados/delete/<id>', empleadosdelete, name="empleadosdelete"),
    path('register/', register, name="register"),
    path('clima', clima, name="clima"),
    path('EE.UU', EE_UU, name="EE.UU"),
    path('Mexico', Mexico, name="Mexico"),
    path('Salud', Salud, name="Salud"),
    path('Mundo', Mundo, name="Mundo"),
    path('Deportes', Deportes, name="Deportes"),
    path('account_locked/', account_locked, name="account_locked"),
    path('suscripcíon', suscripcíon, name="suscripcíon"),
    path('carrito', carrito, name="carrito"),
    path('api/', include(router.urls)),

    path('reset_password/', auth_views.PasswordResetDoneView.as_view(), name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetView.as_view(), name="password_reset_done"),

    path('reset_password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]