from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import viewsets
from django_filters import rest_framework as filters
from django.shortcuts import render
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import *
from .serializers import *


class SupplierViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Suppliers to be viewed or edited.

    retrieve:
    Return a supplier instance.

    create:
    Create a supplier instance.

    update:
    Update a supplier instance.

    destroy:
    Delete a supplier instance.

    list:
    Return all supplier.
        Can be ordered by id, name and bin.
        Can be filtered by name and bin
        Can be searched by name and bin
    """

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    filterset_fields = ['name', 'bin']
    search_fields = ['name', 'bin']
    ordering_fields = ['id', 'bin', 'name']
    ordering = ['id']


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    filterset_fields = ['name', 'industry']
    search_fields = ['name', 'full_name', 'location', 'phone_number']
    ordering_fields = ['id', 'name', 'time_create']
    ordering = ['id']


class IndustryViewSet(viewsets.ModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['id', 'name']
    ordering = ['id']


class ContractorViewSet(viewsets.ModelViewSet):
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer
    filterset_fields = ['name', 'bin']
    search_fields = ['name', 'bin', 'address']
    ordering_fields = ['id', 'bin', 'name']
    ordering = ['id']


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ['name']
    search_fields = ['name', 'full_name']
    ordering_fields = ['id', 'name']
    ordering = ['id']


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['id', 'name']
    ordering = ['id']


class ProjectTypeViewSet(viewsets.ModelViewSet):
    queryset = ProjectType.objects.all()
    serializer_class = ProjectTypeSerializer
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['id', 'name']
    ordering = ['id']


class ProjectStatusViewSet(viewsets.ModelViewSet):
    queryset = ProjectStatus.objects.all()
    serializer_class = ProjectStatusSerializer
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['id', 'name']
    ordering = ['id']


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['id', 'name']
    ordering = ['id']


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['id', 'name']
    ordering = ['id']


class ProjectTeamViewSet(viewsets.ModelViewSet):
    queryset = ProjectTeam.objects.all()
    serializer_class = ProjectTeamSerializer
    filterset_fields = ['project', 'member', 'role']
    ordering_fields = ['id', 'project', 'member', 'role']
    ordering = ['id']


class ProjectFilter(filters.FilterSet):

    year = filters.NumberFilter('fact_start_date', lookup_expr='year')

    member = filters.NumberFilter('projectteam__member_id', lookup_expr='exact')

    class Meta:
        model = Project
        fields = [
            'name',
            'client',
            'product',
            'project_type',
            'project_status',
            'is_commercial',
        ]


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filterset_class = ProjectFilter

    search_fields = [
        'name',
        'description',
        'client_department',
    ]
    ordering_fields = ['id', 'name', 'fact_start_date']
    ordering = ['id']


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    filterset_fields = [
        'name',
        'supplier',
        'contractor',
        'project',
        'parent_contract',
        'is_parent',
    ]
    search_fields = ['name']
    ordering_fields = ['id', 'name']
    ordering = ['id']


class LeadFilter(filters.FilterSet):

    year = filters.NumberFilter('start_date', lookup_expr='year')

    class Meta:
        model = Lead
        fields = [
            'name',
            'status',
            'product',
        ]


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    filterset_class = LeadFilter
    search_fields = ['name', 'description', 'comment']
    ordering_fields = ['id', 'name', 'start_date']
    ordering = ['id']


class ProjectStreamStatusViewSet(viewsets.ModelViewSet):
    queryset = ProjectStreamStatus.objects.all()
    serializer_class = ProjectStreamStatusSerializer
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['id', 'name']
    ordering = ['id']


class ProjectStreamViewSet(viewsets.ModelViewSet):
    queryset = ProjectStream.objects.all()
    serializer_class = ProjectStreamSerializer
    filterset_fields = ['name', 'project', 'status']
    search_fields = ['name']
    ordering_fields = ['id', 'name']
    ordering = ['id']


class ProjectReportFilter(filters.FilterSet):

    project_id = filters.NumberFilter('project_stream__project_id', lookup_expr='exact')

    class Meta:
        model = ProjectReport
        fields = [
            'name',
            'category_id',
            'source_name',
            'project_stream',
        ]


class ProjectReportViewSet(viewsets.ModelViewSet):
    queryset = ProjectReport.objects.all()
    serializer_class = ProjectReportSerializer
    filterset_class = ProjectReportFilter
    # filterset_fields = ['name', 'project_stream']
    search_fields = ['name', 'category_id', 'source_name', 'comment', 'description']
    ordering_fields = ['id', 'name']
    ordering = ['id']


class ImpStageViewSet(viewsets.ModelViewSet):
    queryset = ImpStage.objects.all()
    serializer_class = ImpStageSerializer
    filterset_fields = ['name_ru', 'name_en']
    search_fields = ['name_ru', 'name_en']
    ordering_fields = ['id', 'name_ru', 'name_en']
    ordering = ['id']


class ProjectReportImpStageViewSet(viewsets.ModelViewSet):
    queryset = ProjectReportImpStage.objects.all()
    serializer_class = ProjectReportImpStageSerializer
    filterset_fields = ['status_id', 'project_report', 'imp_stage']
    ordering_fields = ['id', 'status_id']
    ordering = ['id']


class ProjectStreamImpStageViewSet(viewsets.ModelViewSet):
    queryset = ProjectStreamImpStage.objects.all()
    serializer_class = ProjectStreamImpStageSerializer
    filterset_fields = ['project_stream', 'imp_stage']
    search_fields = ['name']
    ordering_fields = ['id', 'name']
    ordering = ['id']


class PMStageViewSet(viewsets.ModelViewSet):
    queryset = PMStage.objects.all()
    serializer_class = PMStageSerializer
    filterset_fields = ['name_ru', 'name_en']
    search_fields = ['name_ru', 'name_en']
    ordering_fields = ['id', 'name_ru', 'name_en']
    ordering = ['id']


class PMStepViewSet(viewsets.ModelViewSet):
    queryset = PMStep.objects.all()
    serializer_class = PMStepSerializer
    filterset_fields = ['name_ru', 'name_en']
    search_fields = ['name_ru', 'name_en']
    ordering_fields = ['id', 'name_ru', 'name_en']
    ordering = ['id']


class ProjectPMStepViewSet(viewsets.ModelViewSet):
    queryset = ProjectPMStep.objects.all()
    serializer_class = ProjectPMStepSerializer
    filterset_fields = ['status_id', 'project_pm_stage', 'pm_step']
    ordering_fields = ['id', 'status_id']
    ordering = ['id']


class ProjectPMStageViewSet(viewsets.ModelViewSet):
    queryset = ProjectPMStage.objects.all()
    serializer_class = ProjectPMStageSerializer
    filterset_fields = [
        'project',
        'pm_stage',
        'is_payable',
        'invoice_number',
        'is_invoice_issued',
        'is_invoice_paid',
    ]
    search_fields = ['invoice_number']
    ordering_fields = ['id', 'status_percent', 'pm_stage']
    ordering = ['pm_stage']


class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['id', 'name']
    ordering = ['id']


class LeadSourceViewSet(viewsets.ModelViewSet):
    queryset = LeadSource.objects.all()
    serializer_class = LeadSourceSerializer
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['id', 'name']
    ordering = ['id']


class ReasonViewSet(viewsets.ModelViewSet):
    queryset = Reason.objects.all()
    serializer_class = ReasonSerializer
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['id', 'name']
    ordering = ['id']


class LeadStatusViewSet(viewsets.ModelViewSet):
    queryset = LeadStatus.objects.all()
    serializer_class = LeadStatusSerializer
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['id', 'name']
    ordering = ['id']


class SalesManagerViewSet(viewsets.ModelViewSet):
    queryset = SalesManager.objects.all()
    serializer_class = SalesManagerSerializer
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['id', 'name']
    ordering = ['id']


class LeadStageViewSet(viewsets.ModelViewSet):
    queryset = LeadStage.objects.all()
    serializer_class = LeadStageSerializer
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['id', 'name']
    ordering = ['id']


class CashViewSet(viewsets.ModelViewSet):
    queryset = Cash.objects.all()
    serializer_class = CashSerializer
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['id', 'name']
    ordering = ['id']


class ProjectPaymentViewSet(viewsets.ModelViewSet):
    queryset = ProjectPayment.objects.all()
    serializer_class = ProjectPaymentSerializer
    filterset_fields = [
        'plan_date',
        'fact_date',
        'invoice',
        'plan_amount',
        'fact_amount',
        'project',
        'cash',
    ]
    search_fields = ['invoice']
    ordering_fields = ['id', 'project', 'cash']
    ordering = ['id']


class ProjectFileViewSet(viewsets.ModelViewSet):
    queryset = ProjectFile.objects.all()
    serializer_class = ProjectFileSerializer
    filterset_fields = ['project']
    search_fields = ['description']
    ordering_fields = ['id', 'project']
    ordering = ['id']
