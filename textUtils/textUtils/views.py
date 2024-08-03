# I have created this website -- Aanchal 
from django.http import HttpResponse  
from django.shortcuts import render  
from django.template import loader

def index(request): 
    # return HttpResponse('''<h1>hello</h1><a href="https://www.youtube.com/results?search_query=django+by+code+with+harry">Django CodeWithHarry</a>''') 
     return render(request,'index.html')

def analyze(request):  
    # return HttpResponse("Remove punc <a href='/'>back</a>")  
    # Get the Text  
     djtext = request.POST.get('text','default')  
    #  Check checkbox values 

     removepunc = request.POST.get('removepunc','off')  
     fullcaps = request.POST.get('fullcaps','off')   
     newlineremover = request.POST.get('newlineremover','off')  
     extraspaceremover = request.POST.get('extraspaceremover','off') 
     charactercounter = request.POST.get('charactercounter','off')
    #  check with checkbox is on 

     if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        analyzed = "" 
        for char in djtext: 
           if  char not in  punctuations: 
               analyzed = analyzed+char

        params = { 
          'purpose':'Remove Punctuations','analyze_text':analyzed
         } 
        djtext = analyzed
     
     if(fullcaps=='on'): 
         analyzed = "" 
         for char in djtext: 
             analyzed = analyzed+char.upper() 
         params = { 
             'purpose':'Change to Uppercase','analyze_text':analyzed
         }            
         djtext = analyzed
     
     if(newlineremover=='on'): 
         analyzed = "" 
         for char in djtext:  
             if char != '\n' and char!= '\r':
               analyzed = analyzed+char 
         params = { 
             'purpose':'Remove the New Lines','analyze_text':analyzed
         }  

         djtext = analyzed         

     if(extraspaceremover == 'on'): 
         analyzed = "" 
         for index,char in enumerate(djtext): 
             if djtext[index] == " " and djtext[index+1] == " ": 
                 pass 
             else: 
                 analyzed = analyzed + char 
         
         params = { 
             'purpose':"Remove Extra Spaces", 
             'analyze_text': analyzed 
         } 

         djtext = analyzed

     
     if(charactercounter == 'on'): 
         counter = 0  
         for char in djtext:  
             counter = counter+1    

         params = { 
             'purpose':"Count the character", 'analyze_text':counter
         }    

     if removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charactercounter != "on": 
         return HttpResponse("Error! Please select any one operand and try again.")

     return render(request,'analyze.html',params)

     
    


