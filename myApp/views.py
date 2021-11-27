from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Doctor, Institution, Patient, QuestionSet
import json
from django.http import HttpResponse, JsonResponse
import random, datetime

from .textEmotionClassifier import *
from .voiceEmotionClassifier import *
from .recording import *
from .speechToText import *
from .textToSpeech import *

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
  # print(voicePredict('temp.wav')) 
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


q_depth = 1
q_parent_id = 0
rand = 0

def chat(request):
    global q_depth, q_parent_id, rand

    if request.GET.get('what') == 'record':
      start()
      context ={'num':1}
      return JsonResponse(context)
    

    elif request.GET.get('what') == 'stop':
      stop()
      sentence = kakaoSTT("./myApp/static/patient_answer.wav")
      
      textEmo = predict(sentence) 
      voiceEmo = voicePredict('./myApp/static/patient_answer.wav')
      print(textEmo)
      print(voiceEmo)

      if(q_depth==1 or q_depth==4 or q_depth==7):
        voiceEmo = ""
        textEmo = ""
        q_parent_id = 0
        rand = random.randrange(0,3)
      if(q_depth==10):
        q_depth=0
        return(JsonResponse({'sentence':sentence, 'question':None}))
      query = QuestionSet.objects.filter(voice_emo=voiceEmo, text_emo=textEmo, depth=q_depth, parent_id=q_parent_id)
      

      print(query[rand].q_num)
      print(query[rand].question)
      
      question = query[rand].question
      
      q_depth += 1
      q_parent_id = query[rand].q_num
      rand = 0

      tts = KakaoTTS(question)
      tts.save("./myApp/static/bot_question.wav")

      context ={'sentence':sentence, 'question':question}
      return JsonResponse(context)


    # 첫 질문
    query = QuestionSet.objects.filter(voice_emo="", text_emo="", depth=1, parent_id=0)
    question = query[random.randrange(0,3)].question
    question = "안녕하세요! " + request.user.get_short_name() + "님, " + question

    tts = KakaoTTS(question)
    tts.save("./myApp/static/bot_question.wav")

    now = datetime.datetime.now()
    nowTime = now.strftime('%H:%M')

    q_depth += 1
    q_parent_id = query[rand].q_num
    rand = 0
    return render(request, 'chat.html', {'question':question, 'nowTime':nowTime})


# def chat(request):

#     return render(request, 'chat.html')


def chatTest(request):

    return render(request, 'chat-test.html')




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