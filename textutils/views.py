# i have created this file ---akash
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
   return render(request,'index.html')
def analyse(request):
    global params,purpose,anaylise_text,c, analysed
    c=0
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    full_caps = request.POST.get('fullcaps', 'off')
    removernewline = request.POST.get('removernewline', 'off')
    extraspace=request.POST.get('extraspaceremover','off')
    charcont=request.POST.get('charcont','off')
    punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_'''
    if (removepunc=='on'):
        analysed=""
        for char in djtext:
            if char not in punctuations:
                analysed=analysed+char
        params = {'purpose': 'extra spac removed', 'anaylise_text': analysed, 'count': c}
        djtext = analysed
    if(full_caps=='on'):
        analysed=""
        for char in djtext:
            analysed=analysed+char.upper()
        params = {'purpose': 'extra spac removed', 'anaylise_text': analysed, 'count': c}
        djtext=analysed
    if ( removernewline == 'on'):
        analysed = ""
        for char in djtext:
            if char!='\n'and char!='\r':
                analysed = analysed + char
        params = {'purpose': 'extra spac removed', 'anaylise_text': analysed, 'count': c}
        djtext=analysed
    if(  extraspace=='on' ):
        analysed= ""
        for index, char in enumerate(djtext):
            if (djtext[index]==" " and djtext[index+1]==" "):
                pass
            else:
                analysed=analysed+char
        params = {'purpose': 'extra spac removed', 'anaylise_text': analysed,'count': c}
        djtext=analysed
    if charcont == 'on':
        c = 0
        for char in djtext:
            c = c + 1
        params = {'purpose': 'extra spac removed', 'anaylise_text': analysed, 'count': c}
    if extraspace=='on'or removernewline=='on'or removepunc == 'on'or charcont=='on'or full_caps == 'on':
        return render(request, 'analyse.html', params)
    if extraspace != 'on' and removernewline != 'on' and removepunc != 'on'and charcont !='on'and full_caps != 'on':
          return HttpResponse("please select any switch")