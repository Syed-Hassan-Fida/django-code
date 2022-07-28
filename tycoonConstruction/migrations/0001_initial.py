# Generated by Django 3.1.4 on 2022-05-24 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estimation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brickCost', models.IntegerField(help_text='Brick Cost')),
                ('sandCost', models.IntegerField(help_text='Sand Cost')),
                ('cementCost', models.IntegerField(help_text='Cement Cost')),
                ('labourCost', models.IntegerField(help_text='Labour Cost')),
                ('steelCost', models.IntegerField(help_text='Steel Cost')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120, null=True)),
                ('last_name', models.CharField(max_length=120, null=True)),
                ('mobile_no', models.IntegerField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('project_address', models.CharField(max_length=200, null=True)),
                ('desc', models.CharField(max_length=300, null=True)),
                ('project_budget', models.IntegerField(max_length=200, null=True)),
                ('meeting_date', models.DateField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='VtoC_req',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('year_of_experience', models.IntegerField()),
                ('projects_done', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='vtoc/')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='bidVendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('projects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tycoonConstruction.projects')),
            ],
        ),
        migrations.CreateModel(
            name='bidContractor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mini_vendors', models.IntegerField(max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('projects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tycoonConstruction.projects')),
            ],
        ),
    ]