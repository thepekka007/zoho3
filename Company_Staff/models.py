from django.db import models
from Register_Login.models import *
# Create your models here.

#---------------- models for zoho modules--------------------



    


class Unit(models.Model):
    # user=models.ForeignKey(User,on_delete=models.CASCADE,default='')
    unit_name=models.CharField(max_length=255)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)

class Items(models.Model):
   
    item_type=models.CharField(max_length=255)
    item_name=models.CharField(max_length=255)
   
    unit=models.ForeignKey(Unit,on_delete=models.CASCADE)
    hsn_code=models.IntegerField(null=True,blank=True)
    tax_reference=models.CharField(max_length=255,null=True)
    intrastate_tax=models.IntegerField(null=True,blank=True)
    interstate_tax=models.IntegerField(null=True,blank=True)

    selling_price=models.IntegerField(null=True,blank=True)
    sales_account=models.CharField(max_length=255)
    sales_description=models.CharField(max_length=255)

    purchase_price=models.IntegerField(null=True,blank=True)
    purchase_account=models.CharField(max_length=255)
    purchase_description=models.CharField(max_length=255)
   
    minimum_stock_to_maintain=models.IntegerField(blank=True,null=True)  
    activation_tag=models.CharField(max_length=255,default='active')
    inventory_account=models.CharField(max_length=255,null=True)

    date=models.DateTimeField(auto_now_add=True)
    opening_stock=models.IntegerField(blank=True,null=True,default=0)
    current_stock=models.IntegerField(blank=True,null=True,default=0)
    opening_stock_per_unit=models.IntegerField(blank=True,null=True,)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    login_details=models.ForeignKey(LoginDetails,on_delete=models.CASCADE)

class Item_Transaction_History(models.Model):
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    logindetails=models.ForeignKey(LoginDetails,on_delete=models.CASCADE)
    items=models.ForeignKey(Items,on_delete=models.CASCADE)
    Date=models.DateField(null=True)
    action=models.CharField(max_length=255,default='Created')

class Items_comments(models.Model):                                              # new model by tinto
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    logindetails=models.ForeignKey(LoginDetails,on_delete=models.CASCADE)
    Items=models.ForeignKey(Items,on_delete=models.CASCADE)
    comments = models.CharField(max_length=255,null=True,blank=True)

class Chart_of_Accounts(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    account_type = models.CharField(max_length=255,null=True,blank=True)
    account_name = models.CharField(max_length=255,null=True,blank=True)
    
    account_code = models.CharField(max_length=255,null=True,blank=True)
    description = models.CharField(max_length=255,null=True,blank=True)
    status=models.CharField(max_length=255,null=True,blank=True,default='Active')
    Create_status = models.CharField(max_length=255,null=True,blank=True,default='added')
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    login_details=models.ForeignKey(LoginDetails,on_delete=models.CASCADE)

class Chart_of_Accounts_History(models.Model):
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    logindetails=models.ForeignKey(LoginDetails,on_delete=models.CASCADE)
    chart_of_accounts=models.ForeignKey(Chart_of_Accounts,on_delete=models.CASCADE)
    Date=models.DateField(null=True)
    action=models.CharField(max_length=255,default='Created')



class chart_of_accounts_comments(models.Model):                                              # new model by tinto
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    logindetails=models.ForeignKey(LoginDetails,on_delete=models.CASCADE)
    chart_of_accounts=models.ForeignKey(Chart_of_Accounts,on_delete=models.CASCADE)
    comments = models.CharField(max_length=255,null=True,blank=True)
    
