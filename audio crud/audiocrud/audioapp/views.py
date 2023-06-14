from django.shortcuts import render,redirect
from . models import *
import os

# Create your views here.
def index(request):
    songs = Song.objects.all()
    return render(request, 'index.html',{'songs':songs})

def delete(request,pk):
    Song.objects.filter(id = pk).delete()
    return redirect('/')

def update(request,uid):
    newdata = Song.objects.get(id = uid)
    return render(request,'update.html',{'newdata':newdata})

def updatedata(request):
    if request.method == "POST":
        id = request.POST['uid']
        # id = Song.objects.get(id=uid)
        title = request.POST['title']
        singers = request.POST['singers']
        image = request.FILES.get('image')
        audio_file = request.FILES.get('audio')
        duration = request.POST['duration']
        updsong = Song.objects.get(id=id)
        updsong.title = title
        updsong.singers = singers
        updsong.duration = duration

        if image:
            updsong.image = image
        if audio_file:
            updsong.audio_file = audio_file

        updsong.save()

        return redirect('/')
    

# def upd(request):
#     if request.method == "POST":
#         hide = request.POST['hide']
#         name = request.POST['name']
#         subject_id = request.POST['subject']
#         subject = Subject.objects.get(id=subject_id)
#         address = request.POST['address']
#         mobile = request.POST['mobile']
#         image = request.FILES.get('image')
#         student = Student.objects.get(id=hide)
#         student.name = name
#         student.address = address
#         student.mobile = mobile
#         student.subject = subject

#         if image:
#             student.image = image

#         student.save()

#         return redirect('/table/')

# def updatedata(request):
#     if request.method == 'POST':
#         uid = request.POST['uid']
#         title = request.POST['title']
#         singers = request.POST['singers']
#         image = request.data['image']
#         audio_file = request.data['audio']
#         duration = request.POST['duration']
        
#         Song.objects.filter(id = uid).update(title = title, singers = singers,image = image, audio_file = audio_file, duration = duration)
#         return redirect('/')

# def update(request,uid):
#     newdata = Song.objects.get(id = uid)
#     if request.method == 'POST':
#         if len(request.FILES) !=0:
#             if len(newdata.image) >0:
#                 os.remove(newdata.image.path)
#             newdata.image = request.FILES['image']
            #   if len(newdata.audio_file) >0:
            #     os.remove(newdata.image.path)
            # newdata.audio_file = request.FILES['audio']
#         newdata.title = request.POST['title']
#         newdata.singers = request.POST['singers']
#         newdata.duration = request.POST['duration']
#         newdata.save()

#     return render(request, 'update.html',{'newdata':newdata})