from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    bin = models.CharField(max_length=12)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    client_header = models.CharField(max_length=255)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    industry = models.ForeignKey('Industry', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name


class Industry(models.Model):
    name = models.CharField(max_length=255)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Contractor(models.Model):
    name = models.CharField(max_length=255)
    bin = models.CharField(max_length=12)
    address = models.CharField(max_length=255)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    client = models.ForeignKey('Client', on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=3)
    full_name = models.CharField(max_length=255)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    industry = models.ForeignKey('Industry', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProjectType(models.Model):
    name = models.CharField(max_length=255)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProjectStatus(models.Model):
    name = models.CharField(max_length=255)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=255)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=255)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProjectTeam(models.Model):

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    project = models.ForeignKey('Project', on_delete=models.PROTECT, null=False)
    member = models.ForeignKey('Member', on_delete=models.PROTECT, null=False)
    role = models.ForeignKey('Role', on_delete=models.PROTECT, null=False)

    def __str__(self):
        return f'{self.member} ({self.role})'


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    client_department = models.CharField(max_length=255)
    ts_start_date = models.DateField(null=True)
    ts_end_date = models.DateField(null=True)
    rm_start_date = models.DateField(null=True)
    rm_end_date = models.DateField(null=True)
    fact_start_date = models.DateField(null=True)
    fact_end_date = models.DateField(null=True)
    contract_amount = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    net_amount = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    sub_amount = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    sub_months = models.SmallIntegerField(default=0)
    is_commercial = models.BooleanField(default=True)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    client = models.ForeignKey('Client', on_delete=models.PROTECT, null=False)
    product = models.ForeignKey('Product', on_delete=models.PROTECT, null=False)
    project_type = models.ForeignKey('ProjectType', on_delete=models.PROTECT, null=False)
    project_status = models.ForeignKey('ProjectStatus', on_delete=models.PROTECT, null=False)
    lead = models.ForeignKey('Lead', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Contract(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    is_parent = models.BooleanField(default=False)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    supplier = models.ForeignKey('Supplier', on_delete=models.PROTECT, null=False)
    contractor = models.ForeignKey('Contractor', on_delete=models.PROTECT, null=False)
    project = models.ForeignKey('Project', on_delete=models.PROTECT, null=False)
    parent_contract = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Lead(models.Model):
    name = models.CharField(max_length=255)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProjectStreamStatus(models.Model):
    name = models.CharField(max_length=255)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProjectStream(models.Model):
    name = models.CharField(max_length=255)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    project = models.ForeignKey('Project', on_delete=models.PROTECT, null=False)
    status = models.ForeignKey('ProjectStreamStatus', on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.name


class ProjectReport(models.Model):
    name = models.CharField(max_length=255)
    category_id = models.CharField(max_length=255)
    source_name = models.CharField(max_length=255)
    comment = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    image_url = models.URLField()

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    project_stream = models.ForeignKey('ProjectStream', on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.name


class ImpStage(models.Model):
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_ru


class ProjectReportImpStage(models.Model):

    status_id = models.BooleanField(default=False, null=False)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    project_report = models.ForeignKey('ProjectReport', on_delete=models.PROTECT, null=False)
    imp_stage = models.ForeignKey('ImpStage', on_delete=models.PROTECT, null=False)

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

    project_stream = models.ForeignKey('ProjectStream', on_delete=models.PROTECT, null=False)
    imp_stage = models.ForeignKey('ImpStage', on_delete=models.PROTECT, null=False)

    def __str__(self):
        return \
            f'project_stream_id: {self.project_stream} - imp_stage_id: {self.imp_stage}'


class PMStage(models.Model):
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_ru


class PMStep(models.Model):
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_ru


class ProjectPMStep(models.Model):

    status_id = models.BooleanField(default=False, null=False)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    project_pm_stage = models.ForeignKey('PMStage', on_delete=models.PROTECT, null=False)
    pm_step = models.ForeignKey('PMStep', on_delete=models.PROTECT, null=False)

    def __str__(self):
        return \
            f'project_pm_stage_id: {self.project_pm_stage} - pm_step_id: {self.pm_step} - status_id: {self.status_id}'

