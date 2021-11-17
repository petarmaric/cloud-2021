from django.db import models


class Visit(models.Model):
    visit_time = models.DateTimeField(auto_now_add=True)
    user_browser = models.CharField(max_length=10000)
    user_ip = models.GenericIPAddressField(unpack_ipv4=True)
