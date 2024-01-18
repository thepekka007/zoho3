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


    # ------------------------- TINTO urls items  START---------------------

        path('new_items',views.new_items,name='new_items'),
        path('items_list',views.items_list,name='items_list'),
        path('create_item',views.create_item,name='create_item'),
        path('itemsoverview/<int:pk>',views.itemsoverview,name='itemsoverview'),
        path('edititems/<int:pr>',views.edititems,name='edititems'),
        path('item_status_edit/<int:pv>',views.item_status_edit,name='item_status_edit'),
        path('shareItemToEmail/<int:pt>',views.shareItemToEmail,name='shareItemToEmail'),
        path('deleteitem/<int:pl>',views.deleteitem,name='deleteitem'),
        path('add_item_comment/<int:pc>',views.add_item_comment,name='add_item_comment'),
        
        path('add_unit',views.add_unit,name='add_unit'),
        path('unit_dropdown',views.unit_dropdown,name = 'unit_dropdown'),
        path('downloadItemSampleImportFile',views.downloadItemSampleImportFile,name='downloadItemSampleImportFile'),
        path('import_item',views.import_item,name='import_item'),
        path('item_view_sort_by_name/<int:pk>',views.item_view_sort_by_name,name='item_view_sort_by_name'),
        path('item_view_sort_by_hsn/<int:pk>',views.item_view_sort_by_hsn,name='item_view_sort_by_hsn'),
        path('filter_item_view_Active/<int:pk>',views.filter_item_view_Active,name='filter_item_view_Active'),
        path('filter_item_view_inActive/<int:pk>',views.filter_item_view_inActive,name='filter_item_view_inActive'),

  #  ----------------------------- TINTO urls items  END-----------------------------

    # -------------------------TINTO Chartof accounts urls  START------------------------

        path('chartofaccounts',views.chartofaccounts,name='chartofaccounts'),
        path('addchartofaccounts',views.addchartofaccounts,name='addchartofaccounts'),
        path('create_account',views.create_account,name='create_account'),
        path('chartofaccountsoverview/<int:pk>',views.chartofaccountsoverview,name='chartofaccountsoverview'),
        path('editchartofaccounts/<int:pr>',views.editchartofaccounts,name='editchartofaccounts'),
        path('deleteaccount/<int:pl>',views.deleteaccount,name='deleteaccount'),
        path('acc_status_edit/<int:pv>',views.acc_status_edit,name='acc_status_edit'),
        path('add_account_comment/<int:pc>',views.add_account_comment,name='add_account_comment'),
    
      
        path('add_account',views.add_account,name='add_account'),
        path('account_dropdown',views.account_dropdown,name = 'account_dropdown'),
        path('account_view_sort_by_name/<int:pk>',views.account_view_sort_by_name,name='account_view_sort_by_name'),
        path('shareaccountToEmail/<int:pt>',views.shareaccountToEmail,name='shareaccountToEmail'),
        path('chartofaccountsActive',views.chartofaccountsActive,name='chartofaccountsActive'),
        path('chartofaccountsInactive',views.chartofaccountsInactive,name='chartofaccountsInactive'),



         #------------------------- TINTO Chartof accounts urls  ENDS----------------------

           path('delete_account_comment/<int:ph>/<int:pr>',views.delete_account_comment,name='delete_account_comment'),
           path('delete_item_comment/<int:ph>/<int:pr>',views.delete_item_comment,name='delete_item_comment'),
           path('accounts_asset_filter',views.accounts_asset_filter,name='accounts_asset_filter'),
            path('accounts_liability_filter',views.accounts_liability_filter,name='accounts_liability_filter'),
             path('accounts_equity_filter',views.accounts_equity_filter,name='accounts_equity_filter'),
              path('accounts_income_filter',views.accounts_income_filter,name='accounts_income_filter'),
               path('accounts_expense_filter',views.accounts_expense_filter,name='accounts_expense_filter'),


           
           
           
           
          
]