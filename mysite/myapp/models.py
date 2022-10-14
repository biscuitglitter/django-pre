from django.db import models

class Listing(models.Model):
    STATUS = (
        ("rent", "rent"),
        ("sell", "sell"),
    )
    CATEGORY = (
        ("apartment", "apartment"),
        ("shop", "shop"),
        ("house", "house"),
        ("studio", "studio")
    )
    reference = models.URLField(max_length=200, null=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS)
    category = models.CharField(max_length=20, null=True, choices=CATEGORY)
    city = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if not self.reference:
            return ""
        return str(self.reference)
