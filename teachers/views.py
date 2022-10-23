from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt # noqa

from webargs.djangoparser import use_args
from webargs.fields import Str

from .forms import CreateTeacherForm
from .forms import UpdateTeacherForm
from .models import Teacher


@use_args(
    {
        'first_name': Str(required=False),
        'last_name': Str(required=False),
    },
    location='query'
)
def get_teachers(request, args):
    teachers = Teacher.objects.all()

    if len(args) and args.get('first_name') or args.get('last_name'):
        teachers = teachers.filter(
            Q(first_name=args.get('first_name', '')) | Q(last_name=args.get('last_name', ''))
        )

    return render(
        request=request,
        template='students/list.html',
        context={
            'title': 'List of teachers',
            'teachers': teachers
        }
    )


def detail_teacher(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)

    return render(request, 'teachers/details.html', {'teacher': teacher})


# @csrf_exempt
def create_teacher(request):
    if request.method == 'GET':
        form = CreateTeacherForm()
    elif request.method == 'POST':
        form = CreateTeacherForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')

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


def update_teacher(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)

    if request.method == 'GET':
        form = UpdateTeacherForm(instance=teacher)
    elif request.method == 'POST':
        form = UpdateTeacherForm(request.POST, instance=teacher)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')

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
