# Generated by Django 2.2 on 2020-01-11 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('status', models.BooleanField()),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_date', models.DateField(verbose_name='Ngày hóa đơn')),
                ('order_total_price', models.FloatField(verbose_name='Tổng tiền')),
                ('order_note', models.TextField(verbose_name='Ghi chú')),
                ('httt', models.CharField(max_length=100, verbose_name='HTTT')),
                ('status', models.IntegerField(verbose_name='Trạng thái')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.Customer')),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.FloatField(verbose_name='Đơn giá')),
                ('discount', models.FloatField(verbose_name='Giảm giá')),
                ('total_price', models.FloatField(verbose_name='Thành tiền')),
                ('note', models.TextField(verbose_name='Ghi chú')),
                ('status', models.CharField(choices=[('Chưa thanh toán', 'Chưa thanh toán'), ('Đã thanh toán', 'Đã thanh toán'), ('Hủy', 'Hủy')], max_length=100)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.Order', verbose_name='Hóa đơn')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.Product', verbose_name='Sản phẩm')),
            ],
            options={
                'db_table': 'orderdetail',
            },
        ),
    ]
