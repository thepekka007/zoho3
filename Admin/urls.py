from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('Payment_Terms',views.payment_terms,name='payment_terms'),
    path('Add_Payment_Terms',views.add_payment_terms,name='add_payment_terms'),
    path('Add_Payment_Terms',views.add_payment_terms,name='add_payment_terms'),

    path('Admin_Dashboard',views.admindash,name='admindash'),
    path('Admin_Distributors',views.admin_distributors,name='admin_distributors'),
    path('Distributor_Requests',views.distributor_requests,name='distributor_requests'),
    path('Admin_Distributor_Accept\<int:id>',views.admin_distributor_accept,name='admin_distributor_accept'),
    path('Admin_Distributor_Reject\<int:id>',views.admin_distributor_reject,name='admin_distributor_reject'),
    path('Distributor_Request_Overview\<int:id>',views.distributor_request_overview,name='distributor_request_overview'),
    path('All_Distributors',views.all_distributors,name='all_distributors'),
    path('Distributor_Details\<int:id>',views.distributor_details,name='distributor_details'),
    

    path('Admin_clients',views.admin_clients,name='admin_clients'),
    path('Client_Requests',views.client_requests,name='client_requests'),
    path('Admin_Client_Accept\<int:id>',views.admin_client_accept,name='admin_client_accept'),
    path('Admin_Client_Reject\<int:id>',views.admin_client_reject,name='admin_client_reject'),
    path('Client_Request_Overview\<int:id>',views.client_request_overview,name='client_request_overview'),
    path('All_Clients',views.all_clients,name='all_clients'),
    path('Client_Details\<int:id>',views.client_details,name='client_details'),
   

   
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)