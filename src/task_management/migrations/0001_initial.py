# Generated by Django 5.0.2 on 2024-02-28 11:43

import abstract.enums
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("abstract", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="Board",
            fields=[
                (
                    "basemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="abstract.basemodel",
                    ),
                ),
                ("name", models.CharField(max_length=abstract.enums.CellSize["XL"])),
            ],
            options={
                "verbose_name_plural": "Boards",
                "db_table": "task_board",
                "managed": True,
            },
            bases=("abstract.basemodel",),
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "basemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="abstract.basemodel",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        max_length=abstract.enums.CellSize["XXXL"],
                        null=True,
                    ),
                ),
                ("due_date", models.DateField(blank=True, null=True)),
            ],
            options={
                "verbose_name_plural": "Tasks",
                "db_table": "task_task",
                "managed": True,
            },
            bases=("abstract.basemodel",),
        ),
        migrations.CreateModel(
            name="List",
            fields=[
                (
                    "basemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="abstract.basemodel",
                    ),
                ),
                ("name", models.CharField(max_length=abstract.enums.CellSize["LARGE"])),
                (
                    "assigned_board",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lists",
                        to="task_management.board",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Lists",
                "db_table": "task_list",
                "managed": True,
            },
            bases=("abstract.basemodel",),
        ),
    ]
