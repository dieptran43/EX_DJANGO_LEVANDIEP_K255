from django.db import models
from Product.models import Product

# Create your models here.
class Customer(models.Model):
    id = models.AutoField(primary_key = True)
    customer_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    status = models.BooleanField()

    def __str__(self):
        return self.customer_name   

    class Meta:
        db_table = "customer"

class Order(models.Model):
    id = models.AutoField(primary_key = True)
    create_date = models.DateField("Ngày hóa đơn")
    customer_id = models.ForeignKey(Customer, on_delete = models.CASCADE)
    order_total_price = models.FloatField("Tổng tiền")
    order_note = models.TextField("Ghi chú")
    httt = models.CharField("HTTT", max_length=100)
    status = models.IntegerField("Trạng thái")

    def __str__(self):
        return self.id   

    class Meta:
        db_table = "order"

class OrderDetail(models.Model):
    type_order = (
        ("Chưa thanh toán", "Chưa thanh toán"),
        ("Đã thanh toán","Đã thanh toán"),
        ("Hủy","Hủy"),
    )
    id = models.AutoField(primary_key = True)
    order_id = models.ForeignKey(Order, verbose_name = "Hóa đơn" ,on_delete = models.CASCADE)
    product_id = models.ForeignKey(Product, verbose_name ="Sản phẩm", on_delete = models.CASCADE)
    price = models.FloatField("Đơn giá")
    discount = models.FloatField("Giảm giá")
    total_price = models.FloatField("Thành tiền")   
    note = models.TextField("Ghi chú")
    status = models.CharField(max_length=100, choices = type_order)

    def __str__(self):
        return self.id  
        
    class Meta:
        db_table = "orderdetail"