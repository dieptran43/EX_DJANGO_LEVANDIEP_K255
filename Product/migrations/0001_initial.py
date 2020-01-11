# Generated by Django 2.2 on 2020-01-11 15:10

import ckeditor_uploader.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=200, unique=True, verbose_name='Tên sản phẩm')),
                ('product_image', models.ImageField(blank=True, upload_to='product_image', verbose_name='Hình sản phẩm')),
                ('size_s', models.FloatField()),
                ('size_m', models.FloatField()),
                ('price', models.FloatField(verbose_name='Đơn giá')),
                ('discount', models.FloatField(verbose_name='Giảm giá')),
                ('description', models.CharField(max_length=200, verbose_name='Tóm tắt')),
                ('description_detail', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Mô tả chi tiết')),
                ('slug', models.SlugField(verbose_name='URL seo')),
                ('stock', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Tồn kho')),
                ('publish_on', models.DateTimeField(blank=True, null=True, verbose_name='Ngày public')),
                ('status', models.BooleanField(default=True, verbose_name='Trạng thái')),
                ('category_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Category.Category', verbose_name='Loại sản phẩm')),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]