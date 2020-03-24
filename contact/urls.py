from django.urls import path

from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.ContactListView.as_view(), name='email_list'),
    path('create/', views.ContactCreateView.as_view(), name='email_send'),
    path('update/<pk>', views.ContactUpdateView.as_view(), name='email_update'),
    path('delete/<pk>', views.ContactDeleteView.as_view(), name='email_delete'),
    path('detail/<pk>', views.ContactDetailView.as_view(), name='email_detail'),
]