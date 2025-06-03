from django.db import models

# Create your models here.
class Topic(models.Model):
    '''사용자가 배우는 주제'''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''모델의 문자열 표현을 반환한다.'''
        return self.text

class Entry(models.Model):
    '''학습한 내용을 저장하는 모델'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        '''모델의 문자열 표현을 반환한다.'''
        return f"{self.text[:50]}..."