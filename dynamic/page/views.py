from django.shortcuts import render
from .models import description



def page(request):

    des1=description()
    des1.id=1
    des1.name="Ab"
    des1.image='c++.jpg'

    des2=description()
    des2.id=2
    des2.name="wp"
    des2.image='c.png'
    des3=description()

    des3.id=3
    des3.name="pv"
    des3.image='css.png'
    dest=[des1,des2,des3]

    return render(request,'home.html',{'dest':dest})
  