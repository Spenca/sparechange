from django.forms import CharField, FileField, Form

class TextForm(Form):
	text_field = CharField()

class UploadForm(Form):
	image_file = FileField()
