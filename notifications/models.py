from django.db import models

# Create your models here.

colors = [
    ('is-primary', 'Primary'),
    ('is-link', 'Link'),
    ('is-info', 'Info'),
    ('is-success', 'Success'),
    ('is-warning', 'Warning'),
    ('is-danger', 'Danger')
]

class NotificationTemplate(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=20, choices=colors, default='is-primary')

    def __str__(self):
        return self.title

class Notification(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    template = models.ForeignKey(NotificationTemplate, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.template.title

    def get_color(self):
        return self.template.color

    def get_date(self):
        return self.date.strftime("%d.%m.%Y %H:%M")

def create_notification(users, title, content, color):
    template = NotificationTemplate(title=title, content=content, color=color)
    template.save()
    for user in users:
        Notification.objects.create(user=user, template=template)