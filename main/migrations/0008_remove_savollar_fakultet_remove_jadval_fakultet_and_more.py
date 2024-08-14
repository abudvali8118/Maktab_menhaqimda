# Generated by Django 5.0.3 on 2024-08-14 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_fakultet_kurs_alter_fakultet_kurs_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savollar',
            name='fakultet',
        ),
        migrations.RemoveField(
            model_name='jadval',
            name='fakultet',
        ),
        migrations.RemoveField(
            model_name='savollar',
            name='fakultet_ru',
        ),
        migrations.RemoveField(
            model_name='jadval',
            name='fakultet_en',
        ),
        migrations.RemoveField(
            model_name='jadval',
            name='fakultet_uz',
        ),
        migrations.RemoveField(
            model_name='savollar',
            name='fakultet_en',
        ),
        migrations.RemoveField(
            model_name='jadval',
            name='fakultet_ru',
        ),
        migrations.RemoveField(
            model_name='savollar',
            name='fakultet_uz',
        ),
        migrations.RemoveField(
            model_name='jadval',
            name='ismi',
        ),
        migrations.RemoveField(
            model_name='jadval',
            name='ismi_en',
        ),
        migrations.RemoveField(
            model_name='jadval',
            name='ismi_ru',
        ),
        migrations.RemoveField(
            model_name='jadval',
            name='ismi_uz',
        ),
        migrations.DeleteModel(
            name='Fakultet',
        ),
        migrations.DeleteModel(
            name='Savollar',
        ),
        migrations.DeleteModel(
            name='Jadval',
        ),
    ]