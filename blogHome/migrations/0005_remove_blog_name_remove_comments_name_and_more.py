# Generated by Django 4.2.9 on 2024-03-09 17:12

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogHome', '0004_comments_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='name',
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reply',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blog',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='reply',
            name='reply',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
