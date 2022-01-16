from django.shortcuts import render
from django.http import HttpResponse
from projects.models import topic, Webpage, AccessRecord

projectsList = [{'id':'1',
'title':'ECO WEB',
'des': 'bla bla bla '},{'id':'2',
'title':'shomam WEB',
'des': 'bla bla bla '},{'id':'3',
'title':'b6e5 WEB',
'des': 'bla bla bla '}]

def projects (request):
    page = 'page1'
    number = 13
    context = {'page':page,'number' :number, 'projects':projectsList}
    return render(request, 'projects/projects.html',context)


def project (request, pk):
    projecObj = None
    for i in projectsList:
        if i['id'] == pk:
            projecObj = i
    return render(request, 'projects/project.html', {'project': projecObj})

def index (request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dic = {'access_records':webpage_list }
    return render(request, 'projects/projects.html',context =date_dic)

