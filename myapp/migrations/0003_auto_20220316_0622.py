# Generated by Django 3.2 on 2022-03-16 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20220315_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(max_length=9)),
                ('date_of_payment', models.DateTimeField(auto_now_add=True)),
                ('discount', models.IntegerField(default=0)),
                ('customer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.membership')),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
