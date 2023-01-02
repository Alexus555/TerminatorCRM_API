from rest_framework import generics
from rest_framework import viewsets
from django.shortcuts import render

from .models import *
from .serializers import *


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class IndustryViewSet(viewsets.ModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer


class ContractorViewSet(viewsets.ModelViewSet):
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProjectTypeViewSet(viewsets.ModelViewSet):
    queryset = ProjectType.objects.all()
    serializer_class = ProjectTypeSerializer


class ProjectStatusViewSet(viewsets.ModelViewSet):
    queryset = ProjectStatus.objects.all()
    serializer_class = ProjectStatusSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class ProjectTeamViewSet(viewsets.ModelViewSet):
    queryset = ProjectTeam.objects.all()
    serializer_class = ProjectTeamSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


class ProjectStreamStatusViewSet(viewsets.ModelViewSet):
    queryset = ProjectStreamStatus.objects.all()
    serializer_class = ProjectStreamStatusSerializer


class ProjectStreamViewSet(viewsets.ModelViewSet):
    queryset = ProjectStream.objects.all()
    serializer_class = ProjectStreamSerializer


class ProjectReportViewSet(viewsets.ModelViewSet):
    queryset = ProjectReport.objects.all()
    serializer_class = ProjectReportSerializer


class ImpStageViewSet(viewsets.ModelViewSet):
    queryset = ImpStage.objects.all()
    serializer_class = ImpStageSerializer


class ProjectReportImpStageViewSet(viewsets.ModelViewSet):
    queryset = ProjectReportImpStage.objects.all()
    serializer_class = ProjectReportImpStageSerializer


class ProjectStreamImpStageViewSet(viewsets.ModelViewSet):
    queryset = ProjectStreamImpStage.objects.all()
    serializer_class = ProjectStreamImpStageSerializer


class PMStageViewSet(viewsets.ModelViewSet):
    queryset = PMStage.objects.all()
    serializer_class = PMStageSerializer


class PMStepViewSet(viewsets.ModelViewSet):
    queryset = PMStep.objects.all()
    serializer_class = PMStepSerializer


class ProjectPMStepViewSet(viewsets.ModelViewSet):
    queryset = ProjectPMStep.objects.all()
    serializer_class = ProjectPMStepSerializer

