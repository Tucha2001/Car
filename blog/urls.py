from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name='about'),
    path('cars/', views.cars, name='cars'),
    path('blog/', views.blog, name='blog'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('detail_car/<int:car_id>', views.detail_car, name='detail_car'),
    path('description_car/', views.description_car, name='description_car'),

]