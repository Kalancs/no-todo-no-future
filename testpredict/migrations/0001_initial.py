# Generated by Django 3.1.2 on 2020-10-13 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Taskclassification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_date', models.CharField(max_length=200)),
            ],
        ),
    ]
