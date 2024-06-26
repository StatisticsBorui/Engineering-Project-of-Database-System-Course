# Generated by Django 4.2.13 on 2024-06-01 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Class",
            fields=[
                (
                    "class_id",
                    models.SmallIntegerField(primary_key=True, serialize=False),
                ),
                ("stu_number", models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="ShowScore",
            fields=[
                ("stu_id_id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=64)),
                ("score1", models.SmallIntegerField(null=True)),
                ("score2", models.SmallIntegerField(null=True)),
                ("score3", models.SmallIntegerField(null=True)),
            ],
            options={
                "db_table": "showscore",
            },
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "stu_id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="users.user",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("major", models.CharField(max_length=128)),
                (
                    "class_id",
                    models.ForeignKey(on_delete=models.SET(0), to="stu_page.class"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Exam",
            fields=[
                (
                    "stu_id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="stu_page.student",
                    ),
                ),
                ("score1", models.SmallIntegerField()),
                ("score2", models.SmallIntegerField()),
                ("score3", models.SmallIntegerField()),
            ],
        ),
    ]
