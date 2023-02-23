from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import TaskList, TaskCreate, TaskUpdate, TaskDelete, TaskDetailView

urlpatterns = [
    path('task-list/', TaskList.as_view(), name='task-list'),  # asview=  class based
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name = 'task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('task-view/<int:pk>/', TaskDetailView.as_view(), name='task-view'),
    path("login",views.login_1,name='login'),
    path("register",views.register,name='register')


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)