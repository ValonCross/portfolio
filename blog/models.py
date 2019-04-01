from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=64)
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=2048)
    image = models.ImageField(upload_to='images/')  # Will be stored below the media folder.

    def __str__(self):
        # The row text displayed in the admin tool.
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
