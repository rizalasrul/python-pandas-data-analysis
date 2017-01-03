from django.shortcuts 	import render
from django.http 		import HttpResponse
from django.template 	import loader
import datetime
import pandas as pd

# Create your views here.

def index(request):
	df 		= pd.read_table("simpleview/data.csv", sep=",");
	datas	= pd.DataFrame(df)
	head 	= pd.DataFrame(df, columns=[datas.columns[0]])
	body	= []
	for i in range(0, df.shape[1]-1):
		body.append(pd.DataFrame(df, columns=[datas.columns[i+1]]))
	df 		= df.to_html(classes="table striped hovered cell-hovered border bordered")
	context = {	'datas'		: datas,
				'heads'		: head,
				'bodies'	: body,
				'df'		: df }
	return render(request, 'simpleview/chart.html', context)

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." %question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response %question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." %question_id)