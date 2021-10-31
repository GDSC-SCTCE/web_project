from django.shortcuts import redirect, render
from .models import Form

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('number')
        role = request.POST.get('role')
        recommend = request.POST.get('radio-group')
        fav_feature = request.POST.get('mostLike')
        comments = request.POST.get('comment')
        
        form = Form(name=name,email=email,age=age,role=role,recommend=recommend,fav_feature=fav_feature,comments=comments)
        form.save()
        return redirect('/')
    else:
        return render(request,'index.html')