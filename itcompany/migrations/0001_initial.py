# Generated by Django 3.1.7 on 2021-05-23 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('is_verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.EmailField(max_length=254)),
                ('reciever', models.EmailField(max_length=254)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('subject', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_numbers', models.IntegerField(max_length=50)),
                ('team_name', models.CharField(max_length=100)),
                ('team_lead', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Payslips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField(max_length=20)),
                ('per_annum', models.IntegerField(max_length=20)),
                ('bank_name', models.CharField(max_length=30)),
                ('tax', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField(max_length=20)),
                ('qualification', models.CharField(max_length=100)),
                ('age', models.IntegerField(max_length=10)),
                ('gender', models.CharField(max_length=50)),
                ('team', models.CharField(max_length=100)),
                ('salary', models.IntegerField(max_length=20)),
                ('photo', models.ImageField(upload_to='media/')),
                ('office', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='itcompany.application')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
