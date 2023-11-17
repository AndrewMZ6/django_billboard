from django.urls import path
from .views import index, form_post, form_get, remove_task, edit_task, form_edit


urlpatterns = [
	path('', index, name='undex'),
	path('form_get/', form_get),
	path('form_post/', form_post),
	path('remove_task/<int:task_id>', remove_task),
	path('edit_task/<int:task_id>', edit_task),
	path('form_edit/<int:task_id>', form_edit),
]