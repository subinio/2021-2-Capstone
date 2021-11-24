from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Doctor, Institution, Patient
import json

#from .textEmotionClassifier import *
#from .voiceEmotionClassifier import *

member_type=None

def checkType(request):
  if request.user.is_authenticated:
    if(Doctor.objects.filter(id=request.user.get_username())):
      return "doctor"
    elif(Patient.objects.filter(id=request.user.get_username())):
      return "patient" 
  else:
    return None
  return None

def index(request):
  age = 0
  emotion =1
  member_type = checkType(request)
  context = {
    	'emotion':emotion,
      'age':age,
      'member_type':member_type
  }
  #질문
  # sentence = input("하고싶은 말을 입력해주세요 : ")
  # print(predict(sentence)) 
  # print(voicePredict('happy.wav')) 
  return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def signin(request):
  if request.method == 'POST':
      user_id = request.POST.get('id','')
      user_pw = request.POST.get('pw','')
      user = auth.authenticate(request, username=user_id, password=user_pw)
      if user is not None:
          auth.login(request, user)
          global member_type
          member_type = checkType(request)
          return redirect('index')
      else:
          return render(request, 'signin.html', {'error': '아이디나 패스워드를 확인하세요'})

  return render(request, 'signin.html')


def signup(request):
  if request.method == 'POST':
    user = User.objects.create_user(request.POST['id'], password=request.POST['pw'], first_name=request.POST['name'])
    auth.login(request, user)
    if(request.POST.get('who') == "doctor"):
      myusers=Doctor()
      myusers.id = request.POST.get('id','')
      myusers.pw = request.POST.get('pw','')
      myusers.name = request.POST.get('name','')
      myusers.institution = request.POST.get('inst_city2','') + " " + request.POST.get('inst_center2','')
      myusers.save()
      return redirect('index')
    else:
      myusers=Patient()
      myusers.id = request.POST.get('id','')
      myusers.pw = request.POST.get('pw','')
      myusers.name = request.POST.get('name','')
      myusers.phone = request.POST.get('phone','')
      myusers.birth = request.POST.get('birth','')
      myusers.gender = request.POST.get('gender','')
      myusers.occupation = request.POST.get('occupation','')
      myusers.institution = request.POST.get('inst_city1','') + " " + request.POST.get('inst_center1','')
      myusers.save()
      return redirect('index')
  
  else:
    insts = Institution.objects
    dict = {}
    for a in insts.all():      
      if a.city in dict.keys():
        dict[a.city].append(a.center)
      else:
        dict[a.city] = [a.center]
    # dict = json.dumps(dict, ensure_ascii=False)
    dict = str(dict)
  return render(request, 'signup.html', {'dict':dict})


# def findpassword(request):
#     myuser = Member.objects
#     input_id = request.POST.get('id', '')
#     input_name = request.POST.get('name', '')
#     input_tel = request.POST.get('phone', '')
#     if request.method == 'POST':
#         for a in myuser.all():
#             if(a.ID == input_id):
#                 if(a.NAME == input_name):
#                     if(a.TEL == input_tel):
#                         return render(request, 'findpassword.html', {'msg': a.PW})
            
        
#     return render(request, 'findpassword.html')


# def findid(request):
#     myuser = Member.objects
#     input_name = request.POST.get('name', '')
#     input_tel = request.POST.get('phone', '')
#     if request.method == 'POST':
#         for a in myuser.all():
#             if(a.NAME == input_name):
#                 if(a.TEL == input_tel):
#                     return render(request, 'findid.html', {'msg': a.ID})
        
    
#     return render(request, 'findid.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')
    return render(request, 'index.html')


def chat(request):

    return render(request, 'chat.html')




#################################################
#### for doctor management page
#################################################

def dashboard(request):
    return render(request, 'dr-dashboard.html')


def groupCalendar(request):
    return render(request, 'dr-groupCalendar.html')


def individualCalendar(request):
    return render(request, 'dr-individualCalendar.html')


def monitoringByPatient(request):
    return render(request, 'dr-monitoringByPatient.html')


def monitoringByTime(request):
    return render(request, 'dr-monitoringByTime.html')