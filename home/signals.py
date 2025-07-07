# home/signals.py
from django.contrib.auth.signals import user_logged_in
from django.contrib.messages import get_messages
from django.dispatch import receiver

@receiver(user_logged_in)
def clear_old_messages_on_login(sender, request, user, **kwargs):
    list(get_messages(request))  # flush old messages on login
