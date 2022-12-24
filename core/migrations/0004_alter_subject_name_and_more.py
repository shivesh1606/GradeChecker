# Generated by Django 4.1.4 on 2022-12-23 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_studentsemester_acgpa_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subject",
            name="name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterUniqueTogether(
            name="studentsemester",
            unique_together={("student", "semester")},
        ),
        migrations.AlterUniqueTogether(
            name="studentsubject",
            unique_together={("student", "semester", "subject")},
        ),
    ]