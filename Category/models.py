from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.AutoField("Mã loại", primary_key= True)
    category_name = models.CharField("Tên Loại", max_length = 100, unique = True)
    category_image = models.ImageField("Hình", upload_to="category_image") 
    #upload_to="category_image" là tên thư mục sẽ upload vào
    status = models.BooleanField(default = True)

    def __str__(self):
        return self.category_name
    
    class Meta:
        db_table ='category'