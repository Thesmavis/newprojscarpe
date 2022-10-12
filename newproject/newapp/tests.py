from django.test import TestCase


from newapp.models import *

class urlTestCase(TestCase):
    def enterurl_de(self):
        url_list_de.objects.create(url="www.google.com")
        url_list_de.objects.create(url="www.amazon.com")

    def product(self):
      
        url_list_de.objects.create(name="sunglass",price="1500")

        # self.assertEqual()
    