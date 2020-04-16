from django.db import models


# python manage.py makemigrations blog
# python manage.py migrate blog



# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=64)
    content=models.CharField(max_length=64)
    name = models.CharField(max_length=64) # 字符串类型，最长不超过6python manage.py makemigrations blog4个字符
    birthday = models.CharField(max_length=64) # 日期类型
    email = models.CharField(max_length=64)  # required=False表示可以为空，默认是True，不能为空
    phone = models.CharField(max_length=64) # 数值类型


    def __str__(self):
        return "标题：{}，字数：{}，概要：{}".format(self.title,len(self.content),self.content[:18])


from django import forms
from django.forms import ModelForm

class Article_Model_Form(forms.ModelForm):   #继承ModelForm类
    class Meta:
        model = Blog    #导入数据表
        fields = ['name', 'birthday','email', 'phone']    #要使用的字段
        exclude = ()  #排除字段