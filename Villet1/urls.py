from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reg/', views.reg, name='reg'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reg2/', views.reg2, name='reg2'),
    path('reg2/adduser', views.adduser, name='adduser'),
    path('logout/', views.logout, name='logout'),
    path('Vadmin/', views.Vadmin, name='Vadmin'),
    path('Vadmin2/', views.Vadmin2, name='Vadmin2'),
    path('Vadmin3/', views.Vadmin3, name='Vadmin3'),

    path('fullinfo/<int:suserid>', views.fullinfo, name='fullinfo'),
    path('fullinfo2/<int:suserid>', views.fullinfo2, name='fullinfo2'),
    path('fullinfo3/<int:suserid>', views.fullinfo3, name='fullinfo3'),
    path('fullinfo4/<int:tt>', views.fullinfo4, name='fullinfo4'),
    path('fullinfo5/<int:tt>', views.fullinfo5, name='fullinfo5'),


    path('fullinfo/approve', views.approve, name='approve'),

    path('transaction/', views.transaction, name='transaction'),
    path('autopay/', views.autopay, name='autopay'),
    path('bill/', views.bill, name='bill'),
    path('inactive/<int:tid>', views.inactive, name='inactive'),

    path('shopingapp/', views.shopingapp, name='shopingapp'),
    path('shopingapp/rq1', views.rq1, name='rq1'),
    path('shopingapp/rq2', views.rq2, name='rq2'),

    path('reg/regdb', views.regdb, name='regdb'),
    path('terms/', views.terms, name='terms'),
    path('login/', views.login, name='login'),
    path('login/logindb', views.logindb, name='logindb'),
    path('admin/', admin.site.urls),
]