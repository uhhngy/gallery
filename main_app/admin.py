from django.contrib import admin
from .models import TextModel
from .models import IllustrationModel
from .models import IllustrationCommentModel
from .models import TextCommentModel

admin.site.register(TextModel)
admin.site.register(IllustrationModel)
admin.site.register(IllustrationCommentModel)
admin.site.register(TextCommentModel)
