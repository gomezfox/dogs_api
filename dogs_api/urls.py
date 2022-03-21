from django.contrib import admin
from django.urls import path, re_path
from dogs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path(r'^$', views.ApiRoot.as_view()),
    path('api/dogs/', views.DogList.as_view()),
    re_path(r'^api/dogs/(?P<pk>[0-9]+)/$', views.DogDetail.as_view()),
    path('api/breeds/', views.BreedList.as_view()),
    re_path(r'^api/breeds/(?P<pk>[0-9]+)/$', views.BreedDetail.as_view()),
]