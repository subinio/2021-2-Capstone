from django.db import models

# Create your models here.

class Doctor(models.Model):
    dr_num = models.AutoField(primary_key=True)
    id = models.CharField(max_length=20)
    pw = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    institution = models.CharField(max_length=50)

    objects = models.Manager()
    def __str__(self):
        return self.id


class Patient(models.Model):
    pt_num = models.AutoField(primary_key=True)
    id = models.CharField(max_length=20)
    pw = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    birth = models.DateField()
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=20)
    institution = models.CharField(max_length=50)

    objects = models.Manager()
    def __str__(self):
        return self.id


class ChattingRoom(models.Model):
    room_num = models.AutoField(primary_key=True)
    pt_num = models.ForeignKey(Patient, on_delete=models.CASCADE)
    created_at = models.DateTimeField()

    objects = models.Manager()
    def __str__(self):
        return self.room_num


class ChattingMsg(models.Model):
    msg_num = models.AutoField(primary_key=True)
    room_num = models.ForeignKey(ChattingRoom, on_delete=models.CASCADE)
    writer_num = models.IntegerField()
    content = models.TextField()
    category = models.CharField(max_length=20)
    created_at = models.DateTimeField()

    objects = models.Manager()
    def __str__(self):
        return self.content


class EmotionResult(models.Model):
    res_num = models.AutoField(primary_key=True)
    msg_num = models.ForeignKey(ChattingMsg, on_delete=models.CASCADE)
    voice_emo = models.CharField(max_length=20)
    text_emo = models.CharField(max_length=20)

    objects = models.Manager()
    def __str__(self):
        return self.res_num


class QuestionSet(models.Model):
    q_num = models.AutoField(primary_key=True)
    voice_emo = models.CharField(max_length=20)
    text_emo = models.CharField(max_length=20)
    question = models.TextField()
    depth = models.IntegerField()
    parent_id = models.IntegerField()

    objects = models.Manager()
    def __str__(self):
        return self.question


class Institution(models.Model):
    inst_num = models.AutoField(primary_key=True)
    city = models.CharField(max_length=20)
    center = models.CharField(max_length=50)
    
    objects = models.Manager()
    def __str__(self):
        return self.center

