# Generated by Django 3.2.3 on 2021-05-30 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0012_alter_topic_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': (('can_delete_every_post', 'Can delete every post'), ('can_add_post', 'Can add post'), ('can_delete_own_post', 'Can delete own post'))},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'permissions': (('can_verify_topics', 'Can verify topics'), ('can_view_all_topics', 'Can view all topics'), ('can_add_topic', 'Can add topic'))},
        ),
    ]
