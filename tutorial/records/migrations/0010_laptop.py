# Generated by Django 4.2 on 2024-09-17 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0009_alter_contactus_contact_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
            ],
        ),
    ]
