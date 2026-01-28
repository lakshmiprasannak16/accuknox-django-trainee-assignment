import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TestModel
from datetime import datetime

@receiver(post_save, sender=TestModel)
def testmodel_post_save(sender, instance, **kwargs):
    print("Signal started at:", datetime.now())
    print("Sleeping for 5 seconds inside signal...")
    time.sleep(5)
    print("Signal finished at:", datetime.now())
