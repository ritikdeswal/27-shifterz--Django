# Generated by Django 3.2.8 on 2021-10-23 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_orderplaced_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.customer'),
        ),
    ]
