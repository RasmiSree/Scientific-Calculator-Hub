from django.shortcuts import render

def home(request):
	return render(request,'scientificcalculator.html')


# Create your views here.
def contact(request):
	return render(request,'scientificcalculator.html')