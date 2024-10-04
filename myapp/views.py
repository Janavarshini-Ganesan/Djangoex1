from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(response):
    return HttpResponse("<h1><b> This is the home page </b></h1> <br> <p><center>Web Application Development using Django Framework</center></p>")
    

def about(response):
    return HttpResponse("<h1><b> This is the about Page </b></h1> <br> <center><p>I am Janavarshini G, UG Student in the Deartment of Information Technology of Kamaraj College of Engineering and Technology.</p> <p>I am passionate about coding. My areas of interest are Machine Learning, Deep Learning, IoT, Security and Networks</p></center>")    
