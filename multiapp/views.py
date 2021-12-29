from django.shortcuts import render
from multiapp.models import multi_insert_data
# Create your views here.
def Detail(request):
	for i in range(3):
		did=int(input('ENTER THE ID :'))
		name=input('ENTER YOUR NAME :')
		age=int(input('ENTER YOUR AGE :'))
		gender=input('ENTER YOUR GENDER :')
		course=input('ENTER THE COURSE :')

		details=multi_insert_data.objects.create(did=did,name=name,age=age,gender=gender,course=course)
		details.save()
	return render(request,'multiapp/display.html')
