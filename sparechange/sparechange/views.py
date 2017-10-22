from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView
from .forms import TextForm, UploadForm
import requests

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_and_render(self, request, text_form, upload_form):
        context = {
            'text_form': text_form,
            'upload_form': upload_form,
        }
        return render(request, self.template_name, context)

    def get(self, request, *args, **kwargs):
        text_form = TextForm()
        upload_form = UploadForm()
        return self.get_context_and_render(request, text_form, upload_form)

    def post(self, request, *args, **kwargs):
        text_form = TextForm(request.POST)
        upload_form = UploadForm(request.POST, request.FILES)
        if text_form.is_valid():
            body_url = text_form.cleaned_data['text_field']
            url = 'https://southcentralus.api.cognitive.microsoft.com/customvision/v1.0/Prediction/28c59880-0bd7-4640-a827-3ec095e9f0b6/url?iterationId=c4891dc9-c410-4c1e-9d89-acd600b3cd82'
            headers = {'Prediction-Key': 'a92ded792ef54446a4d5fb41d0b5184f', 'Content-Type': 'application/json'}
            r = requests.post(url, json = {"Url": body_url}, headers=headers)
            print r.content
            return HttpResponseRedirect('/')
        elif upload_form.is_valid():
            url = 'https://southcentralus.api.cognitive.microsoft.com/customvision/v1.0/Prediction/28c59880-0bd7-4640-a827-3ec095e9f0b6/image?iterationId=c4891dc9-c410-4c1e-9d89-acd600b3cd82'
            data = request.FILES.get('image_file')
            headers = {'Prediction-Key': 'a92ded792ef54446a4d5fb41d0b5184f', 'Content-Type': 'application/octet-stream'}
            r = requests.post(url, data = data, headers=headers)
            print r.content
            return HttpResponseRedirect('/')