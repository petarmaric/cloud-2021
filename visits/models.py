from django.db import models


class Visit(models.Model):
    visit_time = models.DateTimeField(auto_now_add=True, db_index=True)
    user_browser = models.CharField(max_length=10000)
    user_ip = models.GenericIPAddressField(unpack_ipv4=True, db_index=True)

    class Meta:
        get_latest_by = 'visit_time'
        ordering = ['-visit_time']

    def __str__(self):
        return f"{self.user_ip} visited on {self.visit_time}, via {self.user_browser}"
