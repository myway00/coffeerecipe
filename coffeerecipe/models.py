from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
# Create your models here.

class Content(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    body = models.TextField(default='')

    TASTE_CHOICES = [
        ('인생의 쓴맛', '인생의 쓴맛'),
        ('어우달아!', '어우달아!'),
        ('밍밍한 한강물맛', '밍밍한 한강물맛'),
        ('마트..다녀오셨어요?', '마트..다녀오셨어요?'),
        ('매운맛', '매운맛'),
    ]
    taste = models.CharField(max_length=30, choices=TASTE_CHOICES, default='인생의 쓴맛')
    
    SIZE_CHOICES = [
        ('아리아나그란데', '아리아나그란데'),
        ('그란데말입니다', '그란데말입니다'),
        ('그란데밖에없는데', '그란데밖에없는데'),
        ('손에 담아마실게요', '손에 담아마실게요')
    ]
    size = models.CharField(max_length=30, choices=SIZE_CHOICES, default='아리아나그란데')