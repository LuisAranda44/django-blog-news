# Generated by Django 2.1.7 on 2019-04-02 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogNews', '0008_auto_20190402_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='image',
            field=models.ImageField(blank='True', upload_to='news'),
        ),
    ]