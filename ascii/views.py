from django.http import HttpResponse
from django.template import RequestContext, loader
from ascii.models import Input

from django.shortcuts import render

#главная страница приложения, выводит список все Input
def index(request):
	latest_input_list = Input.objects.order_by() [:5]
	#template = loader.get_template('ascii/index.html')
	context = {'latest_input_list': latest_input_list}
	#output_index = ', '.join([p.Input_text for p in latest_input_list])
	return render(request, 'ascii/index.html', context)

def detail(request, input_id):
	return HttpResponse("Input you string then:")

def results(request, input_id):
	response = "You're result: %s."
	return HttpResponse(response % input_id)

