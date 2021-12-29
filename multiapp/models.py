from django.db import models

# Create your models here.
class multi_insert_data(models.Model):
	name=models.CharField(max_length=50)
	age=models.IntegerField()
	gender=models.CharField(max_length=50)
	did=models.CharField(primary_key=True,max_length=50)
	course=models.CharField(max_length=50)

	class meta:
		varbose_name='multi_insert_data'
		varbose_name_plural='multi_insert_datas'


	def _str_(self):
		return self.name 

