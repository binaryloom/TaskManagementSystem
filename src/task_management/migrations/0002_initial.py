# Generated by Django 5.0.2 on 2024-02-29 20:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("task_management", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="board",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(class)s_created_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="board",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(class)s_updated_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="list",
            name="assigned_board",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lists",
                to="task_management.board",
            ),
        ),
        migrations.AddField(
            model_name="list",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(class)s_created_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="list",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(class)s_updated_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="assigned_list",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tasks",
                to="task_management.list",
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="assigned_to",
            field=models.ManyToManyField(
                blank=True, related_name="assigned_tasks", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(class)s_created_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(class)s_updated_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
