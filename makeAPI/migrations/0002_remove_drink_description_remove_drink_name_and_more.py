# Generated by Django 4.1 on 2022-08-16 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("makeAPI", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="drink", name="description",),
        migrations.RemoveField(model_name="drink", name="name",),
        migrations.AddField(
            model_name="drink",
            name="dueDate",
            field=models.CharField(default="8/15/2022", max_length=10),
        ),
        migrations.AddField(
            model_name="drink",
            name="task",
            field=models.CharField(default="nothing", max_length=100),
        ),
        migrations.AddField(
            model_name="drink",
            name="urgency",
            field=models.DecimalField(decimal_places=2, default=1, max_digits=4),
        ),
    ]
