from django.forms import ModelForm
from app.models import TODO

class TodoForm (ModelForm):
    class Meta:
        model=TODO
        fields =("title","status","priority")