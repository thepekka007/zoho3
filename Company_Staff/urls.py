from django.urls import path
from . import views

urlpatterns = [
    # -------------------------------Company section--------------------------------
    path('Company-Dashboard',views.company_dashboard,name='company_dashboard'),
    path('Company-Profile',views.company_profile,name='company_profile'),
    path('Company/Staff-Request',views.company_staff_request,name='company_staff_request'),
    path('Company/Staff-Request/Accept/<int:pk>',views.staff_request_accept,name='staff_request_accept'),
    path('Company/Staff-Request/Reject/<int:pk>',views.staff_request_reject,name='staff_request_reject'),
    path('Company/All-Staffs',views.company_all_staff,name='company_all_staff'),
    path('Company/Staff-Approval/Cancel/<int:pk>',views.staff_approval_cancel,name='staff_approval_cancel'),
   




    # -------------------------------Staff section--------------------------------
    path('Staff-Dashboard',views.staff_dashboard,name='staff_dashboard'),
     path('Staff-Profile',views.staff_profile,name='staff_profile'),


    # -------------------------------Zoho Modules section--------------------------------\


    # tinto urls items

       path('new_items',views.new_items,name='new_items'),
       path('company_items',views.company_items,name='company_items'),
        path('create_item',views.create_item,name='create_item'),
         path('itemsoverview/<int:pk>',views.itemsoverview,name='itemsoverview'),
            path('edititems/<int:pr>',views.edititems,name='edititems'),
         
       
  
    # Chartof accounts urls
         path('chartofaccounts',views.chartofaccounts,name='chartofaccounts'),
        path('addchartofaccounts',views.addchartofaccounts,name='addchartofaccounts'),
         path('create_account',views.create_account,name='create_account'),
          path('chartofaccountsoverview/<int:pk>',views.chartofaccountsoverview,name='chartofaccountsoverview'),
     path('editchartofaccounts/<int:pr>',views.editchartofaccounts,name='editchartofaccounts'),
    
    
]