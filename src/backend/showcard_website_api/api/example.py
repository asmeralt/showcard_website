from rest_framework import routers, serializers, viewsets  # type: ignore[import-untyped]

from showcard_website_api.models.example import JigsawExample, JigsawExampleImage


class JigsawExampleImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = JigsawExampleImage
        fields = ["url", "alt_text"]


# Serializers define the API representation.
class JigsawExampleSerializer(serializers.ModelSerializer):
    images = JigsawExampleImageSerializer(many=True, read_only=True)

    class Meta:
        model = JigsawExample
        fields = ["name", "description", "images"]


# ViewSets define the view behavior.
class JigsawExampleViewSet(viewsets.ModelViewSet):
    queryset = JigsawExample.objects.all()
    serializer_class = JigsawExampleSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"examples", JigsawExampleViewSet)
