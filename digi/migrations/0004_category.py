# Generated by Django 4.2.2 on 2023-07-17 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digi', '0003_remove_sellacc_ac_dob_sellacc_ac_fullname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('category_img', models.ImageField(default='/static/images/travel.jpg', upload_to='static/images/')),
            ],
        ),
    ]
