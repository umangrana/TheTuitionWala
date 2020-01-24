# Generated by Django 3.0 on 2020-01-14 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TuitionWala', '0007_mystudent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute_names', models.CharField(choices=[('Vivekananda foundation', 'Vivekananda foundation'), ('Ragatuition', 'Ragatuition'), ('BRILLIANT ACADEMY', 'BRILLIANT ACADEMY'), ('MelhorInstitute', 'MelhorInstitute'), ('Prasads-Educational-Institutions', 'Prasads-Educational-Institutions'), ('TeachingFish', 'TeachingFish'), ('Srinivasa Coaching Center', 'Srinivasa Coaching Center'), ('Home Tuitions', 'Home Tuitions'), ('Prism Coaching Center', 'Prism Coaching Center'), ('Hemtor Tuitions', 'Hemtor Tuitions')], max_length=200, null=True)),
                ('subjects', models.CharField(choices=[('ENGLISH', 'ENGLISH'), ('MATHEMATICS', 'MATHEMATICS'), ('SOCIAL', 'SOCIAL'), ('PHYSICS', 'PHYSICS'), ('BIOLOGY', 'BIOLOGY'), ('COMMERCE', 'COMMERCE'), ('ECONOMICS', 'ECONOMICS'), ('CIVICS', 'CIVICS'), ('COMPUTER SCIENCES', 'COMPUTER SCIENCES')], max_length=200, null=True)),
                ('fees', models.CharField(choices=[('500-1000 Per Month', '500-1000 Per Month'), ('1000-1500 Per Month', '1000-1500 Per Month'), ('1500-2000 Per Month', '1500-2000 Per Month'), ('Above 2000 Per Month', 'Above 2000 Per Month')], max_length=200, null=True)),
            ],
        ),
    ]
