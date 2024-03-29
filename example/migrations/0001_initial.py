# Generated by Django 3.2.3 on 2021-05-31 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('part_of', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='superunit_of', to='example.place')),
            ],
        ),
        migrations.CreateModel(
            name='MyText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('author', models.ManyToManyField(blank=True, to='example.Author')),
                ('pub_place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='is_publication_place', to='example.place')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='birth_place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='is_place_of_birth', to='example.place'),
        ),
        migrations.AddField(
            model_name='author',
            name='death_place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='is_place_of_death', to='example.place'),
        ),
    ]
