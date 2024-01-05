from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from Register_Login.models import *
from django.contrib import messages


# Create your views here.

@login_required(login_url='login_page')
def admindash(request):
  return render(request, 'admindash.html')

def payment_terms(request):
  terms = PaymentTerms.objects.all()
  return render(request,'payment_terms.html',{'terms':terms})

def add_payment_terms(request):
  if request.method == 'POST':
    num=int(request.POST['num'])
    select=request.POST['select']
    if select == 'Years':
      days=int(num)*365
      pt = PaymentTerms(payment_terms_number = num,payment_terms_value = select,days = days)
      pt.save()
      messages.info(request, 'Payment term is added!')
      return redirect('payment_terms')

    else:  
      days=int(num*30)
      pt = PaymentTerms(payment_terms_number = num,payment_terms_value = select,days = days)
      pt.save()
      messages.info(request, 'Payment term is added!')
      return redirect('payment_terms')


  return redirect('payment_terms')

#distributor approval section----------------------------


def admin_distributors(request):
    return render(request,'distributors.html')

def distributor_requests(request):
  
  distributors = DistributorDetails.objects.filter(superadmin_approval=0).order_by('-id')
  return render(request,'distributor_requests.html',{'distributors':distributors})

def admin_distributor_accept(request,id):
  data=DistributorDetails.objects.filter(id=id).update(superadmin_approval=1)
  return redirect('distributor_requests')

def admin_distributor_reject(request,id):
  data=DistributorDetails.objects.get(id=id)
  data.login_details.delete()
  data.delete()
  return redirect('distributor_requests')

def distributor_request_overview(request,id):
  data=DistributorDetails.objects.get(id=id)
  return render(request,'distributor_request_overview.html',{'data':data})

def all_distributors(request):
  distributors=DistributorDetails.objects.filter(superadmin_approval=1)
  return render(request,'all_distributors.html',{'distributors':distributors})

def distributor_details(request,id):
  data=DistributorDetails.objects.get(id=id)
  return render(request,'distributor_details.html',{'data':data})

#client approval section----------------------------

def admin_clients(request):
    return render(request,'clients.html')

def client_requests(request):
  
  clients = CompanyDetails.objects.filter(superadmin_approval=0,reg_action='self').order_by('-id')
  return render(request,'client_requests.html',{'clients':clients})

def admin_client_accept(request,id):
  data=CompanyDetails.objects.filter(id=id).update(superadmin_approval=1)
  return redirect('client_requests')

def admin_client_reject(request,id):
  data=CompanyDetails.objects.get(id=id)
  data.login_details.delete()
  data.delete()
  return redirect('client_requests')

def client_request_overview(request,id):
  data=CompanyDetails.objects.get(id=id)
  allmodules=ZohoModules.objects.get(company=data,status='New')
  return render(request,'client_request_overview.html',{'company':data,'allmodules':allmodules})

def all_clients(request):
  clients=CompanyDetails.objects.filter(superadmin_approval=1,reg_action='self')
  return render(request,'all_clients.html',{'clients':clients})

def client_details(request,id):
  data=CompanyDetails.objects.get(id=id)
  allmodules=ZohoModules.objects.get(company=data,status='New')
  return render(request,'client_details.html',{'data':data,'allmodules':allmodules})

# Admin notifications------------------------------------

def admin_notification(request):
  data= ZohoModules.objects.filter(update_action=1,status='Pending')

  return render(request,'admin_notification.html',{'data':data})

def module_updation_details(request,mid):
  data= ZohoModules.objects.get(id=mid)
  allmodules= ZohoModules.objects.get(company=data.company,status='Pending')
  old_modules = ZohoModules.objects.get(company=data.company,status='New')

  return render(request,'admin/module_updation_details.html',{'data':data,'allmodules':allmodules,'old_modules':old_modules})

def module_updation_ok(request,mid):
  
  old=ZohoModules.objects.get(company=mid,status='New')
  old.delete()

  data=ZohoModules.objects.get(company=mid,status='Pending')  
  data.status='New'
  data.save()
  data1=ZohoModules.objects.filter(company=mid).update(update_action=0)
  return redirect('admin_notification')



  
  