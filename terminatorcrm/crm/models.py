from datetime import datetime

from django.db import models, transaction


class Supplier(models.Model):
    name = models.CharField(max_length=255, help_text='Supplier name')
    bin = models.CharField(max_length=12, null=True)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    client_header = models.CharField(max_length=255, null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    industry = models.ForeignKey('Industry', on_delete=models.PROTECT, null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Industry(models.Model):
    name = models.CharField(max_length=255)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Contractor(models.Model):
    name = models.CharField(max_length=255)
    bin = models.CharField(max_length=20, null=True, blank=True)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=4)
    full_name = models.CharField(max_length=255, null=True, blank=True)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    category = models.ForeignKey('ProductCategory', on_delete=models.PROTECT, null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class ProjectType(models.Model):
    name = models.CharField(max_length=255)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class ProjectStatus(models.Model):
    name = models.CharField(max_length=255)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=255)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=255)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class ProjectTeam(models.Model):

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    project = models.ForeignKey('Project', on_delete=models.CASCADE, null=False)
    member = models.ForeignKey('Member', on_delete=models.PROTECT, null=False)
    role = models.ForeignKey('Role', on_delete=models.PROTECT, null=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.member} ({self.role})'


class ProjectManager(models.Manager):

    @transaction.atomic
    def create(self, **data):

        project = Project(**data)
        project.save()

        required_stages = PMStage.objects.filter(required_for_project=True).order_by("pk")
        for stage in required_stages:
            ProjectPMStage.objects.create(project=project, pm_stage=stage)

        return project


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    client_department = models.CharField(max_length=255, null=True, blank=True)
    ts_start_date = models.DateField(null=True)
    ts_end_date = models.DateField(null=True)
    rm_start_date = models.DateField(null=True)
    rm_end_date = models.DateField(null=True)
    fact_start_date = models.DateField(null=True)
    fact_end_date = models.DateField(null=True)
    contract_amount = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    net_amount = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    sub_amount = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    sub_months = models.SmallIntegerField(default=0, null=True)
    is_commercial = models.BooleanField(default=True)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    client = models.ForeignKey('Client', on_delete=models.PROTECT, null=False)
    product = models.ForeignKey('Product', on_delete=models.PROTECT, null=False)
    project_type = models.ForeignKey('ProjectType', on_delete=models.PROTECT, null=False, default=0)
    project_status = models.ForeignKey('ProjectStatus', on_delete=models.PROTECT, null=False, default=0)
    lead = models.ForeignKey('Lead', on_delete=models.SET_NULL, null=True)

    objects = ProjectManager()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

    @property
    def get_year(self):
        year = datetime.now().year
        if self.fact_start_date:
            year = self.fact_start_date.year
        return year


class Contract(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    is_parent = models.BooleanField(default=False)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    supplier = models.ForeignKey('Supplier', on_delete=models.PROTECT, null=False)
    contractor = models.ForeignKey('Contractor', on_delete=models.PROTECT, null=True)
    project = models.ForeignKey('Project', on_delete=models.PROTECT, null=True)
    parent_contract = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class ProjectStreamStatus(models.Model):
    name = models.CharField(max_length=255)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class ProjectStreamManager(models.Manager):

    @transaction.atomic
    def create(self, **data):

        stream = ProjectStream(**data)
        stream.save()

        required_stages = ImpStage.objects.filter(required_for_stream=True).order_by("pk")
        for stage in required_stages:
            ProjectStreamImpStage.objects.create(project_stream=stream, imp_stage=stage)

        return stream


class ProjectStream(models.Model):
    name = models.CharField(max_length=255)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    project = models.ForeignKey('Project', on_delete=models.CASCADE, null=False)
    status = models.ForeignKey('ProjectStreamStatus', on_delete=models.PROTECT, null=False)

    objects = ProjectStreamManager()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


def project_report_file_name(instance, filename):
    return '/'.join(['reports', str(instance.id), filename])


class ProjectReportManager(models.Manager):

    @transaction.atomic
    def create(self, **data):
        report = ProjectReport(**data)
        report.save()

        required_stages = ImpStage.objects.filter(required_for_report=True).order_by("pk")
        for stage in required_stages:
            ProjectReportImpStage.objects.create(project_report=report, imp_stage=stage)

        return report


class ProjectReport(models.Model):
    name = models.CharField(max_length=255)
    category_id = models.CharField(max_length=255, null=True, blank=True)
    source_name = models.CharField(max_length=255, null=True, blank=True)
    comment = models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    image_url = models.ImageField(null=True, upload_to=project_report_file_name, blank=True)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    project_stream = models.ForeignKey('ProjectStream', on_delete=models.CASCADE, null=False)

    objects = ProjectReportManager()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

    @property
    def get_image_url(self):
        if self.image_url and hasattr(self.image_url, 'url'):
            return self.image_url.url


class ImpStage(models.Model):

    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255, null=True, blank=True)
    required_for_stream = models.BooleanField(default=False)
    required_for_report = models.BooleanField(default=False)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name_ru


class ProjectReportImpStage(models.Model):

    status_id = models.BooleanField(default=False, null=False)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    project_report = models.ForeignKey('ProjectReport', on_delete=models.CASCADE, null=False)
    imp_stage = models.ForeignKey('ImpStage', on_delete=models.PROTECT, null=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return \
            f'project_report_id: {self.project_report} - imp_stage_id: {self.imp_stage} - status_id: {self.status_id}'


class ProjectStreamImpStage(models.Model):

    rm_start_date = models.DateField(null=True)
    rm_end_date = models.DateField(null=True)
    fact_start_date = models.DateField(null=True)
    fact_end_date = models.DateField(null=True)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    project_stream = models.ForeignKey('ProjectStream', on_delete=models.CASCADE, null=False)
    imp_stage = models.ForeignKey('ImpStage', on_delete=models.PROTECT, null=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return \
            f'project_stream_id: {self.project_stream} - imp_stage_id: {self.imp_stage}'


class PMStage(models.Model):
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255, null=True)
    required_for_project = models.BooleanField(default=False)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name_ru


class PMStep(models.Model):
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255, null=True, blank=True)

    required_for_stage = models.ForeignKey('PMStage', on_delete=models.SET_NULL, null=True)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name_ru


class ProjectPMStep(models.Model):

    status_id = models.BooleanField(default=False, null=False)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    project_pm_stage = models.ForeignKey('ProjectPMStage', on_delete=models.CASCADE, null=False)
    pm_step = models.ForeignKey('PMStep', on_delete=models.PROTECT, null=False)

    class Meta:
        ordering = ['pm_step']

    def __str__(self):
        return \
            f'project_pm_stage_id: {self.project_pm_stage} - pm_step_id: {self.pm_step} - status_id: {self.status_id}'


class ProjectPMStageManager(models.Manager):

    @transaction.atomic
    def create(self, **data):
        project_pm_stage = ProjectPMStage(**data)
        project_pm_stage.save()

        required_steps = PMStep.objects.filter(required_for_stage=project_pm_stage.pm_stage).order_by("pk")
        for step in required_steps:
            ProjectPMStep.objects.create(project_pm_stage=project_pm_stage, pm_step=step)

        return project_pm_stage


class ProjectPMStage(models.Model):

    # status_percent = models.DecimalField(null=True, max_digits=17, decimal_places=2)
    ts_start_date = models.DateField(null=True, blank=True)
    ts_end_date = models.DateField(null=True, blank=True)
    rm_start_date = models.DateField(null=True, blank=True)
    rm_end_date = models.DateField(null=True, blank=True)
    fact_start_date = models.DateField(null=True, blank=True)
    fact_end_date = models.DateField(null=True, blank=True)
    is_payable = models.BooleanField(default=False, null=True)
    invoice_number = models.CharField(max_length=100, null=True, blank=True)
    share_share = models.DecimalField(null=True, max_digits=17, decimal_places=2)
    is_invoice_issued = models.BooleanField(default=False, null=True)
    is_invoice_paid = models.BooleanField(default=False, null=True)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    project = models.ForeignKey('Project', on_delete=models.CASCADE, null=False)
    pm_stage = models.ForeignKey('PMStage', on_delete=models.PROTECT, null=False)

    objects = ProjectPMStageManager()

    class Meta:
        ordering = ['pm_stage']

    @property
    def get_status_percent(self):
        calc_percent = 0
        processed_steps_count = ProjectPMStep.objects.filter(
            project_pm_stage=self.pk,
            status_id=True).count()
        total_steps_count = ProjectPMStep.objects.filter(
            project_pm_stage=self.pk).count()

        if total_steps_count > 0:
            calc_percent = round(float(processed_steps_count / total_steps_count) * 100, 2)

        return calc_percent

    def __str__(self):
        return \
            f'pm_stage_id: {self.pm_stage} - project_id: {self.project}'


class LeadStage(models.Model):
    name = models.CharField(max_length=255)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class SalesManager(models.Model):
    name = models.CharField(max_length=255)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class LeadStatus(models.Model):
    name = models.CharField(max_length=255)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Reason(models.Model):
    name = models.CharField(max_length=255)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class LeadSource(models.Model):
    name = models.CharField(max_length=255)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Agent(models.Model):
    name = models.CharField(max_length=255)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Lead(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500, null=True, blank=True)
    start_date = models.DateField(null=True)
    proposal_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    price = models.DecimalField(null=True, max_digits=17, decimal_places=2)
    comment = models.CharField(max_length=500, null=True, blank=True)
    comment_date = models.DateTimeField(auto_now=True, null=True)
    lead_contact = models.CharField(max_length=255, null=True, blank=True)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    client = models.ForeignKey('Client', on_delete=models.PROTECT, null=True)
    status = models.ForeignKey('LeadStatus', on_delete=models.PROTECT, null=True)
    current_stage = models.ForeignKey('LeadStage', on_delete=models.PROTECT, null=True)
    reason = models.ForeignKey('Reason', on_delete=models.PROTECT, null=True)
    product = models.ForeignKey('Product', on_delete=models.PROTECT, null=True)
    lead_source = models.ForeignKey('LeadSource', on_delete=models.PROTECT, null=True)
    sales_manager = models.ForeignKey('SalesManager', on_delete=models.PROTECT, null=True)
    agent = models.ForeignKey('Agent', on_delete=models.PROTECT, null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

    @property
    def get_year(self):
        year = datetime.now().year
        if self.start_date:
            year = self.start_date.year
        return year


class Cash(models.Model):
    name = models.CharField(max_length=255)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class ProjectPayment(models.Model):

    plan_date = models.DateField(null=True, blank=True)
    fact_date = models.DateField(null=True, blank=True)
    invoice = models.CharField(max_length=100, null=True, blank=True)
    plan_amount = models.DecimalField(null=True, max_digits=17, decimal_places=2)
    fact_amount = models.DecimalField(null=True, max_digits=17, decimal_places=2)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    project = models.ForeignKey('Project', on_delete=models.CASCADE, null=False)
    cash = models.ForeignKey('Cash', on_delete=models.PROTECT, null=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return \
            f'cash_id: {self.cash} - project_id: {self.project}'


def project_file_name(instance, filename):
    return '/'.join(['projects', str(instance.project), filename])


class ProjectFile(models.Model):
    description = models.CharField(max_length=500)
    file = models.FileField(blank=True, null=True, upload_to=project_file_name)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    project = models.ForeignKey('Project', on_delete=models.CASCADE, null=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.description

    @property
    def get_file_url(self):
        if self.file and hasattr(self.file, 'url'):
            return self.file.url
