from django.db import models

class ImagePrompt(models.Model):
    prompt = models.CharField(max_length=200)

    def __str__(self):
        return self.prompt
