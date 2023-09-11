from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import Http404
from django.db.models import Q
from datetime import datetime, timedelta


# Create your views here.
def index(request):
    return render(request, 'index.html')



from .models import VilletUser,ActiveCreditCard,VUTransaction

def adduser(request):
    current_user = request.user

    if request.method == 'POST':
        userid = current_user.id   
        username = current_user.first_name
        email = current_user.email    
        mobile_number = request.POST.get('mobile') 
        dob = request.POST.get('dobi')
        gender = request.POST.get('gender')
        perm_adr = request.POST.get('padd')
        temp_adr = request.POST.get('tadd')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pan=request.POST.get('pan')    
        aadhar=request.POST.get('aad')    
        occn=request.POST.get('ccn')    
        anninc=request.POST.get('ai')    
        exc_cre=request.POST.get('ecl')    
        c_b_name = request.POST.get('cbn')
        designation = request.POST.get('desg')
        no_of_yemp=request.POST.get('noye')


        VU=VilletUser.objects.create(userid=userid,username=username,email=email,mobile_number=mobile_number,dob=dob,gender=gender,
                                  perm_adr=perm_adr,temp_adr=temp_adr,city=city,state=state,pan=pan,aadhar=aadhar,
                                  occn=occn,anninc=anninc,exc_cre=exc_cre,c_b_name=c_b_name,designation=designation,no_of_yemp=no_of_yemp) 
        VU.save()
        messages.success(request, 'We have recived your request and your Villet credit card will be soon activated..') 
    return redirect('/dashboard')





def regdb(request):
    first_name=request.POST['first_name']
    email=request.POST['email']
    username=request.POST['email']
    password=request.POST['password']
    cpassword=request.POST['cpassword']

    if User.objects.filter(username=username).exists() :
        messages.error(request, 'email exists')
        return redirect("/reg")
    
    elif password!=cpassword :
        messages.error(request, 'Password doest match')
        return render(request, 'reg1.html')
    
    else :
        user=User.objects.create_user(username=username,first_name=first_name,email=email,password=password)
        user.save()
        messages.success(request, 'USER CREATED YOU CAN LOGIN NOW ')
        return redirect("/login")
        

def reg(request) : 
    return render(request, 'reg1.html')

def shopingapp(request) : 
    return render(request, 'shopingapp.html')

def rq1(request) :

    tra_name=request.POST['tra_name']
    tra_type=request.POST['tra_type']
    amt=request.POST['amt']
    rec_acc=request.POST['rec_acc']
    vcc=request.POST['vcc']
    peri_tra=request.POST['peri_tra']
    dur=request.POST['dur']
    
    card_num=ActiveCreditCard.objects.values_list('card_number',flat=True)
    
    if any(num == vcc for num in card_num) :
        trans = VUTransaction.objects.filter(Villet_Credit_Card_Number=vcc).order_by('-date_time')
        amt1=0 
        pcre=0
        for transaction in trans :
            amt1=amt1+transaction.amount
                
        cl = get_object_or_404(ActiveCreditCard,card_number=vcc)
        pcre=cl.credit_limit-amt1
        if pcre >= float(amt) :
            NT=VUTransaction.objects.create(Transaction_Name=tra_name,amount=amt,transaction_type=tra_type,
                                Receiver_Account_Number=rec_acc,Villet_Credit_Card_Number=vcc,
                                Periodic_Transaction=peri_tra,Duration=dur)
            NT.save()
            messages.success(request, f"Your Transaction to {tra_name} of Amount Rs.{amt} is successfull")
            return redirect("/shopingapp")
        else :
            messages.success(request, "Please Check Your Credit limit | Transaction Cancelled")
            return redirect("/shopingapp")

    else :
        messages.success(request, 'Card Number does not exist ')
        return redirect("/shopingapp")
    

def rq2(request) :
    tra_name=request.POST['tra_name']
    tra_type=request.POST['tra_type']
    amt=request.POST['amt']
    rec_acc=request.POST['rec_acc']
    vcc=request.POST['vcc']
    card_num=ActiveCreditCard.objects.values_list('card_number',flat=True)
    
    if any(num == vcc for num in card_num) :
        trans = VUTransaction.objects.filter(Villet_Credit_Card_Number=vcc).order_by('-date_time')
        amt1=0 
        pcre=0
        for transaction in trans :
            amt1=amt1+transaction.amount
                
        cl = get_object_or_404(ActiveCreditCard,card_number=vcc)
        pcre=cl.credit_limit-amt1
        if pcre >= float(amt) :
            NT=VUTransaction.objects.create(Transaction_Name=tra_name,amount=amt,transaction_type=tra_type,
                                Receiver_Account_Number=rec_acc,Villet_Credit_Card_Number=vcc)
            NT.save()
            messages.success(request, f"Your Transaction to {tra_name} of Amount Rs.{amt} is successfull")
            return redirect("/shopingapp")
        else :
            messages.success(request, "Please Check Your Credit limit | Transaction Cancelled")
            return redirect("/shopingapp")

    else :
        messages.success(request, 'Card Number does not exist ')
        return redirect("/shopingapp")
    


def fullinfo2(request,suserid) : 
    request_user = ActiveCreditCard.objects.all()
    suser = get_object_or_404(ActiveCreditCard,userid=suserid)
    return render(request,'Vadmin2.html',{'suser':suser,'rqusers':request_user})

def fullinfo(request,suserid) : 
    request_user = VilletUser.objects.all()
    suser = get_object_or_404(VilletUser,userid=suserid)
    return render(request,'Vadmin.html',{'suser':suser,'rqusers':request_user})

def fullinfo3(request,suserid) : 
    request_user = VilletUser.objects.all()
    suser = get_object_or_404(VilletUser,userid=suserid)
    return render(request,'Vadmin3.html',{'suser':suser,'rqusers':request_user})

def approve(request) : 

    if request.method == 'POST':
        
        user_id = request.POST.get('user_id') 
        suser = get_object_or_404(VilletUser,userid=user_id)
        userid = suser.userid   
        user_name = suser.username
        active_numberAV = 1
        credit_limit = request.POST.get('credit_limit') 

    obj=VilletUser.objects.get(userid = userid)
    obj.active_number = 1
    obj.save()
    VAU=ActiveCreditCard.objects.create(userid=userid,user_name=user_name,active_numberAV=active_numberAV,credit_limit=credit_limit) 
    VAU.save()
    return redirect('/Vadmin2')


def logout(request) :
    auth.logout(request)
    return redirect("/")

def Vadmin(request) :

    request_user = VilletUser.objects.all()
    return render(request, 'Vadmin.html',{'rqusers':request_user})

def Vadmin2(request) :

    request_user = ActiveCreditCard.objects.all()
    return render(request, 'Vadmin2.html',{'rqusers':request_user})

def Vadmin3(request) :

    request_user = VilletUser.objects.all()
    return render(request, 'Vadmin3.html',{'rqusers':request_user})


def dashboard(request) : 

    current_user = request.user
    request_user = VilletUser.objects.all()

    try:
        activeuser= get_object_or_404(ActiveCreditCard,userid=current_user.id)
    except ActiveCreditCard.DoesNotExist:
        activeuser = None
    except Http404:
        activeuser = None    

    user_id = -1 
    for user in request_user :
        if current_user.id == user.userid :
            user_id = user.userid 


    user_data = {
        'username': current_user.username,
        'email': current_user.email,
        'first_name':current_user.first_name,
        'id':current_user.id,
        'user_id' : user_id,
    }

    try:
        transactions = VUTransaction.objects.filter(Villet_Credit_Card_Number=activeuser.card_number).order_by('-date_time')[:2]
        trans = VUTransaction.objects.filter(Villet_Credit_Card_Number=activeuser.card_number).order_by('-date_time')

        amt=0 
        pcre=0
        for transaction in trans :
            amt=amt+transaction.amount
        pcre=activeuser.credit_limit-amt
    except AttributeError:
        amt=0 
        pcre=0
        transactions=None
        print("Attribute does not exist")
   
    return render(request, 'dashboard.html',{'user_data':user_data,'activeuser':activeuser,'transactions': transactions,'amt':amt,'pcre':pcre})


def transaction(request) : 
    current_user = request.user

    try:
        activeuser= get_object_or_404(ActiveCreditCard,userid=current_user.id)
    except ActiveCreditCard.DoesNotExist:
        activeuser = None
    except Http404:
        activeuser = None    

    user_data = {
        'username': current_user.username,
        'email': current_user.email,
        'first_name':current_user.first_name,
    }
    transactions = VUTransaction.objects.filter(Villet_Credit_Card_Number=activeuser.card_number).order_by('-date_time')

    return render(request, 'transaction.html',{'user_data':user_data,'transactions': transactions})

def autopay(request) : 
    current_user = request.user

    try:
        activeuser= get_object_or_404(ActiveCreditCard,userid=current_user.id)
    except ActiveCreditCard.DoesNotExist:
        activeuser = None
    except Http404:
        activeuser = None    

    user_data = {
        'username': current_user.username,
        'email': current_user.email,
        'first_name':current_user.first_name,
    }
    transactions = VUTransaction.objects.filter(Q(Villet_Credit_Card_Number=activeuser.card_number)& ~Q(Duration = 0)).order_by('-date_time')

    return render(request, 'autopay.html',{'user_data':user_data,'transactions': transactions})

def bill(request) : 
    current_user = request.user

    try:
        activeuser= get_object_or_404(ActiveCreditCard,userid=current_user.id)
    except ActiveCreditCard.DoesNotExist:
        activeuser = None
    except Http404:
        activeuser = None    

    user_data = {
        'username': current_user.username,
        'email': current_user.email,
        'first_name':current_user.first_name,
    }
    newdate = activeuser.last_bill_date + timedelta(days=30)
    update = ActiveCreditCard.objects.get(userid=current_user.id)
    update.new_bill_date = newdate
    update.save()
    amt=0.00
    camt=0.00
    gamt=0.00
    current_date = datetime.now().date()

    transactions = VUTransaction.objects.filter(Villet_Credit_Card_Number=activeuser.card_number)
    for transaction in transactions :
        amt=amt+float(transaction.amount)
    
    
    if current_date > newdate :
        gamt = round(0.12 * amt,2)

    camt = amt*0.005
    tamt =amt+camt + gamt
    return render(request, 'bill.html',{'user_data':user_data,'amt':amt,'camt':camt,'gamt':gamt,'tamt':tamt,'newdate':newdate})

def inactive(request,tid):
    tran=VUTransaction.objects.get(transaction_id=tid)
    tran.active="inactive"
    tran.save()
    return redirect("/autopay")

def fullinfo4(request,tt) : 
    current_user = request.user

    try:
        activeuser= get_object_or_404(ActiveCreditCard,userid=current_user.id)
    except ActiveCreditCard.DoesNotExist:
        activeuser = None
    except Http404:
        activeuser = None    

    user_data = {
        'username': current_user.username,
        'email': current_user.email,
        'first_name':current_user.first_name,
    }
    transactions = VUTransaction.objects.filter(Villet_Credit_Card_Number=activeuser.card_number).order_by('-date_time')

    ttt = get_object_or_404(VUTransaction,transaction_id=tt)
    return render(request,'transaction.html',{'ttt':ttt,'transactions': transactions,'user_data':user_data})

def fullinfo5(request,tt) : 
    current_user = request.user

    try:
        activeuser= get_object_or_404(ActiveCreditCard,userid=current_user.id)
    except ActiveCreditCard.DoesNotExist:
        activeuser = None
    except Http404:
        activeuser = None    

    user_data = {
        'username': current_user.username,
        'email': current_user.email,
        'first_name':current_user.first_name,
    }
    transactions = VUTransaction.objects.filter(Q(Villet_Credit_Card_Number=activeuser.card_number)& ~Q(Duration = 0)).order_by('-date_time')

    ttt = get_object_or_404(VUTransaction,transaction_id=tt)
    return render(request,'autopay.html',{'ttt':ttt,'transactions': transactions,'user_data' : user_data})


def reg2(request) : 

    current_user = request.user

    user_data = {
        'username': current_user.username,
        'email': current_user.email,
        'first_name':current_user.first_name,
        'id' : current_user.id,
    }
    return render(request, 'reg2.html',{'user_data':user_data})

def login(request):
    return render(request, 'login.html')

def logindb(request):
    username=request.POST['username']
    password=request.POST['password']
    
    user = auth.authenticate(username=username,password=password)
    if user is not None :
        auth.login(request,user)
        current_user = request.user
        user_data = {
        'username': current_user.username,
        'email': current_user.email,
        'first_name':current_user.first_name,
        }

        return redirect('/dashboard',{'user_data':user_data})
    else :
        messages.error(request, 'Invalid Credencials')
        return render(request, 'login.html')

def terms(request):
    return render(request, 'terms.html')