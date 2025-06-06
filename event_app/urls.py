from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('',views.home),
    path('about',views.about),
    path('event',views.event),
    path('gallery',views.gallery),
    path('contact',views.contact),
    path('privateparty',views.privateparty),
    path('wedding',views.wedding),
    path('when',views.when),
    path('blog',views.blog),
    path('booking',views.booking),
    # user
    path('register/', views.register_user, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_user, name='logout'),
    # event
    path('events/', views.event_list, name='events'),
    path('events/<int:pk>/', views.event_detail, name='event_detail'),
    path('events/<int:pk>/book/', views.book_event, name='book_event'),
    
    path("book/<int:event_id>/", views.book_event, name="book_event"),
    path("my-bookings/", views.my_bookings, name="my_bookings"),
    #  user-admin
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('admin-panel/', views.admin_dashboard, name='admin_dashboard'),
]
