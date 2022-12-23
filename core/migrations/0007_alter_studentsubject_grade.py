# Generated by Django 4.1.4 on 2022-12-23 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_alter_studentsubject_semester"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentsubject",
            name="grade",
            field=models.IntegerField(
                choices=[
                    (10, "EX"),
                    (9, "A"),
                    (8, "B"),
                    (7, "C"),
                    (6, "D"),
                    (5, "P"),
                    (0, "F"),
                    (-1, "Unknown"),
                ]
            ),
        ),
    ]
