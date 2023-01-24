from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('puppies/', views.puppies_index, name='index'),
    path('puppies/<int:puppy_id>/', views.puppies_detail, name='detail'),
    path('puppies/create/', views.PuppyCreate.as_view(), name='puppies_create'),
    path('puppies/<int:pk>/update/', views.PuppyUpdate.as_view(), name='puppies_update'),
    path('puppies/<int:pk>/delete/', views.PuppyDelete.as_view(), name='puppies_delete'),
    path('puppies/<int:puppy_id>/add_walkings/', views.add_walkings, name='add_walkings'),
    path('puppies/<int:puppy_id>/assoc_clothes/<int:clothes_id>/', views.assoc_clothes, name='assoc_clothes'),

]
