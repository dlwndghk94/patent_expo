# encoding: utf-8
import json

from django.http import HttpResponse
from django.views.generic import CreateView, DeleteView, ListView
from .models import File
from .response import JSONResponse, response_mimetype
from .serialize import serialize


class FileCreateView(CreateView):
    model = File
    fields = "__all__"


class FileDeleteView(DeleteView):
    model = File

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = JSONResponse(True, mimetype=response_mimetype(request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response


class FileListView(ListView):
    model = File

    def render_to_response(self, context, **response_kwargs):
        files = [ serialize(p) for p in self.get_queryset() ]
        data = {'files': files}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response

def predict(request, *args, **kwargs):
    if request.method == 'POST':
        patent = request.POST.get('textfield', None)
        return HttpResponse(patent)
    return
