from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView
from .forms import UploadForm

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_and_render(self, request, upload_form):
        context = {
            'upload_form': upload_form,
        }
        return render(request, self.template_name, context)

    def get(self, request, *args, **kwargs):
        upload_form = UploadForm()
        return self.get_context_and_render(request, upload_form)

    def post(self, request, *args, **kwargs):
        upload_form = UploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            print 'implementation required'
            # handle_files(request.FILES.get('image_file'))
            return HttpResponseRedirect('/')
        