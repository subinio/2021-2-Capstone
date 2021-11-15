from django.contrib import admin

# Register your models here.

from .models import Doctor, Patient, ChattingRoom, ChattingMsg, EmotionResult, QuestionSet, Institution


admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(ChattingRoom)
admin.site.register(ChattingMsg)
admin.site.register(EmotionResult)
admin.site.register(QuestionSet)
admin.site.register(Institution)
