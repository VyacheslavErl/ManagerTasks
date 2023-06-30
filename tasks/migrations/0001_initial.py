# Generated by Django 4.2.2 on 2023-06-27 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Описание')),
                ('do_before', models.DateField(verbose_name='Дата окончания задачи')),
                ('created_at', models.DateField(auto_now=True, verbose_name='Дата создания задачи')),
                ('image', models.ImageField(upload_to='tasks_image/', verbose_name='Изображение')),
            ],
        ),
    ]