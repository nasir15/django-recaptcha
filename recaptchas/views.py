from django.shortcuts import render , HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import json


def index(request):

    if request.method=='POST':
        email=request.POST['email']  
        password=request.POST['email']  
        client_key=request.POST['g-recaptcha-response']  
        secret_key='6LeKQc0iAAAAAMmJyUcYRNvLUkHCvVEmMBI428SX'
        # print(email,password,client_key,secret_key)

        capthchaData = {
        'secret':secret_key,
        'response' : client_key
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=capthchaData)
        response = json.loads(r.text)
        print('response is ',response)
        verify = response['success']
        print("Your success is: ", verify)

        if verify:
            return HttpResponse('<script> alert("success");</script>')
        else:
            return HttpResponse('<script> alert("not success");</script>')
        
    return render(request,'recaptchas/index.html')

@api_view(['POST'])
def recaptcha(request):
    r = requests.post(
      'https://www.google.com/recaptcha/api/siteverify',
      data={
        'secret': 'YOUR SECRET KEY',
        'response': request.data['captcha_value'],
      }
    )

    return Response({'captcha': r.json()})

