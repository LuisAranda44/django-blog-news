# Generated by Django 2.1.7 on 2019-04-02 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogNews', '0004_auto_20190402_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='image',
            field=models.ImageField(blank='True', default='/home/laranda/Proyecto_inicial/coche.jpeg', upload_to='news'),
        ),
    ]
