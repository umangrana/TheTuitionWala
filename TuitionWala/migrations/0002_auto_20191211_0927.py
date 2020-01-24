# Generated by Django 3.0 on 2019-12-11 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TuitionWala', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('coursesOffered', models.CharField(max_length=250)),
                ('facultyID', models.IntegerField(unique=True)),
                ('email', models.URLField(unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]