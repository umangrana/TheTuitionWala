# Generated by Django 3.0 on 2019-12-16 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TuitionWala', '0002_auto_20191211_0927'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Mobile_No', models.IntegerField()),
            ],
        ),
    ]
