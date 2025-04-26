from django.urls import path
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path('',views.main, name="main"),
    path('post/new/', views.create_post, name='create_post'),
    path('post/<int:pk>/edit/', views.update_post, name='update_post'),
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('contact/',views.contact, name = "contact"),
    path('about/',views.aboutMe, name = "about_me"),
    path('blog/about/',views.aboutBlog, name = "about_blog"),
#login and logout stuff
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('logout/', views.custom_logout_view, name='logout'),
    path('notFound', views.notFound,name='notFound'),


  
]