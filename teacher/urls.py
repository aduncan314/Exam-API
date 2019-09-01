from django.urls import path

from teacher import views

urlpatterns = [
    path('', views.teacher_list),
    path('<int:pk>', views.teacher_detail)
]
