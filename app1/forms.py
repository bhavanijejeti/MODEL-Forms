from django import forms
from app1.models import *
class Topicmodelform(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class Webpagemodelform(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        widgets={'topic_name':forms.RadioSelect,'name':forms.Textarea}

class AccessRecordmodelform(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields='__all__'