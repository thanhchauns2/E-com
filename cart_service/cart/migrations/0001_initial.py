# Generated by Django 4.1.7 on 2023-04-17 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('cart_id', models.CharField(max_length=255)),
                ('items', models.JSONField()),
            ],
        ),
    ]
