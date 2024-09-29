from django.urls import path
from . import views
from .views import EmployeeListView, employee_create, employee_update

urlpatterns = [
    path('', EmployeeListView.as_view(), name='employee_list'),
    path('create/', employee_create, name='employee_create'),
    path('<int:pk>/edit/', employee_update, name='employee_update'),
]
