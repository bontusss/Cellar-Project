from django.urls import path

from . import views

urlpatterns = [
    path('governors/', views.GovernorList.as_view()),
    path('<int:pk>/', views.GovernorDetail.as_view()),
]
