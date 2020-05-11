from django.urls import path

from . import views, api_views

app_name = 'contact'

urlpatterns = [
    path('', views.ContactListView.as_view(), name='email_list'),
    path('create/', views.ContactCreateView.as_view(), name='email_create'),
    path('update/<pk>/', views.ContactUpdateView.as_view(), name='email_update'),
    path('delete/<pk>/', views.ContactDeleteView.as_view(), name='email_delete'),
    path('detail/<pk>/', views.ContactDetailView.as_view(), name='email_detail'),
    path('email/', views.email_view, name='email'),
    path('api/create', api_views.ContactAPIView.as_view()),
    path('api/detail/<pk>', api_views.ContactDetailAPIView.as_view()),
]