from django.db import models


class Party(models.Model):
    city = models.CharField(max_length=100)
    party_type = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()
    land_line_number = models.CharField(max_length=15)
    mobile_number = models.CharField(max_length=15)
    gst_no = models.CharField(max_length=20)
    contact_person = models.CharField(max_length=100)

    def __str__(self):
        return self.party_type

    class Meta:
        db_table = "party_master"
