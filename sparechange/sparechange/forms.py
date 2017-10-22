from django.forms import Form, FileField

class UploadForm(Form):
	image_file = FileField()
