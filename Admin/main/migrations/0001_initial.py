# Generated by Django 5.0.3 on 2024-08-07 12:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fakultet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kurs', models.CharField(choices=[('4-kurs', '4-kurs'), ('2-kurs', '2-kurs'), ('1-kurs', '1-kurs'), ('3-kurs', '3-kurs')], default='1-kurs', max_length=90)),
                ('kurs_uz', models.CharField(choices=[('4-kurs', '4-kurs'), ('2-kurs', '2-kurs'), ('1-kurs', '1-kurs'), ('3-kurs', '3-kurs')], default='1-kurs', max_length=90, null=True)),
                ('kurs_ru', models.CharField(choices=[('4-kurs', '4-kurs'), ('2-kurs', '2-kurs'), ('1-kurs', '1-kurs'), ('3-kurs', '3-kurs')], default='1-kurs', max_length=90, null=True)),
                ('kurs_en', models.CharField(choices=[('4-kurs', '4-kurs'), ('2-kurs', '2-kurs'), ('1-kurs', '1-kurs'), ('3-kurs', '3-kurs')], default='1-kurs', max_length=90, null=True)),
                ('nomi', models.CharField(max_length=300)),
                ('nomi_uz', models.CharField(max_length=300, null=True)),
                ('nomi_ru', models.CharField(max_length=300, null=True)),
                ('nomi_en', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jadval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kurs', models.CharField(choices=[('4-kurs', '4-kurs'), ('2-kurs', '2-kurs'), ('1-kurs', '1-kurs'), ('3-kurs', '3-kurs')], default='1-kurs', max_length=90)),
                ('kurs_uz', models.CharField(choices=[('4-kurs', '4-kurs'), ('2-kurs', '2-kurs'), ('1-kurs', '1-kurs'), ('3-kurs', '3-kurs')], default='1-kurs', max_length=90, null=True)),
                ('kurs_ru', models.CharField(choices=[('4-kurs', '4-kurs'), ('2-kurs', '2-kurs'), ('1-kurs', '1-kurs'), ('3-kurs', '3-kurs')], default='1-kurs', max_length=90, null=True)),
                ('kurs_en', models.CharField(choices=[('4-kurs', '4-kurs'), ('2-kurs', '2-kurs'), ('1-kurs', '1-kurs'), ('3-kurs', '3-kurs')], default='1-kurs', max_length=90, null=True)),
                ('togri_javob', models.IntegerField()),
                ('togri_javob_uz', models.IntegerField(null=True)),
                ('togri_javob_ru', models.IntegerField(null=True)),
                ('togri_javob_en', models.IntegerField(null=True)),
                ('notogri_javob', models.IntegerField()),
                ('notogri_javob_uz', models.IntegerField(null=True)),
                ('notogri_javob_ru', models.IntegerField(null=True)),
                ('notogri_javob_en', models.IntegerField(null=True)),
                ('ball', models.IntegerField()),
                ('timer', models.CharField(max_length=120)),
                ('sana', models.DateField()),
                ('fakultet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.fakultet')),
                ('fakultet_en', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.fakultet')),
                ('fakultet_ru', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.fakultet')),
                ('fakultet_uz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.fakultet')),
                ('ismi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ismi_en', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ismi_ru', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ismi_uz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Savollar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kurs', models.CharField(choices=[('4-kurs', '4-kurs'), ('2-kurs', '2-kurs'), ('1-kurs', '1-kurs'), ('3-kurs', '3-kurs')], default='1-kurs', max_length=90)),
                ('kurs_uz', models.CharField(choices=[('4-kurs', '4-kurs'), ('2-kurs', '2-kurs'), ('1-kurs', '1-kurs'), ('3-kurs', '3-kurs')], default='1-kurs', max_length=90, null=True)),
                ('kurs_ru', models.CharField(choices=[('4-kurs', '4-kurs'), ('2-kurs', '2-kurs'), ('1-kurs', '1-kurs'), ('3-kurs', '3-kurs')], default='1-kurs', max_length=90, null=True)),
                ('kurs_en', models.CharField(choices=[('4-kurs', '4-kurs'), ('2-kurs', '2-kurs'), ('1-kurs', '1-kurs'), ('3-kurs', '3-kurs')], default='1-kurs', max_length=90, null=True)),
                ('savol', models.TextField()),
                ('savol_uz', models.TextField(null=True)),
                ('savol_ru', models.TextField(null=True)),
                ('savol_en', models.TextField(null=True)),
                ('variant1', models.CharField(blank=True, max_length=300, null=True)),
                ('variant1_uz', models.CharField(blank=True, max_length=300, null=True)),
                ('variant1_ru', models.CharField(blank=True, max_length=300, null=True)),
                ('variant1_en', models.CharField(blank=True, max_length=300, null=True)),
                ('variant2', models.CharField(blank=True, max_length=300, null=True)),
                ('variant2_uz', models.CharField(blank=True, max_length=300, null=True)),
                ('variant2_ru', models.CharField(blank=True, max_length=300, null=True)),
                ('variant2_en', models.CharField(blank=True, max_length=300, null=True)),
                ('variant3', models.CharField(blank=True, max_length=300, null=True)),
                ('variant3_uz', models.CharField(blank=True, max_length=300, null=True)),
                ('variant3_ru', models.CharField(blank=True, max_length=300, null=True)),
                ('variant3_en', models.CharField(blank=True, max_length=300, null=True)),
                ('variant4', models.CharField(blank=True, max_length=300, null=True)),
                ('variant4_uz', models.CharField(blank=True, max_length=300, null=True)),
                ('variant4_ru', models.CharField(blank=True, max_length=300, null=True)),
                ('variant4_en', models.CharField(blank=True, max_length=300, null=True)),
                ('javob', models.CharField(max_length=300)),
                ('javob_uz', models.CharField(max_length=300, null=True)),
                ('javob_ru', models.CharField(max_length=300, null=True)),
                ('javob_en', models.CharField(max_length=300, null=True)),
                ('fakultet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.fakultet')),
                ('fakultet_en', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.fakultet')),
                ('fakultet_ru', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.fakultet')),
                ('fakultet_uz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.fakultet')),
            ],
        ),
    ]