from django.test import TestCase

# Create your tests here.
class Product_Catagory(models.Model):
    Pcid=models.PositiveIntegerField()
    PcName=models.CharField(max_length=100)


    def __str__(self):
        return self.PcName

class Product(models.Model):
    PcName=models.ForeignKey(Product_Catagory,on_delete=models.CASCADE)
    Pname=models.CharField(max_length=100)
    Pid=models.PositiveIntegerField()
    price=models.DecimalField(max_digits=8,decimal_places=2)
    date=models.DateField()

    def __str__(self):
        return self.Pname