from django import forms

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True  # custom subclass

class UploadForm(forms.Form):
    files = forms.FileField(
        widget=MultipleFileInput(attrs={"multiple": True}),
        label="Upload Files"
    )
