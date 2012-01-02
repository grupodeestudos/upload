# Create your views here.


from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.servers.basehttp import FileWrapper
from django.template import RequestContext


from main.models import File

def index(request):
    return render_to_response('main/templates/index.html', {'files': File.objects.all()})

def new(r):
    if r.POST:
        novo = File()
        file = r.FILES['file']
        novo.content = file
        novo.name = file.name
        novo.title = r.POST['title']
        novo.save()

        return HttpResponseRedirect('/')
    else:
        return render_to_response('main/templates/new.html', context_instance = RequestContext(r))


def download(r, id):
    f = File.objects.get(id=id)
    resp = HttpResponse(FileWrapper(f.content), content_type='application/octet-stream')
    resp['Content-Disposition'] = 'attachment; filename={0}'.format(f.name)
    return resp


