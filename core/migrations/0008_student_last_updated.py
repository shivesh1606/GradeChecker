# Generated by Django 4.1.4 on 2022-12-23 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_alter_studentsubject_grade"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="last_updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]