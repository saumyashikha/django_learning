from django.shortcuts import render
from enroll.models import Student
# Create your views here.
def stuinfo(request):
    stu = Student.objects.all()
    return render(request, 'stu/stu.html', {'stu':stu})