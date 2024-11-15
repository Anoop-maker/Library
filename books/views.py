from django.shortcuts import render
from books.models import Book
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'home.html')

@login_required
def add(request):
    if(request.method=="POST"):
        t=request.POST['t']
        a=request.POST['a']
        p=request.POST['p']
        l = request.POST['l']
        pa = request.POST['pa']

        c = request.FILES.get('c')
        f = request.FILES.get('f')
        b=Book.objects.create(title=t,author=a,price=p,pages=pa,language=l,cover=c,pdf=f)
        b.save()
        return view(request)
    return render(request,'add.html')

@login_required
def view(request):
    k=Book.objects.all()
    return render(request,'view.html',{'book':k})

@login_required
def details(request,p):
    k=Book.objects.get(id=p)
    return render(request,'details.html',{'book':k})

@login_required
def edit(request,p):
    k = Book.objects.get(id=p)
    if(request.method=="POST"):
        k.title=request.POST['t']
        k.author=request.POST['a']
        k.price=request.POST['p']
        k.pages=request.POST['pa']
        k.language=request.POST['l']
        if(request.FILES.get('i')==None):
            k.save()
        else:
            k.cover=request.FILES.get('i')

        if(request.FILES.get('f') == None):
            k.save()
        else:
            k.pdf = request.FILES.get('f')
        k.save()
        return view(request)

    return render(request,'edit.html',{'book':k})

@login_required()
def delete(request,p):
    k=Book.objects.get(id=p)
    k.delete()
    return view(request)


from django.db.models import Q

def searchbooks(request):
    k=None                         #initialize k as None(no value)
    if(request.method=="POST"):
        query=request.POST['q']    #get input key from form
        if query:
            k=Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))    #it checks the key in title and author field.
            #filter funtion returns only the matching records., icontains-->anywhere inside the field,   i--->caseinsensive{uppercase and lower case select}
    return render(request,'search.html',{'search':k})