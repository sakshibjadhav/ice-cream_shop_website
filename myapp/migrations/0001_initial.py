# Generated by Django 3.1.7 on 2021-04-30 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('address', models.TextField(max_length=122)),
                ('itype', models.CharField(max_length=20)),
                ('flavor', models.CharField(max_length=20)),
                ('quantity', models.CharField(max_length=20)),
                ('date', models.DateField()),
            ],
        ),
    ]