# Generated by Django 3.1.2 on 2020-12-24 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='receiver',
        ),
        migrations.AlterField(
            model_name='message',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='留言日期'),
        ),
        migrations.AlterField(
            model_name='message',
            name='subject',
            field=models.CharField(max_length=200, verbose_name='主旨'),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.CharField(max_length=50, verbose_name='姓名'),
        ),
    ]
