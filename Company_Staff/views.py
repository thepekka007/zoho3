from django.db import models
from django.shortcuts import render,redirect
from Register_Login.models import *
from Company_Staff.models import *
from Register_Login.views import logout
from django.shortcuts import get_object_or_404

from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from xhtml2pdf import pisa
from django.template.loader import get_template
from bs4 import BeautifulSoup
import io
from django.conf import settings
from io import BytesIO
# Create your views here.
from datetime import date
from django.db.models import Max

# -------------------------------Company section--------------------------------

# company dashboard
def company_dashboard(request):
    if 'login_id' in request.session:
        if request.session.has_key('login_id'):
            log_id = request.session['login_id']
           
        else:
            return redirect('/')
        log_details= LoginDetails.objects.get(id=log_id)
        dash_details = CompanyDetails.objects.get(login_details=log_details,superadmin_approval=1,Distributor_approval=1)
        allmodules= ZohoModules.objects.get(company=dash_details,status='New')
        context = {
            'details': dash_details,
            'allmodules': allmodules
        }
        return render(request, 'company/company_dash.html', context)
    else:
        return redirect('/')


# company profile
def company_profile(request):
    if 'login_id' in request.session:
        if request.session.has_key('login_id'):
            log_id = request.session['login_id']
           
        else:
            return redirect('/')
        log_details= LoginDetails.objects.get(id=log_id)
        dash_details = CompanyDetails.objects.get(login_details=log_details,superadmin_approval=1,Distributor_approval=1)
        allmodules= ZohoModules.objects.get(company=dash_details,status='New')
        context = {
            'details': dash_details,
            'allmodules': allmodules
        }
        return render(request, 'company/company_profile.html', context)
    else:
        return redirect('/')

# company profile
def company_staff_request(request):
    if 'login_id' in request.session:
        if request.session.has_key('login_id'):
            log_id = request.session['login_id']
           
        else:
            return redirect('/')
        log_details= LoginDetails.objects.get(id=log_id)
        dash_details = CompanyDetails.objects.get(login_details=log_details,superadmin_approval=1,Distributor_approval=1)
        allmodules= ZohoModules.objects.get(company=dash_details,status='New')
        staff_request=StaffDetails.objects.filter(company=dash_details.id, company_approval=0).order_by('-id')
        context = {
            'details': dash_details,
            'allmodules': allmodules,
            'requests':staff_request,
        }
        return render(request, 'company/staff_request.html', context)
    else:
        return redirect('/')

# company staff accept or reject
def staff_request_accept(request,pk):
    staff=StaffDetails.objects.get(id=pk)
    staff.company_approval=1
    staff.save()
    return redirect('company_staff_request')

def staff_request_reject(request,pk):
    staff=StaffDetails.objects.get(id=pk)
    login_details=LoginDetails.objects.get(id=staff.company.id)
    login_details.delete()
    staff.delete()
    return redirect('company_staff_request')


# All company staff view, cancel staff approval
def company_all_staff(request):
    if 'login_id' in request.session:
        if request.session.has_key('login_id'):
            log_id = request.session['login_id']
           
        else:
            return redirect('/')
        log_details= LoginDetails.objects.get(id=log_id)
        dash_details = CompanyDetails.objects.get(login_details=log_details,superadmin_approval=1,Distributor_approval=1)
        allmodules= ZohoModules.objects.get(company=dash_details,status='New')
        all_staffs=StaffDetails.objects.filter(company=dash_details.id, company_approval=1).order_by('-id')
        print(all_staffs)
        context = {
            'details': dash_details,
            'allmodules': allmodules,
            'staffs':all_staffs,
        }
        return render(request, 'company/all_staff_view.html', context)
    else:
        return redirect('/')

def staff_approval_cancel(request,pk):
    staff=StaffDetails.objects.get(id=pk)
    staff.company_approval=2
    staff.save()
    return redirect('company_all_staff')









# -------------------------------Staff section--------------------------------

# staff dashboard
def staff_dashboard(request):
    if 'login_id' in request.session:
        if request.session.has_key('login_id'):
            log_id = request.session['login_id']
           
        else:
            return redirect('/')
        log_details= LoginDetails.objects.get(id=log_id)
        dash_details = StaffDetails.objects.get(login_details=log_details,company_approval=1)
        allmodules= ZohoModules.objects.get(company=dash_details.company,status='New')
        context={
            'details':dash_details,
            'allmodules': allmodules,
        }
        return render(request,'staff/staff_dash.html',context)
    else:
        return redirect('/')


# staff profile
def staff_profile(request):
    if 'login_id' in request.session:
        if request.session.has_key('login_id'):
            log_id = request.session['login_id']
           
        else:
            return redirect('/')
        log_details= LoginDetails.objects.get(id=log_id)
        dash_details = StaffDetails.objects.get(login_details=log_details,company_approval=1)
        allmodules= ZohoModules.objects.get(company=dash_details.company,status='New')
        context={
            'details':dash_details,
            'allmodules': allmodules,
        }
        return render(request,'staff/staff_profile.html',context)
    else:
        return redirect('/')











# -------------------------------Zoho Modules section--------------------------------
    



    # tinto view items

def company_items(request):
    item=Items.objects.all()

    return render(request, 'zohomodules/company_items.html',{'item':item})
   

def new_items(request):
    units = Unit.objects.all()
    return render(request, 'zohomodules/newitem.html',{'units':units})

def create_item(request):
    
    login_id = request.session['login_id']
    log_user = LoginDetails.objects.get(id=login_id)
    if log_user.user_type == 'Company':
        company_id = request.session['login_id']
        
        if request.method=='POST':
            a=Items()
            b=Item_Transaction_History()
            c = CompanyDetails.objects.get(login_details=company_id)
            b.company=c
            b.logindetails=log_user
            a.login_details=log_user
            a.company=c
            a.item_type = request.POST.get("type",None)
            a.item_name = request.POST.get("name",None)
            unit_id = request.POST.get("unit")
            uid=Unit.objects.get(id=unit_id)
            # unit_instance = get_object_or_404(Unit, id=unit_id)
            a.unit = uid
            a.hsn_code = request.POST.get("hsn",None)
            a.tax_reference = request.POST.get("radio",None)
            a.intrastate_tax = request.POST.get("intra",None)
            a.interstate_tax= request.POST.get("inter",None)
            a.selling_price = request.POST.get("sel_price",None)
            a.sales_account = request.POST.get("sel_acc",None)
            a.sales_description = request.POST.get("sel_desc",None)
            a.purchase_price = request.POST.get("cost_price",None)
            a.purchase_account = request.POST.get("cost_acc",None)
            a.purchase_description = request.POST.get("pur_desc",None)
            a.minimum_stock_to_maintain = request.POST.get("minimum_stock",None)
            a.activation_tag = request.POST.get("status",None)
            a.inventory_account = request.POST.get("invacc",None)
            a.opening_stock = request.POST.get("openstock",None)
            a.save()    
            t=Items.objects.get(id=a.id)
            b.items=t
            b.save()
            return redirect('company_items')
    elif log_user.user_type == 'Staff':
        staff_id = request.session['login_id']
        if request.method=='POST':
            a=Items()
            b=Item_Transaction_History()
            staff = LoginDetails.objects.get(id=staff_id)
            sf = StaffDetails.objects.get(login_details=staff)
            c=sf.company
            b.Date=date.today()
            b.company=c
            b.logindetails=log_user
            a.login_details=log_user
            a.company=c
            a.item_type = request.POST.get("type",None)
            a.item_name = request.POST.get("name",None)
            unit_id = request.POST.get("unit")
            unit_instance = get_object_or_404(Unit, id=unit_id)
            a.unit = unit_instance
            a.hsn_code = request.POST.get("hsn",None)
            a.tax_reference = request.POST.get("radio",None)
            a.intrastate_tax = request.POST.get("intra",None)
            a.interstate_tax= request.POST.get("inter",None)
            a.selling_price = request.POST.get("sel_price",None)
            a.sales_account = request.POST.get("sel_acc",None)
            a.sales_description = request.POST.get("sel_desc",None)
            a.purchase_price = request.POST.get("cost_price",None)
            a.purchase_account = request.POST.get("cost_acc",None)
            a.purchase_description = request.POST.get("pur_desc",None)
            a.minimum_stock_to_maintain = request.POST.get("minimum_stock",None)
            a.activation_tag = request.POST.get("status",None)
            a.inventory_account = request.POST.get("invacc",None)
            a.opening_stock = request.POST.get("openstock",None)
        
        

        
            a.save()    
            t=Items.objects.get(id=a.id)
            b.items=t
            b.save()
            return redirect('company_items')
    return redirect('company_items')




def itemsoverview(request,pk):
    items=Items.objects.all()  
    selitem=Items.objects.get(id=pk)
    stock_value=selitem.opening_stock*selitem.purchase_price  
    latest_date = Item_Transaction_History.objects.filter(items_id=pk).aggregate(latest_date=Max('Date'))['latest_date']    
    filtered_data = Item_Transaction_History.objects.filter(Date=latest_date, items_id=pk)

    return render(request, 'zohomodules/itemsoverview.html',{'items':items,'selitem':selitem,'stock_value':stock_value,'latest_item_id':filtered_data})


def edititems(request, pr):
    # Retrieve the chart of accounts entry
    item = get_object_or_404(Items, id=pr)
    units = Unit.objects.all()

    # Check if 'company_id' is in the session
    login_id = request.session['login_id']
    log_user = LoginDetails.objects.get(id=login_id)
    if log_user.user_type == 'Company':
        company_id = request.session['login_id']
    
        
        if request.method=='POST':
   
            b=Item_Transaction_History()
            c = CompanyDetails.objects.get(login_details=company_id)
            b.company=c
            b.logindetails=log_user
            b.action="Edited"
            b.Date=date.today()
            item.login_details=log_user
            item.company=c
            item.item_type = request.POST.get("type",None)
            item.item_name = request.POST.get("name",None)
            unit_id = request.POST.get("unit")
            unit_instance = get_object_or_404(Unit, id=unit_id)
            item.unit = unit_instance
            item.hsn_code = request.POST.get("hsn",None)
            item.tax_reference = request.POST.get("radio",None)
            item.intrastate_tax = request.POST.get("intra",None)
            item.interstate_tax= request.POST.get("inter",None)
            item.selling_price = request.POST.get("sel_price",None)
            item.sales_account = request.POST.get("sel_acc",None)
            item.sales_description = request.POST.get("sel_desc",None)
            item.purchase_price = request.POST.get("cost_price",None)
            item.purchase_account = request.POST.get("cost_acc",None)
            item.purchase_description = request.POST.get("pur_desc",None)
            item.minimum_stock_to_maintain = request.POST.get("minimum_stock",None)
            item.activation_tag = request.POST.get("status",None)
            item.inventory_account = request.POST.get("invacc",None)
            item.opening_stock = request.POST.get("openstock",None)
            
            # Save the changes
            item.save()
            t=Items.objects.get(id=item.id)
            b.items=t
            b.save()
            # Redirect to another page after successful update
            return redirect('itemsoverview', pr)
    elif log_user.user_type == 'Staff':
        staff_id = request.session['login_id']
        if request.method=='POST':
            a=Items()
            b=Item_Transaction_History()
            staff = LoginDetails.objects.get(id=staff_id)
            sf = StaffDetails.objects.get(login_details=staff)
            c=sf.company
            b.company=c
            b.logindetails=log_user
            b.action="Edited"
            b.Date=date.today()
            a.login_details=log_user
            a.company=c
            item.item_type = request.POST.get("type",None)
            item.item_name = request.POST.get("name",None)
            unit_id = request.POST.get("unit")
            unit_instance = get_object_or_404(Unit, id=unit_id)
            item.unit = unit_instance
            item.hsn_code = request.POST.get("hsn",None)
            item.tax_reference = request.POST.get("radio",None)
            item.intrastate_tax = request.POST.get("intra",None)
            item.interstate_tax= request.POST.get("inter",None)
            item.selling_price = request.POST.get("sel_price",None)
            item.sales_account = request.POST.get("sel_acc",None)
            item.sales_description = request.POST.get("sel_desc",None)
            item.purchase_price = request.POST.get("cost_price",None)
            item.purchase_account = request.POST.get("cost_acc",None)
            item.purchase_description = request.POST.get("pur_desc",None)
            item.minimum_stock_to_maintain = request.POST.get("minimum_stock",None)
            item.activation_tag = request.POST.get("status",None)
            item.inventory_account = request.POST.get("invacc",None)
            item.opening_stock = request.POST.get("openstock",None)
            item.save()
            t=Items.objects.get(id=item.id)
            b.items=t
            b.save()

        return redirect('itemsoverview', pr)
 
    return render(request, 'zohomodules/edititems.html', {'item': item,'units':units})
   
def item_status_edit(request, pv):
    
    selitem = Items.objects.get(id=pv)

    if selitem.activation_tag == 'Active':
        selitem.activation_tag = 'inactive'
        selitem.save()
    elif selitem.activation_tag != 'Active':
        selitem.activation_tag = 'Active'
        selitem.save()

    selitem.save()

    return redirect('itemsoverview',pv)


def shareItemToEmail(request,pt):
    if request.user: 
        try:
            if request.method == 'POST':
                emails_string = request.POST['email_ids']
                # Split the string by commas and remove any leading or trailing whitespace
                emails_list = [email.strip() for email in emails_string.split(',')]
                email_message = request.POST['email_message']
                print(emails_list)
                print('1')
           
           
                item = Items.objects.get(id=pt)
                context = {
                
                    'selitem':item,
                }
                template_path = 'itememailpdf.html'
                template = get_template(template_path)
                html  = template.render(context)
                result = BytesIO()
                pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)#, link_callback=fetch_resources)
                pdf = result.getvalue()
                filename = f'Item Transactipns.pdf'
                subject = f"Transactipns"
                email = EmailMessage(subject, f"Hi,\nPlease find the attached Item transactions. \n{email_message}\n\n--\nRegards,\n{item.item_name}\n{item.item_type}", from_email=settings.EMAIL_HOST_USER,to=emails_list)
                email.attach(filename,pdf,"application/pdf")
                email.send(fail_silently=False)
                msg = messages.success(request, 'Details has been shared via email successfully..!')
                return redirect(itemsoverview,pt)
        except Exception as e:
            print(e)
            messages.error(request, f'{e}')
            return redirect(itemsoverview,pt)   
        
def deleteitem(request,pl):
    items=Items.objects.filter(id=pl)
    items.delete()
    
    return redirect(company_items)

        
# tinto views chart of accounts


def addchartofaccounts(request):
    cur_user = request.user
    user_id=cur_user.id
    print(user_id)
    context={'user_id':user_id}
    return render(request, 'zohomodules/addchartofaccounts.html',context)

def chartofaccounts(request):
    acc=Chart_of_Accounts.objects.all()
    

    return render(request, 'zohomodules/chartofaccounts.html',{'acc':acc})

def create_account(request):
    login_id = request.session['login_id']
    log_user = LoginDetails.objects.get(id=login_id)
    if log_user.user_type == 'Company':
        company_id = request.session['login_id']
        if request.method=='POST':
            a=Chart_of_Accounts()
            b=Chart_of_Accounts_History()
            c = CompanyDetails.objects.get(login_details=company_id)
            b.company=c
            b.logindetails=log_user
            b.action="Created"
            b.Date=date.today()
            a.login_details=log_user
            a.company=c
          
        
            a.account_type = request.POST.get("account_type",None)
            a.account_name = request.POST.get("account_name",None)
            a.account_code = request.POST.get("account_code",None)
            a.description = request.POST.get("description",None)
    
            a.Create_status="active"
            a.save()
            t=Chart_of_Accounts.objects.get(id=a.id)
            b.chart_of_accounts=t
            b.save()
            return redirect('chartofaccounts')
    elif log_user.user_type == 'Staff':
        staff_id = request.session['login_id']
        if request.method=='POST':
            a=Chart_of_Accounts()
            b=Chart_of_Accounts_History()
            staff = LoginDetails.objects.get(id=staff_id)
            sf = StaffDetails.objects.get(login_details=staff)
            a=sf.company
            b.Date=date.today()
            b.company=c
            b.logindetails=log_user
            a.login_details=log_user
            a.company=c
          
        
            a.account_type = request.POST.get("account_type",None)
            a.account_name = request.POST.get("account_name",None)
            a.account_code = request.POST.get("account_code",None)
            a.description = request.POST.get("description",None)
    
            a.Create_status="active"
            a.save()
            t=Chart_of_Accounts.objects.get(id=a.id)
            b.chart_of_accounts=t
            b.save()
            return redirect('chartofaccounts')

    return redirect('addchartofaccounts')

def chartofaccountsoverview(request,pk):
    acc=Chart_of_Accounts.objects.all()  
    selacc=Chart_of_Accounts.objects.get(id=pk)  
    latest_date = Chart_of_Accounts_History.objects.filter(chart_of_accounts_id=pk).aggregate(latest_date=Max('Date'))['latest_date']    
    filtered_data = Chart_of_Accounts_History.objects.filter(Date=latest_date, chart_of_accounts_id=pk)
    return render(request, 'zohomodules/chartofaccountsoverview.html',{'acc':acc,'selacc':selacc,'latest_item_id':filtered_data})


from django.shortcuts import render, redirect

def editchartofaccounts(request, pr):
    # Retrieve the chart of accounts entry
    acc = get_object_or_404(Chart_of_Accounts, id=pr)

    # Check if 'company_id' is in the session
    login_id = request.session['login_id']
    log_user = LoginDetails.objects.get(id=login_id)
    if log_user.user_type == 'Company':
        company_id = request.session['login_id']

        if request.method == 'POST':
        
            b=Chart_of_Accounts_History()
            c = CompanyDetails.objects.get(login_details=company_id)
            b.company=c
            b.logindetails=log_user
            b.action="Edited"
            b.Date=date.today()
            acc.login_details=log_user
            acc.company=c
            # Update the chart of accounts entry with the form data
            acc.account_type = request.POST['account_type']
            acc.account_name = request.POST['account_name']
            acc.account_code = request.POST['account_code']
            acc.description = request.POST['description']
            
            # Save the changes
            acc.save()
            t=Chart_of_Accounts.objects.get(id=acc.id)
            b.chart_of_accounts=t
            b.save()

            # Redirect to another page after successful update
            return redirect('chartofaccountsoverview', pr)
    elif log_user.user_type == 'Staff':
        staff_id = request.session['login_id']
        if request.method=='POST':
         
            b=Chart_of_Accounts_History()
            staff = LoginDetails.objects.get(id=staff_id)
            sf = StaffDetails.objects.get(login_details=staff)
            c=sf.company
            b.company=c
            b.logindetails=log_user
            b.action="Edited"
            b.Date=date.today()
            acc.login_details=log_user
            acc.company=c
            # Update the chart of accounts entry with the form data
            acc.account_type = request.POST['account_type']
            acc.account_name = request.POST['account_name']
            acc.account_code = request.POST['account_code']
            acc.description = request.POST['description']
            
            # Save the changes
            acc.save()
            t=Chart_of_Accounts.objects.get(id=acc.id)
            b.chart_of_accounts=t
            b.save()

            # Redirect to another page after successful update
            return redirect('chartofaccountsoverview', pr)

        return redirect('chartofaccountsoverview', pr)
    return render(request, 'zohomodules/editchartofaccounts.html', {'acc': acc})

def deleteaccount(request,pl):
    acc=Chart_of_Accounts.objects.filter(id=pl)
    acc.delete()
    
    return redirect(chartofaccounts)


def acc_status_edit(request, pv):
    
    selacc = Chart_of_Accounts.objects.get(id=pv)

    if selacc.status == 'Active':
        selacc.status = 'inactive'
        selacc.save()
    elif selacc.status != 'Active':
        selacc.status = 'Active'
        selacc.save()

    selacc.save()

    return redirect('chartofaccountsoverview',pv)
