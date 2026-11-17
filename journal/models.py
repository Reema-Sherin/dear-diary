from django.db import models
from django.conf import settings

class DiaryEntry(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    MOOD_CHOICES = [
    ('happy', 'Happy 😊'),
    ('calm', 'Calm 😌'),
    ('sad', 'Sad 🥺'),
    ('anxious', 'Anxious 😰'),
    ('grateful', 'Grateful 🤍'),
    ('tired', 'Tired 😴'),
    ('angry', 'Angry 😡'),
    ('excited', 'Excited 🤩'),
    ('lonely', 'Lonely 😔'),
    ('nostalgic', 'Nostalgic 🥹'),
    ('confused', 'Confused 😕'),
    ('bored', 'Bored 😐'),
    ('motivated', 'Motivated 💪'),
    ('relaxed', 'Relaxed 😎'),
    ('hopeful', 'Hopeful 🌈'),
    ('disappointed', 'Disappointed 😞'),
    ('overwhelmed', 'Overwhelmed 😵‍💫'),
    ('inspired', 'Inspired ✨'),
    ('jealous', 'Jealous 😒'),
    ('content', 'Content 🙂'),]
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES, blank=True, default='')
    def __str__(self):
        return self.title
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='diary_entries',
        null=True,
        blank=True
    )
    image = models.ImageField(
    upload_to='diary_images/',
    blank=True,
    null=True
    )