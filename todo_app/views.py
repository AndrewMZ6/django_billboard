from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import MyTestModel


# Create your views here.
def index(request):
	results = MyTestModel.objects.all()
	template = loader.get_template("base.html")
	return HttpResponse(template.render({'results':results}, request))


def form_get(request):
	template = loader.get_template("base2.html")
	return HttpResponse(template.render({}, request))


def form_post(request):
	m1 = MyTestModel(name=request.POST['name_name'], age=request.POST['age_name'])
	m1.save()
	return HttpResponseRedirect(reverse('undex'))


def remove_task(request, task_id):
	task_to_remove = MyTestModel.objects.get(pk=task_id)
	task_to_remove.delete()
	return HttpResponseRedirect(reverse('undex'))


def edit_task(request, task_id):
	task_to_edit = MyTestModel.objects.get(pk=task_id)
	task_to_edit.name = request.POST['name_name']
	task_to_edit.age = request.POST['age_name']
	task_to_edit.save()
	return HttpResponseRedirect(reverse('undex'))


def form_edit(request, task_id):
	template = loader.get_template("edit_task.html")
	return HttpResponse(template.render({'task_id':task_id}, request))

