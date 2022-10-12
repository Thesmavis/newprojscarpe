# import os
# from celery import Celery
# import time
# from.models import *
# from datetime import date, timedelta
# import datetime
# from django.shortcuts import render

# broker_url  = os.environ.get("CELERY_BROKER_URL",
#                              "redis://localhost:6378/0"),
# res_backend = os.environ.get("CELERY_RESULT_BACKEND",
#                              "db+postgresql://dbc:dbc@localhost:5434/celery")

# celery_app = Celery(name           = 'tasks',
#                     broker         = broker_url,
#                     result_backend = res_backend)

# @celery_app.task
# def get_g(self,request):
        
#         date_f=Product.objects.all()
#         for j in date_f:
            
#             date_t=j.date
#             date_te=datetime.datetime.strptime(str(date_t),"%Y-%m-%d")
#             days_after = (date_te+timedelta(days=7))
#             print(days_after,'kkkkkkkkkkkkk')
#             if days_after==j.end_date:
#                 de=Product.objects.filter(id=j.id)
#                 de.delete()
                
            
#         return render(request, 'Formen.html')
