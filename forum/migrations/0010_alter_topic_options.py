# Generated by Django 3.2.3 on 2021-05-29 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_alter_topic_allowed_users'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'permissions': (('can_verify_topics', 'Can verify topics'),)},
        ),
    ]
