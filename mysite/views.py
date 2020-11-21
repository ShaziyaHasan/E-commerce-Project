from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


def home(request):
    return HttpResponse("<h1>Welcome</h1>")


def signup(request):
    dic = dict()
    if request.POST.get('first_name') is not None:
        fname=request.POST.get('first_name')
        dic={'uname':fname}
    return render(request, 'signup.html', dic)
    #print(request.GET.get('fname'))
   # print("==>", request.GET.get('fname'))
    #return HttpResponse("Signup")


def dash(request):
    fname = request.POST.get('first_name')
    emailid = request.POST.get('email')
    return render(request, 'dashboard.html', {'uname': fname, 'email': emailid})


class Hello(View):
    def get(self, request):
        return render(request,'signup.html')

    def post(self,request):
        fname = request.POST.get('first_name')
        email = request.POST.get('email')
        return render(request,'dashboard.html',{'uname':fname,'email':email})




