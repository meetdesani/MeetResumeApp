# Generated by Django 4.2.5 on 2023-09-15 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('start_year', models.CharField(max_length=100)),
                ('end_year', models.CharField(max_length=100)),
                ('institute', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('grade', models.CharField(max_length=100)),
            ],
        ),
    ]
