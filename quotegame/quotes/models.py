from django.db import models

# Create your models here.
class Quote(models.Model):
    quote_text = models.CharField(max_length=20000)
    person = models.CharField(max_length=100)
    timestamp = models.IntegerField(default=0)
    def __str__(self):
        return self.quote_text

class Answer(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.answer_text