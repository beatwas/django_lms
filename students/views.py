from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt # noqa

from webargs.djangoparser import use_args
from webargs.fields import Str

from .forms import CreateStudentForm
from .forms import UpdateStudentForm
from .models import Student


def index(request):
    return HttpResponse('Welcome to LMS')


@use_args(
    {
        'first_name': Str(required=False),
        'last_name': Str(required=False),
    },
    location='query'
)
def get_students(request, args):
    students = Student.objects.all()

    if len(args) and args.get('first_name') or args.get('last_name'):
        students = students.filter(
            Q(first_name=args.get('first_name', '')) | Q(last_name=args.get('last_name', ''))
        )

    return render(
        request=request,
        template='students/list.html',
        context={
            'title': 'List of students',
            'students': students
        }
    )


def detail_student(request, student_id):
    student = Student.objects.get(pk=student_id)

    return render(request, 'students/details.html', {'student': student})


# @csrf_exempt
def create_student(request):
    if request.method == 'GET':
        form = CreateStudentForm()
    elif request.method == 'POST':
        form = CreateStudentForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')

    token = get_token(request)

    html_form = f'''
        <form method="get">
            <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
            <table>
                {form.as_table()}
            </table>
            <input type="submit" value="Submit">
        </form>
    '''

    return HttpResponse(html_form)


def update_student(request, student_id):
    student = Student.objects.get(pk=student_id)

    if request.method == 'GET':
        form = UpdateStudentForm(instance=student)
    elif request.method == 'POST':
        form = UpdateStudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')

    token = get_token(request)

    html_form = f'''
        <form method="get">
            <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
            <table>
                {form.as_table()}
            </table>
            <input type="submit" value="Submit">
        </form>
    '''

    return HttpResponse(html_form)
