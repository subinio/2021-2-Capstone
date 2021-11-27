import requests
from decouple import config


SECRET_KEY = config('SECRET_KEY')  #.env 파일에 secret_key

class KakaoTTS:

	def __init__(self, text, API_KEY=SECRET_KEY):
		self.resp = requests.post(
			url="https://kakaoi-newtone-openapi.kakao.com/v1/synthesize",
			headers={
				"Content-Type": "application/xml",
				"Authorization": f"KakaoAK {API_KEY}"
			},
			data=f"<speak><voice name='WOMAN_READ_CALM'>{text}</voice></speak>".encode('utf-8')
		)

	def save(self, filename="./myApp/static/bot_question.wav"):
		with open(filename, "wb") as file:
			file.write(self.resp.content)

