from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

@receiver(post_save, sender=Schedule)
def post_save_sched(sender, instance, created, **kwargs):
    print('Saved an instance with type: {}'.format(sender))

@receiver(post_delete, sender=Schedule)
def post_delete_sched(sender, instance, created, **kwargs):
    print('Saved an instance with type: {}'.format(sender))

@receiver(post_save, sender=Sensor)
def post_save_sensor(sender, instance, created, **kwargs):
    print('Saved an instance with type: {}'.format(sender))

@receiver(post_delete, sender=Sensor)
def post_delete_sensor(sender, instance, created, **kwargs):
    print('Saved an instance with type: {}'.format(sender))
    