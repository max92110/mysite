from django.db import models

# Create your models here.
#Ввод строки для изменения
class Input(models.Model):
	Input_text = models.CharField(max_length=200)
	def __str__(self):
		return self.Input_text

#Измененная строка
class Output(models.Model):
	Output_index = models.ForeignKey(Input)
	Output_text = models.CharField(max_length=200)
	def printOutput(self):
		return self.Output_text



# Пока не нужный класс
class Type(models.Model):
	Type_index = models.ForeignKey(Input)
	Type_text = models.CharField(default='ascii', max_length=20)
	def __str__(self):
		return self.Type_text