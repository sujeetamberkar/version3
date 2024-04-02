from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import Notice
from .forms import CourseMaterialForm
from django.contrib.auth.models import User
from .forms import MarksForm
from .models import StudentMarks
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group

def home(request):
    # Ensure this template path is correct and unique to the teacher's home page
    return render(request, 'teacher/home.html')

def teacher_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.groups.filter(name='teachers').exists():
                login(request, user)
                return redirect('teacher_home')
            else:
                # If the user is not authenticated or not in the 'teachers' group, handle as a failed login attempt
                # Here, you might want to add a message indicating the failure reason
                return render(request, 'teacher/login.html', {'form': form, 'error': 'Invalid credentials or you do not have permission to access this page.'})
    else:
        form = AuthenticationForm()
    return render(request, 'teacher/login.html', {'form': form})

@login_required
def teacher_notice(request):
    if request.method == 'POST':
        notice_content = request.POST.get('notice')
        if notice_content:
            Notice.objects.create(content=notice_content)
            # Redirect to the teacher's home page after the notice is successfully saved
            return redirect('teacher_home')
        else:
            # Optionally, handle the case where the notice content is empty
            # You might want to pass a message indicating the need for notice content
            return render(request, 'teacher/teachernotice.html', {
                'error': 'Please enter some text for the notice.'
            })
    return render(request, 'teacher/teachernotice.html')

def add_course_material(request):
    if request.method == 'POST':
        form = CourseMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teacher_home')  # Adjust as necessary
    else:
        form = CourseMaterialForm()
    return render(request, 'teacher/teachercoursematerial.html', {'form': form})



@login_required
def enter_update_marks(request):
    # Get all users in the 'students' group
    student_group = Group.objects.get(name='students')
    students = student_group.user_set.all()

    if request.method == 'POST':
        for student in students:
            marks_obtained = request.POST.get(f'marks_obtained_{student.id}')
            total_marks = request.POST.get(f'total_marks_{student.id}')
            # Update or create the StudentMarks record
            StudentMarks.objects.update_or_create(
                student=student,
                defaults={
                    'marks_obtained': marks_obtained,
                    'total_marks': total_marks
                }
            )
        return redirect('enter_update_marks')

    # Fetch existing marks for all students
    marks = {mark.student_id: mark for mark in StudentMarks.objects.filter(student__in=students)}

    return render(request, 'teacher/teachermarks.html', {'students': students, 'marks': marks})
