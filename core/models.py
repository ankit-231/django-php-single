from django.db import models
import datetime

# note
# https://docs.djangoproject.com/en/5.0/topics/http/sessions/#extending-database-backed-session-engines
from django.contrib.sessions.base_session import AbstractBaseSession

# Create your models here.

# implementing AbstractBaseSession so that we get full functionality of Django
class Sessions(AbstractBaseSession):
    # mapping django's columns to PHP's Session table's columns
    session_key = models.CharField(db_column='id', unique=True, max_length=255, primary_key=True)
    session_data = models.TextField(db_column='payload')
    # expire_date = models.DateTimeField(db_column='expire', db_index=True)
    # id = models.CharField(unique=True, max_length=255, primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    ip_address = models.CharField(max_length=45, blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    # payload = models.TextField()
    last_activity = models.IntegerField()

    @property
    def expire_date(self):
        unix_epoch_time = self.last_activity
        start_time = datetime.datetime.fromtimestamp(unix_epoch_time)

        # Define the expiry time in minutes
        expiry_minutes = 1440  # 1440 minutes is equivalent to 1 day

        # Calculate the expiry time
        expiry_time = start_time + datetime.timedelta(minutes=expiry_minutes)

        return expiry_time

    class Meta:
        managed = False
        db_table = 'sessions'

class DepartmentHeads(models.Model):
    head_name = models.CharField(max_length=255)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department_heads'



class Departments(models.Model):
    department = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    section_id = models.IntegerField(blank=True, null=True)
    order_column = models.PositiveIntegerField()
    active = models.IntegerField()
    is_emergency = models.IntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_radiology = models.IntegerField()
    head = models.CharField(max_length=255)
    free_followup = models.IntegerField()
    department_type = models.IntegerField()
    room_no = models.IntegerField()
    is_anesthetist = models.IntegerField()
    dep_head = models.ForeignKey(DepartmentHeads, models.DO_NOTHING)
    dep_head_name = models.CharField(max_length=255)
    show_in_admission_flag = models.IntegerField()
    icon = models.TextField(blank=True, null=True)
    dept_name_nepali = models.CharField(max_length=255, blank=True, null=True)
    general_quota = models.IntegerField(blank=True, null=True)
    ehs_quota = models.IntegerField(blank=True, null=True)
    is_online_dept = models.IntegerField()
    account_head_id = models.IntegerField()
    parent_id = models.IntegerField(blank=True, null=True)
    show_in_revenue_report = models.IntegerField()
    account_id = models.PositiveIntegerField(blank=True, null=True)
    cost_center_id = models.PositiveIntegerField(blank=True, null=True)
    enable_sharing_consultant = models.IntegerField()
    enable_sharing_refer_by_consultant = models.IntegerField()
    enable_sharing_service_refer_by_consultant = models.IntegerField()
    max_sharing_percent = models.FloatField()
    department_group = models.IntegerField()
    is_bed_dept = models.IntegerField()
    is_consultant_dept = models.IntegerField()
    is_inventory = models.IntegerField(blank=True, null=True)
    is_lab_dept = models.IntegerField(blank=True, null=True)
    is_procedure = models.IntegerField(blank=True, null=True)
    is_utilization = models.IntegerField(blank=True, null=True)
    show_in_mis_report = models.IntegerField()
    average_service_time = models.IntegerField(blank=True, null=True)
    is_service_appointment = models.IntegerField()
    run_no = models.IntegerField(blank=True, null=True)
    running_date = models.DateField(blank=True, null=True)
    is_main_department = models.IntegerField()
    main_department_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departments'



class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    department = models.ForeignKey(Departments, models.DO_NOTHING, blank=True, null=True)
    doctor_id = models.PositiveIntegerField(blank=True, null=True)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    active = models.CharField(max_length=1)
    change_password = models.IntegerField()
    first_login = models.CharField(max_length=1)
    unidentified_network = models.IntegerField()
    lis_user = models.IntegerField()
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    username = models.CharField(max_length=100)
    is_cashier = models.IntegerField()
    is_watchers = models.IntegerField()
    is_counter = models.IntegerField()
    employee_id = models.PositiveIntegerField()
    agent_id = models.PositiveIntegerField(blank=True, null=True)
    preferred_module = models.PositiveIntegerField(blank=True, null=True)
    is_nurse = models.IntegerField()
    agent_doctor_id = models.TextField(blank=True, null=True)
    enable_report_patient_app = models.IntegerField(blank=True, null=True)
    is_pharmacy_counter = models.IntegerField()
    is_web_user = models.IntegerField()
    pass_field = models.CharField(db_column='pass', max_length=255, blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'users'

