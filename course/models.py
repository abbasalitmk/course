from django.db import models

STATUS_CHOICES = [
    ('Enable', 'Enable'),
    ('Disable', 'Disable'),
]


class Course(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.IntegerField()
    status = models.BooleanField(default=True)
    status_text = models.CharField(
        max_length=7,
        choices=STATUS_CHOICES,
        default='Enable'
    )
    image = models.ImageField(upload_to="course/", null=True, blank=True)

    def __str__(self):
        return self.title
