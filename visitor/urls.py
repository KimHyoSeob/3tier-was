from django.urls import path
from . import views

app_name = 'visitor'

urlpatterns = [
    path('', views.VisitorHomeView.as_view(), name='visitor_home'),
    path('visitor_list/', views.VisitorListView.as_view(), name='visitor_list'),
    path('visitor_detail/<int:pk>', views.VisitorDetailView.as_view(), name='visitor_detail'),
    path('visitor_create/', views.VisitorCreateView.as_view(), name='visitor_create'),
    path('visitor_delete/<int:pk>', views.VisitorDeleteView.as_view(), name='visitor_delete'),
]