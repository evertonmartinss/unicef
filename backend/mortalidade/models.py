from django.db import models

class Country(models.Model):
	class Meta:
		db_table = "country"
	iso_code = models.CharField(max_length=4, primary_key=True)
	country_name = models.CharField(max_length=100)

class Mortality(models.Model):
	class Meta:
		db_table = "mortality"
	iso_code = models.ForeignKey(Country, on_delete=models.CASCADE, db_column='iso_code')
	median = models.TextField(blank=True, null=True) 
	year = models.TextField(blank=True, null=True) 
