from django.db import models

# Create your models here.
class IllustrationModel(models.Model):
    image = models.FileField(upload_to='images',verbose_name="image",help_text="jpg,png")
    tag = models.PositiveSmallIntegerField(
        choices=((1,"NovelAI"),(2,"DALL.E"),(3,"Stable Diffusion"),(4,"Midjourney"),),
        verbose_name="tag"
    )
    title = models.CharField(max_length=120,verbose_name="Title")
    prompt = models.TextField(verbose_name="Prompt")
    seed = models.CharField(max_length=120,verbose_name="Seed")
    description = models.TextField(verbose_name="Description")

    def __str__(self):
        return self.title


class TextModel(models.Model):
    text = models.TextField(verbose_name="Text")
    tag = models.PositiveSmallIntegerField(
        choices=((1,"NovelAI"),(2,"ChatGPT"),(3,"Jasper"),(4,"Other"),),
        verbose_name="tag"
    )
    title = models.CharField(max_length=120,verbose_name="Title")
    description = models.TextField(verbose_name="Description")

    def __str__(self):
        return self.title


class IllustrationCommentModel(models.Model):
    illustration = models.OneToOneField(IllustrationModel,on_delete=models.CASCADE,verbose_name="Illustration")
    human = models.PositiveSmallIntegerField(default=0,verbose_name="Human")
    ai = models.PositiveSmallIntegerField(default=0,verbose_name="AI")


class TextCommentModel(models.Model):
    text = models.OneToOneField(TextModel,on_delete=models.CASCADE,verbose_name="Text")
    human = models.PositiveSmallIntegerField(default=0,verbose_name="Human")
    ai = models.PositiveSmallIntegerField(default=0,verbose_name="AI")