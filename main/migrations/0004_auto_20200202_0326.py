# Generated by Django 2.2.3 on 2020-02-01 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200202_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agt',
            name='college',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='agt',
            name='contactno',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='agt',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='agt',
            name='perform',
            field=models.TextField(),
        ),
    ]
