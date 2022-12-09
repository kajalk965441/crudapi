from django.contrib import admin
from django.urls import path
from . import views
from api.views import studentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="/"),
    path('get_Studentlist/<str:pk>/', views.studentView, name="studentview"),
    path('add-student', views.studentAdd, name="studentadd"),
    path('update-student/<str:pk>/', views.studentUpdate, name="studentupdate"),
    path('delete-student/<str:pk>/', views.studentdelete, name="studentdelete")
]
