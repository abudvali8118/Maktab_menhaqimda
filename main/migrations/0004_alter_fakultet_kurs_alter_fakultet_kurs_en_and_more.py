# Generated by Django 5.0.3 on 2024-08-07 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_fakultet_kurs_alter_fakultet_kurs_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fakultet',
            name='kurs',
            field=models.CharField(choices=[('4-kurs', '4-kurs'), ('1-kurs', '1-kurs'), ('3-kurs', '3-kurs'), ('2-kurs', '2-kurs')], default='1-kurs', max_length=90),
        ),
        migrations.AlterField(
            model_name='fakultet',
            name='kurs_en',
            field=models.CharField(choices=[('4-kurs', '4-kurs'), ('1-kurs', '1-kurs'), ('3-kurs', '3-kurs'), ('2-kurs', '2-kurs')], default='1-kurs', max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='fakultet',
            name='kurs_ru',
            field=models.CharField(choices=[('4-kurs', '4-kurs'), ('1-kurs', '1-kurs'), ('3-kurs', '3-kurs'), ('2-kurs', '2-kurs')], default='1-kurs', max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='fakultet',
            name='kurs_uz',
            field=models.CharField(choices=[('4-kurs', '4-kurs'), ('1-kurs', '1-kurs'), ('3-kurs', '3-kurs'), ('2-kurs', '2-kurs')], default='1-kurs', max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='jadval',
            name='kurs',
            field=models.CharField(choices=[('4-kurs', '4-kurs'), ('1-kurs', '1-kurs'), ('3-kurs', '3-kurs'), ('2-kurs', '2-kurs')], default='1-kurs', max_length=90),
        ),
        migrations.AlterField(
            model_name='jadval',
            name='kurs_en',
            field=models.CharField(choices=[('4-kurs', '4-kurs'), ('1-kurs', '1-kurs'), ('3-kurs', '3-kurs'), ('2-kurs', '2-kurs')], default='1-kurs', max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='jadval',
            name='kurs_ru',
            field=models.CharField(choices=[('4-kurs', '4-kurs'), ('1-kurs', '1-kurs'), ('3-kurs', '3-kurs'), ('2-kurs', '2-kurs')], default='1-kurs', max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='jadval',
            name='kurs_uz',
            field=models.CharField(choices=[('4-kurs', '4-kurs'), ('1-kurs', '1-kurs'), ('3-kurs', '3-kurs'), ('2-kurs', '2-kurs')], default='1-kurs', max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='savollar',
            name='kurs',
            field=models.CharField(choices=[('4-kurs', '4-kurs'), ('1-kurs', '1-kurs'), ('3-kurs', '3-kurs'), ('2-kurs', '2-kurs')], default='1-kurs', max_length=90),
        ),
        migrations.AlterField(
            model_name='savollar',
            name='kurs_en',
            field=models.CharField(choices=[('4-kurs', '4-kurs'), ('1-kurs', '1-kurs'), ('3-kurs', '3-kurs'), ('2-kurs', '2-kurs')], default='1-kurs', max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='savollar',
            name='kurs_ru',
            field=models.CharField(choices=[('4-kurs', '4-kurs'), ('1-kurs', '1-kurs'), ('3-kurs', '3-kurs'), ('2-kurs', '2-kurs')], default='1-kurs', max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='savollar',
            name='kurs_uz',
            field=models.CharField(choices=[('4-kurs', '4-kurs'), ('1-kurs', '1-kurs'), ('3-kurs', '3-kurs'), ('2-kurs', '2-kurs')], default='1-kurs', max_length=90, null=True),
        ),
    ]
