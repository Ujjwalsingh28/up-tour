from django.urls import path


from . import views

urlpatterns=[
    path('',views.index),
    path('home',views.index),
    path('aboutus',views.aboutus),
    path('destinations',views.destinations),
    path('gallery/',views.gallery,name='gallery'),
    path('contactus',views.contactus),
    path('faqs',views.faqs),
    path('varanasi',views.varanasi),
    path('agra',views.agra),
    path('ayodhya',views.ayodhya),
    path('chitrakoot',views.chitrakoot),
    path('lucknow',views.lucknow),
    path('prayagraj',views.prayagraj),
    path('vrindavan',views.vrindavan),
    path('raebareli',views.raebareli),
    path('mirzapur',views.mirzapur),
    path('pratapgarh',views.pratapgarh),
    path('etawah',views.etawah),
    path('raebareli',views.raebareli),
    path('kanpur',views.kanpur),
    path('register',views.register),
    path('login',views.login,name='login'),
    path('logout',views.logout),
]