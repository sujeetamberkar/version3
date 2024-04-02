from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Notice(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class CourseMaterial(models.Model):
    chapter_name = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='course_materials/pdfs/')
    video_url = models.URLField(max_length=1024)

    def __str__(self):
        return self.chapter_name

class StudentMarks(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='marks')
    marks_obtained = models.IntegerField(default=0)
    total_marks = models.IntegerField(default=100)  # Assuming 100 is the total marks for simplicity

    def __str__(self):
        return f"{self.student.username} - {self.marks_obtained}/{self.total_marks}"
