from datetime import date, timedelta
from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.crypto import get_random_string
from Register_Login.models import *

# Create your views here.

def distributor_dashboard(request):
    if 'login_id' in request.session:
        if request.session.has_key('login_id'):
            login_id = request.session['login_id']
            
        else:
            return redirect('/')  
        log_det = LoginDetails.objects.get(id=login_id)
        distributor_det = DistributorDetails.objects.get(login_details=log_det)
    # dash_details = DistributorDetails.objects.get(id=pk,superadmin_approval=1)
    context = {
        'distributor_details': distributor_det
    }
    return render(request, 'distributor_dash.html', context)

def dist_clients(request):
    if 'login_id' in request.session:
        if request.session.has_key('login_id'):
            login_id = request.session['login_id']
            
        else:
            return redirect('/')  
        log_det = LoginDetails.objects.get(id=login_id)
        distributor_det = DistributorDetails.objects.get(login_details=log_det)
    return render(request,'dist_clients.html',{'distributor_details':distributor_det})

def dist_client_requests(request):
    if 'login_id' in request.session:
        if request.session.has_key('login_id'):
            login_id = request.session['login_id']
            
        else:
            return redirect('/')  
        log_det = LoginDetails.objects.get(id=login_id)
        distributor_det = DistributorDetails.objects.get(login_details=log_det)
        clients = CompanyDetails.objects.filter(Distributor_approval=0,distributor=distributor_det).order_by('-id')
    return render(request,'dist_client_requests.html',{'distributor_details':distributor_det,'clients':clients})

def dist_client_accept(request,id):
  data=CompanyDetails.objects.filter(id=id).update(Distributor_approval=1,superadmin_approval=1)
  return redirect('dist_client_requests')

def dist_client_reject(request,id):
  data=CompanyDetails.objects.get(id=id)
  data.login_details.delete()
  data.delete()
  return redirect('dist_client_requests')

def dist_client_request_overview(request,id):
  if 'login_id' in request.session:
        if request.session.has_key('login_id'):
            login_id = request.session['login_id']
            
        else:
            return redirect('/')  
        log_det = LoginDetails.objects.get(id=login_id)
        distributor_det = DistributorDetails.objects.get(login_details=log_det)
        data=CompanyDetails.objects.get(id=id)
        allmodules=ZohoModules.objects.get(company=data,status='New')
        return render(request,'dist_client_request_overview.html',{'company':data,'allmodules':allmodules,'distributor_details':distributor_det})

def dist_all_clients(request):
  if 'login_id' in request.session:
        if request.session.has_key('login_id'):
            login_id = request.session['login_id']
            
        else:
            return redirect('/')  
        log_det = LoginDetails.objects.get(id=login_id)
        distributor_det = DistributorDetails.objects.get(login_details=log_det)
        clients=CompanyDetails.objects.filter(Distributor_approval=1,distributor=distributor_det)
        
        return render(request,'dist_all_clients.html',{'clients':clients,'distributor_details':distributor_det})

def dist_client_details(request,id):
  if 'login_id' in request.session:
        if request.session.has_key('login_id'):
            login_id = request.session['login_id']
            
        else:
            return redirect('/')  
        log_det = LoginDetails.objects.get(id=login_id)
        distributor_det = DistributorDetails.objects.get(login_details=log_det)
        data=CompanyDetails.objects.get(id=id)
        allmodules=ZohoModules.objects.get(company=data,status='New')
        return render(request,'dist_client_details.html',{'company':data,'allmodules':allmodules,'distributor_details':distributor_det})

def distributor_profile(request):
   if 'login_id' in request.session:
        if request.session.has_key('login_id'):
            login_id = request.session['login_id']
            
        else:
            return redirect('/')  
        log_det = LoginDetails.objects.get(id=login_id)
        distributor= DistributorDetails.objects.get(login_details=log_det)
   return render(request,'distributor_profile.html',{'distributor_details':distributor})

def dist_edit_profilePage(request,id):
  
  distributor = DistributorDetails.objects.get(id=id)
  terms=PaymentTerms.objects.all()
  return render(request,'edit_distributor_profile.html',{'terms':terms,'distributor_details':distributor})

def update_distributor_profile(request,id):
    distributor = DistributorDetails.objects.get(id=id)

    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['ph']
        pic = request.FILES.get('image')


        login_data = LoginDetails.objects.get(id=distributor.login_details_id)
        login_data.first_name = fname
        login_data.last_name = lname
        login_data.email = email
        login_data.save()

        distributor.contact = phone
        if pic:
            distributor.image = pic
        distributor.save()

    return redirect('distributor_profile')