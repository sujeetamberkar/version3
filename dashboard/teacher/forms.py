from django import forms
from .models import CourseMaterial
from .models import StudentMarks

class CourseMaterialForm(forms.ModelForm):
    class Meta:
        model = CourseMaterial
        fields = ['chapter_name', 'pdf_file', 'video_url']
class MarksForm(forms.ModelForm):
    class Meta:
        model = StudentMarks
        fields = ['student', 'marks_obtained', 'total_marks']
