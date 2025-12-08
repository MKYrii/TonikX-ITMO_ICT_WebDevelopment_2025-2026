from django.urls import path

from .views import *

urlpatterns = [
    path('admin/cars/', AdminCarListAPIView.as_view(), name='admin-car-list'),
    path('admin/cars/create/', AdminCarCreateAPIView.as_view(), name='admin-car-create'),
    path('admin/cars/<int:pk>/', AdminCarDetailAPIView.as_view(), name='admin-car-detail'),
    path("admin/maintenance_companies/", MaintenanceCompanyListCreateAPIView.as_view(),
         name='admin-maintenance-company-list'),
    path("admin/maintenance_companies/<int:id>/", MaintenanceCompanyDetailAPIView.as_view(),
         name='admin-maintenance-company-detail'),
    path(
        "admin/cars/<int:id>/maintenance/",
        CarMaintenanceAPIView.as_view(),
        name="admin_car_maintenance"
    ),
    path(
        "admin/lease_applications/",
        LeaseApplicationAPIView.as_view(),
        name="admin_lease_applications"
    ),
    path(
        "admin/lease_applications/<int:id>/",
        LeaseApplicationAPIView.as_view(),
        name="admin_lease_application_detail"
    ),
    path(
        "admin/lease_applications/<int:id>/approve/",
        LeaseApplicationAPIView.as_view(),
        name="admin_lease_application_approve"
    ),
    path(
        "admin/leases/",
        LeaseAPIView.as_view(),
        name="admin_leases"
    ),
    path(
        "admin/leases/<int:id>/",
        LeaseAPIView.as_view(),
        name="admin_lease_detail"
    ),
    path(
        "admin/clients/",
        ClientAPIView.as_view(),
        name="admin_clients"
    ),
    path(
        "admin/clients/<int:id>/",
        ClientAPIView.as_view(),
        name="admin_client_detail"
    ),
    path("cars/", CarsListAPIView.as_view(), name="cars_list"),
    path("cars/<int:id>/", CarDetailAPIView.as_view(), name="car_detail"),
    path("cars/<int:id>/application/", CarApplicationAPIView.as_view(), name="car_application"),
    path("admin/car_specifications/", AdminCarSpecificationAPIView.as_view()),
    path("admin/fleets/", AdminFleetAPIView.as_view()),
    path("admin/car_fleets/", AdminCarFleetAPIView.as_view()),
]
