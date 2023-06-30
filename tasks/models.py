from django.db import models
from users.models import UserModel
# Create your models here.


class TaskModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField("Название", max_length=60)
    text = models.TextField("Описание")
    do_before = models.DateField("Дата окончания задачи")
    created_at = models.DateField("Дата создания задачи", auto_now=True)
    image = models.ImageField("Изображение", upload_to="tasks_image/", default='no_image.png', blank=True)


class CommentModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.CharField('Текст', max_length=250)
    date = models.DateField('Дата создания', auto_now=True)
    by_user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    task = models.ForeignKey(TaskModel, on_delete=models.CASCADE)
