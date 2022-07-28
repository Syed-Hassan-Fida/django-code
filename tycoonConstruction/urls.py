from django.urls import path, re_path
# from django.conf.urls import url
from django.urls import include, re_path
from . import views

app_name = 'tycoonConstruction'

urlpatterns = [
    path('', views.index, name='home'),
    path('services/', views.services, name='services'),
    path('hireVendor/', views.Vendor_details, name='hireVendor'),
    path('vendorAdmin/', views.vendor_Admin, name='vendorAdmin'),
    path('contractorAdmin/', views.contractor_Admin, name='contractorAdmin'),
    path('hireContractor/', views.hire_contractor, name='hireContractor'),
    # Bidding route
    path('hireContractor/bidContractor/<int:id>', views.bidContractorr, name='bidContractorr'),
    path('hireVendor/bidVendor/<int:id>',
         views.bid_Vendor, name='bid_Vendor'),
    # cost calculation
    path('costEstimation/', views.cost_estimation, name='costEstimation'),
    path('brickwall/', views.brickwall, name='brickwall'),
    path('walldeduction/', views.walldeduction, name='walldeduction'),
    path('labourcost/', views.labourcost, name='labourcost'),
    path('pillarandbeam/', views.pillarandbeam, name='pillarandbeam'),
    # vendor_details
    path('vendor_details/', views.vendor_admin_details,
         name='vendor_details'),
    path('vtoc_request/', views.vtoc_request, name='vtoc_request'),
    # contractor_details
    path('contractor_details/', views.contractor_details,
         name='contractor_details'),
     # try
     path('projectstry/', views.projectstry,
          name='projectstry'),
]