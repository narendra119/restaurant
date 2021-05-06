# Generated by Django 3.2.2 on 2021-05-06 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_customer_customer_phno'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='order_status',
            field=models.CharField(choices=[('C', 'Completed'), ('N', 'Not Done'), ('D', 'Delivered')], default='N', max_length=1),
        ),
    ]