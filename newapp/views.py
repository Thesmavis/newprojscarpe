from ast import Import
from datetime import date, timedelta
import datetime
import json
import time
from wsgiref import headers
from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .form import *
from django.contrib import messages 
from .serializers import CategorySerializer, ProductSerializer, CustomerSerializer
from .models import *
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from bs4 import BeautifulSoup
import time
# from celery.result import AsyncResult
# from .tasks import get_g



class Homepage_view(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'

    def get(self, request):
        queryset = Product.objects.all()
        return Response({'products': queryset})

def home_page(request):
    return render(request, 'home.html')



def url_view(request):
    plist=Product.objects.all()
    if request.method == 'POST' :
        form = urlform(request.POST)
        data={}
        if form.is_valid():  
            name = request.POST['url']
            date_n=datetime.datetime.now()
            # todate=datetime.datetime.strptime(date_t,"%Y/%m/%d")
            days_after = (date_n+timedelta(days=7)) 
            data= url_list_de(url=name)
            data.save()
            link=name
            f = requests.get(link).text
            soup=BeautifulSoup(f)
            raw=soup.body('script')[0].text
            g=[]
            x=json.loads(raw)

            print(x,'ppppppppppppppppppp')
            f=x[0]
            
            
            try:
                product_name=(f["name"])   
            except:
                product_name=None
            try:
               fe=x[1]
               price=(fe['offers']['price'])
            except:
                price=None
            if price==None:
                try:
                    price=(f['offers']['price'])
                except:  
                    price=None
            try:
               title=(f['title'])
            except:
                title=None
            try:
               url=(f["image"])
            except:
                url= None
            try:
              desc=(f["description"])
            except:
                desc=None
            try:
              m_num=(f['mobile_number'])
            except:
                m_num=None
            try:
              size=f(['size'])
            except:
              size=None
            try:
              category=f(['category'])
            except:
              size=None

            l={"product_name":product_name,
            "price":price,
            "title":title,
            "url":url,
            "description":desc,
            "mobile_number":m_num,
            "size":size,
            } 
          
            g.append(l)
            print(g,'oooooooooooooo')
            for k in g:
                category_save=Category(title=k['product_name'])
                category_save.save()
                prod_save=Product(name=k['product_name'],end_date=days_after,category=category_save,price=k['price'],description=k['description'],mobile_number=k['mobile_number'],imageUrl=k['url'])
                prod_save.save()
          
            return render(request, 'products.html', context = {
         'plist':plist
    })
            
           
        else:
            messages.error(request, "Error")
            form = urlform()

        print('llllllllllllllll')
    return render(request, 'Formen.html')


class productlist(APIView):

    def post(self,request):
        data=[]
        k=url_list_de.objects.all()
        
        for link in k:
            fa = url_list_de.objects.get(id=link.id)
            link=(fa.url)
            print(link)
            f = requests.get(link).text
            hun=BeautifulSoup(f,'html.parser')


        return Response(data)
class deleteafterweek(APIView):
    def get(self,request):
        
        date_f=Product.objects.all()
        for j in date_f:
            
            date_t=j.date
            date_te=datetime.datetime.strptime(str(date_t),"%Y-%m-%d")
            days_after = (date_te+timedelta(days=7))
            print(days_after,'kkkkkkkkkkkkk')
            if days_after==j.end_date:
                de=Product.objects.filter(id=j.id)
                de.delete()
                
            
        return render(request, 'Formen.html')
    
          

def urlauto_call(request):
    plist=Product.objects.all()
    geturllist=url_list_de.objects.all()
    for h in geturllist:
        link=h.url
        print(link)
        f = requests.get(link).text
        soup=BeautifulSoup(f)
        date_n=datetime.datetime.now()
            # todate=datetime.datetime.strptime(date_t,"%Y/%m/%d")
        days_after = (date_n+timedelta(days=7)) 
        raw=soup.body('script')[0].text
        g=[]
        x=json.loads(raw)

        print(x,'ppppppppppppppppppp')
        f=x[0]
        
        
        try:
            product_name=(f["name"])   
        except:
            product_name=None
        try:
            fe=x[1]
            price=(fe['offers']['price'])
        except:
            price=None
        if price==None:
            try:
                price=(f['offers']['price'])
            except:  
                price=None
        try:
            title=(f['title'])
        except:
            title=None
        try:
             url=(f["image"])
        except:
            url= None
        try:
            desc=(f["description"])
        except:
            desc=None
        try:
            m_num=(f['mobile_number'])
        except:
            m_num=None
        try:
           size=f(['size'])
        except:
           size=None
        try:
           category=f(['category'])
        except:
          size=None

        l={"product_name":product_name,
        "price":price,
        "title":title,
        "url":url,
        "description":desc,
        "mobile_number":m_num,
        "size":size,
        } 
    
        g.append(l)
        print(g,'oooooooooooooo')
        for k in g:
                category_save=Category(title=k['product_name'])
                category_save.save()
                prod_save=Product(name=k['product_name'],end_date=days_after,category=category_save,price=k['price'],description=k['description'],mobile_number=k['mobile_number'],imageUrl=k['url'])
                prod_save.save()
        
    return render(request, 'products.html', context = {
        'plist':plist
})
    
    

def issue_tasks():
    tasks = []
    for i in range(5):
        tasks.append(get_g.delay(i, i))
    return tasks

def get_results(task_id):
    task_result = AsyncResult(task_id)
    result = {
        'task_id': task_id,
        'task_status': task_result.status,
        'task_result': task_result.result
    }
    return result

def run_task():
    tasks = issue_tasks()
    while 1:
        done = True
        for task in tasks:
            res = get_results(task.task_id)
            if res['task_status'] == 'SUCCESS' or \
                res['task_status'] == 'FAILURE':
                print(res['task_result'])
            else:
                done = False
                print(res['task_status'])
        print('sleeping for 1 secound ...')
        time.sleep(1)
        if done:
            break

if __name__ == '__main__':
    run_task()
