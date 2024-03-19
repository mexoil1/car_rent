from core.views import BaseGetView

from .filtersets import BrandFilterset, CarModelFilterset
from .models import Brand, CarModel
from .serializers.brief_serializers import (BrandBriefSerialzer,
                                            CarModelBriefSerializer)
from .serializers.model_serializers import BrandSerializer, CarModelSerializer


class BrandView(BaseGetView):
    '''View for brands, only list and retrieve'''
    queryset = Brand.objects.prefetch_related('brand_photo')
    queryset_brief = Brand.objects.only('id', 'title').all()
    serializer_class = BrandSerializer
    serializer_class_brief = BrandBriefSerialzer
    filterset_class = BrandFilterset


class CarModelView(BaseGetView):
    '''View for car models, only list and retrieve'''
    queryset = CarModel.objects.select_related(
        'brand').prefetch_related('carmodel_photo', 'brand__brand_photo')
    queryset_brief = CarModel.objects.only('id', 'title').all()
    serializer_class = CarModelSerializer
    serializer_class_brief = CarModelBriefSerializer
    filterset_class = CarModelFilterset
