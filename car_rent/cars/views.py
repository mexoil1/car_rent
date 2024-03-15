from core.views import BaseGetView

from .models import Brand
from .serializers.brief_serializers import BrandBriefSerialzer
from .serializers.model_serializers import BrandSerializer


class BrandView(BaseGetView):
    '''View for brands, only list and retrieve'''
    queryset = Brand.objects.all()
    queryset_brief = Brand.objects.only('title').all()
    serializer_class = BrandSerializer
    serializer_class_brief = BrandBriefSerialzer
