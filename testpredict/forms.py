from django import forms

from .models import Taskclassification as task_class

class TodoForm(forms.ModelForm):

    class Meta:
        model = task_class
        #fields = ('todo_text',)
        fields = ('item',"completed","deadline",)
        date_field = forms.DateField(
          widget = forms.DateInput(attrs={"type":"date"})
        )
