from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.views.generic.base import TemplateView
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from .forms import *
import random
import sys
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
class homepageview(TemplateView):
    template_name = 'apcitizen/homepage.html'
    
# def login(request):
#     if request.method == "POST":
#         fm = loginform(request.POST)
#         if fm.is_valid():
#             aad_num = request.POST.get('user_name')
#             password = request.POST.get('password')
#             try:
#                 udata = voterregister.objects.get(user_name=aad_num)
#                 pdata = voterregister.objects.get(password=password)
#                 if udata==None:
#                     if pdata==None:
#                         return HttpResponseRedirect('/voteformla/')
#                     else:
#                         messages.add_message(request,messages.ERROR, 'Incorrect Password')
#             except ObjectDoesNotExist:
#                 messages.add_message(request,messages.ERROR, "User does'nt exist!")
#             # response= HttpResponse(f'Hello {aad_num}')
#             # print(aad_num)
#     fm = loginform()
#     return render(request, 'apcitizen/login.html', {'fm':fm})

def register(request):
    if request.method == "POST":
        fm = aadharform(request.POST)
        if fm.is_valid():
            aadhar_num = random.randint(3000000000, 9999999999)
            f_name = fm.cleaned_data['full_name']
            dob = fm.cleaned_data['date_of_birth']
            fa_name = fm.cleaned_data['father_name']
            phone_num = fm.cleaned_data['phone_number']
            data = aadhar(
                full_name=f_name,
                date_of_birth=dob,
                father_name=fa_name,
                phone_number=phone_num,
                aadhar_number=aadhar_num
            )
            data.save()
            messages.add_message(request,messages.SUCCESS, 'Registered Successfully.')
            return HttpResponseRedirect('/getaadhar/')
    else:
        fm = aadharform()
    return render(request, 'apcitizen/register.html', {'fm': fm})

def getaadhar(request):
    data=None
    if request.method == "POST":
        fm = GetAadharForm(request.POST)
        if fm.is_valid():
            mobile = fm.cleaned_data['mobile_number']
        try:
            data = aadhar.objects.get(phone_number=mobile)
        except ObjectDoesNotExist:
            messages.add_message(request,messages.ERROR, "Invalid Phone Number.")
    else:
        fm=GetAadharForm()
    return render(request, 'apcitizen/getaadhar.html',{'form':fm,'aadhar':data})

def voterregisterview(request):
    if request.method == 'POST':
        fm = VoterRegisterForm(request.POST)
        if fm.is_valid():
            user_name = fm.cleaned_data['user_name']
            pwd = fm.cleaned_data['password']
            pwd1 = fm.cleaned_data['confirm_password']
            try:
                aadhar.objects.get(aadhar_number=user_name)
            except ObjectDoesNotExist:
                messages.add_message(request, messages.ERROR, 'Your aadhar data is not exist. Please create aadhar')
            else:
                login_data = voterregister(
                    password = pwd,
                    user_name = user_name,
                    aadhar_number = user_name,
                )
                if pwd != pwd1:
                    messages.add_message(request,messages.ERROR, 'Password and Confirm Password are not same.')
                else:
                    login_data.save()
                    return HttpResponseRedirect('/')
    fm = VoterRegisterForm()
    return render(request, 'apcitizen/voterregister.html',{'form':fm})


def voteformla(request):
    mla_name = []
    party =['YSRCP','TDP','INC','BJP','NOTA']
    try:
        if request.method == 'POST':
            fm = AssemblySelectionForm(request.POST)
            
            if fm.is_valid():
                try:
                    voter = fm.cleaned_data['aadhar_number']
                    aadhar.objects.get(aadhar_number=voter)
                    try:
                        voterregister.objects.get(aadhar_number=voter)
                    except ObjectDoesNotExist:
                        messages.add_message(request,messages.ERROR,"Your name is not in voters list, Please Register as voter.")
                        return redirect('/voterregister/')
                except ObjectDoesNotExist:
                    messages.add_message(request, messages.ERROR, "You are not a citizen of Andhra Pradesh! create aadhar")
                    return redirect('/aadharregister/')
                
                try:
                    mlapolling.objects.get(user=voter)
                except ObjectDoesNotExist:
                    messages.add_message(request,messages.SUCCESS,"You can vote now.")
                
                constituency = fm.cleaned_data['options']
                if constituency == 'Kurnool':
                    mla_name = ['ABDUL HAFEEZ KHAN','T.G.BHARATH','M.JOHN WILSON','VENKATA SUBBA REDDY. B','NOTA']                
                elif constituency == 'Srisailam':
                    mla_name = ['SILPA CHAKRAPANI REDDY','BUDDA RAJASHEKHAR REDDY','NAYAB SYED TASHLIMA','BUDDA SRIKANTH REDDY','NOTA']
                elif constituency == 'Nandyal':
                    mla_name = ['SILPA RAVI CHANDRA KISHORE REDDY','N.M.D FAROOK','GOPAVARAM GOKUL KRISHNA REDDY','MALIKIREDDY SIVA SANKAR REDDY','NOTA']
                elif constituency == 'Nandikotkur':
                    mla_name = ['DARA SUDHEER','G JAYASURYA','THOGURU ARTHUR','G.S.NAGARAJU','NOTA']
                elif constituency == 'Allagadda':
                    mla_name = ['BRIJENDRA REDDY GANGULA(NANI)','AKHILA PRIYA BHUMA','BARAGODLA HUSSAIN BASHA','BOREDDY LAKSHMI REDDY','NOTA']
                elif constituency == 'Kadapa':
                    mla_name = ['AZMATH BASHA SHAIK BEPARI','MADHAVI REDDAPPA GARI','T.K AFZAL ALI KHAN','SREENIVASULU REDDY KANDULA','NOTA']
                elif constituency == 'Pulivendla':
                    mla_name = ['Y S JAGAN MOHAN REDDY','B.TECH RAVI','DHRUVA KUMAR REDDY','PEDABALLI SUSHMA','NOTA']
                elif constituency == 'Kodur':
                    mla_name = ['KORAMUTLA SREENIVASULU','ARAVA SREEDHAR','DEVI GOSALA','PANATHALA SURESH','NOTA']
                elif constituency == 'Kuppam':
                    mla_name = ['K.R.J.BHARATH','NARA CHANDRA BABU NAIDU','A. GOVINDHARUJULU','N.S.THULASINATH','NOTA']
                elif constituency == 'Tirupati':
                    mla_name = ['BHUMANA ABHINAY','A. SATHYAVATHI','K. PRAMILA','BHAVANI SANKAR VALLAMCHETTY','NOTA']
                elif constituency == 'Srikakulam':
                    mla_name = ['DHARMANA PRASADA RAO','GONDU SHANKAR','AMBATI KRISHNA RAO','CHALLA VENKATESWARA RAO','NOTA']
                elif constituency == 'Kadiri':
                    mla_name = ['MAQBOOL B.S.','KANDIKUNTA VENKATA PRASAD','K.S. SHANWAZ','S.V. NAGENDRA PRASAD','NOTA']
                elif constituency == 'Hindupur':
                    mla_name = ['SHAIK MOHAMMED IQBAL','NANDAMURI BALAKRISHNA','T. BALAJI MANOHAR','P.D. PARTHA SARATHY','NOTA']
                elif constituency == 'Adoni':
                    mla_name = ['Y. SAI PRASAD REDDY','KONKA MEENAKSHI NAIDU','BOYA NEELAKANTAPPA','KUNIGIRI NEELAKANTA','NOTA']
                elif constituency == 'Dhone':
                    mla_name = ['BUGGANA RAJA REDDY','KAMBALAPADU EDIGA PRATHAP','VENKATA SIVA REDDY GUNAPALLE','K. RAMANJANEYULU','NOTA']
                elif constituency == 'Pattikonda':
                    mla_name = ['KANGATI SREEDEVI','K.E. SHYAM KUMAR','BOYA KRANTHI NAYUDU','EEDIGA RANGA GOUD','NOTA']
                elif constituency == 'Kodumur':
                    mla_name = ['JARADODDI SUDHAKAR','BURLA. RAMANJANEYULU','DAMODARAN RADHAKRISHNA MURTHY','MEESALA PREM KUMAR','NOTA']
                elif constituency == 'Gajuwaka':
                    mla_name = ['NAGIREDDY TIPPALA','PAWAN KALYAN KONIDALA','GOLLAKOTA VENKATA SUBBA RAO','PULUSU JANARDHANA RAO','NOTA']
                elif constituency == 'Vishakapatnam':
                    mla_name = ['KAMMILA KANNAPARAJU(K.K.RAJU)','GANTA SRINIVASA RAO','GOMPA GOVINDA RAJU','VISHNU KUMAR RAJU PENMETSA','NOTA']
                elif constituency == 'Vizianagaram':
                    mla_name = ['VEERA BHADRA SWAMY KOLAGATLA','ADITI VIJAYALAKSHMI GAJAPATHI RAJU PUSAPATI','SATISH KUMAR SUNKARI','KUSUMANCHI SUBBA RAO','NOTA']
                elif constituency == 'Guntur':
                    mla_name = ['MOHAMMED MUSTAFA SHAIK','MOHAMMED NASEER','JAGAN MOHAN REDDY MADDIREDDY','NERELLA V.S. SURESH','NOTA']
                
                if request.method == 'POST':
        # Check if the user has already voted
                    try:
                        mlapolling.objects.get(user=voter)
                    except ObjectDoesNotExist:
                        # User hasn't voted, proceed with the voting process
                        name = request.POST.get('mla')
                try:
                    mlapolling.objects.get(user=voter)
                except ObjectDoesNotExist:
                    data = mlapolling(user=voter, MLA_name=name)
                    data.save()
                    messages.add_message(request,messages.SUCCESS,"Voted Successfully")
                else:
                    messages.add_message(request,messages.ERROR, "You are not able to vote, as you already voted. THANK YOU")
    except IntegrityError:
        messages.add_message(request, messages.ERROR,"Please vote to any MLA.")

    else:
        fm = AssemblySelectionForm()
    
    candidates = zip(mla_name, party)
    return render(request, 'apcitizen/voteformla.html', {'form': fm, 'candidates': candidates})


def voteformp(request):
    mp_name=[]
    party =['YSRCP','TDP','INC','BJP','NOTA']
    try:
        if request.method == 'POST':
            fm = ParlimentSelectionForm(request.POST)
            
            if fm.is_valid():
                try:
                    voter = fm.cleaned_data['aadhar_number']
                    aadhar.objects.get(aadhar_number=voter)
                    try:
                        voterregister.objects.get(aadhar_number=voter)
                    except ObjectDoesNotExist:
                        messages.add_message(request,messages.ERROR,"Your name is not in voters list, Please Register as voter.")
                        return redirect('/voterregister/')
                except ObjectDoesNotExist:
                    messages.add_message(request, messages.ERROR, "You are not a citizen of Andhra Pradesh! create aadhar")
                    return redirect('/aadharregister/')
                
                try:
                    mppolling.objects.get(user=voter)
                except ObjectDoesNotExist:
                    messages.add_message(request,messages.SUCCESS,"You can vote now.")
                
                constituency = fm.cleaned_data['options']
                
                if constituency == 'Kurnool':
                    mp_name=['B.Y.RAMAIAH','BASTIPATI NAGARAJU PANCHALINGALA','P.G.RAMPULLAIAH YADAV LUCKY-2','SUNKARA SREEDHAR','NOTA']
                elif constituency == 'Kadapa':
                    mp_name=['Y.S.AVINASH REDDY','CHADIPIRALLA BHUPESH SUBBARAMI REDDY','Y.S.SHARMILA REDDY','PANDITI. GURAPPA','NOTA']
                elif constituency == 'Nandyal':
                    mp_name=['POCHA BRAMHANANDA REDDY','DR. BYREDDY SHABARI','J LAKSHMI NARASIMHA YADAV','GOGULA SUGUNAMMA','NOTA']
                elif constituency == 'Thirupati':
                    mp_name=['GURUMOORTHY MADDILA','A.VARAPRASAD','B.BHARANI BAS','VARAPRASAD RAO VELAGAPALLI','NOTA']
                elif constituency == 'Vijayawada':
                    mp_name=['KESINENI SRINIVAS (NANI)','KESINENI SIVANATH (CHINNI)','BHARGAV VALLURU','MEKA VENKATESWARA RAO','NOTA']
                
                if request.method == 'POST':
        # Check if the user has already voted
                    try:
                        mppolling.objects.get(user=voter)
                    except ObjectDoesNotExist:
                        # User hasn't voted, proceed with the voting process
                        name = request.POST.get('mp')
                try:
                    mppolling.objects.get(user=voter)
                except ObjectDoesNotExist:
                    data = mppolling(user=voter, MP_name=name)
                    data.save()
                    messages.add_message(request,messages.SUCCESS,"Voted Successfully")
                else:
                    messages.add_message(request,messages.ERROR, "You are not able to vote, as you already voted. THANK YOU")
    except IntegrityError:
        messages.add_message(request, messages.ERROR,"Please vote to any MP.")

    else:
        fm = ParlimentSelectionForm()
    
    candidates = zip(mp_name, party)
    return render(request, 'apcitizen/voteformp.html', {'form':fm, 'candidates':candidates})