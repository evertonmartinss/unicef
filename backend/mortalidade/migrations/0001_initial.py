# Generated by Django 2.2.1 on 2019-05-07 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('iso_code', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('country_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mortality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('median', models.TextField(blank=True, null=True)),
                ('year', models.TextField(blank=True, null=True)),
                ('iso_code', models.ForeignKey(db_column='iso_code', on_delete=django.db.models.deletion.CASCADE, to='mortalidade.Country')),
            ],
        ),
    ]
