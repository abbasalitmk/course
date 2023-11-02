from django.shortcuts import render, redirect
from .forms import CourseForm
from django.contrib import messages
from .models import Course
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q


@login_required(login_url='login')
def course_view(request):
    courses = Course.objects.all().order_by('-id')
    search_key = request.GET.get('search_key')

    if search_key:
        courses = courses.filter(Q(title__icontains=search_key) | Q(
            description__icontains=search_key))

    items_per_page = 2
    paginator = Paginator(courses, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request, 'short-course-view.html', {"courses": page, "search_key": search_key})


@login_required(login_url='login')
def course_detail_view(request, id):
    courses = Course.objects.get(id=id)

    return render(request, 'short-course-view.html', {"courses": courses})


@login_required(login_url='login')
def course_create(request):
    if request.method == 'POST':
        print("working")
        form = CourseForm(request.POST, request.FILES)
        print("enter")
        if form.is_valid():
            print("valid")
            course = form.save()
            messages.success(request, "Course added successfully")
            return redirect('view')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CourseForm()

    return render(request, 'short-course-create.html', {"form": form})


@login_required(login_url='login')
def course_delete(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('view')


@login_required(login_url='login')
def course_edit(request, id):
    course = Course.objects.get(id=id)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully")
            return redirect('view')
    else:
        form = CourseForm(instance=course)

        return render(request, 'short-course-create.html', {"form": form, "course": course})


@login_required(login_url='login')
def change_status(request, id):
    courses = Course.objects.all().order_by('-id')

    single_course = Course.objects.get(id=id)
    print(single_course.status_text)

    if single_course.status_text == 'Enable':
        single_course.status_text = 'Disable'
        single_course.save()
        return redirect('view')
    else:
        single_course.status_text = 'Enable'
        single_course.save()
        return redirect('view')

    return render(request, 'short-course-view.html', {"courses": courses})
