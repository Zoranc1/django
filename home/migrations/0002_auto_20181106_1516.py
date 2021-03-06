# Generated by Django 2.0.6 on 2018-11-06 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='topic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='books', to='home.Topic'),
        ),
    ]
