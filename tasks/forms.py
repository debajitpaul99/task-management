from django import forms
from tasks.models import Task

# class StyledFromMixin:
#     default_classes = "border-2 border-gray-100 w-full rounded-md" # all common classes

#     def add_styled_widgets(self):
#         for field_name, field in self.fields.items():
#             if isinstance(field.widget, forms.TextInput):
#                 field.widget.attrs.update({
#                     "class": self.default_classes,
#                     "placeholder": f"Enter {field.label.lower()}"
#                 })
#             elif isinstance(field.widget, forms.Textarea):
#                 field.widget.attrs.update({
#                     "class": self.default_classes,
#                     "placeholder": f"Enter {field.label.lower()}"
#                 })
#             elif isinstance(field.widget, forms.SelectDateWidget):
#                 field.widget.attrs.update({
#                     "class": self.default_classes,
#                     "placeholder": f"Enter {field.label.lower()}"
#                 })

# Django model form
class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title","description","due_date","assigned_to"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "border-2 border-gray-100 w-full rounded-md",
                "placeholder": "Enter Task Title"
            }),
            "description": forms.Textarea(attrs={
                "class": "border-2 border-gray-100 w-full rounded-md",
                "placeholder": "Describe the task"
            }),
            "due_date": forms.SelectDateWidget(attrs={
                "class": "border-2 border-gray-100 rounded-md"
            }),
            "assigned_to": forms.CheckboxSelectMultiple
        }