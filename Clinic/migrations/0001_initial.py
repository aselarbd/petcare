# Generated by Django 3.1.1 on 2020-09-02 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('availabilityID', models.AutoField(primary_key=True, serialize=False)),
                ('dateAndTime', models.DateTimeField()),
                ('_created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClinicBase',
            fields=[
                ('clinicID', models.AutoField(primary_key=True, serialize=False)),
                ('clinicName', models.CharField(max_length=100)),
                ('_created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vet',
            fields=[
                ('vetID', models.AutoField(primary_key=True, serialize=False)),
                ('vetName', models.CharField(max_length=100)),
                ('_created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TakenSlots',
            fields=[
                ('takenID', models.AutoField(primary_key=True, serialize=False)),
                ('_created_at', models.DateTimeField(auto_now_add=True)),
                ('availabilityID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clinic.availability')),
                ('clinicID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clinic.clinicbase')),
                ('vetID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clinic.vet')),
            ],
            options={
                'unique_together': {('vetID', 'availabilityID', 'clinicID')},
            },
        ),
    ]