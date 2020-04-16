from django import  forms
class Person_Info(forms.Form):
    name = forms.CharField(max_length=64,)  # 字符串类型，最长不超过4个字符
    birthday = forms.CharField(max_length=64)         #日期类型
    email = forms.CharField(max_length=64)  # required=False表示可以为空，默认是True，不能为空
    phone = forms.CharField(max_length=64)       #数值类型
