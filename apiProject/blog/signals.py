# signals.py
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Post


@receiver(m2m_changed, sender=Post.likes.through)
def validate_likes(sender, instance, action, pk_set, **kwargs):
    if action == "pre_add":
        existing_dislikes = instance.dislikes.filter(pk__in=pk_set)
        if existing_dislikes.exists():
            instance.dislikes.remove(*existing_dislikes)


@receiver(m2m_changed, sender=Post.dislikes.through)
def validate_dislikes(sender, instance, action, pk_set, **kwargs):
    # Check if users being added to dislikes are already in likes
    if action == "pre_add":
        existing_likes = instance.likes.filter(pk__in=pk_set)
        if existing_likes.exists():
            # Remove users from likes before adding to dislikes
            instance.likes.remove(*existing_likes)
