# Generated by Django 3.2.3 on 2021-05-29 22:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0006_alter_post_allowed_users'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={},
        ),
        migrations.RemoveField(
            model_name='post',
            name='allowed_users',
        ),
        migrations.RemoveField(
            model_name='post',
            name='is_hidden',
        ),
        migrations.AddField(
            model_name='topic',
            name='allowed_users',
            field=models.ManyToManyField(related_name='allowed_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
