# Generated by Django 4.0.6 on 2023-08-31 11:35

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set(),
        ),
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
        migrations.CreateModel(
            name='ProductTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shop.product')),
            ],
            options={
                'verbose_name': 'product Translation',
                'db_table': 'shop_product_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shop.category')),
            ],
            options={
                'verbose_name': 'category Translation',
                'db_table': 'shop_category_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
    ]


"""
replace the two occurrences of the following line:
bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
with the following one:
bases=(parler.models.TranslatableModel, models.Model),
This is a fix for a minor issue found in the django-parler version you are using.
This change is necessary to prevent the migration from failing when applying it.
"""

