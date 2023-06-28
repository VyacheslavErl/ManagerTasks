from django.db import models

# Create your models here.


class TaskModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField("Название", max_length=60)  # название задачи
    text = models.TextField("Описание")  # описание задачи
    do_before = models.DateField("Дата окончания задачи")  # дата окончания задачи
    created_at = models.DateField("Дата создания задачи", auto_now=True)  # дата создания задачи
    image = models.ImageField("Изображение", upload_to="tasks_image/", default='no_image.png', blank=True)  # Изображение задачи
