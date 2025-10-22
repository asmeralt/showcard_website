import uuid

from django.db import models


class JigsawExampleImage(models.Model):

    class Meta:
        db_table = "jigsaw_example_image"

    id = models.UUIDField(name="index", primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    url = models.URLField(name="url")
    alt_text = models.CharField(name="alt_text", max_length=140)


class JigsawExample(models.Model):

    class Meta:
        db_table = "jigsaw_example"

    id = models.UUIDField(name="index", primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField("name", max_length=30)
    description = models.TextField(max_length=1000)
    images = models.ManyToManyField(to=JigsawExampleImage)
