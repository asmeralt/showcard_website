from django.db import models


class JigsawExample(models.Model):

    class Meta:
        db_table = "jigsaw_example"

    id = models.UUIDField(name="index", primary_key=True, unique=True)
    name = models.CharField("name", max_length=30)
    description = models.TextField(max_length=1000)
