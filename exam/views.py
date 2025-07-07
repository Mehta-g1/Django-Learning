from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
class Questions:
    def __init__(self,que,a,b,c,d):
        self.que = que
        self.a = a
        self.b = b
        self.c = c
        self.d = d

# def about(requ)

def contact(request) :
    quote = "Water the root, enjoy the fruit !"
    return render(request,'contact.html',{'quote':quote})

def Home(request) :
    return render(request,'home.html')

def About(request) :
    return render(request,'about.html')

def questions(request) :
    questions = [
        Questions("1. Which of the following is NOT a core programming concept?","Variables","Conditionals","Algorithms","Functions"),
        Questions("2. What does the acronym 'OOP' stand for in programming?","Object-Oriented Programming","Operational Output Programming","Organized Online Procedures","Output Object Programming "),
        Questions("3. Which language is commonly used for both front-end and back-end web development?","Java","C#","JavaScript","Python "),
        Questions("4. Which type of language is used to automate tasks and manage dynamic web content?","Compiled Language","Machine Language","Scripting Language","Low-level Language "),
        Questions("5. What is the primary function of a compiler in programming?","To execute code directly","To translate source code into machine code","To debug code","To store data ")
    ]
     
    data = {'questions':questions}

    return render(request,'testpaper.html',data)