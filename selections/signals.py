from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Selection

# Register the function as a receiver function
@receiver(m2m_changed, sender=Selection.users_like.through)
def users_like_changed(sender, instance, **kwargs):
  # only call if signal has been launched
  instance.total_likes = instance.users_like.count()
  instance.save()
