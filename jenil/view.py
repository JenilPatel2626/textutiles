from django.shortcuts import render


def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')

def home(request):
    return render(request, 'home.html')

def removepun(request):
    djtext=request.GET.get('text','default')
    check=request.GET.get('checkbox','none')
    pun='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    remove=""
    if check=="on": 
        for char in djtext:
            if char not in pun:
                remove=remove+char
        
    else:
        remove=djtext
    
    print(remove)
    param={'analyase':remove,'count1':len(remove.strip())}
    return render(request, 'removepun.html',param)