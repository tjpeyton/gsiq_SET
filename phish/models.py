from django.db import models

class Client(models.Model):
    company = models.CharField(max_length=200)
    cid = models.IntegerField(default=0)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.company

    def getCampaignId(self):
        return self.cid

    def getCampaignPass(self):
        return self.password
