from django.shortcuts import render


class CareerViewSet(viewsets.ModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer


class LineCategoryViewSet(viewsets.ModelViewSet):
    queryset = LineCategory.objects.all()
    serializer_class = LineCategorySerializer


class ContractNumberViewSet(viewsets.ModelViewSet):
    queryset = ContractNumber.objects.all()
    serializer_class = ContractNumberSerializer


class ParentNumberViewSet(viewsets.ModelViewSet):
    queryset = ParentNumber.objects.all()
    serializer_class = ParentNumberSerializer
