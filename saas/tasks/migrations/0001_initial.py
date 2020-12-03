# Generated by Django 3.1.3 on 2020-12-03 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('assignee', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('todo', 'To Do'), ('in_progress', 'In-progress'), ('qa', 'Quality Assesment'), ('done', 'Done')], default='todo', max_length=32)),
                ('priority', models.CharField(choices=[('low', 'Low'), ('med', 'Medium'), ('high', 'High')], default='low', max_length=32)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
