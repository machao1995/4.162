from django.shortcuts import render
# import blog.models
import markdown
# Create your views here.
from . import models


def index(request):
    Blog = models.Blog()
    blog=models.Blog.objects.all().first()
    blog_content=markdown.markdown(blog.content)
    return render(request,"blog.html",{'blog':blog,"blog_content":blog_content})
def persondetail(request):
    Blog = models.Blog()
    blog=models.Blog.objects.all().first()
    # blog_content=markdown.markdown(blog.content)
    return render(request,"persondetail.html",{'blog':blog,"blog_content":

        blog.content})


from django.shortcuts import render,HttpResponse
from .forms import Person_Info  #导入form表单




# def person(request):
#
#     person_obj = Person_Info()  # 创建了这个对象
#     if request.method == 'POST':
#         form_obj = Person_Info(request.POST)
#         if form_obj.is_valid():
#             print("form is valid ^_^** ", form_obj.cleaned_data)  # 返回表单数据，是字典形式
#
#
#
#             name = form_obj.cleaned_data.get('name')  # 取出填写的name的值
#             Blog =models.Blog()
#
#             Blog.name=form_obj.cleaned_data.get('name')
#             Blog.birthday = form_obj.cleaned_data.get('birthday')
#             Blog.email = form_obj.cleaned_data.get('email')
#             Blog.phone = form_obj.cleaned_data.get('phone')
#             # Blog.name = name
#
#
#             Blog.is_active = 0
#             Blog.save()
#
#
#             # if name == 'lily':
#             #     return HttpResponse('*lily*')
#         else:
#             errors = form_obj.errors
#             print("form is invalid T_T... ", errors)  # .errors 获取错误信息
#
#             return render(request, 'errorinfo.html', {'obj': form_obj, 'errors': form_obj.errors})
#
#     return render(request,'info.html',{'obj':person_obj})  #然后把对象传给html

from .models import Article_Model_Form
def article_modelform(request):
    # form = Article_Model_Form()  #创建一个表单来添加一条数据
    if request.method == 'POST':
        form = Article_Model_Form(request.POST)
        if form.is_valid():   # 判断表单是否合法
            print("form is ok", form.cleaned_data)
            form.save()   # 将合法的数据保存到数据表中
        else:
            error_msg = form.errors
            # return render(request, 'blog.html', {"article_form": form ,"errors": error_msg})
    # return render(request, 'blog.html', {"article_form": form})




def person(request):

    person_obj = Person_Info()  # 创建了这个对象
    data = models.Blog.objects.all()
    if request.method == 'POST':
        form_obj = Person_Info(request.POST)


        if form_obj.is_valid():
            print("form is valid ^_^** ", form_obj.cleaned_data)  # 返回表单数据，是字典形式



            name = form_obj.cleaned_data.get('name')  # 取出填写的name的值
            Blog =models.Blog()

            Blog.name=form_obj.cleaned_data.get('name')
            Blog.birthday = form_obj.cleaned_data.get('birthday')
            Blog.email = form_obj.cleaned_data.get('email')
            Blog.phone = form_obj.cleaned_data.get('phone')
            # Blog.name = name


            Blog.is_active = 0
            Blog.save()


            # if name == 'lily':
            #     return HttpResponse('*lily*')
        else:
            errors = form_obj.errors
            print("form is invalid T_T... ", errors)  # .errors 获取错误信息

            return render(request, 'errorinfo.html', {'obj': form_obj,'errors': form_obj.errors})

    return render(request,'info.html',{'obj':person_obj, 'data':data})  #然后把对象传给html

from .models import Article_Model_Form



