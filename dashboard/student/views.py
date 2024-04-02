from django.shortcuts import render
from teacher.models import Notice  # Import the Notice model from the teacher app
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from teacher.models import CourseMaterial  # Assuming CourseMaterial is in the teacher app
from teacher.models import StudentMarks  # Assuming StudentMarks is in the teacher app
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'student/home.html')


def student_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            # Check if authenticated user belongs to the 'students' group
            if user is not None and user.groups.filter(name='students').exists():
                login(request, user)
                return redirect('home')  # Redirect to the student's home page
            else:
                # If user is not authenticated or not part of the 'students' group
                # Consider adding a message to indicate login failure or unauthorized access
                return render(request, 'student/login.html', {'form': form, 'error': 'Invalid credentials or you do not have permission to access this page.'})
    else:
        form = AuthenticationForm()
    return render(request, 'student/login.html', {'form': form})

def student_notice(request):
    # Fetch all notices ordered by creation date descending (newest first)
    notices = Notice.objects.all().order_by('-created_at')
    return render(request, 'student/studentnotice.html', {'notices': notices})

def show_course_material(request):
    materials = CourseMaterial.objects.all()
    return render(request, 'student/studentcoursematerial.html', {'materials': materials})
@login_required
def view_marks(request):
    try:
        marks_instance = StudentMarks.objects.get(student=request.user)
        percentage = (marks_instance.marks_obtained / marks_instance.total_marks) * 100
    except StudentMarks.DoesNotExist:
        marks_instance = None
        percentage = None

    return render(request, 'student/view_marks.html', {
        'marks_instance': marks_instance,
        'percentage': percentage,
    })
