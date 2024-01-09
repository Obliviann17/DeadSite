from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path('product/<slug:product_slug>', views.product_page, name="product_page"),
    path('about/', views.about_us, name="about"),
    path('contact_us/', views.contact_us, name="contact"),
    path('products/', views.products, name="products"),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout_page, name='logout'),

]