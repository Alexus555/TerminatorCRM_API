import datetime

from rest_framework import serializers

from .models import *


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('__all__')

    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('__all__')

    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ('__all__')

    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)


class ContractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractor
        fields = ('__all__')

    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')

    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('__all__')

    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)


class ProjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectType
        fields = ('__all__')

    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)


class ProjectStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectStatus
        fields = ('__all__')

    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('__all__')

    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('__all__')

    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)


class ProjectTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTeam
        fields = ('__all__')

    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)

    member_details = serializers.SerializerMethodField()
    role_details = serializers.SerializerMethodField()
    project_details = serializers.SerializerMethodField()

    def get_member_details(self, instance):
        return MemberSerializer(instance.member).data

    def get_role_details(self, instance):
        return RoleSerializer(instance.role).data

    def get_project_details(self, instance):
        return ProjectShortSerializer(instance.project).data


class ProjectShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = [
            'time_create',
            'time_update',
        ]

    client_details = serializers.SerializerMethodField()

    year = serializers.SerializerMethodField()

    def get_client_details(self, instance):
        return ClientSerializer(instance.client, many=False, read_only=True).data

    def get_year(self, instance):
        return instance.fact_start_date.year


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('__all__')

    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)

    current_stage_details = serializers.SerializerMethodField()

    team = serializers.SerializerMethodField()
    client_details = serializers.SerializerMethodField()

    year = serializers.SerializerMethodField()

    def get_current_stage_details(self, instance):

        current_pm_stage = None

        # for projects with subscriptions we use different algorithm
        if instance.sub_amount > 0:
            now = datetime.datetime.now().date()
            fact_end_date = instance.fact_end_date

            if fact_end_date is not None \
                    and fact_end_date <= now:
                current_pm_stage = PMStage.objects.get(stage_descriptor='E')
            else:
                current_pm_stage = PMStage.objects.get(stage_descriptor='P')
        else:
            pm_stages = ProjectPMStage.objects.filter(project=instance)
            current_pm_step = \
                ProjectPMStep.objects.filter(
                    project_pm_stage__in=pm_stages,
                    status_id=False).order_by('pm_step').first()

            if current_pm_step is not None:
                current_pm_stage = current_pm_step.project_pm_stage.pm_stage

        return PMStageSerializer(instance=current_pm_stage, many=False).data

    def get_team(self, instance):
        return ProjectTeamSerializer(instance.projectteam_set, many=True).data

    def get_client_details(self, instance):
        return ClientSerializer(instance.client, many=False, read_only=True).data

    def get_year(self, instance):
        return instance.fact_start_date.year


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ('__all__')

    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('__all__')

    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)


class ProjectStreamStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectStreamStatus
        fields = ('__all__')

    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)


class ProjectStreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectStream
        fields = ('__all__')

    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)

    project_stream_imp_stages = serializers.SerializerMethodField()
    project_reports = serializers.SerializerMethodField()

    status_details = serializers.SerializerMethodField()
    project_details = serializers.SerializerMethodField()

    def get_status_details(self, instance):
        return ProjectStreamStatusSerializer(instance.status).data

    def get_project_details(self, instance):
        return ProjectShortSerializer(instance.project).data

    def get_project_stream_imp_stages(self, instance):
        return ProjectStreamImpStageSerializer(instance.projectstreamimpstage_set, many=True).data

    def get_project_reports(self, instance):
        return ProjectReportSerializer(instance.projectreport_set, many=True).data


class ProjectReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectReport
        fields = ('__all__')

    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)

    project_report_imp_stages = serializers.SerializerMethodField()

    def get_project_report_imp_stages(self, instance):
        return ProjectReportImpStageSerializer(instance.projectreportimpstage_set, many=True).data


class ImpStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImpStage
        fields = ('__all__')

    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)


class ProjectReportImpStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectReportImpStage
        fields = ('__all__')

    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)

    imp_stage_details = serializers.SerializerMethodField()

    def get_imp_stage_details(self, instance):
        return ImpStageSerializer(instance.imp_stage, many=False, read_only=True).data


class ProjectStreamImpStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectStreamImpStage
        fields = ('__all__')

    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)

    imp_stage_details = serializers.SerializerMethodField()

    def get_imp_stage_details(self, instance):
        return ImpStageSerializer(instance.imp_stage, many=False, read_only=True).data


class PMStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PMStage
        fields = ('__all__')

    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)


class PMStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = PMStep
        fields = ('__all__')

    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)


class ProjectPMStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPMStep
        fields = ('__all__')

    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)

    pm_step_details = serializers.SerializerMethodField()

    def get_pm_step_details(self, instance):
        return PMStepSerializer(instance.pm_step, many=False, read_only=True).data


class ProjectPMStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPMStage
        fields = ('__all__')

    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)

    steps = serializers.SerializerMethodField()
    pm_stage_details = serializers.SerializerMethodField()

    def get_steps(self, instance):
        return ProjectPMStepSerializer(instance.projectpmstep_set, many=True).data

    def get_pm_stage_details(self, instance):
        return PMStageSerializer(instance.pm_stage, many=False, read_only=True).data


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ('__all__')

    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)


class LeadSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadSource
        fields = ('__all__')

    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)


class LeadStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadStatus
        fields = ('__all__')

    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)


class ReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reason
        fields = ('__all__')

    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)


class SalesManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesManager
        fields = ('__all__')

    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)


class LeadStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadStage
        fields = ('__all__')

    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)

