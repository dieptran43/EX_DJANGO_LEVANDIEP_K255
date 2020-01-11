from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator
from Category.models import Category

# Create your models here.
#ckeditor
from ckeditor_uploader.fields import RichTextUploadingField
import datetime

class Product(models.Model):
    id = models.AutoField(primary_key = True)
    product_name = models.CharField("Tên sản phẩm", max_length = 200, unique=True)
    category_type = models.ForeignKey(Category, on_delete= models.CASCADE, verbose_name = u'Loại sản phẩm')
    product_image = models.ImageField("Hình sản phẩm", upload_to='product_image', blank = True)
    size_s = models.FloatField()
    size_m = models.FloatField()
    price = models.FloatField("Đơn giá")
    discount = models.FloatField("Giảm giá")
    description = models.CharField("Tóm tắt", max_length=200)
    #description = models.TextField("Tóm tắt", max_length=200)
    #description_detail = models.TextField("Mô tả chi tiết")
    description_detail = RichTextUploadingField("Mô tả chi tiết")
    slug = models.SlugField("URL seo")
    stock = models.IntegerField('Tồn kho',validators=[MinValueValidator(0)])
    publish_on = models.DateTimeField("Ngày public",blank=True, null=True)
    status = models.BooleanField("Trạng thái", default = True)

    def __str__(self):
        return self.product_name
    
    def save(self, slug="", *args, **kwargs):
        if not self.publish_on:
            self.publish_on = datetime.datetime.now()
            
        if not self.slug:
            self.slug = slugify(self.product_name)
        return super(Product, self).save(*args, **kwargs)

    class Meta:
        db_table ="product"
    
