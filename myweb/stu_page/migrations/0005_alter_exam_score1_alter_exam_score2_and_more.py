# Generated by Django 4.2.13 on 2024-06-03 11:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("stu_page", "0004_rename_class_class0"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exam",
            name="score1",
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="exam",
            name="score2",
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="exam",
            name="score3",
            field=models.SmallIntegerField(null=True),
        ),
    ]
