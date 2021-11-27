import requests
import json
from decouple import config

# Text To Speech

SECRET_KEY = config('SECRET_KEY')  #.env 파일에 secret_key

headers = {
    #Transfer-Encoding: chunked # 보내는 양을 모를 때 헤더에 포함한다.
    'Host': 'kakaoi-newtone-openapi.kakao.com',
    'Content-Type': 'application/octet-stream',
    'X-DSS-Service': 'DICTATION',
    'Authorization': f'KakaoAK {SECRET_KEY}',
}

def kakaoSTT(AUDIO_PATH):
  data = open(AUDIO_PATH, "rb").read() # wav 파일을 바이너리 형태로 변수에 저장한다.
  response = requests.post('https://kakaoi-newtone-openapi.kakao.com/v1/recognize', headers=headers, data=data)
  # 요청 URL과 headers, data를 post방식으로 보내준다.

  print(response.text)

  result_json_string = response.text[response.text.index('{"type":"finalResult"'):response.text.rindex('}')+1]
  result = json.loads(result_json_string)
  print(result)
  print(result['value'])

  return result['value']


