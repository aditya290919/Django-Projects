# Generated by Django 4.1.6 on 2023-02-20 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://tse3.mm.bing.net/th?id=OIP.N0JNvG4iu61u97rvu8FZWgHaFe&pid=Api&P=0', max_length=500),
        ),
    ]
