from django.db import models
from django.contrib.auth.models import User

class CV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_file = models.FileField(upload_to='cv_files/')
    content = models.TextField(blank=True)  # Store the CV contents as text

    def __str__(self):
        return f"{self.user.username}'s CV"
