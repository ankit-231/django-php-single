# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class 7980AccBillwiseAdjustments(models.Model):
    voucher_no = models.CharField(max_length=191)
    bill_no = models.CharField(max_length=191)
    total_amount = models.FloatField()
    adjustment_amount = models.FloatField()
    balance_amount = models.FloatField()
    tds_amount = models.FloatField()
    vat_amount = models.FloatField()
    discount_amount = models.FloatField()
    purchase_bills_payment_tracker_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    voucher_detail_id = models.IntegerField(blank=True, null=True)
    prov_voucher_no = models.CharField(max_length=191, blank=True, null=True)
    reference_voucher_no = models.CharField(max_length=191, blank=True, null=True)
    debit = models.FloatField()
    credit = models.FloatField()
    account_id = models.PositiveIntegerField()
    is_opening_balance = models.IntegerField()
    period_id = models.PositiveIntegerField()
    company_id = models.PositiveIntegerField()
    account_code = models.CharField(max_length=191, blank=True, null=True)
    status = models.IntegerField(db_comment='0->provisional,1->final')
    vtype = models.CharField(max_length=100)
    is_adj = models.IntegerField(blank=True, null=True)
    revenue_center = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '7980_acc_billwise_adjustments'


class 7980AccBillwiseAdjustmentsProvisional(models.Model):
    final_billwise_adjustment_id = models.PositiveIntegerField(blank=True, null=True)
    provisional_voucher_no = models.CharField(max_length=191, blank=True, null=True)
    bill_no = models.CharField(max_length=191, blank=True, null=True)
    debit = models.FloatField()
    credit = models.FloatField()
    total_amount = models.FloatField()
    adjustment_amount = models.FloatField()
    balance_amount = models.FloatField()
    tds_amount = models.FloatField()
    provisional_voucher_detail_id = models.IntegerField(blank=True, null=True)
    prov_voucher_no = models.CharField(max_length=191, blank=True, null=True)
    reference_voucher_no = models.CharField(max_length=191, blank=True, null=True)
    account_id = models.PositiveIntegerField()
    is_opening_balance = models.IntegerField()
    period_id = models.PositiveIntegerField()
    company_id = models.PositiveIntegerField()
    account_code = models.CharField(max_length=191, blank=True, null=True)
    status = models.IntegerField()
    vtype = models.CharField(max_length=191)
    is_adj = models.IntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    final_voucher_no = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '7980_acc_billwise_adjustments_provisional'


class 7980AccCostCenterTransactions(models.Model):
    cost_center = models.ForeignKey('AccCostCenter', models.DO_NOTHING)
    voucher_detail_id = models.PositiveIntegerField()
    period = models.ForeignKey('AccPeriod', models.DO_NOTHING)
    created_by = models.PositiveIntegerField()
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='updated_by', blank=True, null=True)
    debit_amount = models.FloatField()
    credit_amount = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_opening_balance = models.IntegerField()
    voucher_code = models.CharField(max_length=191, blank=True, null=True)
    account_code = models.CharField(max_length=191, blank=True, null=True)
    account_id = models.PositiveIntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    company_id = models.PositiveIntegerField(blank=True, null=True)
    date_posted = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '7980_acc_cost_center_transactions'


class 7980AccCostCenterTransactionsProvisional(models.Model):
    cost_center = models.ForeignKey('AccCostCenter', models.DO_NOTHING)
    provisional_voucher_detail_id = models.PositiveIntegerField()
    voucher_detail_id = models.PositiveIntegerField()
    debit_amount = models.FloatField()
    credit_amount = models.FloatField()
    date_posted = models.DateTimeField()
    period = models.ForeignKey('AccPeriod', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    is_opening_balance = models.IntegerField()
    provisional_voucher_no = models.CharField(max_length=191, blank=True, null=True)
    voucher_no = models.CharField(max_length=191, blank=True, null=True)
    account_code = models.CharField(max_length=191, blank=True, null=True)
    account = models.ForeignKey('AccAccounts', models.DO_NOTHING)
    status = models.IntegerField(db_comment='Default 0 -> pending, 1->approved')
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '7980_acc_cost_center_transactions_provisional'


class 7980AccVoucherDetails(models.Model):
    move = models.ForeignKey('7980AccVouchers', models.DO_NOTHING)
    journal_id = models.PositiveIntegerField()
    account = models.ForeignKey('AccAccounts', models.DO_NOTHING)
    debit = models.FloatField()
    credit = models.FloatField()
    balance = models.FloatField()
    date_posted = models.DateTimeField(blank=True, null=True)
    reconciled = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    company = models.ForeignKey('Company', models.DO_NOTHING)
    period = models.ForeignKey('AccPeriod', models.DO_NOTHING)
    total_credit_amount = models.FloatField()
    total_debit_amount = models.FloatField()
    description = models.TextField(db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    acc_code = models.CharField(max_length=20, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    is_delete = models.IntegerField()
    customer_id = models.CharField(max_length=191, blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    reconciled_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='reconciled_by', blank=True, null=True)
    reconciled_at = models.DateTimeField(blank=True, null=True)
    reconciliation_remarks = models.CharField(max_length=191, blank=True, null=True)
    tax_type = models.CharField(max_length=191, blank=True, null=True)
    tax_type_percentage = models.FloatField(blank=True, null=True)
    billwise_adjustment_id = models.PositiveIntegerField(blank=True, null=True)
    against_acc_id = models.PositiveIntegerField(blank=True, null=True)
    narration = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '7980_acc_voucher_details'


class 7980AccVoucherDetailsProvisional(models.Model):
    prov = models.ForeignKey('7980AccVouchersProvisional', models.DO_NOTHING)
    journal = models.ForeignKey('AccJournal', models.DO_NOTHING)
    account = models.ForeignKey('AccAccounts', models.DO_NOTHING)
    debit = models.FloatField()
    credit = models.FloatField()
    balance = models.FloatField()
    date_posted = models.DateTimeField(blank=True, null=True)
    reconciled = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    company_id = models.PositiveIntegerField()
    period_id = models.PositiveIntegerField()
    total_credit_amount = models.FloatField()
    total_debit_amount = models.FloatField()
    description = models.CharField(max_length=191, blank=True, null=True)
    acc_code = models.CharField(max_length=20, blank=True, null=True)
    is_delete = models.IntegerField()
    customer_id = models.PositiveIntegerField(blank=True, null=True)
    json_data = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '7980_acc_voucher_details_provisional'


class 7980AccVouchers(models.Model):
    name = models.TextField(blank=True, null=True)
    reference = models.CharField(max_length=191, blank=True, null=True)
    journal_id = models.PositiveIntegerField()
    status = models.IntegerField()
    date_posted = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    period = models.ForeignKey('AccPeriod', models.DO_NOTHING)
    vtype = models.CharField(max_length=3, blank=True, null=True)
    bill_no = models.CharField(max_length=20, blank=True, null=True)
    patient_id = models.IntegerField(blank=True, null=True)
    voucher_no = models.CharField(unique=True, max_length=20, blank=True, null=True)
    invoice_no = models.CharField(max_length=255)
    vendor_bill_date = models.DateField(blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    is_opening_balance_voucher = models.IntegerField()
    is_doctor_share = models.IntegerField(blank=True, null=True)
    provisional_id = models.CharField(max_length=20, blank=True, null=True)
    approved_by = models.PositiveIntegerField(blank=True, null=True)
    approved_on = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    pdc_status = models.IntegerField()
    patient_type = models.CharField(max_length=191, blank=True, null=True)
    cheque_no = models.CharField(max_length=191, blank=True, null=True)
    in_pat_id = models.PositiveIntegerField(blank=True, null=True)
    emergency_pat_id = models.PositiveIntegerField(blank=True, null=True)
    dialysis_pat_id = models.PositiveIntegerField(blank=True, null=True)
    patno = models.CharField(max_length=100, blank=True, null=True)
    is_bulk = models.IntegerField(blank=True, null=True)
    voucher_sub_type = models.CharField(max_length=100, blank=True, null=True)
    manual_invoice_no = models.CharField(max_length=100, blank=True, null=True)
    cheque_date = models.DateField(blank=True, null=True)
    payee_name = models.CharField(max_length=191, blank=True, null=True)
    drawn_on = models.DateField(blank=True, null=True)
    drawn_on_bank = models.PositiveIntegerField(blank=True, null=True)
    vendor_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = '7980_acc_vouchers'


class 7980AccVouchersProvisional(models.Model):
    name = models.CharField(max_length=191)
    reference = models.CharField(max_length=191, blank=True, null=True)
    journal = models.ForeignKey('AccJournal', models.DO_NOTHING)
    status = models.IntegerField()
    date_posted = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    company_id = models.PositiveIntegerField()
    period_id = models.PositiveIntegerField()
    vtype = models.CharField(max_length=3, blank=True, null=True)
    bill_no = models.CharField(max_length=20, blank=True, null=True)
    patient_id = models.IntegerField(blank=True, null=True)
    voucher_no = models.CharField(max_length=20, blank=True, null=True)
    invoice_no = models.IntegerField()
    account_id = models.PositiveIntegerField(blank=True, null=True)
    source = models.CharField(max_length=191, blank=True, null=True)
    is_opening_balance_voucher = models.IntegerField()
    serialdata = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    post_date = models.DateField(blank=True, null=True)
    totalamount = models.FloatField(db_column='totalAmount')  # Field name made lowercase.
    terms_id = models.IntegerField()
    bank_id = models.IntegerField(blank=True, null=True)
    card_no = models.CharField(max_length=191, blank=True, null=True)
    cheque_no = models.CharField(max_length=191, blank=True, null=True)
    files_data = models.TextField(blank=True, null=True)
    pan_no = models.CharField(max_length=191, blank=True, null=True)
    cheque_date = models.DateTimeField(blank=True, null=True)
    drawn_on = models.DateTimeField(blank=True, null=True)
    is_bulk = models.IntegerField()
    approved_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='approved_by', blank=True, null=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', related_name='7980accvouchersprovisional_created_by_set', blank=True, null=True)
    drawn_on_bank = models.PositiveIntegerField(blank=True, null=True)
    final_voucher_no = models.CharField(max_length=191, blank=True, null=True)
    manual_invoice_no = models.CharField(max_length=191, blank=True, null=True)
    payee_name = models.CharField(max_length=191, blank=True, null=True)
    vendor_bill_date = models.DateField(blank=True, null=True)
    voucher_sub_type = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '7980_acc_vouchers_provisional'


class 8081AccBillwiseAdjustments(models.Model):
    voucher_no = models.CharField(max_length=191)
    bill_no = models.CharField(max_length=191)
    total_amount = models.FloatField()
    adjustment_amount = models.FloatField()
    balance_amount = models.FloatField()
    tds_amount = models.FloatField()
    vat_amount = models.FloatField()
    discount_amount = models.FloatField()
    purchase_bills_payment_tracker_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    voucher_detail_id = models.IntegerField(blank=True, null=True)
    prov_voucher_no = models.CharField(max_length=191, blank=True, null=True)
    reference_voucher_no = models.CharField(max_length=191, blank=True, null=True)
    debit = models.FloatField()
    credit = models.FloatField()
    account_id = models.PositiveIntegerField()
    is_opening_balance = models.IntegerField()
    period_id = models.PositiveIntegerField()
    company_id = models.PositiveIntegerField()
    account_code = models.CharField(max_length=191, blank=True, null=True)
    status = models.IntegerField(db_comment='0->provisional,1->final')
    vtype = models.CharField(max_length=100)
    is_adj = models.IntegerField(blank=True, null=True)
    revenue_center = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '8081_acc_billwise_adjustments'


class 8081AccBillwiseAdjustmentsProvisional(models.Model):
    final_billwise_adjustment_id = models.PositiveIntegerField(blank=True, null=True)
    provisional_voucher_no = models.CharField(max_length=191, blank=True, null=True)
    bill_no = models.CharField(max_length=191, blank=True, null=True)
    debit = models.FloatField()
    credit = models.FloatField()
    total_amount = models.FloatField()
    adjustment_amount = models.FloatField()
    balance_amount = models.FloatField()
    tds_amount = models.FloatField()
    provisional_voucher_detail_id = models.IntegerField(blank=True, null=True)
    final_voucher_no = models.CharField(max_length=191, blank=True, null=True)
    reference_voucher_no = models.CharField(max_length=191, blank=True, null=True)
    account_id = models.PositiveIntegerField()
    is_opening_balance = models.IntegerField()
    period_id = models.PositiveIntegerField()
    company_id = models.PositiveIntegerField()
    account_code = models.CharField(max_length=191, blank=True, null=True)
    status = models.IntegerField()
    vtype = models.CharField(max_length=191)
    is_adj = models.IntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '8081_acc_billwise_adjustments_provisional'


class 8081AccCostCenterTransactions(models.Model):
    cost_center = models.ForeignKey('AccCostCenter', models.DO_NOTHING)
    voucher_detail_id = models.PositiveIntegerField()
    period = models.ForeignKey('AccPeriod', models.DO_NOTHING)
    created_by = models.PositiveIntegerField()
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='updated_by', blank=True, null=True)
    debit_amount = models.FloatField()
    credit_amount = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_opening_balance = models.IntegerField()
    voucher_code = models.CharField(max_length=191, blank=True, null=True)
    account_code = models.CharField(max_length=191, blank=True, null=True)
    account_id = models.PositiveIntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    company_id = models.PositiveIntegerField(blank=True, null=True)
    date_posted = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '8081_acc_cost_center_transactions'


class 8081AccCostCenterTransactionsProvisional(models.Model):
    cost_center = models.ForeignKey('AccCostCenter', models.DO_NOTHING)
    provisional_voucher_detail_id = models.PositiveIntegerField()
    voucher_detail_id = models.PositiveIntegerField(blank=True, null=True)
    debit_amount = models.FloatField()
    credit_amount = models.FloatField()
    date_posted = models.DateTimeField()
    period = models.ForeignKey('AccPeriod', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    is_opening_balance = models.IntegerField()
    provisional_voucher_no = models.CharField(max_length=191, blank=True, null=True)
    voucher_no = models.CharField(max_length=191, blank=True, null=True)
    account_code = models.CharField(max_length=191, blank=True, null=True)
    account = models.ForeignKey('AccAccounts', models.DO_NOTHING)
    status = models.IntegerField(db_comment='Default 0 -> pending, 1->approved')
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '8081_acc_cost_center_transactions_provisional'


class 8081AccVoucherDetails(models.Model):
    move = models.ForeignKey('8081AccVouchers', models.DO_NOTHING)
    journal_id = models.PositiveIntegerField()
    account = models.ForeignKey('AccAccounts', models.DO_NOTHING)
    debit = models.FloatField()
    credit = models.FloatField()
    balance = models.FloatField()
    date_posted = models.DateTimeField(blank=True, null=True)
    reconciled = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    company = models.ForeignKey('Company', models.DO_NOTHING)
    period = models.ForeignKey('AccPeriod', models.DO_NOTHING)
    total_credit_amount = models.FloatField()
    total_debit_amount = models.FloatField()
    description = models.TextField(db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    acc_code = models.CharField(max_length=20, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    is_delete = models.IntegerField()
    customer_id = models.CharField(max_length=191, blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    reconciled_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='reconciled_by', blank=True, null=True)
    reconciled_at = models.DateTimeField(blank=True, null=True)
    reconciliation_remarks = models.CharField(max_length=191, blank=True, null=True)
    tax_type = models.CharField(max_length=191, blank=True, null=True)
    tax_type_percentage = models.FloatField(blank=True, null=True)
    billwise_adjustment_id = models.PositiveIntegerField(blank=True, null=True)
    against_acc_id = models.PositiveIntegerField(blank=True, null=True)
    narration = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '8081_acc_voucher_details'


class 8081AccVoucherDetailsProvisional(models.Model):
    prov = models.ForeignKey('8081AccVouchersProvisional', models.DO_NOTHING)
    journal_id = models.PositiveIntegerField()
    account = models.ForeignKey('AccAccounts', models.DO_NOTHING)
    debit = models.FloatField()
    credit = models.FloatField()
    balance = models.FloatField()
    date_posted = models.DateTimeField(blank=True, null=True)
    reconciled = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    company_id = models.PositiveIntegerField()
    period_id = models.PositiveIntegerField()
    total_credit_amount = models.FloatField()
    total_debit_amount = models.FloatField()
    description = models.CharField(max_length=255, blank=True, null=True)
    acc_code = models.CharField(max_length=20, blank=True, null=True)
    is_delete = models.IntegerField()
    customer_id = models.CharField(max_length=191, blank=True, null=True)
    json_data = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '8081_acc_voucher_details_provisional'


class 8081AccVouchers(models.Model):
    name = models.TextField(blank=True, null=True)
    reference = models.CharField(max_length=191, blank=True, null=True)
    journal_id = models.PositiveIntegerField()
    status = models.IntegerField()
    date_posted = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    period = models.ForeignKey('AccPeriod', models.DO_NOTHING)
    vtype = models.CharField(max_length=3, blank=True, null=True)
    bill_no = models.CharField(max_length=20, blank=True, null=True)
    patient_id = models.IntegerField(blank=True, null=True)
    voucher_no = models.CharField(unique=True, max_length=20, blank=True, null=True)
    invoice_no = models.CharField(max_length=255)
    vendor_bill_date = models.DateField(blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    is_opening_balance_voucher = models.IntegerField()
    is_doctor_share = models.IntegerField(blank=True, null=True)
    provisional_id = models.CharField(max_length=20, blank=True, null=True)
    approved_by = models.PositiveIntegerField(blank=True, null=True)
    approved_on = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    pdc_status = models.IntegerField()
    patient_type = models.CharField(max_length=191, blank=True, null=True)
    cheque_no = models.CharField(max_length=191, blank=True, null=True)
    in_pat_id = models.PositiveIntegerField(blank=True, null=True)
    emergency_pat_id = models.PositiveIntegerField(blank=True, null=True)
    dialysis_pat_id = models.PositiveIntegerField(blank=True, null=True)
    patno = models.CharField(max_length=100, blank=True, null=True)
    is_bulk = models.IntegerField(blank=True, null=True)
    voucher_sub_type = models.CharField(max_length=100, blank=True, null=True)
    manual_invoice_no = models.CharField(max_length=100, blank=True, null=True)
    cheque_date = models.DateField(blank=True, null=True)
    payee_name = models.CharField(max_length=191, blank=True, null=True)
    drawn_on = models.DateField(blank=True, null=True)
    drawn_on_bank = models.PositiveIntegerField(blank=True, null=True)
    vendor_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = '8081_acc_vouchers'


class 8081AccVouchersProvisional(models.Model):
    name = models.TextField()
    reference = models.CharField(max_length=191, blank=True, null=True)
    journal_id = models.PositiveIntegerField()
    status = models.IntegerField()
    date_posted = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    company_id = models.PositiveIntegerField()
    period_id = models.PositiveIntegerField()
    vtype = models.CharField(max_length=3, blank=True, null=True)
    bill_no = models.CharField(max_length=20, blank=True, null=True)
    patient_id = models.IntegerField(blank=True, null=True)
    voucher_no = models.CharField(unique=True, max_length=20, blank=True, null=True)
    invoice_no = models.IntegerField()
    vendor_bill_date = models.DateField(blank=True, null=True)
    account_id = models.PositiveIntegerField(blank=True, null=True)
    source = models.CharField(max_length=191, blank=True, null=True)
    is_opening_balance_voucher = models.IntegerField()
    serialdata = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    post_date = models.DateField(blank=True, null=True)
    totalamount = models.FloatField(db_column='totalAmount')  # Field name made lowercase.
    terms_id = models.IntegerField()
    bank_id = models.IntegerField(blank=True, null=True)
    card_no = models.CharField(max_length=191, blank=True, null=True)
    cheque_no = models.CharField(max_length=191, blank=True, null=True)
    files_data = models.TextField(blank=True, null=True)
    cheque_date = models.DateField(blank=True, null=True)
    drawn_on = models.DateField(blank=True, null=True)
    pan_no = models.IntegerField(blank=True, null=True)
    is_bulk = models.IntegerField()
    approved_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='approved_by', blank=True, null=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', related_name='8081accvouchersprovisional_created_by_set', blank=True, null=True)
    voucher_sub_type = models.CharField(max_length=191, blank=True, null=True)
    manual_invoice_no = models.CharField(max_length=191, blank=True, null=True)
    final_voucher_no = models.CharField(max_length=191, blank=True, null=True)
    drawn_on_bank = models.ForeignKey('AccBanks', models.DO_NOTHING, db_column='drawn_on_bank', blank=True, null=True)
    payee_name = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '8081_acc_vouchers_provisional'


class Stbal(models.Model):
    category_id = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    generic_id = models.IntegerField(blank=True, null=True)
    generic_name = models.CharField(max_length=255, blank=True, null=True)
    shortfirm = models.CharField(max_length=255, blank=True, null=True)
    manufacturer_id = models.IntegerField(blank=True, null=True)
    manufacturer = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    catalogue_id = models.IntegerField(blank=True, null=True)
    catalogue = models.CharField(max_length=255, blank=True, null=True)
    unit = models.CharField(max_length=255, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    batch = models.CharField(max_length=255, blank=True, null=True)
    exp_date = models.CharField(max_length=10, blank=True, null=True)
    c_price = models.IntegerField(blank=True, null=True)
    s_price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'STBAL'


class AccAccountDetailTypes(models.Model):
    name = models.CharField(max_length=191)
    account_type = models.ForeignKey('AccAccountTypes', models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField()
    last_updated_by = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    increase_decrease = models.CharField(max_length=2)
    type = models.PositiveIntegerField()
    trx_type = models.PositiveIntegerField(blank=True, null=True)
    class_id = models.PositiveIntegerField()
    sub_class_id = models.PositiveIntegerField(blank=True, null=True)
    is_contra = models.IntegerField(blank=True, null=True)
    schedule_no = models.IntegerField()
    code = models.CharField(max_length=20, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    parent_code = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_account_detail_types'


class AccAccountTypes(models.Model):
    name = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField()
    last_updated_by = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    class_id = models.PositiveIntegerField()
    code = models.CharField(max_length=20, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    is_used = models.IntegerField(db_comment='Filter to show/hide all accounts related to the account types for transactions.')

    class Meta:
        managed = False
        db_table = 'acc_account_types'


class AccAccounts(models.Model):
    name = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    account_type = models.ForeignKey(AccAccountTypes, models.DO_NOTHING)
    account_detail_type_id = models.PositiveIntegerField()
    parent_id = models.PositiveIntegerField()
    balance_as_of = models.FloatField(blank=True, null=True)
    balance_as_of_date = models.DateField(blank=True, null=True)
    original_cost_as_of = models.FloatField(blank=True, null=True)
    original_cost_as_of_date = models.DateField(blank=True, null=True)
    track_depreciation = models.IntegerField()
    created_by = models.PositiveIntegerField()
    last_updated_by = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    company_id = models.PositiveIntegerField()
    is_default = models.IntegerField()
    code = models.CharField(max_length=20, blank=True, null=True)
    tax_type = models.CharField(max_length=191, blank=True, null=True)
    tax_type_percentage = models.FloatField(blank=True, null=True)
    is_cost_center = models.IntegerField(blank=True, null=True)
    order = models.PositiveIntegerField(blank=True, null=True)
    acc_type = models.CharField(max_length=5, blank=True, null=True)
    is_used = models.IntegerField()
    adjust_bill_wise = models.IntegerField(blank=True, null=True)
    show_in_transaction_breakup = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_accounts'


class AccAccountsBalance(models.Model):
    account = models.ForeignKey(AccAccounts, models.DO_NOTHING)
    balance = models.FloatField()
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_accounts_balance'


class AccAttachments(models.Model):
    voucher_no = models.CharField(max_length=191)
    path = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_attachments'


class AccBanks(models.Model):
    name = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_banks'


class AccBillDetails(models.Model):
    bill_id = models.PositiveIntegerField()
    account_id = models.PositiveIntegerField()
    product_id = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    discount_amount = models.FloatField(blank=True, null=True)
    tax_amount = models.FloatField()
    total = models.FloatField()
    journal_id = models.IntegerField()
    period_id = models.IntegerField()
    company_id = models.IntegerField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    expense_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_bill_details'


class AccBillDocs(models.Model):
    bill_id = models.IntegerField()
    original_name = models.CharField(max_length=191)
    file_url = models.CharField(max_length=191)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_bill_docs'


class AccBills(models.Model):
    bill_number = models.CharField(max_length=191)
    order_number = models.CharField(max_length=191, blank=True, null=True)
    bill_status = models.IntegerField()
    vendor_id = models.IntegerField()
    mailing_address = models.CharField(max_length=191, blank=True, null=True)
    term_id = models.IntegerField()
    bill_date = models.DateField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    amount = models.FloatField()
    discount = models.FloatField()
    tax_amount = models.FloatField()
    total = models.FloatField()
    note = models.CharField(max_length=191, blank=True, null=True)
    period_id = models.IntegerField()
    company_id = models.IntegerField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    payment_method_id = models.IntegerField(blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    ref_no = models.CharField(max_length=191, blank=True, null=True)
    permit_no = models.CharField(max_length=191, blank=True, null=True)
    bill_type = models.CharField(max_length=191, blank=True, null=True)
    check_no = models.CharField(max_length=191, blank=True, null=True)
    print_later = models.IntegerField()
    shipping_customer_id = models.IntegerField(blank=True, null=True)
    shipping_address = models.CharField(max_length=191, blank=True, null=True)
    shipping_via = models.CharField(max_length=191, blank=True, null=True)
    email = models.CharField(max_length=191, blank=True, null=True)
    journal_id = models.IntegerField(blank=True, null=True)
    tds_amount = models.FloatField()
    tds_payment_flag = models.IntegerField()
    vat_payment_flag = models.IntegerField()
    payee_account_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    voucher_no = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_bills'


class AccBillwiseAdjustments(models.Model):
    voucher_no = models.CharField(max_length=191)
    bill_no = models.CharField(max_length=191)
    total_amount = models.FloatField()
    adjustment_amount = models.FloatField()
    balance_amount = models.FloatField()
    tds_amount = models.FloatField()
    vat_amount = models.FloatField()
    discount_amount = models.FloatField()
    purchase_bills_payment_tracker_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    voucher_detail_id = models.IntegerField(blank=True, null=True)
    prov_voucher_no = models.CharField(max_length=191, blank=True, null=True)
    reference_voucher_no = models.CharField(max_length=191, blank=True, null=True)
    debit = models.FloatField()
    credit = models.FloatField()
    account_id = models.PositiveIntegerField()
    is_opening_balance = models.IntegerField()
    period_id = models.PositiveIntegerField()
    company_id = models.PositiveIntegerField()
    account_code = models.CharField(max_length=191, blank=True, null=True)
    status = models.IntegerField(db_comment='0->provisional,1->final')

    class Meta:
        managed = False
        db_table = 'acc_billwise_adjustments'


class AccBillwiseAdjustmentsProvisional(models.Model):
    final_billwise_adjustment_id = models.PositiveIntegerField(blank=True, null=True)
    provisional_voucher_no = models.CharField(max_length=191, blank=True, null=True)
    bill_no = models.CharField(max_length=191, blank=True, null=True)
    debit = models.FloatField()
    credit = models.FloatField()
    total_amount = models.FloatField()
    adjustment_amount = models.FloatField()
    balance_amount = models.FloatField()
    tds_amount = models.FloatField()
    provisional_voucher_detail_id = models.IntegerField(blank=True, null=True)
    prov_voucher_no = models.CharField(max_length=191, blank=True, null=True)
    reference_voucher_no = models.CharField(max_length=191, blank=True, null=True)
    account_id = models.PositiveIntegerField()
    is_opening_balance = models.IntegerField()
    period_id = models.PositiveIntegerField()
    company_id = models.PositiveIntegerField()
    account_code = models.CharField(max_length=191, blank=True, null=True)
    status = models.IntegerField()
    vtype = models.CharField(max_length=191)
    is_adj = models.IntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_billwise_adjustments_provisional'


class AccBranchInfo(models.Model):
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company_name = models.CharField(max_length=191)
    email = models.CharField(max_length=191, blank=True, null=True)
    phone_no = models.CharField(max_length=191, blank=True, null=True)
    mobile_no = models.CharField(max_length=191, blank=True, null=True)
    fax = models.CharField(max_length=191, blank=True, null=True)
    short_name = models.CharField(max_length=191, blank=True, null=True)
    website = models.CharField(max_length=191, blank=True, null=True)
    address = models.CharField(max_length=191)
    vat_no = models.CharField(max_length=191, blank=True, null=True)
    pan_no = models.CharField(max_length=191, blank=True, null=True)
    branch_logo = models.CharField(max_length=191, blank=True, null=True)
    is_active = models.IntegerField()
    accounting_method = models.IntegerField()
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_branch_info'


class AccChequePrintTemplates(models.Model):
    title = models.CharField(max_length=191)
    default_fontsize = models.IntegerField()
    date_format = models.CharField(max_length=191)
    font_name = models.CharField(max_length=191)
    payee_header_text = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_cheque_print_templates'


class AccClass(models.Model):
    class_field = models.CharField(db_column='class', max_length=191)  # Field renamed because it was a Python reserved word.
    debit = models.CharField(max_length=191)
    credit = models.CharField(max_length=191)
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_class'


class AccCostCenter(models.Model):
    code = models.CharField(unique=True, max_length=15)
    name = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField()
    last_updated_by = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=3)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_cost_center'


class AccCostCenterTransactions(models.Model):
    cost_center = models.ForeignKey(AccCostCenter, models.DO_NOTHING)
    voucher_detail = models.ForeignKey('AccVoucherDetails', models.DO_NOTHING)
    period = models.ForeignKey('AccPeriod', models.DO_NOTHING)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by')
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='updated_by', related_name='acccostcentertransactions_updated_by_set', blank=True, null=True)
    debit_amount = models.FloatField()
    credit_amount = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    company_id = models.PositiveIntegerField(blank=True, null=True)
    date_posted = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'acc_cost_center_transactions'


class AccCostCenterTransactionsProvisional(models.Model):
    cost_center = models.ForeignKey(AccCostCenter, models.DO_NOTHING)
    provisional_voucher_detail_id = models.PositiveIntegerField()
    voucher_detail_id = models.PositiveIntegerField()
    debit_amount = models.FloatField()
    credit_amount = models.FloatField()
    date_posted = models.DateTimeField()
    period = models.ForeignKey('AccPeriod', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    is_opening_balance = models.IntegerField()
    provisional_voucher_no = models.CharField(max_length=191, blank=True, null=True)
    voucher_no = models.CharField(max_length=191, blank=True, null=True)
    account_code = models.CharField(max_length=191, blank=True, null=True)
    account = models.ForeignKey(AccAccounts, models.DO_NOTHING)
    status = models.IntegerField(db_comment='Default 0 -> pending, 1->approved')
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_cost_center_transactions_provisional'


class AccCustomerTypes(models.Model):
    name = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_customer_types'


class AccEstimate(models.Model):
    estimate_no = models.CharField(max_length=191)
    customer_id = models.PositiveIntegerField()
    customer_name = models.CharField(max_length=191)
    customer_email = models.CharField(max_length=191, blank=True, null=True)
    billing_address = models.CharField(max_length=191)
    estimate_date = models.DateField()
    expiration_date = models.DateField(blank=True, null=True)
    location_of_sales = models.CharField(max_length=191, blank=True, null=True)
    shipping_address = models.CharField(max_length=191, blank=True, null=True)
    shipping_via = models.CharField(max_length=191, blank=True, null=True)
    shipping_date = models.DateField(blank=True, null=True)
    shipping_amount = models.FloatField(blank=True, null=True)
    shipping_tax = models.IntegerField(blank=True, null=True)
    tracking_no = models.CharField(max_length=191, blank=True, null=True)
    remarks = models.CharField(max_length=191, blank=True, null=True)
    status = models.IntegerField()
    discount_percent = models.IntegerField()
    tax_percent = models.IntegerField()
    tax_amount = models.FloatField()
    amt_wo_tax = models.FloatField()
    amt_w_tax = models.FloatField()
    amt_bd = models.FloatField()
    amt_ad = models.FloatField()
    discount_amount = models.FloatField()
    master_total = models.FloatField()
    company_id = models.IntegerField()
    period_id = models.IntegerField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_estimate'


class AccEstimateDetails(models.Model):
    estimate_id = models.PositiveIntegerField()
    product_id = models.PositiveIntegerField()
    product_name = models.CharField(max_length=191)
    description = models.TextField()
    qtantity = models.PositiveIntegerField()
    tax_percent = models.IntegerField()
    discount_percent = models.IntegerField()
    tax_amount = models.FloatField()
    amt_wo_tax = models.FloatField()
    amt_w_tax = models.FloatField()
    amt_bd = models.FloatField()
    amt_ad = models.FloatField()
    discount_amount = models.FloatField()
    rate = models.FloatField()
    is_bundle = models.IntegerField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_estimate_details'


class AccEventLogs(models.Model):
    name = models.CharField(max_length=191)
    remarks = models.TextField()
    ip_address = models.CharField(max_length=191, blank=True, null=True)
    old_value = models.TextField(blank=True, null=True)
    new_value = models.TextField(blank=True, null=True)
    company_id = models.PositiveIntegerField()
    period_id = models.PositiveIntegerField()
    type = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_event_logs'


class AccFiscalYear(models.Model):
    name = models.CharField(max_length=191)
    date_fr = models.DateField()
    date_to = models.DateField()
    nepali_fr = models.CharField(max_length=191, blank=True, null=True)
    nepali_to = models.CharField(max_length=191, blank=True, null=True)
    short_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_fiscal_year'


class AccInventoryAssets(models.Model):
    inventory_asset = models.CharField(max_length=191)
    status = models.PositiveIntegerField()
    created_by = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_inventory_assets'


class AccInvoiceDocs(models.Model):
    invoice_id = models.IntegerField()
    original_name = models.CharField(max_length=191)
    file_url = models.CharField(max_length=191)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_invoice_docs'


class AccJournal(models.Model):
    type = models.PositiveIntegerField()
    memo = models.CharField(max_length=191, blank=True, null=True)
    default_credit_account_id = models.PositiveIntegerField()
    default_debit_account_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    company_id = models.PositiveIntegerField()
    period_id = models.PositiveIntegerField()
    account_date = models.DateField(blank=True, null=True)
    account_head_id = models.IntegerField(blank=True, null=True)
    journal_number = models.CharField(max_length=191, blank=True, null=True)
    reference_no = models.CharField(max_length=191, blank=True, null=True)
    verfiy_status = models.IntegerField()
    ledger_id = models.IntegerField()
    patient_ledger_id = models.IntegerField()
    master_bill_id = models.IntegerField()
    refund_status = models.IntegerField()
    purchase_id = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_journal'


class AccMasterStockIssues(models.Model):
    master_stock_issues_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    msi_opening_stocks_id = models.PositiveIntegerField()
    msi_closing_stocks_id = models.PositiveIntegerField()
    received_from_store = models.PositiveIntegerField(blank=True, null=True)
    stock_issues_remarks = models.TextField(blank=True, null=True)
    stock_issue_no = models.CharField(max_length=191)
    master_stock_issue_cancel_status = models.IntegerField()
    master_stock_issues_created_by = models.PositiveIntegerField()
    master_stock_issues_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_master_stock_issues'


class AccMoveLineBak(models.Model):
    id = models.PositiveIntegerField()
    move_id = models.PositiveIntegerField()
    journal_id = models.PositiveIntegerField()
    account_id = models.PositiveIntegerField()
    debit = models.FloatField()
    credit = models.FloatField()
    balance = models.FloatField()
    date_posted = models.DateTimeField(blank=True, null=True)
    reconciled = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    company_id = models.PositiveIntegerField()
    period_id = models.PositiveIntegerField()
    total_credit_amount = models.FloatField()
    total_debit_amount = models.FloatField()
    description = models.CharField(max_length=255, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    acc_code = models.CharField(max_length=20, db_collation='utf8mb4_unicode_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_move_line_bak'


class AccPartnerDocs(models.Model):
    partner_id = models.IntegerField()
    original_name = models.CharField(max_length=191)
    file_url = models.CharField(max_length=191)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_partner_docs'


class AccPartners(models.Model):
    company = models.CharField(max_length=191)
    title = models.CharField(max_length=191, blank=True, null=True)
    first_name = models.CharField(max_length=191, blank=True, null=True)
    middle_name = models.CharField(max_length=191, blank=True, null=True)
    last_name = models.CharField(max_length=191, blank=True, null=True)
    display_name = models.CharField(max_length=191)
    company_id = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=191, blank=True, null=True)
    phone_no = models.CharField(max_length=191, blank=True, null=True)
    mobile_no = models.CharField(max_length=191, blank=True, null=True)
    fax = models.CharField(max_length=191, blank=True, null=True)
    others = models.CharField(max_length=191, blank=True, null=True)
    website = models.CharField(max_length=191, blank=True, null=True)
    parent_customer_id = models.IntegerField()
    address_street = models.CharField(max_length=191, blank=True, null=True)
    address_city_town = models.CharField(max_length=191, blank=True, null=True)
    address_state_provence = models.CharField(max_length=191, blank=True, null=True)
    address_country = models.CharField(max_length=191, blank=True, null=True)
    billing_shipping_address_status = models.CharField(max_length=191, blank=True, null=True)
    shipping_address_street = models.CharField(max_length=191, blank=True, null=True)
    shipping_address_city_town = models.CharField(max_length=191, blank=True, null=True)
    shipping_address_state_provence = models.CharField(max_length=191, blank=True, null=True)
    shipping_address_country = models.CharField(max_length=191, blank=True, null=True)
    tax_exempt_status = models.IntegerField()
    payment_method_id = models.IntegerField()
    term_id = models.IntegerField()
    customer_type_id = models.IntegerField()
    account_no = models.CharField(max_length=191, blank=True, null=True)
    notes = models.CharField(max_length=191, blank=True, null=True)
    partner_type = models.IntegerField()
    created_by = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    pan_no = models.IntegerField(blank=True, null=True)
    account_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_partners'


class AccPaymentMethods(models.Model):
    name = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_payment_methods'


class AccPeriod(models.Model):
    fiscal_year = models.ForeignKey(AccFiscalYear, models.DO_NOTHING)
    status = models.IntegerField()
    company_id = models.PositiveIntegerField()
    is_closed = models.IntegerField()
    book_type = models.IntegerField()
    is_active = models.IntegerField()
    allow_backdate_entry_from_account = models.IntegerField()
    allow_backdate_entry_from_dolphin = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'acc_period'


class AccPermissionRole(models.Model):
    permission_id = models.PositiveIntegerField()
    role_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'acc_permission_role'


class AccPermissionUser(models.Model):
    permission_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'acc_permission_user'


class AccPermissions(models.Model):
    name = models.CharField(unique=True, max_length=191)
    display_name = models.CharField(max_length=191, blank=True, null=True)
    description = models.CharField(max_length=191, blank=True, null=True)
    category = models.CharField(max_length=191, blank=True, null=True)
    is_parent = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_permissions'


class AccPivotBillJournal(models.Model):
    bill_id = models.PositiveIntegerField()
    journal_id = models.PositiveIntegerField()
    payment_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_pivot_bill_journal'


class AccPivotInvoiceJournal(models.Model):
    invoice_id = models.PositiveIntegerField()
    journal_id = models.PositiveIntegerField()
    payment_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_pivot_invoice_journal'


class AccPivotProductServices(models.Model):
    bundle_id = models.PositiveIntegerField()
    product_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'acc_pivot_product_services'


class AccProductAndServiceTypes(models.Model):
    type = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_product_and_service_types'


class AccProductAndServices(models.Model):
    product_type = models.PositiveIntegerField()
    name = models.CharField(max_length=191)
    sku = models.CharField(max_length=191, blank=True, null=True)
    category_id = models.PositiveIntegerField(blank=True, null=True)
    qty_on_hand = models.PositiveIntegerField(blank=True, null=True)
    as_of_date = models.CharField(max_length=191, blank=True, null=True)
    reorder_point = models.PositiveIntegerField(blank=True, null=True)
    inventory_asset_id = models.PositiveIntegerField(blank=True, null=True)
    sales_price = models.FloatField()
    cost_price = models.FloatField()
    income_account_id = models.PositiveIntegerField(blank=True, null=True)
    is_taxable = models.IntegerField()
    tax_category_id = models.PositiveIntegerField(blank=True, null=True)
    item_id = models.PositiveIntegerField(blank=True, null=True)
    expenses_account_id = models.PositiveIntegerField(blank=True, null=True)
    vendor_id = models.PositiveIntegerField(blank=True, null=True)
    is_purchase = models.IntegerField()
    is_sales = models.IntegerField()
    is_bundle = models.IntegerField()
    image = models.TextField(blank=True, null=True)
    sales_info = models.TextField(blank=True, null=True)
    purchase_info = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    company_id = models.PositiveIntegerField()
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    tax_percent = models.FloatField()

    class Meta:
        managed = False
        db_table = 'acc_product_and_services'


class AccProductCategories(models.Model):
    category = models.CharField(max_length=191)
    status = models.PositiveIntegerField()
    created_by = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_product_categories'


class AccPurchaseBillPaymentTrackers(models.Model):
    bill_id = models.PositiveIntegerField()
    vendor_id = models.PositiveIntegerField()
    payment_date = models.DateField()
    payment_amount = models.FloatField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    voucher_no = models.CharField(max_length=20, blank=True, null=True)
    cheque_no = models.CharField(max_length=20, blank=True, null=True)
    cheque_date = models.DateField(blank=True, null=True)
    drawn_on = models.DateField(blank=True, null=True)
    drawn_on_bank = models.PositiveIntegerField(blank=True, null=True)
    payee_name = models.CharField(max_length=191, blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'acc_purchase_bill_payment_trackers'


class AccReportSignature(models.Model):
    company_id = models.PositiveIntegerField(blank=True, null=True)
    period_id = models.PositiveIntegerField(blank=True, null=True)
    name = models.CharField(max_length=191, blank=True, null=True)
    designation = models.CharField(max_length=191, blank=True, null=True)
    signature = models.TextField(blank=True, null=True)
    report_type = models.IntegerField(blank=True, null=True)
    alignment = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_report_signature'


class AccRequisition(models.Model):
    branch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    requisition_no = models.CharField(max_length=191)
    period_id = models.CharField(max_length=191, blank=True, null=True)
    requisition_date = models.DateField(blank=True, null=True)
    requester = models.CharField(max_length=191)
    status = models.IntegerField()
    remarks = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_requisition'


class AccRequisitionDetail(models.Model):
    branch_id = models.PositiveIntegerField()
    requisition_id = models.PositiveIntegerField()
    catalogue_id = models.PositiveIntegerField()
    quantity = models.IntegerField()
    status = models.IntegerField()
    pacs_size = models.IntegerField()
    reorder_level = models.IntegerField()
    remarks = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_requisition_detail'


class AccRoleUser(models.Model):
    role_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    user_type = models.CharField(max_length=191)
    company_id = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'acc_role_user'


class AccRoles(models.Model):
    name = models.CharField(unique=True, max_length=191)
    display_name = models.CharField(max_length=191, blank=True, null=True)
    description = models.CharField(max_length=191, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_roles'


class AccSalesInvoiceBundleDetails(models.Model):
    sales_invoice_detail_id = models.PositiveIntegerField()
    product_id = models.PositiveIntegerField()
    product_name = models.CharField(max_length=191)
    description = models.TextField()
    qtantity = models.PositiveIntegerField()
    refund_status = models.PositiveIntegerField()
    service_date = models.DateField()
    tax_percent = models.IntegerField()
    discount_percent = models.IntegerField()
    tax_amount = models.FloatField()
    amt_wo_tax = models.FloatField()
    amt_w_tax = models.FloatField()
    amt_bd = models.FloatField()
    amt_ad = models.FloatField()
    discount_amount = models.FloatField()
    rate = models.FloatField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_sales_invoice_bundle_details'


class AccSalesInvoiceDocs(models.Model):
    sales_invoice_master_id = models.IntegerField()
    original_name = models.CharField(max_length=191)
    file_url = models.CharField(max_length=191)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_sales_invoice_docs'


class AccSalesInvoiceMaster(models.Model):
    invoice_no = models.CharField(max_length=191)
    customer_id = models.PositiveIntegerField()
    customer_name = models.CharField(max_length=191)
    customer_email = models.CharField(max_length=191, blank=True, null=True)
    invoice_type = models.IntegerField()
    payment_type = models.IntegerField()
    terms_id = models.IntegerField()
    billing_address = models.CharField(max_length=191)
    invoice_date = models.DateField()
    due_date = models.DateField(blank=True, null=True)
    shipping_address = models.CharField(max_length=191, blank=True, null=True)
    shipping_via = models.CharField(max_length=191, blank=True, null=True)
    shipping_date = models.DateField(blank=True, null=True)
    shipping_amount = models.IntegerField(blank=True, null=True)
    shipping_tax = models.IntegerField(blank=True, null=True)
    tracking_no = models.CharField(max_length=191, blank=True, null=True)
    location_of_sales = models.CharField(max_length=191, blank=True, null=True)
    remarks = models.CharField(max_length=191, blank=True, null=True)
    refund_status = models.IntegerField()
    master_refund_id = models.IntegerField(blank=True, null=True)
    credit_status = models.IntegerField()
    cancel_status = models.IntegerField()
    discount_percent = models.IntegerField()
    tax_percent = models.IntegerField()
    tender_amt = models.FloatField()
    tax_amount = models.FloatField()
    amt_wo_tax = models.FloatField()
    amt_w_tax = models.FloatField()
    amt_bd = models.FloatField()
    amt_ad = models.FloatField()
    discount_amount = models.FloatField()
    master_total = models.FloatField()
    received_amt = models.FloatField()
    due_amount = models.FloatField()
    bank_id = models.IntegerField(blank=True, null=True)
    card_no = models.CharField(max_length=191, blank=True, null=True)
    cheque_no = models.CharField(max_length=191, blank=True, null=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    company_id = models.PositiveIntegerField()
    period_id = models.PositiveIntegerField()
    journal_id = models.PositiveIntegerField()
    account_id = models.IntegerField(blank=True, null=True)
    receipt_date = models.CharField(max_length=191, blank=True, null=True)
    prpa = models.CharField(max_length=191, blank=True, null=True)
    reference_no = models.CharField(max_length=191, blank=True, null=True)
    sale_type = models.CharField(max_length=191, blank=True, null=True)
    credit_memo_date = models.CharField(max_length=191, blank=True, null=True)
    estimate_date = models.CharField(max_length=191, blank=True, null=True)
    expiration_date = models.CharField(max_length=191, blank=True, null=True)
    tds_amount = models.FloatField()
    tds_payment_flag = models.IntegerField()
    vat_payment_flag = models.IntegerField()
    receivable_account_id = models.IntegerField(blank=True, null=True)
    reference = models.ForeignKey('MasterBills', models.DO_NOTHING, db_column='reference', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_sales_invoice_master'


class AccSalesInvoiceMasterDetails(models.Model):
    sales_invoice_master_id = models.PositiveIntegerField()
    product_id = models.PositiveIntegerField()
    product_type_id = models.PositiveIntegerField()
    product_name = models.CharField(max_length=191)
    product_type_name = models.CharField(max_length=191)
    description = models.TextField()
    qtantity = models.PositiveIntegerField()
    refund_status = models.PositiveIntegerField()
    service_date = models.DateField()
    tax_percent = models.IntegerField()
    discount_percent = models.IntegerField()
    tax_amount = models.FloatField()
    amt_wo_tax = models.FloatField()
    amt_w_tax = models.FloatField()
    amt_bd = models.FloatField()
    amt_ad = models.FloatField()
    discount_amount = models.FloatField()
    rate = models.FloatField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_bundle = models.PositiveIntegerField()
    account_id = models.IntegerField(blank=True, null=True)
    sales_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_sales_invoice_master_details'


class AccSalesInvoicePayments(models.Model):
    sales_invoice_master_id = models.PositiveIntegerField()
    customer_id = models.PositiveIntegerField()
    payment_type = models.PositiveIntegerField()
    payment_date = models.DateField()
    amount = models.FloatField()
    refund_status = models.IntegerField()
    status = models.IntegerField()
    remarks = models.TextField(blank=True, null=True)
    reference_no = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    voucher_no = models.CharField(max_length=20, blank=True, null=True)
    cheque_no = models.CharField(max_length=255, blank=True, null=True)
    cheque_date = models.CharField(max_length=255, blank=True, null=True)
    drawn_on = models.CharField(max_length=255, blank=True, null=True)
    drawn_on_bank = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_sales_invoice_payments'


class AccStockIssues(models.Model):
    stock_issue_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    master_stock_issues_id = models.PositiveIntegerField()
    stock_issue_no = models.CharField(max_length=191)
    master_stock_purchases_id = models.PositiveIntegerField()
    stock_purchases_id = models.PositiveIntegerField()
    stock_purchases_no = models.CharField(max_length=191)
    si_opening_stocks_id = models.PositiveIntegerField()
    si_closing_stocks_id = models.PositiveIntegerField()
    catalogue_id = models.PositiveIntegerField()
    catalogue_type_id = models.PositiveIntegerField(blank=True, null=True)
    master_returns_id = models.PositiveIntegerField(blank=True, null=True)
    returns_no = models.CharField(max_length=191, blank=True, null=True)
    store_id = models.PositiveIntegerField(blank=True, null=True)
    received_from_store = models.PositiveIntegerField(blank=True, null=True)
    batch = models.CharField(max_length=191, blank=True, null=True)
    i_quantity = models.FloatField()
    i_stock_quantity = models.FloatField()
    i_revert_quantity = models.FloatField()
    expiry_date = models.CharField(max_length=191, blank=True, null=True)
    cost_price = models.FloatField(blank=True, null=True)
    selling_price = models.FloatField(blank=True, null=True)
    profit_percent = models.FloatField(blank=True, null=True)
    stock_issue_status = models.IntegerField()
    stock_issue_created_by = models.PositiveIntegerField(blank=True, null=True)
    stock_issue_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_stock_issues'


class AccStores(models.Model):
    store_id = models.AutoField(primary_key=True)
    is_main_store = models.IntegerField()
    branch_id = models.PositiveIntegerField()
    store_name = models.CharField(max_length=191)
    store_description = models.TextField(blank=True, null=True)
    is_pos = models.IntegerField()
    active = models.IntegerField()
    store_created_by = models.PositiveIntegerField()
    store_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_stores'


class AccSubClass(models.Model):
    class_type_id = models.PositiveIntegerField()
    sub_class = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'acc_sub_class'


class AccTaxCategories(models.Model):
    name = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    status = models.PositiveIntegerField()
    created_by = models.PositiveIntegerField()
    last_updated_by = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    product_type = models.IntegerField()
    tax_percent = models.FloatField()

    class Meta:
        managed = False
        db_table = 'acc_tax_categories'


class AccTaxableItems(models.Model):
    name = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    tax_categories_id = models.PositiveIntegerField()
    status = models.PositiveIntegerField()
    created_by = models.PositiveIntegerField()
    last_updated_by = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_taxable_items'


class AccTdsDetail(models.Model):
    tds_master = models.ForeignKey('AccTdsMaster', models.DO_NOTHING)
    acc = models.ForeignKey(AccAccounts, models.DO_NOTHING)
    efffrom = models.DateField()
    effto = models.DateField(blank=True, null=True)
    percent = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_tds_detail'


class AccTdsMaster(models.Model):
    name = models.CharField(max_length=191)
    code = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_tds_master'


class AccTerms(models.Model):
    name = models.CharField(max_length=191)
    days = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_terms'


class AccTransTypeParents(models.Model):
    parent_id = models.PositiveIntegerField(blank=True, null=True)
    voucher_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_trans_type_parents'


class AccTransactionTypes(models.Model):
    name = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    code = models.CharField(max_length=5, blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'acc_transaction_types'


class AccVoucherDetails(models.Model):
    move = models.ForeignKey('AccVouchers', models.DO_NOTHING)
    journal = models.ForeignKey(AccJournal, models.DO_NOTHING)
    account = models.ForeignKey(AccAccounts, models.DO_NOTHING)
    debit = models.FloatField()
    credit = models.FloatField()
    balance = models.FloatField()
    date_posted = models.DateTimeField(blank=True, null=True)
    reconciled = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    company_id = models.PositiveIntegerField()
    period_id = models.PositiveIntegerField()
    total_credit_amount = models.FloatField()
    total_debit_amount = models.FloatField()
    description = models.CharField(max_length=255, blank=True, null=True)
    acc_code = models.CharField(max_length=20, blank=True, null=True)
    is_delete = models.IntegerField()
    customer_id = models.IntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    tax_type = models.CharField(max_length=191, blank=True, null=True)
    tax_type_percentage = models.FloatField(blank=True, null=True)
    reconciled_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='reconciled_by', blank=True, null=True)
    reconciled_at = models.DateTimeField(blank=True, null=True)
    reconciliation_remarks = models.CharField(max_length=191, blank=True, null=True)
    billwise_adjustment_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_voucher_details'


class AccVoucherDetailsProvisional(models.Model):
    prov = models.ForeignKey('AccVouchersProvisional', models.DO_NOTHING)
    journal = models.ForeignKey(AccJournal, models.DO_NOTHING)
    account = models.ForeignKey(AccAccounts, models.DO_NOTHING)
    debit = models.FloatField()
    credit = models.FloatField()
    balance = models.FloatField()
    date_posted = models.DateTimeField(blank=True, null=True)
    reconciled = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    company_id = models.PositiveIntegerField()
    period_id = models.PositiveIntegerField()
    total_credit_amount = models.FloatField()
    total_debit_amount = models.FloatField()
    description = models.CharField(max_length=191, blank=True, null=True)
    acc_code = models.CharField(max_length=20, blank=True, null=True)
    is_delete = models.IntegerField()
    customer_id = models.PositiveIntegerField(blank=True, null=True)
    json_data = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_voucher_details_provisional'


class AccVouchers(models.Model):
    name = models.CharField(max_length=191, blank=True, null=True)
    reference = models.CharField(max_length=191, blank=True, null=True)
    journal = models.ForeignKey(AccJournal, models.DO_NOTHING)
    status = models.IntegerField()
    date_posted = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    company_id = models.PositiveIntegerField()
    period_id = models.PositiveIntegerField()
    vtype = models.CharField(max_length=3, blank=True, null=True)
    bill_no = models.CharField(max_length=20, blank=True, null=True)
    patient_id = models.IntegerField(blank=True, null=True)
    voucher_no = models.CharField(max_length=20, blank=True, null=True)
    invoice_no = models.IntegerField()
    account_id = models.IntegerField(blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    is_opening_balance_voucher = models.IntegerField()
    provisional_id = models.CharField(max_length=20, blank=True, null=True)
    approved_by = models.PositiveIntegerField(blank=True, null=True)
    approved_on = models.DateTimeField(blank=True, null=True)
    is_doctor_share = models.IntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    patient_type = models.CharField(max_length=191, blank=True, null=True)
    cheque_no = models.CharField(max_length=191, blank=True, null=True)
    in_pat_id = models.PositiveIntegerField(blank=True, null=True)
    emergency_pat_id = models.PositiveIntegerField(blank=True, null=True)
    dialysis_pat_id = models.PositiveIntegerField(blank=True, null=True)
    is_bulk = models.IntegerField()
    manual_invoice_no = models.CharField(max_length=191, blank=True, null=True)
    patno = models.CharField(max_length=100, blank=True, null=True)
    pdc_status = models.IntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    voucher_sub_type = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_vouchers'


class AccVouchersProvisional(models.Model):
    name = models.CharField(max_length=191)
    reference = models.CharField(max_length=191)
    journal = models.ForeignKey(AccJournal, models.DO_NOTHING)
    status = models.IntegerField()
    date_posted = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    company_id = models.PositiveIntegerField()
    period_id = models.PositiveIntegerField()
    vtype = models.CharField(max_length=3, blank=True, null=True)
    bill_no = models.CharField(max_length=20, blank=True, null=True)
    patient_id = models.IntegerField(blank=True, null=True)
    voucher_no = models.CharField(max_length=20, blank=True, null=True)
    invoice_no = models.IntegerField()
    account_id = models.PositiveIntegerField(blank=True, null=True)
    source = models.CharField(max_length=191, blank=True, null=True)
    is_opening_balance_voucher = models.IntegerField()
    serialdata = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    post_date = models.DateField(blank=True, null=True)
    totalamount = models.FloatField(db_column='totalAmount')  # Field name made lowercase.
    terms_id = models.IntegerField()
    bank_id = models.IntegerField(blank=True, null=True)
    card_no = models.CharField(max_length=191, blank=True, null=True)
    cheque_no = models.CharField(max_length=191, blank=True, null=True)
    files_data = models.TextField(blank=True, null=True)
    pan_no = models.CharField(max_length=191, blank=True, null=True)
    cheque_date = models.DateTimeField(blank=True, null=True)
    drawn_on = models.DateTimeField(blank=True, null=True)
    is_bulk = models.IntegerField()
    approved_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='approved_by', blank=True, null=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', related_name='accvouchersprovisional_created_by_set', blank=True, null=True)
    drawn_on_bank = models.PositiveIntegerField(blank=True, null=True)
    final_voucher_no = models.CharField(max_length=191, blank=True, null=True)
    manual_invoice_no = models.CharField(max_length=191, blank=True, null=True)
    payee_name = models.CharField(max_length=191, blank=True, null=True)
    vendor_bill_date = models.DateField(blank=True, null=True)
    voucher_sub_type = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_vouchers_provisional'


class AccountHeads(models.Model):
    account_head = models.CharField(max_length=255, blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    company_id = models.IntegerField()
    period_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'account_heads'


class AccountLogs(models.Model):
    created_by = models.PositiveIntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)
    acc_sales_id = models.PositiveIntegerField(blank=True, null=True)
    journal_id = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_logs'


class AdditionalSpecimen(models.Model):
    specimen_name = models.CharField(max_length=255)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'additional_specimen'


class Address(models.Model):
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address'


class Advices(models.Model):
    visit_id = models.IntegerField()
    patient_id = models.IntegerField()
    advice = models.CharField(max_length=191)
    active = models.IntegerField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    ipd_id = models.IntegerField()
    er_id = models.IntegerField()
    admission_advice = models.TextField(blank=True, null=True)
    refer_doctor_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'advices'


class AgentPatients(models.Model):
    test_order_master_id = models.PositiveIntegerField()
    full_name = models.CharField(max_length=255, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    age_type = models.CharField(max_length=255, blank=True, null=True)
    approve_status = models.IntegerField()
    master_bill_id = models.PositiveIntegerField()
    patient_id = models.PositiveIntegerField()
    service_bill_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent_patients'


class AgentUserTable(models.Model):
    discount_group_percent_id = models.IntegerField(blank=True, null=True)
    username = models.CharField(unique=True, max_length=255)
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    active = models.IntegerField()
    role = models.IntegerField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    remember_token = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    partner_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent_user_table'


class AllLogs(models.Model):
    loggable_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    loggable_type = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    data = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'all_logs'


class Amenities(models.Model):
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    branch = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'amenities'


class ApiKeyAccessEvents(models.Model):
    api_key = models.ForeignKey('ApiKeys', models.DO_NOTHING)
    ip_address = models.CharField(max_length=45)
    url = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_key_access_events'


class ApiKeyAdminEvents(models.Model):
    api_key = models.ForeignKey('ApiKeys', models.DO_NOTHING)
    ip_address = models.CharField(max_length=45)
    event = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_key_admin_events'


class ApiKeys(models.Model):
    name = models.CharField(max_length=255)
    key = models.CharField(max_length=64)
    active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_keys'


class AppMenuRole(models.Model):
    app_menu_id = models.PositiveIntegerField()
    role_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'app_menu_role'


class AppMenus(models.Model):
    name = models.CharField(max_length=191, blank=True, null=True)
    display_name = models.CharField(max_length=191, blank=True, null=True)
    url = models.CharField(max_length=191, blank=True, null=True)
    order = models.PositiveIntegerField(blank=True, null=True)
    active = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    tab = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_menus'


class AppliedPosition(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applied_position'


class Appointments(models.Model):
    pat_id = models.PositiveIntegerField()
    doctor_id = models.PositiveIntegerField()
    schedule_id = models.PositiveIntegerField()
    patient_name = models.CharField(max_length=255)
    doctor_name = models.CharField(max_length=255)
    type = models.IntegerField()
    appointment_number = models.CharField(max_length=255, blank=True, null=True)
    walk_in_status = models.IntegerField()
    app_start = models.DateField(blank=True, null=True)
    app_end = models.DateField(blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appointments'


class ArcMachineLogDetails(models.Model):
    id = models.PositiveIntegerField()
    machine_log_id = models.IntegerField()
    sample_id = models.CharField(max_length=255)
    test_id = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    flag = models.CharField(max_length=255)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arc_machine_log_details'


class ArcMachineLogs(models.Model):
    id = models.PositiveIntegerField()
    machine_name = models.CharField(max_length=255)
    probe_id = models.IntegerField()
    uuid = models.CharField(max_length=255)
    data = models.TextField()
    sample_id = models.CharField(max_length=255)
    patient_id = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    result_date_time = models.TextField()

    class Meta:
        managed = False
        db_table = 'arc_machine_logs'


class AssignTemplates(models.Model):
    template_id = models.IntegerField()
    doctor_id = models.IntegerField()
    is_round_charge = models.IntegerField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    sharing_template_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assign_templates'


class BackupLogs(models.Model):
    filename = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=255)
    type = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'backup_logs'


class Banks(models.Model):
    bank_name = models.CharField(max_length=255)
    short = models.CharField(max_length=255)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banks'


class BasePlans(models.Model):
    doctor_id = models.PositiveIntegerField()
    dept_id = models.PositiveIntegerField()
    doctor_name = models.CharField(max_length=255)
    dept_name = models.CharField(max_length=255)
    status = models.IntegerField()
    data = models.TextField()
    day_start_time = models.CharField(max_length=255)
    day_end_time = models.CharField(max_length=255)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    day_code = models.IntegerField(blank=True, null=True)
    timegap = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_plans'


class Batch(models.Model):
    batch = models.CharField(max_length=255)
    is_active = models.IntegerField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'batch'


class BatchPatients(models.Model):
    site_id = models.PositiveIntegerField()
    site_name = models.CharField(max_length=255)
    no_of_patients = models.IntegerField()
    no_of_tests = models.IntegerField()
    site_referral_person = models.PositiveIntegerField()
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    mobile_no = models.CharField(max_length=255, blank=True, null=True)
    district_id = models.IntegerField()
    district_name = models.CharField(max_length=255, blank=True, null=True)
    test_id = models.IntegerField()
    test_name = models.CharField(max_length=255, blank=True, null=True)
    is_covid_test = models.CharField(max_length=255)
    collected_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'batch_patients'


class BedTransferPolicy(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bed_transfer_policy'


class Beds(models.Model):
    ward = models.CharField(max_length=255)
    room_type = models.CharField(max_length=255)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    branch = models.PositiveIntegerField()
    bed_no = models.CharField(max_length=45, blank=True, null=True)
    ward_id = models.IntegerField(blank=True, null=True)
    room_type_id = models.IntegerField(blank=True, null=True)
    occupy_status = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    floor_id = models.PositiveIntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    disp_cat_name = models.CharField(max_length=255, blank=True, null=True)
    disp_main_cat_name = models.CharField(max_length=255, blank=True, null=True)
    displaycat = models.CharField(max_length=100, blank=True, null=True)
    shortname = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beds'


class BillDetailTeam(models.Model):
    bill_detail_id = models.PositiveIntegerField()
    master_bill_id = models.PositiveIntegerField()
    doctor_id = models.PositiveIntegerField()
    item_id = models.PositiveIntegerField()
    percentage = models.FloatField()
    amount = models.FloatField()
    consultant_incharge = models.PositiveIntegerField()
    refer_by_consultant = models.PositiveIntegerField()
    performing_consultant = models.PositiveIntegerField()
    service_refer_by_consultant = models.PositiveIntegerField()
    additional_consultant = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill_detail_team'


class BillDetails(models.Model):
    refund_status = models.CharField(max_length=1)
    master_bill = models.ForeignKey('MasterBills', models.DO_NOTHING, blank=True, null=True)
    item = models.ForeignKey('Items', models.DO_NOTHING, blank=True, null=True)
    item_type = models.IntegerField()
    item_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    amt_wo_tax = models.FloatField(blank=True, null=True)
    detail_tax_amt = models.FloatField(blank=True, null=True)
    amt_w_tax = models.FloatField(blank=True, null=True)
    amt_bd = models.FloatField(blank=True, null=True)
    department = models.ForeignKey('Departments', models.DO_NOTHING, blank=True, null=True)
    detail_discount_amt = models.FloatField(blank=True, null=True)
    amt_ad = models.FloatField(blank=True, null=True)
    created_by = models.PositiveIntegerField()
    remarks = models.CharField(max_length=255, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    discount_percentage = models.FloatField()
    rate = models.FloatField(blank=True, null=True)
    doc_percentage = models.CharField(max_length=255, blank=True, null=True)
    sharing = models.FloatField()
    tds = models.CharField(db_column='TDS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    doc_id = models.PositiveIntegerField(blank=True, null=True)
    doctor_name = models.CharField(max_length=255, blank=True, null=True)
    tds_amount = models.FloatField()
    branch = models.PositiveIntegerField()
    revenue_center = models.IntegerField(blank=True, null=True)
    category_type = models.PositiveIntegerField()
    bill_type = models.FloatField()
    surgery_discount_flag = models.IntegerField()
    anesthesia_discount_flag = models.IntegerField()
    hospital = models.FloatField()
    department_0 = models.FloatField(db_column='department')  # Field renamed because of name conflict.
    anesthesist = models.FloatField()
    fund = models.FloatField()
    depreciation = models.FloatField()
    instrument = models.FloatField()
    hospital_discount = models.IntegerField()
    department_discount = models.IntegerField()
    anesthesist_discount = models.IntegerField()
    fund_discount = models.IntegerField()
    depreciation_discount = models.IntegerField()
    instrument_discount = models.IntegerField()
    package_items = models.CharField(max_length=255, blank=True, null=True)
    batch_id = models.PositiveIntegerField()
    appliance = models.FloatField()
    appliance_discount = models.IntegerField()
    online_purchase = models.IntegerField()
    group_item_id = models.IntegerField()
    group_item_name = models.CharField(max_length=255, blank=True, null=True)
    doctor_discount_per = models.PositiveIntegerField(blank=True, null=True)
    doctor_discount_total_amt = models.FloatField(blank=True, null=True)
    s_billdetails_id = models.PositiveIntegerField()
    ipd_bed_details_id = models.PositiveIntegerField()
    doctor_id = models.IntegerField()
    additional_consultant = models.PositiveIntegerField()
    consultant_incharge = models.PositiveIntegerField()
    created_at_date = models.DateField(blank=True, null=True)
    deduction_status = models.IntegerField()
    doctor_discount = models.FloatField()
    doctor_percentage = models.FloatField()
    doctype = models.CharField(max_length=100, blank=True, null=True)
    hospital_discount_amount = models.FloatField()
    hospital_percentage = models.FloatField()
    is_medication = models.IntegerField()
    is_pharmacy_item = models.IntegerField()
    labno = models.CharField(max_length=100, blank=True, null=True)
    package_id = models.PositiveIntegerField(blank=True, null=True)
    patno = models.CharField(max_length=100, blank=True, null=True)
    performing_consultant = models.PositiveIntegerField()
    rate_group = models.CharField(max_length=100, blank=True, null=True)
    rate_group_id = models.PositiveIntegerField(blank=True, null=True)
    refe_refu_icode = models.CharField(max_length=100, blank=True, null=True)
    refer_by_consultant = models.PositiveIntegerField()
    refund_posting_status = models.IntegerField()
    refund_voucher_id = models.PositiveIntegerField()
    refund_voucher_no = models.CharField(max_length=255, blank=True, null=True)
    revert_status = models.IntegerField()
    room_type_id = models.PositiveIntegerField(blank=True, null=True)
    service_refer_by_consultant = models.PositiveIntegerField()
    sno = models.IntegerField(blank=True, null=True)
    surgery_item_type = models.CharField(max_length=100, blank=True, null=True)
    surgerycode = models.CharField(max_length=100, blank=True, null=True)
    ssf_adjustment_remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill_details'


class BillwiseAdjustments(models.Model):
    voucher_no = models.CharField(max_length=191)
    bill_no = models.CharField(max_length=191)
    total_amount = models.FloatField()
    adjustment_amount = models.FloatField()
    balance_amount = models.FloatField()
    tds_amount = models.FloatField()
    vat_amount = models.FloatField()
    discount_amount = models.FloatField()
    purchase_bills_payment_tracker_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'billwise_adjustments'


class BipannaNagarikPatientLedgers(models.Model):
    pat_id = models.IntegerField()
    in_pat_id = models.IntegerField()
    master_bill_id = models.IntegerField()
    s_masterbill_id = models.IntegerField()
    ref_master_id = models.IntegerField()
    deposit_id = models.IntegerField()
    deposit_refund_id = models.IntegerField()
    bill_no = models.CharField(max_length=255)
    fiscalyear = models.CharField(db_column='fiscalYear', max_length=255)  # Field name made lowercase.
    reference_bill_no = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.IntegerField()
    child_id = models.IntegerField()
    discount_group = models.IntegerField()
    discount_type = models.IntegerField()
    debt_amt = models.DecimalField(max_digits=8, decimal_places=2)
    credit_amt = models.DecimalField(max_digits=8, decimal_places=2)
    bill_type = models.CharField(max_length=1)
    remarks = models.TextField()
    branch = models.PositiveIntegerField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    payment_type = models.IntegerField()
    rate_type_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bipanna_nagarik_patient_ledgers'


class BirthMotherInformation(models.Model):
    in_patient = models.ForeignKey('InPatients', models.DO_NOTHING)
    name = models.CharField(max_length=255)
    dob = models.CharField(max_length=255)
    ward_name = models.CharField(max_length=255)
    ward = models.ForeignKey('Wards', models.DO_NOTHING)
    bed_no = models.CharField(max_length=255)
    bed = models.ForeignKey(Beds, models.DO_NOTHING)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'birth_mother_information'


class BirthRegister(models.Model):
    in_patient = models.ForeignKey('InPatients', models.DO_NOTHING)
    name = models.CharField(max_length=255)
    dob = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    birth_type = models.PositiveIntegerField()
    time_of_birth = models.TimeField()
    weight = models.FloatField()
    no_of_birth = models.IntegerField()
    birth_order = models.IntegerField()
    fathers_name = models.CharField(max_length=255)
    birther_mother = models.ForeignKey(BirthMotherInformation, models.DO_NOTHING)
    ward_name = models.CharField(max_length=255)
    ward = models.ForeignKey('Wards', models.DO_NOTHING)
    bed_no = models.CharField(max_length=255)
    bed = models.ForeignKey(Beds, models.DO_NOTHING)
    age = models.IntegerField()
    status = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'birth_register'


class Blogs(models.Model):
    title = models.CharField(max_length=191)
    link_url = models.CharField(max_length=191)
    image = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blogs'


class BloodBagReturn(models.Model):
    form_date = models.DateField(blank=True, null=True)
    patient_name = models.CharField(max_length=191)
    ipd_num = models.IntegerField()
    patient_id = models.IntegerField()
    bed_no = models.CharField(max_length=191, blank=True, null=True)
    bloodgroup = models.CharField(db_column='bloodGroup', max_length=191, blank=True, null=True)  # Field name made lowercase.
    blood_bag_number = models.CharField(max_length=191, blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    reason_to_return_bloodbank = models.TextField(blank=True, null=True)
    name_of_staff = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    component = models.CharField(max_length=191, blank=True, null=True)
    er_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'blood_bag_return'


class BloodMonitoringDetails(models.Model):
    monitoring = models.ForeignKey('BloodMonitoringMaster', models.DO_NOTHING)
    variables = models.CharField(max_length=191, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    variable_group = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blood_monitoring_details'


class BloodMonitoringMaster(models.Model):
    patient_id = models.IntegerField()
    in_pat_id = models.IntegerField()
    blood_bag_number = models.CharField(max_length=191, blank=True, null=True)
    component = models.CharField(max_length=191, blank=True, null=True)
    cross_match = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    collection_date = models.DateField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    transfused_amount = models.CharField(max_length=191, blank=True, null=True)
    approved_by = models.IntegerField(blank=True, null=True)
    er_id = models.IntegerField()
    receive_by = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blood_monitoring_master'


class BloodSugarMonitoringChart(models.Model):
    reported_date = models.CharField(max_length=191, blank=True, null=True)
    reported_time = models.CharField(max_length=191, blank=True, null=True)
    treatment = models.CharField(max_length=191)
    remarks = models.CharField(max_length=191, blank=True, null=True)
    nurse_name = models.CharField(max_length=191)
    patient_id = models.IntegerField()
    in_pat_id = models.IntegerField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    value = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'blood_sugar_monitoring_chart'


class BodyReceiver(models.Model):
    receiver_name = models.CharField(max_length=255, blank=True, null=True)
    relationship = models.IntegerField(blank=True, null=True)
    citizenship_no = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    r_date = models.CharField(max_length=255, blank=True, null=True)
    r_time = models.TimeField(blank=True, null=True)
    status = models.IntegerField()
    death_register_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'body_receiver'


class BookingInitiationLog(models.Model):
    schedule_list_id = models.PositiveIntegerField()
    initiated_by = models.PositiveIntegerField(blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    country = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking_initiation_log'


class Branch(models.Model):
    branch = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    website = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    slogan = models.CharField(max_length=255, blank=True, null=True)
    pan_no = models.CharField(max_length=255, blank=True, null=True)
    vat_no = models.CharField(max_length=255, blank=True, null=True)
    short_name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField()
    bill_prefix = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'branch'


class BudgetHeadDetails(models.Model):
    budget_head = models.ForeignKey('BudgetHeads', models.DO_NOTHING, blank=True, null=True)
    type_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budget_head_details'


class BudgetHeadTransactions(models.Model):
    budget_head = models.ForeignKey('BudgetHeads', models.DO_NOTHING, blank=True, null=True)
    fiscal_year_id = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    amt = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budget_head_transactions'


class BudgetHeads(models.Model):
    budget_head = models.CharField(max_length=255, blank=True, null=True)
    budget_sub_head = models.CharField(max_length=255, blank=True, null=True)
    type_status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budget_heads'


class BudgetSetup(models.Model):
    speciality_id = models.PositiveIntegerField()
    source_name = models.CharField(max_length=255)
    patient_qty = models.IntegerField()
    service_qty = models.IntegerField()
    amount = models.FloatField()
    fiscalyear = models.CharField(max_length=255)
    month = models.CharField(max_length=255)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    source = models.ForeignKey('SpecialityHeads', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budget_setup'


class BulkPatients(models.Model):
    art = models.IntegerField()
    fname = models.CharField(max_length=255)
    mname = models.CharField(max_length=255, blank=True, null=True)
    lname = models.CharField(max_length=255)
    age = models.IntegerField()
    age_type = models.CharField(max_length=1)
    gender = models.CharField(max_length=255)
    key_population = models.IntegerField(blank=True, null=True)
    art_start_date = models.CharField(max_length=255, blank=True, null=True)
    current_regimen = models.CharField(max_length=255, blank=True, null=True)
    last_cd4_count_result = models.CharField(max_length=255, blank=True, null=True)
    date_of_referral_for_vl = models.CharField(max_length=255, blank=True, null=True)
    date_of_vl_conducted = models.CharField(max_length=255, blank=True, null=True)
    vl_result = models.CharField(max_length=255, blank=True, null=True)
    batch_id = models.CharField(max_length=255, blank=True, null=True)
    patient_id = models.CharField(max_length=255, blank=True, null=True)
    status_of_report = models.CharField(max_length=255, blank=True, null=True)
    threshold = models.CharField(max_length=255, blank=True, null=True)
    times_of_testing = models.CharField(max_length=255, blank=True, null=True)
    site_id = models.CharField(max_length=255, blank=True, null=True)
    time_of_repeation = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bulk_patients'


class Cache(models.Model):
    key = models.CharField(unique=True, max_length=255)
    value = models.TextField()
    expiration = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cache'


class CallRecords(models.Model):
    doctor = models.ForeignKey('Doctors', models.DO_NOTHING)
    appoint_date = models.DateField()
    pat_id = models.IntegerField()
    pat_name = models.CharField(max_length=255)
    pat_phone = models.CharField(max_length=255)
    issue = models.CharField(max_length=255)
    called_date = models.DateField(blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    ipd_id = models.IntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'call_records'


class CallcenterLogs(models.Model):
    data = models.TextField()
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'callcenter_logs'


class Cardex(models.Model):
    patient_id = models.IntegerField()
    ipd_id = models.IntegerField()
    medication_id = models.IntegerField()
    date = models.CharField(max_length=191)
    time = models.CharField(max_length=191)
    dose = models.CharField(max_length=191, blank=True, null=True)
    batch_no = models.CharField(max_length=191, blank=True, null=True)
    expiry_date = models.CharField(max_length=191, blank=True, null=True)
    given_by = models.CharField(max_length=191)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    er_id = models.IntegerField()
    qty = models.IntegerField()
    medicine_name = models.CharField(max_length=191, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    dialysis_pat_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cardex'


class Cardiovasculars(models.Model):
    visit_id = models.IntegerField()
    medicaldetails_id = models.IntegerField()
    patient_id = models.IntegerField()
    heart_sound = models.TextField(blank=True, null=True)
    heart_murmur_status = models.IntegerField()
    heart_murmur_remark = models.TextField(blank=True, null=True)
    ecg_findings = models.TextField(blank=True, null=True)
    echo_findings = models.TextField(blank=True, null=True)
    others = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    ipd_id = models.IntegerField()
    er_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cardiovasculars'


class CaseType(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    active = models.IntegerField()
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'case_type'


class CatalogueGenericNames(models.Model):
    generic_name = models.CharField(unique=True, max_length=191)
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    generic_id = models.IntegerField(blank=True, null=True)
    md_code = models.CharField(max_length=191)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catalogue_generic_names'


class CatalogueLocation(models.Model):
    catalogue_id = models.PositiveBigIntegerField()
    store_id = models.PositiveBigIntegerField()
    rack = models.CharField(max_length=191, blank=True, null=True)
    rack_number = models.CharField(max_length=191, blank=True, null=True)
    location_name = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogue_location'


class CataloguePriceLogs(models.Model):
    catalogue_price_log_id = models.AutoField(primary_key=True)
    catalogue_id = models.PositiveIntegerField()
    purchase_order_no = models.CharField(max_length=191)
    updated_cost_price = models.FloatField()
    updated_selling_price = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogue_price_logs'


class CatalogueTypes(models.Model):
    catalogue_type_id = models.AutoField(primary_key=True)
    catalogue_type_name = models.CharField(max_length=191)
    is_narcotic = models.IntegerField()
    catalogue_type_created_by = models.PositiveIntegerField()
    catalogue_type_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogue_types'


class Catalogues(models.Model):
    catalogue_id = models.AutoField(primary_key=True)
    unit = models.ForeignKey('UnitInventories', models.DO_NOTHING)
    vendor = models.ForeignKey('VendorInventories', models.DO_NOTHING)
    catalogue_type = models.ForeignKey(CatalogueTypes, models.DO_NOTHING)
    catalogue_generic = models.ForeignKey(CatalogueGenericNames, models.DO_NOTHING)
    catalogue_name = models.CharField(max_length=191)
    catalogue_unit_value = models.CharField(max_length=191)
    catalogue_value_unit = models.CharField(max_length=191)
    catalogue_max_stock = models.PositiveIntegerField()
    catalogue_min_stock = models.PositiveIntegerField()
    catalogue_delivery_time = models.PositiveIntegerField()
    catalogue_safety_stock = models.PositiveIntegerField()
    insurance_flag = models.IntegerField(blank=True, null=True)
    insurance_rate = models.FloatField(blank=True, null=True)
    cost_price = models.FloatField()
    selling_price = models.FloatField()
    profit_percent = models.FloatField()
    catalogue_status = models.IntegerField()
    expiry_alert_days = models.IntegerField()
    catalogue_taxable = models.IntegerField()
    catalogue_discountable = models.IntegerField()
    catalogue_courier_charge = models.IntegerField()
    catalogue_cc_per = models.FloatField()
    catalogue_image = models.TextField(blank=True, null=True)
    catalogue_description = models.TextField(blank=True, null=True)
    catalogue_created_by = models.PositiveIntegerField(blank=True, null=True)
    catalogue_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    reorder = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    pacssize = models.CharField(max_length=100, blank=True, null=True)
    is_consumable = models.IntegerField(blank=True, null=True)
    md_code = models.IntegerField(blank=True, null=True)
    is_medicine = models.IntegerField()
    item_code = models.CharField(max_length=191, blank=True, null=True)
    is_pharmacy_taxable = models.IntegerField(blank=True, null=True)
    insurance_service = models.ForeignKey('ItemInsurances', models.DO_NOTHING, blank=True, null=True)
    ssf_service = models.ForeignKey('ItemSsf', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogues'


class CategoryPatient(models.Model):
    category_name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_patient'


class CategoryWiseBudgets(models.Model):
    category = models.ForeignKey('PatientCategories', models.DO_NOTHING)
    source_name = models.CharField(max_length=255)
    patient_qty = models.IntegerField()
    service_qty = models.IntegerField()
    amount = models.FloatField()
    fiscalyear = models.CharField(max_length=255)
    month = models.CharField(max_length=255)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='updated_by', related_name='categorywisebudgets_updated_by_set', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    per_day_amount = models.FloatField()
    per_day_patient_qty = models.FloatField()
    per_day_service_qty = models.FloatField()

    class Meta:
        managed = False
        db_table = 'category_wise_budgets'


class CauseOfDeath(models.Model):
    death_register_id = models.PositiveIntegerField()
    death_type = models.CharField(max_length=255, blank=True, null=True)
    hospital_death_type = models.CharField(max_length=255, blank=True, null=True)
    cause_of_death = models.CharField(max_length=255, blank=True, null=True)
    diagnosis = models.CharField(max_length=255, blank=True, null=True)
    immediate_cause = models.CharField(max_length=255, blank=True, null=True)
    underlying_cause = models.CharField(max_length=255, blank=True, null=True)
    contributory_cause = models.CharField(max_length=255, blank=True, null=True)
    pronounced_by_1 = models.CharField(max_length=255, blank=True, null=True)
    pronounced_by_2 = models.CharField(max_length=255, blank=True, null=True)
    method_of_disposition = models.IntegerField(blank=True, null=True)
    is_autospy_done = models.IntegerField()
    permission_for_autospy = models.PositiveIntegerField(blank=True, null=True)
    pregnency_death = models.IntegerField()
    is_delevery_done = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cause_of_death'


class CertificateBirthTypes(models.Model):
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'certificate_birth_types'


class ClinicalCathedral(models.Model):
    name = models.CharField(max_length=191)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clinical_cathedral'


class ClinicalConfigurations(models.Model):
    display_name = models.CharField(max_length=191, blank=True, null=True)
    name = models.CharField(max_length=191, blank=True, null=True)
    type = models.CharField(max_length=191, blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    module_category = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clinical_configurations'


class ClinicalDental(models.Model):
    patient_id = models.IntegerField()
    visit_id = models.IntegerField()
    medical_history = models.TextField(blank=True, null=True)
    soft_tissue = models.TextField(blank=True, null=True)
    hard_tissue = models.TextField(blank=True, null=True)
    clinical_diagnosis = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clinical_dental'


class ClinicalIpdCathedral(models.Model):
    patient_id = models.IntegerField()
    inpatient_id = models.IntegerField()
    cathedral_id = models.IntegerField()
    status = models.CharField(max_length=191)
    date = models.DateField()
    time = models.CharField(max_length=191, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    inserted_by = models.CharField(max_length=191, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clinical_ipd_cathedral'


class ClinicalIpdLines(models.Model):
    patient_id = models.IntegerField()
    inpatient_id = models.IntegerField()
    line_id = models.IntegerField()
    status = models.CharField(max_length=191)
    date = models.DateField()
    time = models.CharField(max_length=191, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    inserted_by = models.CharField(max_length=191, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clinical_ipd_lines'


class ClinicalLines(models.Model):
    name = models.CharField(max_length=191)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clinical_lines'


class ClinicalTemplateAdvice(models.Model):
    name = models.CharField(max_length=191)
    status = models.IntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clinical_template_advice'


class ClinicalTemplateAdviceDetail(models.Model):
    template_id = models.PositiveIntegerField()
    advice = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clinical_template_advice_detail'


class ClinicalTemplateDiagnosis(models.Model):
    name = models.CharField(max_length=191)
    status = models.IntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clinical_template_diagnosis'


class ClinicalTemplateDiagnosisDetail(models.Model):
    template_id = models.PositiveIntegerField()
    disease_name = models.CharField(max_length=191)
    disease_code = models.CharField(max_length=191, blank=True, null=True)
    type = models.CharField(max_length=191)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clinical_template_diagnosis_detail'


class ClinicalTemplateExamination(models.Model):
    name = models.CharField(max_length=191)
    status = models.IntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    default_template = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clinical_template_examination'


class ClinicalTemplateExaminationDetail(models.Model):
    template_id = models.PositiveIntegerField()
    examination = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clinical_template_examination_detail'


class ClinicalTemplateMedication(models.Model):
    name = models.CharField(max_length=191)
    status = models.IntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    default_template = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clinical_template_medication'


class ClinicalTemplateMedicationDetail(models.Model):
    template_id = models.PositiveIntegerField()
    drug_name = models.CharField(max_length=191)
    drug_id = models.IntegerField(blank=True, null=True)
    dose = models.CharField(max_length=191, blank=True, null=True)
    dose_unit = models.CharField(max_length=191, blank=True, null=True)
    types_unit = models.CharField(max_length=191, blank=True, null=True)
    frequency_id = models.IntegerField(blank=True, null=True)
    frequency = models.CharField(max_length=191, blank=True, null=True)
    route = models.CharField(max_length=191, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    continue_status = models.IntegerField()
    duration = models.CharField(max_length=191, blank=True, null=True)
    duration_unit = models.CharField(max_length=191, blank=True, null=True)
    reorder_qty = models.CharField(max_length=191, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    is_external = models.IntegerField()
    is_self = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clinical_template_medication_detail'


class ClinicalTemplateObservation(models.Model):
    name = models.CharField(max_length=191)
    status = models.IntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clinical_template_observation'


class ClinicalTemplateObservationDetail(models.Model):
    template_id = models.PositiveIntegerField()
    past_history = models.TextField(blank=True, null=True)
    history_notes = models.TextField(blank=True, null=True)
    complaint = models.TextField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    duration_type = models.CharField(max_length=191, blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    family_history = models.TextField(blank=True, null=True)
    gynae_history = models.TextField(blank=True, null=True)
    past_inv_report = models.TextField(blank=True, null=True)
    personal_social_history = models.TextField(blank=True, null=True)
    present_inv_report = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clinical_template_observation_detail'


class ClinicalTemplateTests(models.Model):
    name = models.CharField(max_length=191)
    status = models.IntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_procedure = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clinical_template_tests'


class ClinicalTemplateTestsDetail(models.Model):
    template_id = models.PositiveIntegerField(primary_key=True)  # The composite primary key (template_id, item_id) found, that is not supported. The first column is selected.
    item_id = models.PositiveIntegerField()
    temp = models.IntegerField()
    test_name = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clinical_template_tests_detail'
        unique_together = (('template_id', 'item_id'),)


class ClinicalTemplateVaccine(models.Model):
    name = models.CharField(max_length=191)
    status = models.IntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clinical_template_vaccine'


class ClinicalTemplateVaccineDetail(models.Model):
    template_id = models.PositiveIntegerField()
    vaccine = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    vaccine_id = models.IntegerField()
    dose = models.CharField(max_length=191, blank=True, null=True)
    frequency = models.CharField(max_length=191, blank=True, null=True)
    route = models.CharField(max_length=191, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clinical_template_vaccine_detail'


class ClosingStockDetails(models.Model):
    closing_stock_details_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    closing_stocks_id = models.PositiveIntegerField()
    stock_purchases_id = models.PositiveIntegerField()
    supplier_id = models.PositiveIntegerField()
    catalogue_id = models.PositiveIntegerField()
    actual_qty = models.IntegerField()
    reconcile_qty = models.IntegerField()
    reconcile_percent = models.FloatField()
    closing_stock_details_created_by = models.PositiveIntegerField()
    closing_stock_details_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'closing_stock_details'


class ClosingStocks(models.Model):
    closing_stocks_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    store_id = models.IntegerField()
    is_opened_flag = models.IntegerField()
    closing_stocks_tot_catalogue_qty = models.PositiveIntegerField()
    closing_stocks_remarks = models.TextField(blank=True, null=True)
    closing_stocks_created_by = models.PositiveIntegerField()
    closing_stocks_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'closing_stocks'


class CodeSequence(models.Model):
    status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'code_sequence'


class ColorCodes(models.Model):
    new_patient = models.CharField(max_length=255)
    free_followup = models.CharField(max_length=255)
    paid_followup = models.CharField(max_length=255)
    break_field = models.CharField(db_column='break', max_length=255)  # Field renamed because it was a Python reserved word.
    schedule = models.CharField(max_length=255)
    not_scheduled = models.CharField(max_length=255)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'color_codes'


class ColourCodes(models.Model):
    type_id = models.IntegerField()
    category = models.IntegerField()
    color_code = models.CharField(max_length=255)
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colour_codes'


class CommonSharing(models.Model):
    sharing_type = models.CharField(max_length=255, blank=True, null=True)
    type_wise_id = models.PositiveIntegerField()
    sharing_method = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    general_amount = models.FloatField()
    general_per = models.FloatField()
    cash_opd_amount = models.FloatField()
    cash_opd_per = models.FloatField()
    credit_opd_amount = models.FloatField()
    credit_opd_per = models.FloatField()
    package_amount = models.FloatField()
    package_per = models.FloatField()
    ipd_amount = models.FloatField()
    ipd_per = models.FloatField()
    assistant_self_amount = models.FloatField()
    assistant_self_per = models.FloatField()
    assistant_consultant_amount = models.FloatField()
    assistant_consultant_per = models.FloatField()
    tds_per = models.FloatField()
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    branch_id = models.PositiveIntegerField()
    consultant_type = models.IntegerField()
    is_scheduled = models.IntegerField()
    category_type = models.PositiveIntegerField()
    rate_group_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'common_sharing'


class CommonSharingDoctors(models.Model):
    common_sharing_id = models.PositiveIntegerField()
    general_amount = models.FloatField()
    general_per = models.FloatField()
    cash_opd_amount = models.FloatField()
    cash_opd_per = models.FloatField()
    credit_opd_amount = models.FloatField()
    credit_opd_per = models.FloatField()
    package_amount = models.FloatField()
    package_per = models.FloatField()
    ipd_amount = models.FloatField()
    ipd_per = models.FloatField()
    doctor_id = models.IntegerField()
    doctor_name = models.CharField(max_length=255, blank=True, null=True)
    consultant_type = models.IntegerField()
    is_scheduled = models.IntegerField()
    schedule_from = models.DateField(blank=True, null=True)
    schedule_to = models.DateField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'common_sharing_doctors'


class CommonSharingSchedules(models.Model):
    common_sharing = models.ForeignKey(CommonSharing, models.DO_NOTHING)
    general_amount = models.FloatField()
    general_per = models.FloatField()
    cash_opd_amount = models.FloatField()
    cash_opd_per = models.FloatField()
    credit_opd_amount = models.FloatField()
    credit_opd_per = models.FloatField()
    package_amount = models.FloatField()
    package_per = models.FloatField()
    ipd_amount = models.FloatField()
    ipd_per = models.FloatField()
    schedule_from = models.DateField(blank=True, null=True)
    schedule_to = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'common_sharing_schedules'


class Company(models.Model):
    company = models.CharField(max_length=191)
    address = models.CharField(max_length=191, blank=True, null=True)
    website = models.CharField(max_length=191, blank=True, null=True)
    contact = models.CharField(max_length=191, blank=True, null=True)
    slogan = models.CharField(max_length=191, blank=True, null=True)
    pan_no = models.CharField(max_length=191, blank=True, null=True)
    vat_no = models.CharField(max_length=191, blank=True, null=True)
    short_name = models.CharField(max_length=191, blank=True, null=True)
    is_active = models.IntegerField()
    book_type = models.IntegerField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    company_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'company'


class Complaints(models.Model):
    visit_id = models.IntegerField()
    medicaldetails_id = models.IntegerField()
    patient_id = models.IntegerField()
    complaint = models.TextField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    duration_type = models.CharField(max_length=191, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    ipd_id = models.IntegerField()
    er_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'complaints'


class Configurations(models.Model):
    display_name = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    module_category = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'configurations'


class ConfigurationsCustomLabels(models.Model):
    module = models.CharField(max_length=191)
    label = models.CharField(max_length=191)
    value = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'configurations_custom_labels'


class ConsentForms(models.Model):
    document_name = models.CharField(max_length=255)
    document_code = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consent_forms'


class Countries(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_code = models.CharField(max_length=191)
    country_name = models.CharField(max_length=191)
    rate_type = models.IntegerField()
    dialling_code = models.CharField(max_length=255, blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'


class CountriesNationality(models.Model):
    code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries_nationality'


class Country(models.Model):
    country = models.CharField(max_length=255)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class CovidAssessment(models.Model):
    patient_id = models.IntegerField()
    ipd_id = models.IntegerField()
    fever_onset_date = models.CharField(max_length=191, blank=True, null=True)
    afebrile_since = models.CharField(max_length=191, blank=True, null=True)
    chill_status = models.IntegerField()
    chill_remarks = models.CharField(max_length=191, blank=True, null=True)
    cough_status = models.IntegerField()
    cough_remarks = models.CharField(max_length=191, blank=True, null=True)
    vomiting_status = models.IntegerField()
    vomiting_remarks = models.CharField(max_length=191, blank=True, null=True)
    decrease_appetite_status = models.IntegerField()
    decrease_appetite_remarks = models.CharField(max_length=191, blank=True, null=True)
    loss_of_taste_status = models.IntegerField()
    loss_of_taste_remarks = models.CharField(max_length=191, blank=True, null=True)
    other_symptoms_status = models.IntegerField()
    other_symptoms_remarks = models.CharField(max_length=191, blank=True, null=True)
    dyspnea_status = models.IntegerField()
    dyspnea_remarks = models.CharField(max_length=191, blank=True, null=True)
    diarrhea_status = models.IntegerField()
    diarrhea_remarks = models.CharField(max_length=191, blank=True, null=True)
    loss_of_smell_status = models.IntegerField()
    loss_of_smell_remarks = models.CharField(max_length=191, blank=True, null=True)
    ocular_symptoms_status = models.IntegerField()
    ocular_symptoms_remarks = models.CharField(max_length=191, blank=True, null=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    er_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'covid_assessment'


class CovidPatientRecords(models.Model):
    date_of_collection = models.CharField(max_length=255, blank=True, null=True)
    sample_no = models.CharField(max_length=255)
    result = models.CharField(max_length=255)
    patient_name = models.CharField(max_length=255)
    age = models.IntegerField(blank=True, null=True)
    age_type = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    dob_bs = models.CharField(max_length=255, blank=True, null=True)
    dob_ad = models.CharField(max_length=255, blank=True, null=True)
    patient_mobile = models.CharField(max_length=255, blank=True, null=True)
    patient_email = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    revert_status = models.IntegerField()
    patient_id = models.IntegerField(blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    municipality_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'covid_patient_records'


class CreditNotes(models.Model):
    credit_note_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    supplier_id = models.PositiveIntegerField(blank=True, null=True)
    master_credit_note_id = models.PositiveIntegerField()
    credit_note_no = models.CharField(max_length=191, blank=True, null=True)
    sp_opening_stocks_id = models.PositiveIntegerField()
    sp_closing_stocks_id = models.PositiveIntegerField()
    catalogue_type_id = models.PositiveIntegerField()
    catalogue_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    batch = models.CharField(max_length=191)
    quantity = models.IntegerField()
    expiry_date = models.CharField(max_length=191)
    never_expiry = models.IntegerField()
    cp_before_tax = models.FloatField()
    discount_per = models.FloatField()
    discount_amount = models.FloatField()
    is_taxable = models.IntegerField()
    taxable_amt = models.FloatField()
    tax_per = models.FloatField()
    tax_amount = models.FloatField()
    cost_price = models.FloatField()
    credit_note_remarks = models.TextField(blank=True, null=True)
    credit_note_status = models.IntegerField()
    credit_note_created_by = models.PositiveIntegerField()
    credit_note_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    courier_charge = models.FloatField()
    bonus_expire_flag = models.IntegerField()
    stock_purchases_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'credit_notes'


class CreditPurchaseLedgers(models.Model):
    supplier_id = models.PositiveIntegerField()
    branch_id = models.PositiveIntegerField()
    master_stock_purchase_id = models.IntegerField()
    master_retrun_id = models.IntegerField()
    reference_purchase_no = models.CharField(max_length=191, blank=True, null=True)
    receipt_no = models.CharField(max_length=191, blank=True, null=True)
    dr_amt = models.FloatField()
    cr_amt = models.FloatField()
    type = models.CharField(max_length=1)
    payment_date = models.DateField()
    payment_type = models.IntegerField()
    bank_id = models.IntegerField(blank=True, null=True)
    card_no = models.CharField(max_length=191, blank=True, null=True)
    cheque_no = models.CharField(max_length=191, blank=True, null=True)
    remarks = models.TextField()
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'credit_purchase_ledgers'


class Currencies(models.Model):
    currency_name = models.CharField(max_length=255)
    country_name = models.CharField(max_length=255)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    currency_symbol = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'currencies'


class CustomerGroups(models.Model):
    customer_group = models.CharField(max_length=191)
    active = models.IntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_groups'


class CustomerType(models.Model):
    customer_group = models.ForeignKey(CustomerGroups, models.DO_NOTHING, blank=True, null=True)
    customer_type = models.CharField(max_length=191)
    discount_percentage = models.FloatField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_type'


class DailyBedOccupancies(models.Model):
    room_type = models.ForeignKey('RoomTypes', models.DO_NOTHING, blank=True, null=True)
    available_beds = models.IntegerField()
    stay_beds = models.IntegerField()
    occupancy_percent = models.FloatField()
    occupancy_date = models.DateTimeField(blank=True, null=True)
    new_patient_count = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daily_bed_occupancies'


class DashboardData(models.Model):
    dashboard_name = models.CharField(max_length=255)
    dashboard_datas = models.TextField()
    graph_datas = models.TextField()
    branch = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashboard_data'


class Dashboards(models.Model):
    name = models.CharField(max_length=255)
    value = models.TextField()
    type = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    branch = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'dashboards'


class DeathRegister(models.Model):
    in_pat_id = models.PositiveIntegerField()
    gender = models.CharField(max_length=255, blank=True, null=True)
    dob = models.CharField(max_length=255, blank=True, null=True)
    ward_name = models.CharField(max_length=255, blank=True, null=True)
    ward_id = models.PositiveIntegerField(blank=True, null=True)
    bed_no = models.CharField(max_length=255, blank=True, null=True)
    bed_id = models.PositiveIntegerField(blank=True, null=True)
    death_date = models.CharField(max_length=255, blank=True, null=True)
    death_time = models.TimeField(blank=True, null=True)
    place_of_death = models.IntegerField(blank=True, null=True)
    mothers_name = models.CharField(max_length=255, blank=True, null=True)
    fathers_or_husbands_name = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    country = models.IntegerField(blank=True, null=True)
    provience = models.IntegerField(blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    municipality = models.CharField(max_length=255, blank=True, null=True)
    tole = models.CharField(max_length=255, blank=True, null=True)
    ward_add = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    age_type = models.CharField(max_length=255, blank=True, null=True)
    marital_status = models.IntegerField(blank=True, null=True)
    death_date_bs = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    emergency_pat_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'death_register'


class DefaultDepartmentDiscountPercent(models.Model):
    dept_id = models.IntegerField()
    discount_group_id = models.IntegerField()
    discount_group_percent_id = models.IntegerField()
    default_discount = models.FloatField()
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'default_department_discount_percent'


class DefaultDepartmentDiscountPercentTemplate(models.Model):
    dept_id = models.IntegerField()
    discount_template_id = models.IntegerField()
    default_discount = models.FloatField()
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'default_department_discount_percent_template'


class DeliverySite(models.Model):
    name = models.CharField(max_length=191, db_collation='utf8mb4_unicode_ci')
    address = models.CharField(max_length=191, db_collation='utf8mb4_unicode_ci')
    contact = models.CharField(max_length=191, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    description = models.TextField(db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delivery_site'


class Denominations(models.Model):
    title = models.IntegerField()
    status = models.CharField(max_length=8)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'denominations'


class DepartmentBudgets(models.Model):
    department_id = models.IntegerField()
    qty = models.FloatField()
    actual_budget = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department_budgets'


class DepartmentDoctor(models.Model):
    department = models.OneToOneField('Departments', models.DO_NOTHING, primary_key=True)  # The composite primary key (department_id, doctor_id) found, that is not supported. The first column is selected.
    doctor = models.ForeignKey('Doctors', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'department_doctor'
        unique_together = (('department', 'doctor'),)


class DepartmentDoctors(models.Model):
    department_id = models.IntegerField()
    doctor_id = models.IntegerField()
    department_type_id = models.IntegerField()
    default_doctor = models.IntegerField()
    display_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'department_doctors'


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


class DepartmentTypes(models.Model):
    department_type_id = models.AutoField(primary_key=True)
    department_type_name = models.CharField(max_length=255)
    active = models.IntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department_types'


class DepartmentWiseBudgets(models.Model):
    department = models.ForeignKey('Departments', models.DO_NOTHING)
    patient_qty = models.IntegerField()
    service_qty = models.IntegerField()
    amount = models.FloatField()
    fiscalyear = models.CharField(max_length=255)
    month = models.CharField(max_length=255)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='updated_by', related_name='departmentwisebudgets_updated_by_set', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    source_name = models.CharField(max_length=255)
    per_day_amount = models.FloatField()
    per_day_patient_qty = models.FloatField()
    per_day_service_qty = models.FloatField()

    class Meta:
        managed = False
        db_table = 'department_wise_budgets'


class DepartmentWiseSharing(models.Model):
    doctor = models.ForeignKey('Doctors', models.DO_NOTHING)
    department = models.ForeignKey('Departments', models.DO_NOTHING)
    share_percent = models.FloatField()
    share_amount = models.FloatField()
    share_wo_anesthetist_per = models.FloatField()
    share_wo_anesthetist_amount = models.FloatField()
    tds_percent = models.FloatField()
    share_additional_doctor_per = models.FloatField()
    share_additional_doctor_amount = models.FloatField()
    status = models.IntegerField()
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department_wise_sharing'


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


class DepartmentwiseDiscount(models.Model):
    dept = models.ForeignKey(Departments, models.DO_NOTHING)
    category_type = models.ForeignKey('PatientCategories', models.DO_NOTHING, db_column='category_type')
    rate_group_id = models.PositiveIntegerField()
    dept_discount = models.FloatField(blank=True, null=True)
    opd_discount = models.FloatField(blank=True, null=True)
    ipd_discount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departmentwise_discount'


class DepositTypes(models.Model):
    deposit_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deposit_types'


class DesignationSharings(models.Model):
    doctor_sharing_ipds_id = models.PositiveIntegerField()
    designation_id = models.PositiveIntegerField()
    share_percent = models.FloatField()
    share_amount = models.FloatField()
    share_wo_anesthetist_per = models.FloatField()
    share_wo_anesthetist_amount = models.FloatField()
    tds_percent = models.FloatField()
    doctor_id = models.IntegerField()
    doctor_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'designation_sharings'


class Designations(models.Model):
    designation = models.CharField(max_length=255)
    status = models.IntegerField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'designations'


class DeviceUsers(models.Model):
    user_id = models.PositiveBigIntegerField()
    user_type = models.CharField(max_length=191)
    registration_id = models.CharField(max_length=191)
    device_type = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device_users'


class Devices(models.Model):
    machine = models.ForeignKey('Machines', models.DO_NOTHING, blank=True, null=True)
    device_name = models.CharField(max_length=255)
    department_id = models.IntegerField()
    port = models.CharField(max_length=255)
    uuid = models.CharField(max_length=255)
    active = models.CharField(max_length=1)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    request_ip = models.CharField(max_length=15)
    branch = models.PositiveIntegerField()
    protocol = models.CharField(max_length=255)
    listen_ip = models.CharField(max_length=255)
    listen_port = models.CharField(max_length=255)
    server_ip = models.CharField(max_length=255)
    server_port = models.CharField(max_length=255)
    logmode = models.CharField(max_length=1)
    restart = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'devices'


class Diagnosis(models.Model):
    visit_id = models.IntegerField()
    patient_id = models.IntegerField()
    disease_name = models.CharField(max_length=191)
    disease_code = models.CharField(max_length=191, blank=True, null=True)
    is_icd = models.IntegerField()
    is_primary = models.IntegerField()
    confirmed = models.IntegerField()
    confirmed_by = models.IntegerField(blank=True, null=True)
    active = models.IntegerField()
    remarks = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    start_date = models.CharField(max_length=191, blank=True, null=True)
    duration = models.CharField(max_length=191, blank=True, null=True)
    day = models.CharField(max_length=191, blank=True, null=True)
    ipd_id = models.IntegerField()
    er_id = models.IntegerField()
    display_order = models.IntegerField()
    diseasename = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diagnosis'


class DialysisPatients(models.Model):
    pat_id = models.PositiveIntegerField()
    pat_type = models.PositiveIntegerField()
    bed_id = models.PositiveIntegerField(blank=True, null=True)
    admission_date = models.CharField(max_length=255, blank=True, null=True)
    admission_date_eng = models.CharField(max_length=255, blank=True, null=True)
    admission_time = models.TimeField(blank=True, null=True)
    dept_id = models.PositiveIntegerField()
    deposited_by = models.PositiveIntegerField(blank=True, null=True)
    discharge_by = models.PositiveIntegerField(blank=True, null=True)
    discharge_date = models.CharField(max_length=255, blank=True, null=True)
    discharge_date_eng = models.CharField(max_length=255, blank=True, null=True)
    branch_id = models.PositiveIntegerField()
    category_type = models.PositiveIntegerField()
    discount_group_id = models.PositiveIntegerField(blank=True, null=True)
    discount_group_percent_id = models.PositiveIntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    consultant = models.ForeignKey('Doctors', models.DO_NOTHING, blank=True, null=True)
    refer_by = models.ForeignKey('Doctors', models.DO_NOTHING, db_column='refer_by', related_name='dialysispatients_refer_by_set', blank=True, null=True)
    in_pat_id = models.PositiveIntegerField()
    is_ipd_transfer = models.IntegerField()
    patage = models.IntegerField(blank=True, null=True)
    patno = models.CharField(max_length=100, blank=True, null=True)
    patage_type = models.CharField(max_length=1)
    discharge_type = models.IntegerField()
    is_category_type_update = models.IntegerField()
    ready_to_discharge_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dialysis_patients'


class DietGroup(models.Model):
    diet_group = models.CharField(max_length=255)
    icon_url = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diet_group'


class DietGroupDetails(models.Model):
    diet_group_id = models.PositiveIntegerField()
    diet_group_name = models.CharField(max_length=255, blank=True, null=True)
    diets_info = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diet_group_details'


class DietGroups(models.Model):
    group_name = models.CharField(max_length=255)
    icon_url = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diet_groups'


class DigestiveSystems(models.Model):
    visit_id = models.IntegerField()
    medicaldetails_id = models.IntegerField()
    patient_id = models.IntegerField()
    tonsils = models.TextField(blank=True, null=True)
    abdomen_disten = models.IntegerField()
    abdomen_tender = models.IntegerField()
    liver_enlarge = models.IntegerField()
    stool_freq = models.TextField(blank=True, null=True)
    stool_consistency = models.TextField(blank=True, null=True)
    usg_finding = models.TextField(blank=True, null=True)
    spleen_palpable = models.IntegerField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    ipd_id = models.IntegerField()
    er_id = models.IntegerField()
    bowel_sound = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'digestive_systems'


class DischargeSummaries(models.Model):
    in_pat_id = models.IntegerField()
    pat_id = models.IntegerField()
    diagnosis = models.TextField()
    case_summary = models.TextField()
    patient_condition = models.CharField(max_length=255)
    treatment = models.TextField()
    clinical_notes = models.TextField()
    follow_up = models.TextField()
    advice = models.TextField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    pregnancy_status = models.IntegerField()
    gravida = models.CharField(max_length=255, blank=True, null=True)
    pregnancy_remarks = models.TextField(blank=True, null=True)
    abortion_status = models.IntegerField()
    abortion_type = models.CharField(max_length=255, blank=True, null=True)
    abortion_trimester = models.CharField(max_length=255, blank=True, null=True)
    death_status = models.IntegerField()
    death_type = models.CharField(max_length=255, blank=True, null=True)
    hospital_death_type = models.CharField(max_length=255, blank=True, null=True)
    parity = models.CharField(max_length=255, blank=True, null=True)
    abortus = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField()
    age_type = models.CharField(max_length=255, blank=True, null=True)
    branch = models.CharField(max_length=45, blank=True, null=True)
    death_reason = models.TextField(blank=True, null=True)
    gestation = models.CharField(max_length=255, blank=True, null=True)
    initial_diagnosis = models.TextField()
    birth_delete_status = models.IntegerField()
    approval_status = models.IntegerField(blank=True, null=True)
    approved_by = models.IntegerField(blank=True, null=True)
    check_flags_data = models.TextField(blank=True, null=True)
    complaint_notes = models.TextField(blank=True, null=True)
    discharge_type = models.CharField(max_length=255, blank=True, null=True)
    discharge_type_status = models.IntegerField()
    emergency_pat_id = models.IntegerField(blank=True, null=True)
    history_notes = models.TextField(blank=True, null=True)
    impression_section1 = models.TextField(blank=True, null=True)
    impression_section2 = models.TextField(blank=True, null=True)
    impression_title = models.CharField(max_length=255, blank=True, null=True)
    past_history = models.TextField(blank=True, null=True)
    psysiotherapy = models.TextField(blank=True, null=True)
    registrar_approval_status = models.IntegerField()
    registrar_approved_by = models.IntegerField(blank=True, null=True)
    registrar_rejection_message = models.TextField(blank=True, null=True)
    rejection_message = models.CharField(max_length=255, blank=True, null=True)
    procedure = models.TextField(blank=True, null=True)
    approval_source = models.CharField(max_length=255, blank=True, null=True)
    approve_doc_id = models.IntegerField(blank=True, null=True)
    dialysis_pat_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discharge_summaries'


class DischargeSummaryApprovalHistory(models.Model):
    discharge_summary = models.ForeignKey(DischargeSummaries, models.DO_NOTHING)
    rejection_message = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='updated_by')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    registrar_approval_status = models.IntegerField()
    registrar_rejection_message = models.TextField(blank=True, null=True)
    registrar_approved_by = models.IntegerField(blank=True, null=True)
    approved_by = models.IntegerField(blank=True, null=True)
    approve_doc_id = models.IntegerField(blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discharge_summary_approval_history'


class DischargeTypeSetups(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discharge_type_setups'


class DiscountGroupPercent(models.Model):
    discount_group = models.ForeignKey('DiscountGroups', models.DO_NOTHING, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    agent_login = models.IntegerField()
    discount_head = models.CharField(max_length=255)
    discount_percentage = models.FloatField()
    autoload = models.IntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    discount_cat = models.PositiveIntegerField()
    active = models.IntegerField()
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    warning_amount = models.FloatField(blank=True, null=True)
    max_amount = models.FloatField(blank=True, null=True)
    valid_from = models.CharField(max_length=255, blank=True, null=True)
    valid_to = models.CharField(max_length=255, blank=True, null=True)
    never_expiry = models.IntegerField()
    one_time_discount = models.IntegerField()
    partner_id = models.IntegerField(blank=True, null=True)
    outsource_discount_percentage = models.FloatField()
    credit_limit_status = models.IntegerField()
    credit_limit_amount = models.FloatField(blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discount_group_percent'


class DiscountGroups(models.Model):
    discount_group = models.CharField(max_length=255)
    active = models.IntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_credit_client = models.IntegerField()
    is_party = models.IntegerField()
    branch = models.PositiveIntegerField()
    is_bipannanagarik = models.IntegerField(db_column='is_bipannaNagarik')  # Field name made lowercase.
    is_insurance = models.IntegerField()
    is_pharmacy = models.IntegerField()
    no_ticket_charge = models.IntegerField(blank=True, null=True)
    r_center_id = models.IntegerField()
    is_ssf = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'discount_groups'


class DiscountTemplateDetails(models.Model):
    discount_template_id = models.PositiveIntegerField()
    item = models.ForeignKey('Items', models.DO_NOTHING)
    rate_type = models.IntegerField()
    discount = models.FloatField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    discount_amt = models.FloatField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discount_template_details'


class DiscountTemplates(models.Model):
    template = models.CharField(max_length=255)
    is_active = models.IntegerField()
    branch = models.PositiveIntegerField()
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discount_templates'


class DiscountTypeTestPivot(models.Model):
    discount_group_percent = models.ForeignKey(DiscountGroupPercent, models.DO_NOTHING)
    item = models.ForeignKey('Items', models.DO_NOTHING)
    rate_type = models.IntegerField()
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discount_type_test_pivot'


class DisplaySetup(models.Model):
    name = models.CharField(unique=True, max_length=255)
    token = models.CharField(max_length=255)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'display_setup'


class DispositionMethods(models.Model):
    method = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disposition_methods'


class Districts(models.Model):
    district = models.CharField(max_length=255)
    zone = models.ForeignKey('Zones', models.DO_NOTHING, blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'districts'


class DoctorConsultationSharingTemplate(models.Model):
    template_name = models.CharField(max_length=255)
    share_percent = models.FloatField()
    share_amount = models.FloatField()
    share_wo_anesthetist_per = models.FloatField()
    share_wo_anesthetist_amount = models.FloatField()
    tds_percent = models.FloatField()
    status = models.IntegerField()
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    publish_date = models.DateTimeField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctor_consultation_sharing_template'


class DoctorListAppointments(models.Model):
    dept_id = models.IntegerField()
    doc_name = models.CharField(max_length=255)
    dept_name = models.CharField(max_length=255)
    organization_name = models.CharField(max_length=255)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'doctor_list_appointments'


class DoctorSharingInformation(models.Model):
    doctor_id = models.PositiveIntegerField()
    doctor_name = models.CharField(max_length=255)
    doctor_share_per = models.FloatField()
    tds = models.FloatField()
    share_amount = models.FloatField()
    tds_amount = models.FloatField()
    item_id = models.PositiveIntegerField()
    test_id = models.PositiveIntegerField()
    test_item_name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    rate = models.FloatField()
    tax_amount = models.FloatField()
    amount = models.FloatField()
    patient_id = models.PositiveIntegerField()
    patient_member_id = models.PositiveIntegerField()
    patient_cat_id = models.PositiveIntegerField()
    master_bill_id = models.PositiveIntegerField()
    bill_detail_id = models.PositiveIntegerField()
    discount_group_id = models.PositiveIntegerField()
    discount_group_percent_id = models.PositiveIntegerField()
    bill_no = models.CharField(max_length=255)
    bill_discount_per = models.FloatField()
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctor_sharing_information'


class DoctorSharingIpds(models.Model):
    department_type_id = models.PositiveIntegerField()
    department_id = models.PositiveIntegerField()
    item_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    category_id = models.IntegerField()
    referal_amount = models.FloatField()
    referal_per = models.FloatField()

    class Meta:
        managed = False
        db_table = 'doctor_sharing_ipds'


class DoctorSharings(models.Model):
    doctor_id = models.IntegerField()
    department_id = models.IntegerField()
    item_id = models.IntegerField()
    item_name = models.CharField(max_length=255)
    rate = models.DecimalField(max_digits=10, decimal_places=4)
    doc_share_per = models.DecimalField(max_digits=10, decimal_places=4)
    tds = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctor_sharings'


class Doctors(models.Model):
    doctor_name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    nmc_number = models.PositiveIntegerField()
    specialization = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    doctor_title = models.CharField(max_length=255)
    total = models.FloatField()
    amount = models.FloatField()
    tax = models.FloatField()
    followup_total = models.FloatField()
    followup_amount = models.FloatField()
    followup_tax = models.FloatField()
    branch = models.PositiveIntegerField()
    active = models.IntegerField()
    sharing_doctor_id = models.IntegerField()
    is_pharmacy = models.IntegerField()
    image = models.TextField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    online = models.IntegerField()
    display_order = models.IntegerField()
    account_id = models.IntegerField()
    speciality_id = models.IntegerField(blank=True, null=True)
    enable_sharing = models.IntegerField(blank=True, null=True)
    is_sharing_default = models.IntegerField(blank=True, null=True)
    sharing_inherit_from = models.PositiveIntegerField(blank=True, null=True)
    is_team = models.IntegerField()
    cost_center = models.ForeignKey(AccCostCenter, models.DO_NOTHING, blank=True, null=True)
    consultant_incharge_tds_per = models.FloatField()
    consultant_tds_per = models.FloatField()
    service_refer_by_tds_per = models.FloatField()
    refer_by_tds_per = models.FloatField()
    sharing_exceptional_percentage = models.FloatField(blank=True, null=True)
    followup_day = models.IntegerField(blank=True, null=True)
    consultant_incharge_tds_per_ipd = models.FloatField()
    consultant_tds_per_ipd = models.FloatField()
    service_refer_by_tds_per_ipd = models.FloatField()
    refer_by_tds_per_ipd = models.FloatField()
    account_id_ipd = models.IntegerField()
    dental_speciality_id = models.IntegerField()
    additional_consultant_tds_per_ipd = models.FloatField()
    contact = models.CharField(max_length=255, blank=True, null=True)
    enable_sharing_additional_consultant = models.IntegerField()
    is_batch_wise = models.IntegerField(blank=True, null=True)
    is_team_doctor = models.IntegerField()
    remarks = models.TextField(blank=True, null=True)
    room_no = models.CharField(max_length=100, blank=True, null=True)
    users_id = models.TextField(blank=True, null=True)
    whatsapp_number = models.CharField(max_length=255, blank=True, null=True)
    enable_graph_in_opd_prescription = models.IntegerField(blank=True, null=True)
    enable_vitals_prescription = models.IntegerField()
    opd_mri_service_referal_share_no_tds = models.CharField(max_length=100, blank=True, null=True)
    ipd_mri_service_referal_share_no_tds = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctors'


class Drugs(models.Model):
    drug_name = models.CharField(max_length=255)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    drug_code = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drugs'


class EcgReports(models.Model):
    sample_code = models.CharField(max_length=255)
    item_id = models.PositiveIntegerField()
    sample_collection_id = models.PositiveIntegerField()
    patient_id = models.PositiveIntegerField(blank=True, null=True)
    test_id = models.PositiveIntegerField(blank=True, null=True)
    department_id = models.PositiveIntegerField(blank=True, null=True)
    verified_by = models.IntegerField(blank=True, null=True)
    verified_at = models.DateTimeField(blank=True, null=True)
    verify = models.IntegerField()
    provision_verified_by = models.IntegerField()
    provision_verified_at = models.DateTimeField()
    status = models.FloatField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    rvid_value_diastole = models.FloatField(blank=True, null=True)
    rvid_value_systole = models.FloatField(blank=True, null=True)
    ivs_value_diastole = models.FloatField(blank=True, null=True)
    ivs_value_systole = models.FloatField(blank=True, null=True)
    lvid_value_diastole = models.FloatField(blank=True, null=True)
    lvid_value_systole = models.FloatField(blank=True, null=True)
    pw_value_diastole = models.FloatField(blank=True, null=True)
    pw_value_systole = models.FloatField(blank=True, null=True)
    fs_value_diastole = models.FloatField(blank=True, null=True)
    ef_value_diastole = models.FloatField(blank=True, null=True)
    aorta_value = models.FloatField(blank=True, null=True)
    la_value = models.FloatField(blank=True, null=True)
    acs_value = models.FloatField(blank=True, null=True)
    edv_value = models.FloatField(blank=True, null=True)
    esv_value = models.FloatField(blank=True, null=True)
    ef_value = models.FloatField(blank=True, null=True)
    pulmonary_valve_status = models.CharField(max_length=255, blank=True, null=True)
    pulmonary_valve_mean_velocity = models.FloatField(blank=True, null=True)
    pulmonary_valve_mean_gradient = models.FloatField(blank=True, null=True)
    pulmonary_valve_peak_velocity = models.FloatField(blank=True, null=True)
    pulmonary_valve_peak_gradient = models.FloatField(blank=True, null=True)
    pulmonary_regurgitation = models.CharField(max_length=255, blank=True, null=True)
    mitral_valve_aml_status = models.CharField(max_length=255, blank=True, null=True)
    mitral_valve_pml_status = models.CharField(max_length=255, blank=True, null=True)
    mitral_valve_planimetry = models.FloatField(blank=True, null=True)
    mitral_valve_pressure_half_time = models.FloatField(blank=True, null=True)
    mitral_valve_mean_velocity = models.FloatField(blank=True, null=True)
    mitral_valve_mean_gradient = models.FloatField(blank=True, null=True)
    mitral_valve_e_velocity = models.FloatField(blank=True, null=True)
    mitral_valve_e_gradient = models.FloatField(blank=True, null=True)
    mitral_valve_a_velocity = models.FloatField(blank=True, null=True)
    mitral_valve_a_gradient = models.FloatField(blank=True, null=True)
    mitral_regurgitation = models.CharField(max_length=255, blank=True, null=True)
    aortic_valve_status = models.CharField(max_length=255, blank=True, null=True)
    aortic_valve_mean_velocity = models.FloatField(blank=True, null=True)
    aortic_valve_mean_gradient = models.FloatField(blank=True, null=True)
    aortic_valve_peak_velocity = models.FloatField(blank=True, null=True)
    aortic_valve_peak_gradient = models.FloatField(blank=True, null=True)
    aortic_regurgitation = models.CharField(max_length=255, blank=True, null=True)
    tricuspid_valve_status = models.CharField(max_length=255, blank=True, null=True)
    tricuspid_valve_mean_velocity = models.FloatField(blank=True, null=True)
    tricuspid_valve_mean_gradient = models.FloatField(blank=True, null=True)
    tricuspid_valve_peak_velocity = models.FloatField(blank=True, null=True)
    tricuspid_valve_peak_gradient = models.FloatField(blank=True, null=True)
    tricuspid_regurgitation = models.CharField(max_length=255, blank=True, null=True)
    tricuspid_valve_tr_velocity = models.FloatField(blank=True, null=True)
    tricuspid_valve_tr_pressuce_gradient = models.FloatField(blank=True, null=True)
    intra_atrial_septum = models.CharField(max_length=255, blank=True, null=True)
    intra_ventricular_septum = models.CharField(max_length=255, blank=True, null=True)
    pericardium = models.CharField(max_length=255, blank=True, null=True)
    wall_motion = models.CharField(max_length=255, blank=True, null=True)
    final_impression = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ecg_reports'


class ElectronicPayVendor(models.Model):
    name = models.CharField(max_length=255)
    logo = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'electronic_pay_vendor'


class EmergencyRegistration(models.Model):
    pat = models.ForeignKey('Patients', models.DO_NOTHING)
    pat_type = models.PositiveIntegerField()
    bed_id = models.PositiveIntegerField(blank=True, null=True)
    admission_date = models.DateField(blank=True, null=True)
    admission_date_eng = models.DateField(blank=True, null=True)
    admission_time = models.TimeField(blank=True, null=True)
    dept_id = models.PositiveIntegerField()
    deposited_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='deposited_by', blank=True, null=True)
    discharge_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='discharge_by', related_name='emergencyregistration_discharge_by_set', blank=True, null=True)
    discharge_date = models.DateField(blank=True, null=True)
    discharge_date_eng = models.DateField(blank=True, null=True)
    branch_id = models.PositiveIntegerField()
    category_type = models.PositiveIntegerField()
    discount_group = models.ForeignKey(DiscountGroups, models.DO_NOTHING, blank=True, null=True)
    discount_group_percent = models.ForeignKey(DiscountGroupPercent, models.DO_NOTHING, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', related_name='emergencyregistration_created_by_set', blank=True, null=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='updated_by', related_name='emergencyregistration_updated_by_set', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    pat_admission_type_id = models.PositiveIntegerField(blank=True, null=True)
    consultant = models.ForeignKey(Doctors, models.DO_NOTHING, blank=True, null=True)
    refer_by = models.ForeignKey(Doctors, models.DO_NOTHING, db_column='refer_by', related_name='emergencyregistration_refer_by_set', blank=True, null=True)
    is_ipd_transfer = models.IntegerField()
    admitted_triage_id = models.IntegerField(blank=True, null=True)
    patage = models.IntegerField(blank=True, null=True)
    patno = models.CharField(max_length=100, blank=True, null=True)
    ref_hospital = models.CharField(max_length=255, blank=True, null=True)
    ref_hospital_id = models.PositiveIntegerField(blank=True, null=True)
    triage_id = models.PositiveIntegerField()
    patage_type = models.CharField(max_length=1)
    death_status = models.IntegerField()
    death_time = models.DateTimeField(blank=True, null=True)
    discharge_type = models.IntegerField()
    is_category_type_update = models.IntegerField()
    ready_to_discharge_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emergency_registration'


class EndocrineSystems(models.Model):
    visit_id = models.IntegerField()
    medicaldetails_id = models.IntegerField()
    patient_id = models.IntegerField()
    facial_app = models.TextField(blank=True, null=True)
    ketone_smell_status = models.IntegerField()
    ketone_smell_remarks = models.TextField(blank=True, null=True)
    saving_freq = models.IntegerField(blank=True, null=True)
    hirsutism = models.TextField(blank=True, null=True)
    eyes_sign_status = models.IntegerField()
    eyes_sign_remarks = models.TextField(blank=True, null=True)
    exopthalmos_status = models.IntegerField()
    exopthalmos_remarks = models.TextField(blank=True, null=True)
    tremor_status = models.IntegerField()
    tremor_remarks = models.TextField(blank=True, null=True)
    lid_retract_status = models.IntegerField()
    lid_retract_remarks = models.TextField(blank=True, null=True)
    visual_dist_status = models.IntegerField()
    visual_dist_remarks = models.TextField(blank=True, null=True)
    palpation_status = models.IntegerField()
    palpation_remarks = models.TextField(blank=True, null=True)
    thyroid_palpation_status = models.IntegerField()
    thyroid_palpation_remarks = models.TextField(blank=True, null=True)
    regional_lymp_status = models.IntegerField()
    regional_lymp_remarks = models.TextField(blank=True, null=True)
    gynecomastia_status = models.IntegerField()
    gynecomastia_remarks = models.TextField(blank=True, null=True)
    galactorrhoea_status = models.IntegerField()
    galactorrhoea_remarks = models.TextField(blank=True, null=True)
    peripheral_pulses = models.TextField(blank=True, null=True)
    other = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    ipd_id = models.IntegerField()
    er_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'endocrine_systems'


class Ent(models.Model):
    patient_id = models.IntegerField()
    visit_id = models.IntegerField()
    title_name = models.TextField()
    sub_title = models.TextField()
    checked_status = models.IntegerField()
    value = models.TextField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ent'


class EprescriptionAnalysisDashboardPermission(models.Model):
    display_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    show = models.IntegerField()
    div_icon = models.CharField(max_length=255)
    font_icon = models.CharField(max_length=255)
    font_class = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    display_type = models.CharField(max_length=255)
    cursor_pointer = models.IntegerField()
    user = models.ForeignKey('Users', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eprescription_analysis_dashboard_permission'


class EquipmentUtilisationMaster(models.Model):
    equipment_name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    fiscal_year = models.ForeignKey(AccFiscalYear, models.DO_NOTHING)
    month = models.PositiveIntegerField()
    patient_qty = models.IntegerField()
    service_qty = models.IntegerField()
    cancel_status = models.IntegerField()
    amount = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    avg_service_time = models.FloatField(blank=True, null=True)
    breakdown_period = models.IntegerField()
    delete_at = models.DateTimeField(blank=True, null=True)
    total_available_days = models.IntegerField()
    total_available_time = models.IntegerField()
    total_no_equipment = models.IntegerField(blank=True, null=True)
    show_in_mis_reports = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'equipment_utilisation_master'


class EquipmentUtilisationMasterdetail(models.Model):
    equipment_utilisation_master_id = models.PositiveIntegerField()
    service = models.ForeignKey('Items', models.DO_NOTHING)
    cancel_status = models.IntegerField()
    delete_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    avg_service_time = models.FloatField()
    patient_qty = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'equipment_utilisation_masterdetail'


class ErrorLogs(models.Model):
    instance = models.CharField(max_length=255)
    patient_id = models.IntegerField(blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True)
    doctor_id = models.IntegerField(blank=True, null=True)
    item_id = models.IntegerField(blank=True, null=True)
    master_bill_id = models.IntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=255)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    error_request = models.TextField()

    class Meta:
        managed = False
        db_table = 'error_logs'


class ExerciseList(models.Model):
    name = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exercise_list'


class ExternalCategories(models.Model):
    categories = models.CharField(max_length=20, blank=True, null=True)
    status = models.IntegerField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'external_categories'


class ExternalResultEntries(models.Model):
    patient_id = models.PositiveIntegerField(blank=True, null=True)
    test_id = models.PositiveIntegerField(blank=True, null=True)
    parameter_id = models.PositiveIntegerField(blank=True, null=True)
    is_panel = models.IntegerField()
    is_package = models.IntegerField()
    package_id = models.IntegerField()
    package_name = models.CharField(max_length=191, blank=True, null=True)
    panel_id = models.PositiveIntegerField(blank=True, null=True)
    title = models.IntegerField()
    value = models.CharField(max_length=191, blank=True, null=True)
    remarks = models.CharField(max_length=191, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    visit_id = models.IntegerField()
    source = models.CharField(max_length=191)
    source_date = models.CharField(max_length=191)
    deleted_at = models.DateTimeField(blank=True, null=True)
    ref_min = models.CharField(max_length=191, blank=True, null=True)
    ref_max = models.CharField(max_length=191, blank=True, null=True)
    q_range = models.TextField(blank=True, null=True)
    unit_id = models.IntegerField(blank=True, null=True)
    unit_name = models.CharField(max_length=191, blank=True, null=True)
    ipd_id = models.IntegerField()
    er_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'external_result_entries'


class EyeDryWet(models.Model):
    patient_id = models.IntegerField()
    visit_id = models.IntegerField()
    dry_wet_flag = models.IntegerField(blank=True, null=True)
    right_eye_sph = models.CharField(max_length=191, blank=True, null=True)
    right_eye_cyl = models.CharField(max_length=191, blank=True, null=True)
    right_eye_axis = models.CharField(max_length=191, blank=True, null=True)
    right_eye_vision = models.CharField(max_length=191, blank=True, null=True)
    left_eye_sph = models.CharField(max_length=191, blank=True, null=True)
    left_eye_cyl = models.CharField(max_length=191, blank=True, null=True)
    left_eye_axis = models.CharField(max_length=191, blank=True, null=True)
    left_eye_vision = models.CharField(max_length=191, blank=True, null=True)
    addition_value = models.CharField(max_length=191, blank=True, null=True)
    addition_select = models.CharField(max_length=191, blank=True, null=True)
    ipd_dipd = models.CharField(max_length=191, blank=True, null=True)
    ipd_nipd = models.CharField(max_length=191, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    right_eye_sph_value = models.CharField(max_length=191, blank=True, null=True)
    right_eye_cyl_value = models.CharField(max_length=191, blank=True, null=True)
    left_eye_sph_value = models.CharField(max_length=191, blank=True, null=True)
    left_eye_cyl_value = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eye_dry_wet'


class EyeHistory(models.Model):
    patient_id = models.IntegerField()
    visit_id = models.IntegerField()
    visit_date = models.DateField()
    visit_type = models.CharField(max_length=191)
    past_history = models.TextField(blank=True, null=True)
    prior_surgery = models.TextField(blank=True, null=True)
    current_medications = models.TextField(blank=True, null=True)
    systemic_disease = models.TextField(blank=True, null=True)
    allergy = models.TextField(blank=True, null=True)
    additional_information = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eye_history'


class EyeHistoryVisitReason(models.Model):
    history_id = models.IntegerField()
    visit_reason = models.CharField(max_length=191)
    reason_duration = models.IntegerField()
    duration_type = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'eye_history_visit_reason'


class EyeInvestigation(models.Model):
    patient_id = models.IntegerField()
    visit_id = models.IntegerField()
    blood_pressure = models.CharField(max_length=191, blank=True, null=True)
    orthoptic_evaluation = models.CharField(max_length=191, blank=True, null=True)
    schirmer_test_value = models.CharField(max_length=191, blank=True, null=True)
    schirmer_test_re = models.CharField(max_length=191, blank=True, null=True)
    schirmer_test_le = models.CharField(max_length=191, blank=True, null=True)
    probing_test_re = models.CharField(max_length=191, blank=True, null=True)
    probing_test_le = models.CharField(max_length=191, blank=True, null=True)
    syringing_re = models.CharField(max_length=191, blank=True, null=True)
    syringing_le = models.CharField(max_length=191, blank=True, null=True)
    iop_value = models.CharField(max_length=191, blank=True, null=True)
    iop_re = models.CharField(max_length=191, blank=True, null=True)
    iop_le = models.CharField(max_length=191, blank=True, null=True)
    occular_photography_ffa = models.CharField(max_length=191, blank=True, null=True)
    occular_photography_fundus_photo = models.CharField(max_length=191, blank=True, null=True)
    occular_photography_as_photo = models.CharField(max_length=191, blank=True, null=True)
    perimetry_value = models.CharField(max_length=191, blank=True, null=True)
    perimetry_le = models.CharField(max_length=191, blank=True, null=True)
    perimetry_re = models.CharField(max_length=191, blank=True, null=True)
    color_vision_re = models.CharField(max_length=191, blank=True, null=True)
    color_vision_le = models.CharField(max_length=191, blank=True, null=True)
    biometry_axial_length_re = models.CharField(max_length=191, blank=True, null=True)
    biometry_axial_length_le = models.CharField(max_length=191, blank=True, null=True)
    keratometry_k1_re = models.CharField(max_length=191, blank=True, null=True)
    keratometry_k1_le = models.CharField(max_length=191, blank=True, null=True)
    keratometry_k2_re = models.CharField(max_length=191, blank=True, null=True)
    keratometry_k2_le = models.CharField(max_length=191, blank=True, null=True)
    iol_power_select_re = models.CharField(max_length=191, blank=True, null=True)
    iol_power_value_re = models.CharField(max_length=191, blank=True, null=True)
    iol_power_select_le = models.CharField(max_length=191, blank=True, null=True)
    iol_power_value_le = models.CharField(max_length=191, blank=True, null=True)
    irrigation_re = models.CharField(max_length=191, blank=True, null=True)
    irrigation_le = models.CharField(max_length=191, blank=True, null=True)
    tbut_le = models.CharField(max_length=191, blank=True, null=True)
    tbut_re = models.CharField(max_length=191, blank=True, null=True)
    bscan_le = models.CharField(max_length=191, blank=True, null=True)
    bscan_re = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    plan_of_action_le = models.CharField(max_length=191, blank=True, null=True)
    plan_of_action_re = models.CharField(max_length=191, blank=True, null=True)
    oct_scan_le = models.CharField(max_length=191, blank=True, null=True)
    oct_scan_re = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eye_investigation'


class EyeIopGonio(models.Model):
    patient_id = models.IntegerField()
    visit_id = models.IntegerField()
    time = models.CharField(max_length=191, blank=True, null=True)
    method = models.CharField(max_length=191, blank=True, null=True)
    right_iop = models.CharField(max_length=191, blank=True, null=True)
    top_od = models.CharField(max_length=191, blank=True, null=True)
    left_od = models.CharField(max_length=191, blank=True, null=True)
    bottom_od = models.CharField(max_length=191, blank=True, null=True)
    right_od = models.CharField(max_length=191, blank=True, null=True)
    left_iop = models.CharField(max_length=191, blank=True, null=True)
    top_os = models.CharField(max_length=191, blank=True, null=True)
    left_os = models.CharField(max_length=191, blank=True, null=True)
    bottom_os = models.CharField(max_length=191, blank=True, null=True)
    right_os = models.CharField(max_length=191, blank=True, null=True)
    glaucoma_comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eye_iop_gonio'


class FailedJobs(models.Model):
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class FeedbackAnswers(models.Model):
    qn_id = models.IntegerField()
    qn_type = models.CharField(max_length=255, db_collation='utf8mb3_unicode_ci')
    nep_ans = models.CharField(max_length=255, db_collation='utf8mb3_unicode_ci')
    eng_ans = models.CharField(max_length=255, db_collation='utf8mb3_unicode_ci')
    has_text_field = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='deleted_by', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feedback_answers'


class FeedbackHeading(models.Model):
    nep_hed = models.CharField(max_length=255, blank=True, null=True)
    eng_hed = models.CharField(max_length=255, blank=True, null=True)
    form_type = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='deleted_by', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feedback_heading'


class FeedbackQuestions(models.Model):
    header_id = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField()
    nep_qn = models.CharField(max_length=255)
    eng_qn = models.CharField(max_length=255)
    qn_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='deleted_by', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feedback_questions'


class FeedbackUserAnswers(models.Model):
    qn_id = models.IntegerField()
    ans_id = models.IntegerField()
    patient_id = models.IntegerField(blank=True, null=True)
    visit_id = models.IntegerField(blank=True, null=True)
    in_pat_id = models.IntegerField(blank=True, null=True)
    text = models.CharField(max_length=255)
    user_ans_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feedback_user_answers'


class FinalIpMig(models.Model):
    patient_id = models.CharField(max_length=11, blank=True, null=True)
    discharge_date = models.CharField(max_length=10, blank=True, null=True)
    discharge_date_nep = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'final_ip_mig'


class FingerTemplates(models.Model):
    type_id = models.IntegerField()
    type = models.CharField(max_length=1)
    template = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'finger_templates'


class FixedAssetProjectedTurnover(models.Model):
    fixed_asset = models.ForeignKey('InvCatalogues', models.DO_NOTHING)
    service = models.ForeignKey('Items', models.DO_NOTHING)
    source_name = models.CharField(max_length=255)
    patient_qty = models.IntegerField()
    service_qty = models.IntegerField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='updated_by', related_name='fixedassetprojectedturnover_updated_by_set', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    fiscal_year = models.ForeignKey(AccFiscalYear, models.DO_NOTHING)
    month = models.PositiveIntegerField()
    fiscalyear = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fixed_asset_projected_turnover'


class Floors(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    is_package_applied_for_bed_charge = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'floors'


class FluidManagement(models.Model):
    patient_id = models.IntegerField()
    inpatient_id = models.IntegerField()
    source = models.IntegerField()
    time = models.CharField(max_length=191, blank=True, null=True)
    name = models.CharField(max_length=191, blank=True, null=True)
    volume = models.FloatField()
    fluid_type = models.IntegerField()
    remarks = models.CharField(max_length=191, blank=True, null=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    er_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fluid_management'


class FonePayRequests(models.Model):
    patient_id = models.PositiveIntegerField()
    in_pat_id = models.PositiveIntegerField()
    emergency_pat_id = models.PositiveIntegerField()
    dialysis_pat_id = models.PositiveIntegerField()
    amt = models.FloatField()
    qty = models.IntegerField()
    remark_one = models.TextField(blank=True, null=True)
    remark_two = models.TextField(blank=True, null=True)
    hash_value = models.TextField()
    prn = models.CharField(unique=True, max_length=255)
    response_status = models.IntegerField()
    initiated_by = models.PositiveIntegerField()
    vendor = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    request_from = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fone_pay_requests'


class FormFields(models.Model):
    field_type = models.CharField(max_length=255)
    label = models.CharField(max_length=255, blank=True, null=True)
    group_name = models.CharField(max_length=255, blank=True, null=True)
    sub_group_name = models.CharField(max_length=255, blank=True, null=True)
    option_fields = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    position = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    default = models.CharField(max_length=255, blank=True, null=True)
    unit = models.CharField(max_length=255, blank=True, null=True)
    default_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'form_fields'


class Freezers(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=12)
    active = models.CharField(max_length=1)
    description = models.TextField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by')
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'freezers'


class FrequencyMedication(models.Model):
    frequency = models.CharField(max_length=191)
    times = models.IntegerField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frequency_medication'


class GeneralOtregisters(models.Model):
    inpatient_id = models.IntegerField(blank=True, null=True)
    patient_id = models.IntegerField()
    bill_no = models.CharField(max_length=255)
    received_from = models.CharField(max_length=255, blank=True, null=True)
    pre_diagnosis = models.TextField(blank=True, null=True)
    post_diagnosis = models.TextField(blank=True, null=True)
    operative_procedure = models.CharField(max_length=255, blank=True, null=True)
    type_of_anesthesia = models.CharField(max_length=255, blank=True, null=True)
    operation_charge = models.CharField(max_length=255, blank=True, null=True)
    master_bill_id = models.PositiveIntegerField()
    bill_detail_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    desc_of_operation = models.TextField(blank=True, null=True)
    finding = models.TextField(blank=True, null=True)
    procedure = models.TextField(blank=True, null=True)
    free_code_no = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'general_otregisters'


class GenitalUrinaries(models.Model):
    visit_id = models.IntegerField()
    medicaldetails_id = models.IntegerField()
    patient_id = models.IntegerField()
    michturition_diff_status = models.IntegerField()
    michturition_diff_remarks = models.TextField(blank=True, null=True)
    michturition_freq = models.IntegerField(blank=True, null=True)
    oedema_status = models.IntegerField()
    oedema_remarks = models.TextField(blank=True, null=True)
    kidney_palpable = models.IntegerField()
    kidney_palpable_remarks = models.TextField(blank=True, null=True)
    bladder_palpable = models.IntegerField()
    bladder_palpable_remarks = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    ipd_id = models.IntegerField()
    er_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'genital_urinaries'


class HandoverDetails(models.Model):
    handover = models.ForeignKey('Handovers', models.DO_NOTHING)
    denomination_title = models.CharField(max_length=255)
    quantity = models.IntegerField()
    total = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'handover_details'


class Handovers(models.Model):
    sales_amount = models.FloatField()
    ho_amount = models.FloatField()
    net_amount = models.FloatField()
    ho_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='ho_by')
    ho_created_at = models.DateTimeField()
    to_amount = models.FloatField(blank=True, null=True)
    to_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='to_by', related_name='handovers_to_by_set')
    to_created_at = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=1)
    diff = models.FloatField()
    balance = models.FloatField()
    last_master_bill = models.ForeignKey('MasterBills', models.DO_NOTHING)
    status = models.CharField(max_length=1)
    handover_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_module = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'handovers'


class Helplines(models.Model):
    doctor = models.ForeignKey(Doctors, models.DO_NOTHING)
    patient = models.ForeignKey('Patients', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    complaint = models.CharField(max_length=255, blank=True, null=True)
    solution = models.CharField(max_length=255, blank=True, null=True)
    medication = models.CharField(max_length=255, blank=True, null=True)
    lab_test = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    ipd_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'helplines'


class HmisDataset(models.Model):
    name1 = models.CharField(max_length=255, blank=True, null=True)
    name2 = models.CharField(max_length=255, blank=True, null=True)
    dataelement = models.CharField(db_column='dataElement', max_length=255, blank=True, null=True)  # Field name made lowercase.
    categoryoptioncombo = models.CharField(db_column='categoryOptionCombo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data_set_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hmis_dataset'


class HmisPostReportLog(models.Model):
    user_id = models.IntegerField()
    instance = models.CharField(max_length=255)
    dataset = models.TextField(blank=True, null=True)
    year = models.CharField(max_length=255, blank=True, null=True)
    month = models.CharField(max_length=255, blank=True, null=True)
    complete = models.CharField(max_length=255, blank=True, null=True)
    log_type = models.PositiveIntegerField()
    remarks = models.CharField(max_length=255, blank=True, null=True)
    conflict = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hmis_post_report_log'


class HmisSetup(models.Model):
    key = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hmis_setup'


class HmisTestMappings(models.Model):
    name = models.CharField(max_length=255)
    test_id = models.IntegerField()
    parameter_id = models.IntegerField()
    branch = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    dataelement = models.CharField(db_column='dataElement', max_length=255, blank=True, null=True)  # Field name made lowercase.
    categoryoptioncombo = models.CharField(db_column='categoryOptionCombo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    positive_test_result = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hmis_test_mappings'


class Hospitals(models.Model):
    hospital_name = models.CharField(max_length=255)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hospitals'


class IcdCode(models.Model):
    code = models.CharField(max_length=191)
    disease = models.CharField(max_length=191)
    codewithseparator = models.CharField(db_column='CodeWithSeparator', max_length=100, blank=True, null=True)  # Field name made lowercase.
    longdescription = models.CharField(db_column='LongDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hippacovered = models.IntegerField(db_column='HippaCovered', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    is_icd = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    code_with_seperator = models.CharField(max_length=255)
    hippa_covered = models.IntegerField()
    long_des = models.TextField()

    class Meta:
        managed = False
        db_table = 'icd_code'


class IcdCodes(models.Model):
    code = models.CharField(max_length=191)
    disease = models.CharField(max_length=191)
    is_icd = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    code_with_seperator = models.CharField(max_length=255, blank=True, null=True)
    long_des = models.TextField()
    hippa_covered = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icd_codes'


class ImuSetups(models.Model):
    imu_url = models.CharField(max_length=255)
    imu_user_name = models.CharField(max_length=255)
    imu_password = models.TextField()
    imu_lab_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imu_setups'


class ImuSyncLogs(models.Model):
    patient_id = models.IntegerField()
    code = models.CharField(max_length=255)
    master_bill_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    age_type = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    province_id = models.IntegerField()
    district_id = models.IntegerField()
    municipality_id = models.IntegerField()
    ward = models.IntegerField(blank=True, null=True)
    tole = models.CharField(max_length=255, blank=True, null=True)
    registered_at = models.CharField(max_length=255)
    sample_collected_date = models.CharField(max_length=255)
    lab_received_date = models.CharField(max_length=255)
    lab_test_date = models.CharField(max_length=255)
    lab_test_time = models.CharField(max_length=255, blank=True, null=True)
    lab_result = models.CharField(max_length=255)
    status = models.IntegerField()
    message = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    imu_swab_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imu_sync_logs'


class InPatBedChargeIssueTracker(models.Model):
    in_pat_id = models.PositiveIntegerField(blank=True, null=True)
    issue_msg = models.TextField()
    issue_status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'in_pat_bed_charge_issue_tracker'


class InPatients(models.Model):
    pat_id = models.IntegerField()
    admission_date = models.CharField(max_length=255)
    admission_time = models.CharField(max_length=255, blank=True, null=True)
    pat_dept_id = models.IntegerField()
    u_dept_id = models.IntegerField()
    ref_dept_id = models.IntegerField(blank=True, null=True)
    consultant_dept_id = models.IntegerField()
    doctor_id = models.IntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deposited_by = models.CharField(max_length=255, blank=True, null=True)
    pat_type = models.IntegerField(blank=True, null=True)
    discharged_by = models.IntegerField(blank=True, null=True)
    discharged_date = models.DateField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    cancel_admission = models.IntegerField()
    admission_date_eng = models.DateField(blank=True, null=True)
    discharge_date_eng = models.CharField(max_length=255)
    branch = models.PositiveIntegerField()
    category_type = models.IntegerField()
    pharmacy_clearance = models.IntegerField()
    pharmacy_clearance_at = models.DateTimeField(blank=True, null=True)
    ot_waiting = models.IntegerField()
    discount_group_id = models.IntegerField(blank=True, null=True)
    discount_group_percent_id = models.IntegerField(blank=True, null=True)
    ref_doctor_id = models.IntegerField()
    pat_admission_type_id = models.PositiveIntegerField(blank=True, null=True)
    covid_status = models.CharField(max_length=255, blank=True, null=True)
    covid_vaccine_status = models.CharField(max_length=255, blank=True, null=True)
    case_type = models.CharField(max_length=255, blank=True, null=True)
    feedback_status = models.IntegerField()
    from_eme = models.IntegerField()
    additional_doctor_id = models.PositiveIntegerField(blank=True, null=True)
    credit_remark_by = models.IntegerField(blank=True, null=True)
    credit_remarks = models.TextField(blank=True, null=True)
    death_status = models.IntegerField()
    death_time = models.DateTimeField(blank=True, null=True)
    dialysis_pat_id = models.PositiveIntegerField()
    dialysis_transfer_status = models.IntegerField()
    emergency_pat_id = models.PositiveIntegerField(blank=True, null=True)
    from_dialysis = models.IntegerField()
    master_bill_no = models.CharField(max_length=255, blank=True, null=True)
    mother_inpat_id = models.IntegerField(blank=True, null=True)
    notifiable_disease = models.IntegerField()
    patage = models.IntegerField(blank=True, null=True)
    patno = models.CharField(max_length=100, blank=True, null=True)
    patstatus = models.CharField(max_length=255, blank=True, null=True)
    ready_to_discharge_date = models.DateTimeField(blank=True, null=True)
    ref_hospital = models.CharField(max_length=255, blank=True, null=True)
    ref_hospital_id = models.PositiveIntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    patage_type = models.CharField(max_length=1)
    bed_update_after_revert = models.IntegerField()
    birth_certificate_print_count = models.IntegerField()
    discharge_type = models.IntegerField(blank=True, null=True)
    is_category_type_update = models.IntegerField()
    notifiable_disease_remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'in_patients'


class IncomeHeads(models.Model):
    income_head = models.CharField(max_length=255)
    created_by = models.IntegerField()
    updated_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    mig_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'income_heads'


class InpatientAttachment(models.Model):
    patient_id = models.IntegerField()
    inpatient_id = models.IntegerField()
    path = models.CharField(max_length=191, blank=True, null=True)
    file_name = models.CharField(max_length=191, blank=True, null=True)
    uploaded_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    er_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inpatient_attachment'


class InstrumentalInvestigationImages(models.Model):
    investigation_id = models.IntegerField()
    visit_id = models.IntegerField()
    patient_id = models.IntegerField()
    image = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    ipd_id = models.IntegerField()
    er_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'instrumental_investigation_images'


class InstrumentalInvestigations(models.Model):
    visit_id = models.IntegerField()
    patient_id = models.IntegerField()
    investigation_type_id = models.IntegerField(blank=True, null=True)
    investigation_subtype_id = models.IntegerField(blank=True, null=True)
    investigation_date = models.DateField()
    remarks = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    ipd_id = models.IntegerField()
    er_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'instrumental_investigations'


class InsuranceClaimDocuments(models.Model):
    insurance_no = models.CharField(max_length=255)
    claim_no = models.CharField(max_length=255)
    base64_img = models.TextField()
    upload_status = models.IntegerField()
    img_path = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insurance_claim_documents'


class InsuranceClaims(models.Model):
    patient_id = models.PositiveIntegerField()
    master_bill = models.ForeignKey('MasterBills', models.DO_NOTHING, blank=True, null=True)
    claim_no = models.CharField(max_length=255)
    insurance_liability_amount = models.FloatField()
    total_amount = models.FloatField()
    insurance_no = models.CharField(max_length=255)
    billable_date = models.DateTimeField()
    insurance_uuid = models.CharField(max_length=255)
    response = models.JSONField(blank=True, null=True)
    status = models.IntegerField()
    created_by = models.PositiveIntegerField()
    disease_code_id = models.PositiveIntegerField(blank=True, null=True)
    disease_code = models.CharField(max_length=255, blank=True, null=True)
    pharmacy_master_bill = models.ForeignKey('PPharmacyMasterBills', models.DO_NOTHING, blank=True, null=True)
    nmc_no = models.CharField(max_length=255, blank=True, null=True)
    claim_submit_msg = models.TextField(blank=True, null=True)
    is_zero_opd = models.IntegerField()
    explanation = models.TextField(blank=True, null=True)
    mark_as_complete = models.IntegerField()
    resubmit_claim = models.IntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    is_claimcode_change = models.IntegerField()
    claim_status = models.CharField(max_length=255, blank=True, null=True)
    confirmed_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insurance_claims'


class InsuranceLetters(models.Model):
    patient_id = models.IntegerField()
    inpatient_id = models.IntegerField()
    subject = models.CharField(max_length=191, blank=True, null=True)
    letter_content = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    er_id = models.IntegerField()
    visit_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'insurance_letters'


class InsurancePatientDetails(models.Model):
    patient = models.ForeignKey('Patients', models.DO_NOTHING, blank=True, null=True)
    insurance_no = models.CharField(max_length=255)
    insurance_uuid = models.CharField(max_length=255)
    first_service_center = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    expiry_date = models.DateTimeField()
    balance = models.FloatField()
    html_response = models.TextField(blank=True, null=True)
    img_path = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    extension = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insurance_patient_details'


class InvAssetsTransactions(models.Model):
    asset_id = models.PositiveIntegerField()
    accession_number = models.CharField(max_length=191)
    trx_type = models.IntegerField()
    store_id = models.PositiveIntegerField()
    from_store_id = models.PositiveIntegerField(blank=True, null=True)
    from_user = models.PositiveIntegerField(blank=True, null=True)
    to_user = models.PositiveIntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=191, blank=True, null=True)
    asset_status = models.PositiveIntegerField()
    created_by = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    performed_by = models.CharField(max_length=191, blank=True, null=True)
    performed_date = models.CharField(max_length=191, blank=True, null=True)
    next_schedule_date = models.CharField(max_length=191, blank=True, null=True)
    from_owner_approval = models.PositiveIntegerField(blank=True, null=True)
    to_owner_approval = models.PositiveIntegerField(blank=True, null=True)
    from_table_flag = models.PositiveIntegerField(blank=True, null=True)
    to_table_flag = models.PositiveIntegerField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    is_old_norvic = models.IntegerField(blank=True, null=True)
    maintenance_type = models.IntegerField(blank=True, null=True)
    to_asset_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_assets_transactions'


class InvAssetsTransfer(models.Model):
    accession_number = models.ForeignKey('InvPurchaseAccession', models.DO_NOTHING, db_column='accession_number', blank=True, null=True)
    from_store = models.ForeignKey('InvStores', models.DO_NOTHING, db_column='from_store', blank=True, null=True)
    to_store = models.ForeignKey('InvStores', models.DO_NOTHING, db_column='to_store', related_name='invassetstransfer_to_store_set', blank=True, null=True)
    from_field = models.IntegerField(db_column='from')  # Field renamed because it was a Python reserved word.
    to = models.IntegerField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    from_approved_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='from_approved_by', related_name='invassetstransfer_from_approved_by_set', blank=True, null=True)
    to_approved_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='to_approved_by', related_name='invassetstransfer_to_approved_by_set', blank=True, null=True)
    from_approved_at = models.DateTimeField(blank=True, null=True)
    to_approved_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.CharField(max_length=191)
    status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_assets_transfer'


class InvBillDetails(models.Model):
    inv_bill_detail_id = models.AutoField(primary_key=True)
    branch_id = models.IntegerField()
    transfer_branch_id = models.PositiveBigIntegerField()
    inv_master_bill_id = models.IntegerField()
    stock_issue_id = models.IntegerField()
    batch = models.CharField(max_length=191, blank=True, null=True)
    store_id = models.IntegerField()
    customer_id = models.IntegerField()
    refund_status = models.IntegerField()
    cancel_status = models.IntegerField()
    transfer_branch_status = models.PositiveIntegerField()
    catalogue_type_id = models.IntegerField()
    catalogue_id = models.IntegerField()
    quantity = models.FloatField()
    cost_price = models.FloatField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    actual_rate = models.FloatField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    taxable_amt = models.FloatField(blank=True, null=True)
    tax_amt = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    discount_percentage = models.IntegerField()
    is_taxable = models.IntegerField()
    tax_per = models.IntegerField()
    expiry_date = models.CharField(max_length=191, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    foreign_item_rate = models.FloatField(blank=True, null=True)
    customer_item_id = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_bill_details'


class InvBillReceipts(models.Model):
    receipt_no = models.CharField(max_length=191)
    customer_id = models.IntegerField()
    transfer_branch_id = models.PositiveBigIntegerField()
    amount = models.FloatField()
    type = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_bill_receipts'


class InvCatalogueGenericNames(models.Model):
    generic_name = models.CharField(unique=True, max_length=191)
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    depreciation_class_id = models.IntegerField(blank=True, null=True)
    life = models.FloatField(blank=True, null=True)
    catalogue_generic_code = models.CharField(max_length=5, blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    is_main = models.IntegerField(blank=True, null=True)
    is_old_norvic = models.IntegerField(blank=True, null=True)
    ref_gid = models.IntegerField(blank=True, null=True)
    sgrp = models.CharField(max_length=191, blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inv_catalogue_generic_names'


class InvCatalogueLocation(models.Model):
    catalogue_id = models.PositiveBigIntegerField()
    store_id = models.PositiveBigIntegerField()
    location_name = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_catalogue_location'


class InvCatalogueStocksLog(models.Model):
    catalogue_id = models.IntegerField()
    qty = models.IntegerField()
    store_id = models.IntegerField()
    tqty = models.IntegerField()
    s_l_type = models.CharField(max_length=10)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_catalogue_stocks_log'


class InvCatalogueTypes(models.Model):
    catalogue_type_id = models.AutoField(primary_key=True)
    catalogue_type_name = models.CharField(max_length=191)
    asset_flag = models.PositiveIntegerField()
    category_number = models.CharField(max_length=191)
    catalogue_type_created_by = models.PositiveIntegerField()
    catalogue_type_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    catalogue_type_code = models.CharField(max_length=5, blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    is_old_norvic = models.IntegerField(blank=True, null=True)
    ref_catalogue_type_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inv_catalogue_types'


class InvCatalogues(models.Model):
    catalogue_id = models.AutoField(primary_key=True)
    unit_id = models.PositiveIntegerField()
    vendor_id = models.PositiveIntegerField()
    catalogue_type_id = models.PositiveIntegerField()
    catalogue_generic_id = models.PositiveIntegerField()
    catalogue_master_id = models.IntegerField(blank=True, null=True)
    catalogue_name = models.CharField(max_length=191)
    catalogue_short_form = models.CharField(unique=True, max_length=10, blank=True, null=True)
    catalogue_unit_value = models.CharField(max_length=191)
    catalogue_value_unit = models.CharField(max_length=191)
    catalogue_max_stock = models.PositiveIntegerField()
    catalogue_min_stock = models.PositiveIntegerField()
    catalogue_delivery_time = models.PositiveIntegerField()
    catalogue_safety_stock = models.PositiveIntegerField()
    cost_price = models.FloatField()
    selling_price = models.FloatField()
    profit_percent = models.FloatField()
    catalogue_status = models.IntegerField()
    expiry_alert_days = models.IntegerField()
    catalogue_taxable = models.IntegerField()
    non_inventory_item = models.IntegerField()
    catalogue_discountable = models.IntegerField()
    catalogue_image = models.TextField(blank=True, null=True)
    catalogue_description = models.TextField(blank=True, null=True)
    catalogue_created_by = models.PositiveIntegerField()
    catalogue_updated_by = models.PositiveIntegerField(blank=True, null=True)
    reorder = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_expiry = models.PositiveIntegerField()
    is_batch = models.PositiveIntegerField()
    item_code = models.CharField(max_length=191, blank=True, null=True)
    is_service_item = models.IntegerField()
    model_no = models.CharField(max_length=191, blank=True, null=True)
    is_fixed_asset = models.IntegerField()
    pac_size = models.IntegerField()
    pac_size_unit = models.CharField(max_length=191, blank=True, null=True)
    temperature = models.CharField(max_length=191, blank=True, null=True)
    ipdrate = models.FloatField(blank=True, null=True)
    is_old_norvic = models.IntegerField(blank=True, null=True)
    purchase_rate = models.FloatField(blank=True, null=True)
    ref_catalogue_id = models.IntegerField(blank=True, null=True)
    is_zero_charge = models.IntegerField()
    tax_per = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_catalogues'


class InvClosingStockDetails(models.Model):
    closing_stock_details_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    closing_stocks_id = models.PositiveIntegerField()
    stock_purchases_id = models.PositiveIntegerField()
    catalogue_id = models.PositiveIntegerField()
    actual_qty = models.IntegerField()
    reconcile_qty = models.IntegerField()
    reconcile_percent = models.FloatField()
    closing_stock_details_created_by = models.PositiveIntegerField()
    closing_stock_details_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_closing_stock_details'


class InvClosingStocks(models.Model):
    closing_stocks_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    store_id = models.IntegerField()
    is_opened_flag = models.IntegerField()
    closing_stocks_tot_catalogue_qty = models.PositiveIntegerField()
    closing_stocks_remarks = models.TextField(blank=True, null=True)
    closing_stocks_created_by = models.PositiveIntegerField()
    closing_stocks_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_closing_stocks'


class InvCreditPurchaseLedgers(models.Model):
    supplier_id = models.PositiveIntegerField()
    branch_id = models.PositiveIntegerField()
    master_stock_purchase_id = models.IntegerField()
    master_retrun_id = models.IntegerField()
    reference_purchase_no = models.CharField(max_length=191, blank=True, null=True)
    receipt_no = models.CharField(max_length=191, blank=True, null=True)
    dr_amt = models.FloatField()
    cr_amt = models.FloatField()
    type = models.CharField(max_length=1)
    payment_date = models.DateField()
    payment_type = models.IntegerField()
    bank_id = models.IntegerField(blank=True, null=True)
    card_no = models.CharField(max_length=191, blank=True, null=True)
    cheque_no = models.CharField(max_length=191, blank=True, null=True)
    remarks = models.TextField()
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_credit_purchase_ledgers'


class InvCustomerLedgers(models.Model):
    customer_id = models.PositiveIntegerField()
    transfer_branch_id = models.PositiveBigIntegerField()
    customer_group_id = models.PositiveIntegerField(blank=True, null=True)
    customer_type_id = models.PositiveIntegerField(blank=True, null=True)
    branch_id = models.PositiveIntegerField()
    inv_master_bill_id = models.IntegerField()
    inv_master_refund_id = models.IntegerField()
    reference_bill_no = models.CharField(max_length=191, blank=True, null=True)
    receipt_no = models.CharField(max_length=191, blank=True, null=True)
    dr_amt = models.FloatField()
    cr_amt = models.FloatField()
    bill_type = models.CharField(max_length=1)
    payment_type = models.IntegerField()
    bank_id = models.IntegerField(blank=True, null=True)
    card_no = models.CharField(max_length=191, blank=True, null=True)
    cheque_no = models.CharField(max_length=191, blank=True, null=True)
    remarks = models.TextField()
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_customer_ledgers'


class InvCustomers(models.Model):
    company_name = models.CharField(max_length=191)
    email = models.CharField(max_length=191)
    phone_no = models.CharField(max_length=191, blank=True, null=True)
    address = models.CharField(max_length=191)
    country = models.CharField(max_length=191)
    status = models.IntegerField()
    branch = models.IntegerField()
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    display_name = models.CharField(max_length=191)
    first_name = models.CharField(max_length=191)
    middle_name = models.CharField(max_length=191, blank=True, null=True)
    last_name = models.CharField(max_length=191)
    mobile_no = models.CharField(max_length=191, blank=True, null=True)
    website = models.CharField(max_length=191, blank=True, null=True)
    other = models.CharField(max_length=191, blank=True, null=True)
    state = models.CharField(max_length=191, blank=True, null=True)
    city = models.CharField(max_length=191, blank=True, null=True)
    shipping_address = models.CharField(max_length=191)
    shipping_country = models.CharField(max_length=191)
    shipping_state = models.CharField(max_length=191, blank=True, null=True)
    shipping_city = models.CharField(max_length=191, blank=True, null=True)
    shipping_address_detail = models.IntegerField()
    acc_account_id = models.IntegerField(blank=True, null=True)
    customer_vat_no = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_customers'


class InvDepreciationClass(models.Model):
    class_name = models.CharField(max_length=191)
    descrption = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    dep_per = models.FloatField()

    class Meta:
        managed = False
        db_table = 'inv_depreciation_class'


class InvFiscal(models.Model):
    fiscal_year = models.PositiveIntegerField(blank=True, null=True)
    from_ad = models.PositiveIntegerField()
    to_ad = models.PositiveIntegerField()
    status = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_fiscal'


class InvGoodReceiptNote(models.Model):
    branch_id = models.PositiveIntegerField()
    user_role_id = models.PositiveIntegerField()
    supplier_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    program_id = models.PositiveIntegerField(blank=True, null=True)
    purchase_order_id = models.IntegerField()
    purchases_order_no = models.CharField(max_length=191, blank=True, null=True)
    good_receipt_note_no = models.CharField(max_length=191)
    good_receipt_note_status = models.IntegerField()
    approved_status = models.PositiveIntegerField()
    user_role_name = models.CharField(max_length=191)
    good_receipt_note_delivery_site = models.CharField(max_length=191)
    good_receipt_note_delivery_date = models.DateTimeField()
    good_receipt_note_approved_by = models.CharField(max_length=191)
    good_receipt_order_date = models.DateField()
    good_receipt_note_remarks = models.TextField(blank=True, null=True)
    good_receipt_note_created_by = models.PositiveIntegerField()
    good_receipt_note_updated_by = models.PositiveIntegerField(blank=True, null=True)
    sub_total = models.FloatField(blank=True, null=True)
    tax_per = models.FloatField(blank=True, null=True)
    tax_amount = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    completed_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inv_good_receipt_note'


class InvGoodReceiptNoteCatalogues(models.Model):
    branch_id = models.PositiveIntegerField()
    good_receipt_note_id = models.PositiveIntegerField()
    program_id = models.PositiveIntegerField(blank=True, null=True)
    good_receipt_note_catalogue_id = models.PositiveIntegerField()
    good_receipt_note_catalogue_quantity = models.FloatField()
    good_receipt_note_catalogue_status = models.IntegerField()
    good_receipt_note_catalogue_remarks = models.TextField(blank=True, null=True)
    good_receipt_note_catalogue_created_by = models.PositiveIntegerField()
    good_receipt_note_catalogue_updated_by = models.PositiveIntegerField(blank=True, null=True)
    good_receipt_note_catalogue_rate = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_good_receipt_note_catalogues'


class InvGrn(models.Model):
    branch_id = models.PositiveIntegerField()
    master_grn_id = models.PositiveIntegerField()
    grn_number = models.CharField(max_length=191, blank=True, null=True)
    program_id = models.IntegerField(blank=True, null=True)
    supplier_id = models.IntegerField(blank=True, null=True)
    manufacture_id = models.IntegerField()
    sp_opening_stocks_id = models.PositiveIntegerField()
    sp_closing_stocks_id = models.PositiveIntegerField()
    catalogue_type_id = models.PositiveIntegerField()
    catalogue_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    batch = models.CharField(max_length=191)
    p_quantity = models.FloatField()
    p_stock_quantity = models.FloatField()
    expiry_date = models.CharField(max_length=191)
    cost_price = models.FloatField()
    selling_price = models.FloatField()
    profit_percent = models.FloatField()
    stock_purchases_remarks = models.TextField(blank=True, null=True)
    stock_purchases_status = models.IntegerField()
    stock_purchases_created_by = models.PositiveIntegerField()
    stock_purchases_updated_by = models.PositiveIntegerField(blank=True, null=True)
    purchase_return_status = models.IntegerField()
    registered_book_no = models.CharField(max_length=191, blank=True, null=True)
    registered_page_no = models.CharField(max_length=191, blank=True, null=True)
    p_return_quantity = models.FloatField()
    disposed_qty = models.PositiveIntegerField()
    expired_breakage_id = models.PositiveIntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=191, blank=True, null=True)
    cp_before_tax = models.FloatField()
    discount_per = models.FloatField()
    discount_amount = models.FloatField()
    is_taxable = models.IntegerField()
    taxable_amt = models.FloatField()
    tax_per = models.FloatField()
    tax_amount = models.FloatField()
    asset_purchase_no = models.CharField(max_length=191, blank=True, null=True)
    asset_purchase_date = models.CharField(max_length=191, blank=True, null=True)
    salvage_value = models.CharField(max_length=191, blank=True, null=True)
    warranty_period = models.CharField(max_length=191, blank=True, null=True)
    asset_status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    purchases_order_id = models.PositiveIntegerField(blank=True, null=True)
    purchase_order_no = models.CharField(max_length=191, blank=True, null=True)
    approved_status = models.PositiveIntegerField(blank=True, null=True)
    cancel_status = models.IntegerField()
    remaining_quantity = models.IntegerField()
    country_of_origin = models.CharField(max_length=100, blank=True, null=True)
    effamt = models.FloatField()
    installation_date = models.CharField(max_length=100, blank=True, null=True)
    is_old_norvic = models.IntegerField(blank=True, null=True)
    lqty = models.FloatField(blank=True, null=True)
    manufacture_date = models.CharField(max_length=255, blank=True, null=True)
    model_no = models.CharField(max_length=255, blank=True, null=True)
    mrp = models.FloatField()
    net_value = models.FloatField(blank=True, null=True)
    purchase_date = models.DateField(blank=True, null=True)
    purchase_price = models.FloatField(blank=True, null=True)
    ref_purchase_id = models.IntegerField(blank=True, null=True)
    salvage = models.CharField(max_length=191, blank=True, null=True)
    serial_no = models.CharField(max_length=191, blank=True, null=True)
    useful_life = models.IntegerField(blank=True, null=True)
    warnt_period = models.CharField(max_length=191, blank=True, null=True)
    eff_rate = models.FloatField(blank=True, null=True)
    invoice_no = models.CharField(max_length=100, blank=True, null=True)
    purchase_order_catalogue_id = models.PositiveIntegerField(blank=True, null=True)
    salestaxper = models.IntegerField(blank=True, null=True)
    t_po_no = models.CharField(max_length=100, blank=True, null=True)
    tstore_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_grn'


class InvGroupwiseSummaryReport(models.Model):
    json_data = models.TextField(blank=True, null=True)
    sdate = models.DateField(blank=True, null=True)
    store_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'inv_groupwise_summary_report'


class InvInPatientBillDetails(models.Model):
    inv_inpatient_bill_detail_id = models.AutoField(primary_key=True)
    inv_inpatient_master_bill_id = models.PositiveIntegerField()
    stock_issue_id = models.PositiveIntegerField()
    batch = models.CharField(max_length=191, blank=True, null=True)
    branch_id = models.PositiveIntegerField()
    patient_id = models.PositiveIntegerField(blank=True, null=True)
    in_pat_id = models.PositiveIntegerField(blank=True, null=True)
    store_id = models.PositiveIntegerField()
    refund_status = models.CharField(max_length=1)
    cancel_status = models.CharField(max_length=1)
    catalogue_type_id = models.PositiveIntegerField()
    catalogue_id = models.PositiveIntegerField()
    rate = models.FloatField()
    cost_price = models.FloatField()
    expiry_date = models.CharField(max_length=191)
    quantity = models.IntegerField()
    total_sales_quantity = models.PositiveIntegerField()
    refund_quantity = models.PositiveIntegerField()
    amount = models.FloatField()
    discount_percentage = models.PositiveIntegerField()
    discount = models.FloatField()
    is_taxable = models.IntegerField()
    taxable_amt = models.FloatField()
    tax_per = models.FloatField()
    tax = models.FloatField()
    total = models.FloatField()
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    patient_med_id = models.PositiveIntegerField(blank=True, null=True)
    refunded_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_in_patient_bill_details'


class InvInPatientMasterService(models.Model):
    store_id = models.PositiveIntegerField()
    total_qty = models.IntegerField()
    branch_id = models.PositiveIntegerField()
    patient_id = models.PositiveIntegerField()
    inpatient_id = models.PositiveIntegerField()
    status = models.PositiveIntegerField()
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    ap_pannel = models.CharField(max_length=191, blank=True, null=True)
    apply_tds = models.IntegerField(blank=True, null=True)
    cancel_date = models.DateTimeField(blank=True, null=True)
    cancel_rmks = models.CharField(max_length=191, blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    discount_amt = models.FloatField(blank=True, null=True)
    discount_per = models.FloatField(blank=True, null=True)
    patno = models.CharField(max_length=191, blank=True, null=True)
    ramt = models.FloatField(blank=True, null=True)
    return_status = models.IntegerField()
    service_bill_no = models.CharField(max_length=191, blank=True, null=True)
    taxable_amt = models.FloatField(blank=True, null=True)
    total_amt = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_in_patient_master_service'


class InvInPatientService(models.Model):
    in_patient_master_servie_id = models.PositiveIntegerField()
    patient_id = models.PositiveIntegerField()
    inpatient_id = models.PositiveIntegerField()
    qty = models.IntegerField()
    catalogue_id = models.PositiveIntegerField()
    item_id = models.PositiveIntegerField()
    catalogue_type_id = models.PositiveIntegerField()
    batch = models.CharField(max_length=191, db_collation='utf8mb4_unicode_ci')
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    return_quantity = models.IntegerField()
    amt_after_tax = models.FloatField(blank=True, null=True)
    amt_before_discount = models.FloatField(blank=True, null=True)
    cost_price = models.FloatField(blank=True, null=True)
    discount_amt = models.FloatField(blank=True, null=True)
    discount_per = models.FloatField(blank=True, null=True)
    expire_date = models.DateField(blank=True, null=True)
    mrp = models.FloatField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    sales_amt_per = models.FloatField(blank=True, null=True)
    selling_price = models.FloatField(blank=True, null=True)
    service_bill_no = models.CharField(max_length=100, blank=True, null=True)
    stock_date = models.DateField(blank=True, null=True)
    store_id = models.IntegerField(blank=True, null=True)
    taxable_amt = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    eff_rate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_in_patient_service'


class InvIssueReturns(models.Model):
    issue_return_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    ir_opening_stocks_id = models.PositiveIntegerField()
    ir_closing_stocks_id = models.PositiveIntegerField()
    master_returns_id = models.PositiveIntegerField()
    master_stock_issue_id = models.IntegerField(blank=True, null=True)
    stock_issue_id = models.IntegerField(blank=True, null=True)
    catalogue_type_id = models.PositiveIntegerField()
    catalogue_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    return_to_store = models.PositiveIntegerField()
    batch = models.CharField(max_length=191)
    i_revert_quantity = models.PositiveIntegerField()
    expiry_date = models.CharField(max_length=191)
    cost_price = models.FloatField()
    selling_price = models.FloatField()
    profit_percent = models.FloatField()
    issue_return_status = models.IntegerField()
    expiry_return_status = models.IntegerField()
    issue_return_created_by = models.PositiveIntegerField()
    issue_return_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    againstissno = models.CharField(db_column='AGAINSTISSNO', max_length=191, blank=True, null=True)  # Field name made lowercase.
    mrp = models.FloatField(blank=True, null=True)
    returns_no = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_issue_returns'


class InvManageExpireBreakage(models.Model):
    name = models.CharField(max_length=191, blank=True, null=True)
    status = models.PositiveIntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_manage_expire_breakage'


class InvMasterBills(models.Model):
    inv_master_bill_id = models.AutoField(primary_key=True)
    branch_id = models.IntegerField()
    transfer_branch_id = models.PositiveBigIntegerField()
    bill_no = models.CharField(max_length=191)
    invoice_no = models.CharField(max_length=191, blank=True, null=True)
    customer_id = models.IntegerField()
    reference_master_bill_id = models.IntegerField(blank=True, null=True)
    store_id = models.IntegerField(blank=True, null=True)
    pan = models.CharField(max_length=191, blank=True, null=True)
    customer_name = models.CharField(max_length=191)
    transfer_branch_name = models.CharField(max_length=191, blank=True, null=True)
    sales_order_id = models.IntegerField(blank=True, null=True)
    sales_order_no = models.CharField(max_length=191, blank=True, null=True)
    refund_status = models.IntegerField()
    cancel_status = models.IntegerField()
    transfer_branch_status = models.PositiveIntegerField()
    print_count = models.IntegerField()
    tender_amt = models.FloatField(blank=True, null=True)
    return_amt = models.FloatField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    taxable_amt = models.FloatField(blank=True, null=True)
    tax = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    customer_group_id = models.IntegerField(blank=True, null=True)
    customer_type_id = models.IntegerField(blank=True, null=True)
    customer_type_percent = models.IntegerField(blank=True, null=True)
    payment_type = models.IntegerField(blank=True, null=True)
    bank_id = models.IntegerField()
    card_no = models.CharField(max_length=191, blank=True, null=True)
    cheque_no = models.CharField(max_length=191, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created_at_nepali_date = models.CharField(max_length=10, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)
    exchange_rate = models.FloatField(blank=True, null=True)
    freight_charge = models.FloatField()
    port_destination = models.CharField(max_length=191, blank=True, null=True)
    port = models.CharField(max_length=191, blank=True, null=True)
    delivery_terms = models.TextField(blank=True, null=True)
    hs_no = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_master_bills'


class InvMasterGrn(models.Model):
    master_grn_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    supplier_id = models.PositiveIntegerField(blank=True, null=True)
    program_id = models.IntegerField(blank=True, null=True)
    msp_opening_stocks_id = models.PositiveIntegerField()
    msp_closing_stocks_id = models.PositiveIntegerField()
    grn_number = models.CharField(max_length=191, blank=True, null=True)
    supplier_bill_no = models.CharField(max_length=191, blank=True, null=True)
    supplier_bill_date = models.CharField(max_length=191, blank=True, null=True)
    total_quantity = models.FloatField()
    amount = models.FloatField(blank=True, null=True)
    discount_amount = models.FloatField(blank=True, null=True)
    discount_per = models.FloatField(blank=True, null=True)
    tax_per = models.FloatField(blank=True, null=True)
    tax_amount = models.FloatField(blank=True, null=True)
    other_charges = models.FloatField()
    total_amount = models.FloatField(blank=True, null=True)
    payment_type = models.IntegerField(blank=True, null=True)
    master_grn_remarks = models.TextField(blank=True, null=True)
    master_grn_cancel_remarks = models.TextField(blank=True, null=True)
    master_grn_good_in_date = models.DateField(blank=True, null=True)
    master_grn_good_in_nepali_date = models.CharField(max_length=191, blank=True, null=True)
    master_grn_cancel_status = models.IntegerField()
    master_grn_created_by = models.PositiveIntegerField()
    master_grn_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    asset_status = models.IntegerField(blank=True, null=True)
    approved_by = models.IntegerField(blank=True, null=True)
    stock_purchases_status = models.PositiveIntegerField()
    purchases_order_id = models.PositiveIntegerField(blank=True, null=True)
    purchase_order_no = models.CharField(max_length=191, blank=True, null=True)
    approved_status = models.PositiveIntegerField(blank=True, null=True)
    completed_status = models.IntegerField()
    terms_and_condition = models.CharField(max_length=191, blank=True, null=True)
    pre_approved = models.IntegerField()
    final_approved = models.IntegerField()
    pre_approved_by = models.CharField(max_length=191, blank=True, null=True)
    final_approved_by = models.CharField(max_length=191, blank=True, null=True)
    gate_entry_no = models.CharField(max_length=191, blank=True, null=True)
    gate_entry_date = models.DateTimeField(blank=True, null=True)
    credit_days = models.IntegerField()
    final_approved_date = models.CharField(max_length=191, blank=True, null=True)
    is_old_norvic = models.IntegerField(blank=True, null=True)
    pre_approved_date = models.CharField(max_length=191, blank=True, null=True)
    round_off = models.FloatField(blank=True, null=True)
    supplier_bill_date_bs = models.CharField(max_length=191, blank=True, null=True)
    tdsamt = models.CharField(max_length=191, blank=True, null=True)
    tdsledger = models.CharField(max_length=191, blank=True, null=True)
    tdsperc = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_master_grn'


class InvMasterPurchaseReturns(models.Model):
    master_purchases_return_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    mpr_opening_stocks_id = models.PositiveIntegerField()
    mpr_closing_stocks_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    supplier_id = models.PositiveIntegerField()
    purchases_return_no = models.CharField(max_length=191)
    return_status = models.IntegerField()
    total_return_qty = models.FloatField()
    total_return_amount = models.FloatField()
    master_purchases_return_remarks = models.TextField(blank=True, null=True)
    master_purchases_returns_created_by = models.PositiveIntegerField()
    master_purchases_returns_updated_by = models.PositiveIntegerField(blank=True, null=True)
    asset_status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    approved_status = models.IntegerField()
    return_type = models.IntegerField()
    tdsamt = models.CharField(max_length=191, blank=True, null=True)
    tdsledger = models.CharField(max_length=191, blank=True, null=True)
    tdsperc = models.CharField(max_length=191, blank=True, null=True)
    approved_by = models.PositiveIntegerField(blank=True, null=True)
    approved_date = models.DateTimeField(blank=True, null=True)
    roundoff = models.FloatField()
    sub_total = models.FloatField()

    class Meta:
        managed = False
        db_table = 'inv_master_purchase_returns'


class InvMasterRefunds(models.Model):
    inv_master_refund_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    inv_master_bill_id = models.PositiveIntegerField()
    inv_refund_store_id = models.PositiveIntegerField()
    inv_refund_bill_no = models.CharField(max_length=191)
    inv_refund_remarks = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_master_refunds'


class InvMasterReturns(models.Model):
    master_returns_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    mr_opening_stocks_id = models.PositiveIntegerField()
    mr_closing_stocks_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    return_to_store = models.PositiveIntegerField()
    returns_no = models.CharField(max_length=191)
    total_qty = models.FloatField()
    issue_return_status = models.PositiveIntegerField()
    expiry_return_status = models.PositiveIntegerField()
    master_returns_remarks = models.CharField(max_length=191, blank=True, null=True)
    master_returns_created_by = models.PositiveIntegerField()
    master_returns_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    approved_status = models.IntegerField()
    approve_by = models.PositiveIntegerField(blank=True, null=True)
    receive_status = models.IntegerField()
    return_type = models.IntegerField()
    t_return_to_store_id = models.BigIntegerField(blank=True, null=True)
    t_store_id = models.BigIntegerField(blank=True, null=True)
    tdsamt = models.CharField(max_length=191, blank=True, null=True)
    tdsledger = models.CharField(max_length=191, blank=True, null=True)
    tdsperc = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_master_returns'


class InvMasterServiceReturn(models.Model):
    store_id = models.PositiveIntegerField()
    branch_id = models.PositiveIntegerField()
    patient_id = models.PositiveIntegerField()
    inpatient_id = models.PositiveIntegerField()
    total_return_qty = models.IntegerField()
    return_status = models.PositiveIntegerField()
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    ap_pannel = models.CharField(max_length=191, blank=True, null=True)
    apply_tds = models.IntegerField(blank=True, null=True)
    cancel_date = models.DateTimeField(blank=True, null=True)
    cancel_rmks = models.CharField(max_length=191, blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    discount_amt = models.FloatField(blank=True, null=True)
    discount_per = models.FloatField(blank=True, null=True)
    patno = models.CharField(max_length=191, blank=True, null=True)
    ramt = models.FloatField(blank=True, null=True)
    service_return_no = models.CharField(max_length=191, blank=True, null=True)
    taxable_amt = models.FloatField(blank=True, null=True)
    total_amt = models.FloatField(blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_master_service_return'


class InvMasterStockConsumptions(models.Model):
    master_stock_consumption_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveBigIntegerField()
    msc_opening_stocks_id = models.PositiveBigIntegerField()
    msc_closing_stocks_id = models.PositiveBigIntegerField()
    store_id = models.PositiveBigIntegerField()
    record_store_id = models.PositiveBigIntegerField()
    consumption_no = models.CharField(max_length=191)
    status = models.IntegerField()
    consumption_date = models.CharField(max_length=191)
    consumption_nepali_date = models.CharField(max_length=191)
    remarks = models.TextField(blank=True, null=True)
    created_by = models.PositiveBigIntegerField()
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    master_stock_issues_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_master_stock_consumptions'


class InvMasterStockIssues(models.Model):
    master_stock_issues_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    msi_opening_stocks_id = models.PositiveIntegerField()
    msi_closing_stocks_id = models.PositiveIntegerField()
    received_from_store = models.PositiveIntegerField()
    stock_issues_remarks = models.TextField(blank=True, null=True)
    stock_issue_no = models.CharField(max_length=191)
    master_stock_issue_cancel_status = models.IntegerField()
    master_stock_issues_created_by = models.PositiveIntegerField()
    master_stock_issues_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    approved_by = models.IntegerField(blank=True, null=True)
    cancel_status = models.IntegerField()
    received_by = models.IntegerField(blank=True, null=True)
    rstock_no = models.CharField(max_length=100, blank=True, null=True)
    tdsamt = models.CharField(max_length=191, blank=True, null=True)
    tdsledger = models.CharField(max_length=191, blank=True, null=True)
    tdsperc = models.CharField(max_length=191, blank=True, null=True)
    terms_and_condition = models.CharField(max_length=191, blank=True, null=True)
    approved_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_master_stock_issues'


class InvMasterStockPurchases(models.Model):
    master_stock_purchases_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    currency_id = models.IntegerField(blank=True, null=True)
    current_amount = models.FloatField(blank=True, null=True)
    store_id = models.PositiveIntegerField()
    supplier_id = models.PositiveIntegerField(blank=True, null=True)
    purchases_order_id = models.PositiveIntegerField(blank=True, null=True)
    msp_opening_stocks_id = models.PositiveIntegerField()
    msp_closing_stocks_id = models.PositiveIntegerField()
    stock_purchases_no = models.CharField(max_length=191, blank=True, null=True)
    supplier_bill_no = models.CharField(max_length=191, blank=True, null=True)
    supplier_bill_date = models.CharField(max_length=191, blank=True, null=True)
    purchases_order_no = models.CharField(max_length=191, blank=True, null=True)
    good_receipt_note_id = models.IntegerField(blank=True, null=True)
    good_receipt_note_no = models.CharField(max_length=191, blank=True, null=True)
    total_quantity = models.FloatField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    discount_amount = models.FloatField(blank=True, null=True)
    discount_per = models.FloatField(blank=True, null=True)
    tax_per = models.FloatField(blank=True, null=True)
    tax_amount = models.FloatField(blank=True, null=True)
    other_charges = models.FloatField()
    total_amount = models.FloatField(blank=True, null=True)
    payment_type = models.IntegerField(blank=True, null=True)
    master_stock_purchases_remarks = models.TextField(blank=True, null=True)
    master_stock_purchases_cancel_remarks = models.TextField(blank=True, null=True)
    stock_purchases_good_in_date = models.DateField(blank=True, null=True)
    stock_purchases_good_in_nepali_date = models.CharField(max_length=191, blank=True, null=True)
    master_stock_purchases_cancel_status = models.IntegerField()
    approved_status = models.PositiveIntegerField()
    master_stock_purchases_created_by = models.PositiveIntegerField()
    master_stock_purchases_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    program_id = models.IntegerField(blank=True, null=True)
    asset_status = models.IntegerField(blank=True, null=True)
    journal_id = models.CharField(max_length=191, blank=True, null=True)
    approved_by = models.IntegerField(blank=True, null=True)
    completed_status = models.IntegerField()
    terms_and_condition = models.CharField(max_length=100, blank=True, null=True)
    tds_amt = models.FloatField(blank=True, null=True)
    tds_percentage = models.FloatField(blank=True, null=True)
    approved_date = models.DateTimeField(blank=True, null=True)
    country_of_origin = models.CharField(max_length=100, blank=True, null=True)
    credit_days = models.CharField(max_length=100, blank=True, null=True)
    gate_entry_date = models.DateTimeField(blank=True, null=True)
    gate_entry_no = models.CharField(max_length=191, blank=True, null=True)
    is_old_norvic = models.IntegerField(blank=True, null=True)
    ref_master_stock_purchases_id = models.IntegerField(blank=True, null=True)
    round_off = models.FloatField(blank=True, null=True)
    supplier_bill_date_bs = models.CharField(max_length=191, blank=True, null=True)
    tdsamt = models.CharField(max_length=191, blank=True, null=True)
    tdsledger = models.CharField(max_length=191, blank=True, null=True)
    tdsperc = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_master_stock_purchases'


class InvOpeningStocks(models.Model):
    opening_stocks_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    store = models.PositiveIntegerField()
    opening_stocks_tot_stock_qty = models.PositiveIntegerField()
    opening_stocks_remarks = models.TextField(blank=True, null=True)
    opening_stocks_created_by = models.PositiveIntegerField()
    opening_stocks_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_old_norvic = models.IntegerField(blank=True, null=True)
    ref_opening_stock_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_opening_stocks'


class InvPaymentMethod(models.Model):
    payment_mode = models.CharField(max_length=191)
    editable = models.IntegerField(blank=True, null=True)
    active = models.IntegerField()
    payment_method_type = models.CharField(max_length=191, blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_pharmacy = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_payment_method'


class InvPermissionRole(models.Model):
    permission_id = models.PositiveIntegerField()
    role_id = models.PositiveIntegerField()
    access_type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_permission_role'


class InvPermissionUser(models.Model):
    permission_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'inv_permission_user'


class InvPermissions(models.Model):
    name = models.CharField(max_length=191)
    display_name = models.CharField(max_length=191, blank=True, null=True)
    description = models.CharField(max_length=191, blank=True, null=True)
    category = models.CharField(max_length=191, blank=True, null=True)
    is_parent = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    ims_type = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'inv_permissions'


class InvPivotBilldetailStockissues(models.Model):
    inv_pivot_billdetail_stockissue_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    inv_master_bill_id = models.PositiveIntegerField()
    inv_bill_detail_id = models.PositiveIntegerField()
    stock_issue_id = models.PositiveIntegerField()
    quantity = models.FloatField()
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_pivot_billdetail_stockissues'


class InvPivotCatalogues(models.Model):
    parent_catalogue_id = models.IntegerField()
    child_catalogue_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_pivot_catalogues'


class InvPivotInPatientServiceStockIssue(models.Model):
    inpatient_master_service_id = models.PositiveIntegerField()
    inpatient_service_id = models.PositiveIntegerField()
    stock_issue_id = models.PositiveIntegerField()
    qty = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_pivot_in_patient_service_stock_issue'


class InvPivotLocationUsers(models.Model):
    location_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    module_name = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_pivot_location_users'


class InvPivotPurchasereturnStockpurchases(models.Model):
    pivot_purchasereturn_stockpurchase_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    master_purchases_return_id = models.PositiveIntegerField()
    purchase_return_id = models.PositiveIntegerField()
    stock_purchases_id = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    pivot_purchasereturn_stockpurchase_created_by = models.PositiveIntegerField()
    pivot_purchasereturn_stockpurchase_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_pivot_purchasereturn_stockpurchases'


class InvPivotStockPurchaseSupplierDiscountBonus(models.Model):
    stock_purchases_id = models.IntegerField()
    bonus_qty = models.CharField(max_length=191, blank=True, null=True)
    discount = models.CharField(max_length=191, blank=True, null=True)
    supplier_manufacture_discount_id = models.IntegerField()
    catalogue_cost_price = models.CharField(max_length=191, blank=True, null=True)
    cp_before_tax = models.CharField(max_length=191, blank=True, null=True)
    cp_before_tax_chg = models.CharField(max_length=191, blank=True, null=True)
    cost_price = models.CharField(max_length=191, blank=True, null=True)
    cost_price_chg = models.CharField(max_length=191, blank=True, null=True)
    item_bonus_qty = models.CharField(max_length=191, blank=True, null=True)
    bonus_qty_chg = models.CharField(max_length=191, blank=True, null=True)
    discount_per = models.CharField(max_length=191, blank=True, null=True)
    discount_per_chg = models.CharField(max_length=191, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_pivot_stock_purchase_supplier_discount_bonus'


class InvPivotStockPurchases(models.Model):
    pivot_stock_purchases_id = models.AutoField(primary_key=True)
    stock_purchases_id = models.CharField(max_length=191)
    stock_purchases_no = models.CharField(max_length=191)
    catalogue_id = models.PositiveIntegerField()
    batch = models.CharField(max_length=191)
    free_status = models.IntegerField()
    expiry_date = models.CharField(max_length=191)
    never_expiry = models.IntegerField()
    cp_before_tax = models.FloatField()
    discount_per = models.FloatField()
    discount_amount = models.FloatField()
    is_taxable = models.IntegerField()
    taxable_amt = models.FloatField()
    tax_per = models.FloatField()
    tax_amount = models.FloatField()
    cost_price = models.FloatField()
    selling_price = models.FloatField()
    profit_percent = models.FloatField()
    pivot_purchases_created_by = models.PositiveIntegerField()
    pivot_purchases_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_pivot_stock_purchases'


class InvPivotStockconsumptionsStockissues(models.Model):
    stock_consumption_id = models.PositiveBigIntegerField()
    stock_issue_id = models.PositiveBigIntegerField()
    quantity = models.FloatField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_pivot_stockconsumptions_stockissues'


class InvPivotStoreUsers(models.Model):
    user_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    is_primary = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inv_pivot_store_users'


class InvPrograms(models.Model):
    name = models.CharField(max_length=191)
    code = models.CharField(max_length=191)
    status = models.IntegerField()
    description = models.TextField()
    branch_id = models.PositiveIntegerField()
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_programs'


class InvPurchaseAccession(models.Model):
    stock_purchases_id = models.PositiveIntegerField()
    catalogue_id = models.PositiveIntegerField()
    accession_number = models.CharField(unique=True, max_length=191, blank=True, null=True)
    current_location = models.ForeignKey('InvStores', models.DO_NOTHING, db_column='current_location')
    tracking_status = models.IntegerField()
    status = models.PositiveIntegerField()
    cancel_status = models.IntegerField()
    branch_id = models.PositiveIntegerField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    table_flag = models.PositiveIntegerField(blank=True, null=True)
    sub_location = models.PositiveIntegerField(blank=True, null=True)
    catalogue_type_id = models.IntegerField(blank=True, null=True)
    catalogue_generic_id = models.IntegerField(blank=True, null=True)
    item_code = models.CharField(max_length=191, blank=True, null=True)
    cl_id = models.CharField(max_length=100, blank=True, null=True)
    discard = models.CharField(max_length=255, blank=True, null=True)
    grn_id = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    is_old_norvic = models.IntegerField(blank=True, null=True)
    ref_ipa_id = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    sbl_id = models.IntegerField(blank=True, null=True)
    discard_by = models.IntegerField(blank=True, null=True)
    discard_remarks = models.CharField(max_length=191, blank=True, null=True)
    is_issued = models.IntegerField()
    issue_id = models.IntegerField(blank=True, null=True)
    issue_no = models.CharField(max_length=191, blank=True, null=True)
    per_discarded_at = models.DateTimeField(blank=True, null=True)
    pre_discard = models.IntegerField()
    pre_discard_reauest_by = models.IntegerField(blank=True, null=True)
    pre_discard_remarks = models.CharField(max_length=191, blank=True, null=True)
    undiscard_by = models.IntegerField(blank=True, null=True)
    undiscard_remarks = models.CharField(max_length=191, blank=True, null=True)
    reference_code = models.CharField(max_length=191)
    voucher_no = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'inv_purchase_accession'


class InvPurchaseOrderCatalogues(models.Model):
    purchase_order_catalogue_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    purchase_order_id = models.PositiveIntegerField()
    program_id = models.PositiveIntegerField(blank=True, null=True)
    catalogue_id = models.PositiveIntegerField()
    purchase_order_catalogue_quantity = models.FloatField()
    purchase_order_catalogue_rate = models.FloatField()
    sub_total = models.FloatField()
    tax_per = models.FloatField(blank=True, null=True)
    tax_amount = models.FloatField(blank=True, null=True)
    total = models.FloatField()
    purchase_order_catalogue_status = models.IntegerField()
    purchase_order_catalogue_remarks = models.TextField(blank=True, null=True)
    purchase_order_catalogue_created_by = models.PositiveIntegerField()
    purchase_order_catalogue_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    manufacture_id = models.PositiveIntegerField()
    temperature = models.FloatField(blank=True, null=True)
    foreign_item_rate = models.FloatField(blank=True, null=True)
    inv_purchase_request_id = models.IntegerField(blank=True, null=True)
    discount = models.IntegerField()
    discount_amount = models.IntegerField()
    remaining_purchase_order_catalogue = models.IntegerField()
    completed_status = models.IntegerField()
    fix_store_id = models.IntegerField(blank=True, null=True)
    purchase_request_no = models.CharField(max_length=191)
    grn_qty = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_purchase_order_catalogues'


class InvPurchaseOrders(models.Model):
    purchase_order_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    user_role_id = models.PositiveIntegerField()
    supplier_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    program_id = models.PositiveIntegerField(blank=True, null=True)
    requisition_id = models.IntegerField()
    purchase_order_no = models.CharField(max_length=191)
    purchase_order_status = models.IntegerField()
    approved_status = models.PositiveIntegerField()
    user_role_name = models.CharField(max_length=191)
    purchase_order_delivery_site = models.CharField(max_length=191)
    purchase_order_delivery_date = models.DateTimeField()
    purchase_order_date = models.DateField()
    purchase_order_approved_by = models.CharField(max_length=191, blank=True, null=True)
    purchase_order_prepared_by = models.CharField(max_length=191, blank=True, null=True)
    sub_total = models.FloatField()
    tax_per = models.FloatField()
    tax_amount = models.FloatField()
    total = models.FloatField()
    purchase_order_remarks = models.TextField(blank=True, null=True)
    purchase_order_created_by = models.PositiveIntegerField()
    purchase_order_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    approved_by = models.IntegerField(blank=True, null=True)
    completed_status = models.IntegerField()
    currency_id = models.IntegerField(blank=True, null=True)
    exchange_rate = models.FloatField(blank=True, null=True)
    terms_and_condition = models.CharField(max_length=191, blank=True, null=True)
    supplier_bill_no = models.CharField(max_length=191, blank=True, null=True)
    supplier_bill_date = models.CharField(max_length=191, blank=True, null=True)
    credit_days = models.IntegerField()
    vat_no = models.CharField(max_length=191, blank=True, null=True)
    payment_type = models.IntegerField()
    approved_at = models.DateTimeField(blank=True, null=True)
    fix_store_id = models.IntegerField(blank=True, null=True)
    payment_term = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_purchase_orders'


class InvPurchaseRequest(models.Model):
    branch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    requester = models.CharField(max_length=191)
    purchase_request_no = models.CharField(max_length=191)
    requisition_date = models.DateField()
    sales_order_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    remarks = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    purchase_request = models.IntegerField(blank=True, null=True)
    approved_by = models.IntegerField(blank=True, null=True)
    terms_and_condition = models.TextField(blank=True, null=True)
    completed_status = models.IntegerField()
    from_department = models.IntegerField()
    from_sub_store = models.IntegerField()
    from_requistion_id = models.IntegerField(blank=True, null=True)
    requisition_to_request_status = models.IntegerField()
    approved_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_purchase_request'


class InvPurchaseRequestDetail(models.Model):
    branch_id = models.PositiveIntegerField()
    requisition_id = models.PositiveIntegerField(blank=True, null=True)
    inv_purchase_request_id = models.PositiveIntegerField()
    catalogue_id = models.PositiveIntegerField()
    quantity = models.FloatField()
    remaining_quantity = models.IntegerField()
    status = models.IntegerField()
    pacs_size = models.IntegerField(blank=True, null=True)
    reorder_level = models.IntegerField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_purchase_request_detail'


class InvPurchaseReturns(models.Model):
    purchase_return_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    pr_opening_stocks_id = models.PositiveIntegerField()
    pr_closing_stocks_id = models.PositiveIntegerField()
    master_purchases_return_id = models.PositiveIntegerField()
    stock_purchases_id = models.PositiveIntegerField()
    catalogue_type_id = models.PositiveIntegerField()
    catalogue_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    batch = models.CharField(max_length=191)
    return_quantity = models.FloatField()
    expiry_date = models.CharField(max_length=191)
    cost_price = models.FloatField()
    selling_price = models.FloatField()
    profit_percent = models.FloatField()
    purchase_return_status = models.IntegerField()
    purchase_return_remarks = models.TextField(blank=True, null=True)
    purchase_return_created_by = models.PositiveIntegerField()
    purchase_return_updated_by = models.PositiveIntegerField(blank=True, null=True)
    asset_status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    eff_rate = models.FloatField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    tax_per = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_purchase_returns'


class InvReorderEmail(models.Model):
    email = models.CharField(max_length=191, blank=True, null=True)
    name = models.CharField(max_length=191, blank=True, null=True)
    status = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_reorder_email'


class InvReorderEmailLogs(models.Model):
    reorder_email_id = models.IntegerField(blank=True, null=True)
    stock_purchases_id = models.IntegerField(blank=True, null=True)
    stock_purchases_no = models.CharField(max_length=191, blank=True, null=True)
    stock_issue_id = models.IntegerField(blank=True, null=True)
    stock_issue_no = models.CharField(max_length=191, blank=True, null=True)
    catalogue_id = models.IntegerField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_reorder_email_logs'


class InvRequisitionDetail(models.Model):
    branch_id = models.PositiveIntegerField()
    requisition_id = models.PositiveIntegerField()
    catalogue_id = models.PositiveIntegerField()
    quantity = models.FloatField()
    remaining_quantity = models.IntegerField()
    status = models.IntegerField()
    reorder_level = models.IntegerField(blank=True, null=True)
    pacs_size = models.IntegerField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    requisition_no = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_requisition_detail'


class InvRequisitions(models.Model):
    branch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    requisition_no = models.CharField(max_length=191)
    requisition_date = models.DateField()
    sales_order_id = models.IntegerField(blank=True, null=True)
    requester = models.CharField(max_length=191)
    status = models.IntegerField()
    remarks = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    purchase_request = models.IntegerField(blank=True, null=True)
    approved_by = models.IntegerField(blank=True, null=True)
    terms_and_condition = models.CharField(max_length=191, blank=True, null=True)
    completed_status = models.IntegerField()
    from_department = models.IntegerField()
    from_sub_store = models.IntegerField()
    from_requistion_id = models.IntegerField(blank=True, null=True)
    requisition_to_request_status = models.IntegerField()
    is_sub_store = models.IntegerField(blank=True, null=True)
    t_store_id = models.IntegerField(blank=True, null=True)
    t_to_store_id = models.IntegerField(blank=True, null=True)
    to_store_id = models.IntegerField(blank=True, null=True)
    approved_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_requisitions'


class InvRoleUser(models.Model):
    role_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    user_type = models.CharField(max_length=191)
    branch_id = models.CharField(max_length=191)
    ims_type = models.CharField(max_length=191)
    auto_primary = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_role_user'


class InvRoles(models.Model):
    name = models.CharField(max_length=191)
    display_name = models.CharField(max_length=191, blank=True, null=True)
    description = models.CharField(max_length=191, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    ims_type = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'inv_roles'


class InvSalesOrderDetails(models.Model):
    sales_order_id = models.PositiveIntegerField()
    catalogue_id = models.PositiveIntegerField()
    sales_order_catalogue_quantity = models.IntegerField()
    sales_order_catalogue_status = models.IntegerField()
    sales_order_catalogue_remarks = models.TextField(blank=True, null=True)
    sales_order_catalogue_created_by = models.PositiveIntegerField()
    sales_order_catalogue_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    inner = models.PositiveIntegerField(blank=True, null=True)
    outer = models.PositiveIntegerField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    foreign_item_rate = models.FloatField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    amount_without_tax = models.FloatField(blank=True, null=True)
    batch = models.CharField(max_length=100, blank=True, null=True)
    branch_id = models.IntegerField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    customer_item_id = models.CharField(max_length=191, blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    discount_percentage = models.FloatField(blank=True, null=True)
    expiry_date = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    store_id = models.IntegerField(blank=True, null=True)
    tax = models.FloatField(blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_sales_order_details'


class InvSalesOrders(models.Model):
    branch_id = models.PositiveIntegerField()
    customer_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    sales_order_no = models.CharField(max_length=191)
    sales_order_status = models.IntegerField()
    salse_order_delivery_site = models.CharField(max_length=191)
    salse_order_delivery_date = models.DateTimeField()
    salse_order_received_by = models.CharField(max_length=191)
    salse_order_remarks = models.TextField(blank=True, null=True)
    sales_order_created_by = models.PositiveIntegerField()
    sales_order_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    invoice_status = models.IntegerField()
    currency_id = models.IntegerField(blank=True, null=True)
    exchange_rate = models.FloatField(blank=True, null=True)
    amount = models.FloatField()
    amount_without_tax = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    return_status = models.IntegerField(blank=True, null=True)
    sales_order_delivery_date = models.DateTimeField()
    sales_order_delivery_site = models.CharField(max_length=191)
    sales_order_received_by = models.CharField(max_length=191)
    sales_order_remarks = models.CharField(max_length=100, blank=True, null=True)
    tax = models.FloatField(blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_sales_orders'


class InvServiceReturnDetail(models.Model):
    inv_master_service_return_id = models.PositiveIntegerField()
    patient_id = models.PositiveIntegerField()
    inpatient_id = models.PositiveIntegerField()
    catalogue_id = models.PositiveIntegerField()
    item_id = models.PositiveIntegerField()
    catalogue_type_id = models.PositiveIntegerField()
    batch = models.CharField(max_length=191)
    return_qty = models.IntegerField()
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    amt_after_tax = models.FloatField(blank=True, null=True)
    amt_before_discount = models.FloatField(blank=True, null=True)
    cost_price = models.FloatField(blank=True, null=True)
    discount_amt = models.FloatField(blank=True, null=True)
    discount_per = models.FloatField(blank=True, null=True)
    eff_rate = models.FloatField(blank=True, null=True)
    expire_date = models.DateField(blank=True, null=True)
    inpatient_service_id = models.CharField(max_length=191, blank=True, null=True)
    mrp = models.FloatField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    sales_amt_per = models.FloatField(blank=True, null=True)
    service_return_no = models.CharField(max_length=100, blank=True, null=True)
    stock_date = models.DateField(blank=True, null=True)
    store_id = models.IntegerField(blank=True, null=True)
    taxable_amt = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_service_return_detail'


class InvStockConsumptions(models.Model):
    stock_consumption_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveBigIntegerField()
    sc_opening_stocks_id = models.PositiveBigIntegerField()
    sc_closing_stocks_id = models.PositiveBigIntegerField()
    master_stock_consumption_id = models.PositiveBigIntegerField()
    store_id = models.PositiveBigIntegerField()
    record_store_id = models.PositiveBigIntegerField()
    catalogue_type_id = models.PositiveBigIntegerField()
    catalogue_id = models.PositiveBigIntegerField()
    batch = models.CharField(max_length=191)
    expiry_date = models.CharField(max_length=191)
    quantity = models.FloatField()
    cost_price = models.FloatField()
    selling_price = models.FloatField()
    profit_percent = models.FloatField()
    consumption_no = models.CharField(max_length=191)
    status = models.IntegerField()
    consumption_date = models.CharField(max_length=191)
    amount = models.FloatField()
    total = models.FloatField()
    created_by = models.PositiveBigIntegerField()
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    stock_issue_id = models.PositiveIntegerField(blank=True, null=True)
    stock_issue_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_stock_consumptions'


class InvStockIssues(models.Model):
    stock_issue_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    master_stock_issues_id = models.PositiveIntegerField()
    stock_issue_no = models.CharField(max_length=191)
    master_stock_purchases_id = models.PositiveIntegerField()
    stock_purchases_id = models.PositiveIntegerField()
    stock_purchases_no = models.CharField(max_length=191)
    si_opening_stocks_id = models.PositiveIntegerField()
    si_closing_stocks_id = models.PositiveIntegerField()
    catalogue_id = models.PositiveIntegerField()
    catalogue_type_id = models.PositiveIntegerField()
    master_returns_id = models.PositiveIntegerField(blank=True, null=True)
    returns_no = models.CharField(max_length=191, blank=True, null=True)
    store_id = models.PositiveIntegerField()
    received_from_store = models.PositiveIntegerField()
    batch = models.CharField(max_length=191)
    i_quantity = models.FloatField()
    i_stock_quantity = models.FloatField()
    i_revert_quantity = models.FloatField()
    expiry_date = models.CharField(max_length=191)
    cost_price = models.FloatField()
    selling_price = models.FloatField()
    profit_percent = models.FloatField()
    stock_issue_status = models.IntegerField()
    stock_issue_created_by = models.PositiveIntegerField()
    stock_issue_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    registered_book_no = models.CharField(max_length=191, blank=True, null=True)
    registered_page_no = models.CharField(max_length=191, blank=True, null=True)
    requisition_no = models.CharField(max_length=191, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    parent_stock_issue_id = models.PositiveIntegerField(blank=True, null=True)
    cancel_status = models.IntegerField()
    discount_amount = models.FloatField(blank=True, null=True)
    discount_per = models.FloatField(blank=True, null=True)
    effrate = models.FloatField(blank=True, null=True)
    grn_id = models.IntegerField(blank=True, null=True)
    grn_no = models.CharField(max_length=191, blank=True, null=True)
    mater_grn_id = models.IntegerField(blank=True, null=True)
    mrp = models.FloatField(blank=True, null=True)
    rec_status = models.IntegerField(blank=True, null=True)
    received_date = models.DateTimeField(blank=True, null=True)
    tax_amount = models.FloatField(blank=True, null=True)
    tax_per = models.FloatField(blank=True, null=True)
    temp_req_no = models.CharField(max_length=190, blank=True, null=True)
    rec_eff_rate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_stock_issues'


class InvStockLog(models.Model):
    store_id = models.PositiveIntegerField(blank=True, null=True)
    branch_id = models.PositiveIntegerField(blank=True, null=True)
    catalogue_id = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    purchase_number = models.CharField(max_length=191, blank=True, null=True)
    issue_number = models.PositiveIntegerField(blank=True, null=True)
    total_stock = models.PositiveIntegerField(blank=True, null=True)
    remaining_stock = models.PositiveIntegerField(blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    batch = models.CharField(max_length=191, blank=True, null=True)
    remark = models.CharField(max_length=191, blank=True, null=True)
    type = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    grn_id = models.IntegerField(blank=True, null=True)
    grn_no = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_stock_log'


class InvStockPurchases(models.Model):
    stock_purchases_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    master_stock_purchases_id = models.PositiveIntegerField()
    stock_purchases_no = models.CharField(max_length=191, blank=True, null=True)
    purchases_order_id = models.PositiveIntegerField(blank=True, null=True)
    purchases_order_no = models.CharField(max_length=191, blank=True, null=True)
    good_receipt_note_id = models.IntegerField(blank=True, null=True)
    good_receipt_note_no = models.CharField(max_length=191, blank=True, null=True)
    sp_opening_stocks_id = models.PositiveIntegerField()
    sp_closing_stocks_id = models.PositiveIntegerField()
    catalogue_type_id = models.PositiveIntegerField()
    catalogue_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    batch = models.CharField(max_length=191)
    p_quantity = models.FloatField()
    p_stock_quantity = models.FloatField()
    p_return_quantity = models.FloatField()
    disposed_qty = models.PositiveIntegerField()
    expired_breakage_id = models.PositiveIntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=191, blank=True, null=True)
    expiry_date = models.CharField(max_length=191)
    cp_before_tax = models.FloatField()
    discount_per = models.FloatField()
    discount_amount = models.FloatField()
    is_taxable = models.IntegerField()
    taxable_amt = models.FloatField()
    tax_per = models.FloatField()
    tax_amount = models.FloatField()
    cost_price = models.FloatField()
    selling_price = models.FloatField()
    profit_percent = models.FloatField()
    stock_purchases_remarks = models.TextField(blank=True, null=True)
    stock_purchases_status = models.IntegerField()
    approved_status = models.PositiveIntegerField()
    purchase_return_status = models.IntegerField()
    stock_purchases_created_by = models.PositiveIntegerField()
    stock_purchases_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    foreign_cp = models.FloatField(blank=True, null=True)
    registered_book_no = models.CharField(max_length=191, blank=True, null=True)
    registered_page_no = models.CharField(max_length=191, blank=True, null=True)
    program_id = models.IntegerField(blank=True, null=True)
    supplier_id = models.IntegerField(blank=True, null=True)
    manufacture_id = models.IntegerField()
    salvage = models.IntegerField(blank=True, null=True)
    asset_status = models.IntegerField(blank=True, null=True)
    warnt_period = models.IntegerField()
    asset_purchase_no = models.CharField(max_length=191, blank=True, null=True)
    asset_purchase_date = models.DateTimeField(blank=True, null=True)
    model_no = models.CharField(max_length=191, blank=True, null=True)
    serial_no = models.CharField(max_length=191, blank=True, null=True)
    purchase_date = models.DateField(blank=True, null=True)
    purchase_invoice_no = models.CharField(max_length=191, blank=True, null=True)
    manufacture_date = models.DateField(blank=True, null=True)
    country_of_origin = models.CharField(max_length=191, blank=True, null=True)
    net_value = models.FloatField()
    purchase_price = models.FloatField()
    installation_date = models.DateField(blank=True, null=True)
    useful_life = models.PositiveIntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    grn_id = models.IntegerField(blank=True, null=True)
    is_old_norvic = models.IntegerField(blank=True, null=True)
    mrp = models.FloatField(blank=True, null=True)
    ref_stock_purchases_id = models.IntegerField(blank=True, null=True)
    ri = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_stock_purchases'


class InvStockQuantities(models.Model):
    catalogue_id = models.IntegerField()
    store_id = models.IntegerField()
    quantity = models.IntegerField()
    assest_flag = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_stock_quantities'


class InvStockReportLogs(models.Model):
    branch_id = models.PositiveIntegerField()
    data = models.TextField()
    date = models.DateField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_stock_report_logs'


class InvStores(models.Model):
    store_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    store_name = models.CharField(max_length=191)
    store_description = models.TextField(blank=True, null=True)
    is_pos = models.IntegerField()
    active = models.IntegerField()
    store_created_by = models.PositiveIntegerField()
    store_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_main_store = models.IntegerField()
    lead_time = models.CharField(max_length=191, blank=True, null=True)
    delivery_day = models.CharField(max_length=191, blank=True, null=True)
    stock_days = models.CharField(max_length=191, blank=True, null=True)
    parent_id = models.IntegerField()
    is_sub_store = models.IntegerField()
    sub_store_id = models.IntegerField(blank=True, null=True)
    department_id = models.PositiveIntegerField()
    cost_center_id = models.IntegerField(blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    is_fixed_asset_main_store = models.IntegerField()
    code = models.CharField(max_length=192, blank=True, null=True)
    is_old_norvic = models.IntegerField(blank=True, null=True)
    ref_store_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_stores'


class InvSupplierWiseManufactureDiscount(models.Model):
    supplier_id = models.PositiveIntegerField(blank=True, null=True)
    manufacture_id = models.PositiveIntegerField(blank=True, null=True)
    catalogue_id = models.PositiveIntegerField(blank=True, null=True)
    catalogue_type_id = models.PositiveIntegerField(blank=True, null=True)
    bonus_qty = models.PositiveIntegerField(blank=True, null=True)
    discount = models.PositiveIntegerField(blank=True, null=True)
    cost_price = models.FloatField()
    selling_price = models.FloatField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_supplier_wise_manufacture_discount'


class InvSuppliers(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    supplier_name = models.CharField(max_length=191)
    supplier_code = models.CharField(unique=True, max_length=191)
    supplier_address = models.CharField(max_length=191, blank=True, null=True)
    supplier_email = models.CharField(max_length=191, blank=True, null=True)
    supplier_description = models.TextField(blank=True, null=True)
    supplier_pan_vat = models.CharField(max_length=191)
    supplier_contact = models.CharField(max_length=191)
    supplier_status = models.IntegerField()
    supplier_created_by = models.PositiveIntegerField()
    supplier_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    acc_partner_id = models.IntegerField()
    acc_account_id = models.IntegerField()
    tds_percentage = models.IntegerField()
    terms = models.IntegerField()
    acc_cost_center_id = models.IntegerField(blank=True, null=True)
    credit_days = models.IntegerField()
    is_old_norvic = models.IntegerField(blank=True, null=True)
    ref_supplier_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_suppliers'


class InvTransactionStatus(models.Model):
    code = models.PositiveIntegerField()
    name = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'inv_transaction_status'


class InvTransactionType(models.Model):
    type = models.PositiveIntegerField()
    name = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'inv_transaction_type'


class InvUnitInventories(models.Model):
    unit_inventory_id = models.AutoField(primary_key=True)
    unit_inventory_name = models.CharField(max_length=191)
    unit_inventory_created_by = models.PositiveIntegerField()
    unit_inventory_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_unit_inventories'


class InvVendors(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    vendor_name = models.CharField(max_length=191)
    vendor_country = models.CharField(max_length=191)
    vendor_address = models.CharField(max_length=191, blank=True, null=True)
    vendor_status = models.IntegerField()
    vendor_created_by = models.PositiveIntegerField()
    vendor_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_old_norvic = models.IntegerField(blank=True, null=True)
    ref_vendor_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_vendors'


class InventoryConfigs(models.Model):
    name = models.CharField(max_length=191)
    value = models.TextField()
    type = models.CharField(max_length=191)
    description = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'inventory_configs'


class InventoryLogs(models.Model):
    asset_no = models.CharField(max_length=191)
    asset_id = models.IntegerField()
    modified_by = models.CharField(max_length=191)
    modified_date = models.DateField()
    remarks = models.CharField(max_length=191)
    type = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_old_norvic = models.IntegerField(blank=True, null=True)
    ref_asset_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory_logs'


class InvestigationSubtypes(models.Model):
    investigation_type_id = models.IntegerField()
    investigation_subtype = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'investigation_subtypes'


class InvestigationTypes(models.Model):
    investigation_type = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'investigation_types'


class IpAdmission(models.Model):
    slno = models.AutoField(db_column='SlNo', primary_key=True)  # Field name made lowercase.
    admission_date = models.CharField(max_length=10)
    patient_id = models.CharField(max_length=29)
    diagnosis = models.CharField(max_length=32, blank=True, null=True)
    u_dept_id = models.CharField(max_length=4)
    ref_dept_id = models.IntegerField()
    status = models.IntegerField()
    pat_type = models.IntegerField()
    category_type = models.IntegerField(blank=True, null=True)
    discharge_date = models.CharField(max_length=10, blank=True, null=True)
    final = models.CharField(max_length=1, blank=True, null=True)
    admission_date_eng = models.CharField(max_length=10, blank=True, null=True)
    discharge_date_nep = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ip_admission'


class IpAdmission1(models.Model):
    slno = models.IntegerField(db_column='SlNo', primary_key=True)  # Field name made lowercase.
    admission_date = models.CharField(max_length=10)
    patient_id = models.CharField(max_length=29)
    diagnosis = models.CharField(db_column='Diagnosis', max_length=32, blank=True, null=True)  # Field name made lowercase.
    admission_date_eng = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'ip_admission_1'


class IpdBedDetails(models.Model):
    in_pat_id = models.IntegerField()
    pat_id = models.IntegerField()
    emergency_pat_id = models.IntegerField()
    dialysis_pat_id = models.IntegerField()
    ward_id = models.IntegerField()
    ward_name = models.CharField(max_length=255)
    room_type_id = models.IntegerField()
    room_type_name = models.CharField(max_length=255)
    bed_id = models.IntegerField()
    bed_charge = models.FloatField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField()
    cancel_status = models.IntegerField()
    s_billdetail_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    date = models.DateField()
    day = models.FloatField()
    fromdate = models.DateTimeField(blank=True, null=True)
    is_patient_attendant = models.IntegerField()
    reserve_status = models.IntegerField()
    temp_pat_id = models.IntegerField()
    todate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ipd_bed_details'


class IpdBeds(models.Model):
    in_pat_id = models.IntegerField()
    pat_id = models.IntegerField()
    emergency_pat_id = models.IntegerField()
    dialysis_pat_id = models.IntegerField()
    ward_id = models.IntegerField()
    ward_name = models.CharField(max_length=255)
    room_type_id = models.IntegerField()
    room_type_name = models.CharField(max_length=255)
    bed_id = models.IntegerField()
    cancel_status = models.IntegerField()
    discharge_status = models.IntegerField()
    total_days = models.IntegerField()
    bed_charge = models.FloatField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_patient_attendant = models.IntegerField()
    reserve_status = models.IntegerField()
    temp_pat_id = models.IntegerField()
    transfer_bed = models.IntegerField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ipd_beds'


class IpdDoctorDetails(models.Model):
    in_pat_id = models.IntegerField()
    pat_id = models.IntegerField()
    emergency_pat_id = models.IntegerField()
    dialysis_pat_id = models.IntegerField()
    doctor_id = models.IntegerField()
    doctor_name = models.CharField(max_length=255)
    dept_id = models.IntegerField()
    dept_name = models.CharField(max_length=255)
    round_charge = models.FloatField()
    room_type_id = models.IntegerField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField()
    cancel_status = models.IntegerField()
    s_billdetail_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    date = models.DateField()
    consultant_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ipd_doctor_details'


class IpdDoctorShares(models.Model):
    in_pat_id = models.IntegerField()
    pat_id = models.IntegerField()
    s_bill_detail_id = models.IntegerField()
    item_id = models.IntegerField()
    designation_id = models.IntegerField()
    doctor_id = models.IntegerField()
    doctor_name = models.CharField(max_length=255)
    tds_per = models.FloatField(db_column='TDS_per')  # Field name made lowercase.
    tds_amt = models.FloatField(db_column='TDS_amt')  # Field name made lowercase.
    share_per = models.FloatField()
    share_amt = models.FloatField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    category_id = models.IntegerField()
    lock_status = models.IntegerField()
    cancel_status = models.IntegerField()
    m_bill_detail_id = models.IntegerField()
    master_bill_id = models.IntegerField()
    s_master_bill_id = models.IntegerField()
    type = models.IntegerField()
    refunded = models.IntegerField()
    ref_share_id = models.IntegerField()
    gross = models.FloatField()
    dis_per = models.FloatField()
    dis_amt = models.FloatField()
    journal_id = models.IntegerField()
    consultant_type = models.IntegerField(blank=True, null=True)
    emergency_pat_id = models.PositiveIntegerField()
    amt_ad = models.FloatField(blank=True, null=True)
    voucher_id = models.PositiveIntegerField()
    acc_bill_id = models.PositiveIntegerField()
    package_bill_detail_id = models.PositiveIntegerField(blank=True, null=True)
    inherit_category_type = models.PositiveIntegerField()
    account_posting_status = models.IntegerField()
    deduction_posting_status = models.IntegerField()
    deduction_status = models.IntegerField()
    deduction_voucher_id = models.PositiveIntegerField()
    deduction_voucher_no = models.CharField(max_length=255, blank=True, null=True)
    dialysis_pat_id = models.PositiveIntegerField()
    exceptional_category_type = models.PositiveIntegerField()
    package_item_id = models.PositiveIntegerField()
    repost_status = models.IntegerField()
    reverse_posting_status = models.IntegerField()
    reverse_voucher_id = models.PositiveIntegerField()
    reverse_voucher_no = models.CharField(max_length=255, blank=True, null=True)
    sharing_percent = models.FloatField()
    team_doctor_id = models.PositiveIntegerField()
    team_doctor_name = models.CharField(max_length=255, blank=True, null=True)
    team_doctor_percent = models.FloatField(blank=True, null=True)
    voucher_no = models.CharField(max_length=255, blank=True, null=True)
    refund_detail_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ipd_doctor_shares'


class IpdDoctors(models.Model):
    in_pat_id = models.IntegerField()
    pat_id = models.IntegerField()
    emergency_pat_id = models.IntegerField()
    dialysis_pat_id = models.IntegerField()
    doctor_id = models.IntegerField()
    doctor_name = models.CharField(max_length=255)
    dept_id = models.IntegerField()
    dept_name = models.CharField(max_length=255)
    cancel_status = models.IntegerField()
    discharge_status = models.IntegerField()
    room_type_id = models.IntegerField()
    total_days = models.IntegerField()
    round_charge = models.FloatField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    consultant_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ipd_doctors'


class IpdLogs(models.Model):
    in_pat_id = models.IntegerField()
    pat_id = models.IntegerField()
    ward_id = models.IntegerField()
    ward_name = models.CharField(max_length=255)
    room_type_id = models.IntegerField()
    room_type_name = models.CharField(max_length=255)
    bed_id = models.IntegerField()
    department_id = models.IntegerField()
    department_name = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    admitted_date = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    emerg_pat_id = models.PositiveIntegerField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ipd_logs'


class IpdNoticeLogs(models.Model):
    inpat_id = models.PositiveIntegerField()
    remarks = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    del_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ipd_notice_logs'


class IpdNurses(models.Model):
    pat_id = models.IntegerField()
    in_pat_id = models.IntegerField()
    emergency_pat_id = models.IntegerField()
    nurse_id = models.IntegerField()
    nurse_name = models.CharField(max_length=255)
    created_by = models.IntegerField()
    updated_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ipd_nurses'


class Ips(models.Model):
    address = models.CharField(max_length=255)
    active = models.IntegerField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ips'


class IssueMidasVoucher(models.Model):
    voucher_no = models.CharField(unique=True, max_length=255)
    in_pat_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issue_midas_voucher'


class IssueReturns(models.Model):
    issue_return_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    ir_opening_stocks_id = models.PositiveIntegerField()
    ir_closing_stocks_id = models.PositiveIntegerField()
    master_returns_id = models.PositiveIntegerField()
    master_stock_issue_id = models.PositiveIntegerField()
    stock_issue_id = models.PositiveIntegerField()
    catalogue_type_id = models.PositiveIntegerField()
    catalogue_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    return_to_store = models.PositiveIntegerField()
    batch = models.CharField(max_length=191)
    i_revert_quantity = models.PositiveIntegerField()
    expiry_date = models.CharField(max_length=191)
    cost_price = models.FloatField()
    selling_price = models.FloatField()
    profit_percent = models.FloatField()
    issue_return_status = models.IntegerField()
    expiry_return_status = models.IntegerField()
    issue_return_created_by = models.PositiveIntegerField()
    issue_return_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issue_returns'


class ItemInsurances(models.Model):
    service_code = models.CharField(max_length=255)
    service_name = models.CharField(max_length=255)
    service_price = models.FloatField(blank=True, null=True)
    item_type = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_insurances'


class ItemRefundLogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    master_bill_id = models.PositiveBigIntegerField(blank=True, null=True)
    bill_detail_id = models.PositiveBigIntegerField(blank=True, null=True)
    test_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    package_test_pivot_ids = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_refund_logs'


class ItemServiceWiseBudgets(models.Model):
    item_id = models.PositiveIntegerField()
    code = models.PositiveIntegerField()
    patient_qty = models.IntegerField()
    per_day_patient_qty = models.FloatField()
    service_qty = models.IntegerField()
    per_day_service_qty = models.FloatField()
    amount = models.FloatField()
    per_day_amount = models.FloatField()
    fiscalyear = models.IntegerField()
    month = models.IntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_service_wise_budgets'


class ItemSsf(models.Model):
    service_code = models.CharField(max_length=255)
    service_name = models.CharField(max_length=255)
    service_price = models.FloatField(blank=True, null=True)
    item_type = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    service_validity_from = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_ssf'


class ItemTags(models.Model):
    parent_item_id = models.PositiveIntegerField()
    child_item_id = models.PositiveIntegerField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_tags'


class ItemTeams(models.Model):
    item = models.ForeignKey('Items', models.DO_NOTHING)
    visit_type = models.ForeignKey('VisitTypes', models.DO_NOTHING)
    percentage = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_teams'


class ItemTemplate(models.Model):
    template_name = models.CharField(max_length=255)
    item_id = models.IntegerField()
    publish_date = models.DateTimeField()
    status = models.IntegerField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    department_id = models.IntegerField()
    item_type = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'item_template'


class Items(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    department = models.ForeignKey(Departments, models.DO_NOTHING, blank=True, null=True)
    is_active = models.IntegerField()
    is_lab_item = models.IntegerField()
    is_discountable = models.IntegerField()
    is_package = models.IntegerField()
    is_pharmacy = models.IntegerField()
    pharmacy_type = models.IntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    single_page = models.IntegerField()
    taxable = models.IntegerField()
    item_type = models.CharField(max_length=4)
    is_opdbill = models.IntegerField()
    mig_id = models.IntegerField(blank=True, null=True)
    doctor_id = models.IntegerField()
    doctor_name = models.CharField(max_length=255)
    doctor_share = models.FloatField()
    tds = models.FloatField()
    followup_doctor_share = models.FloatField()
    followup_tds = models.FloatField()
    is_registration = models.IntegerField()
    is_helpline = models.IntegerField()
    department_type = models.PositiveIntegerField(blank=True, null=True)
    room_type_id = models.IntegerField()
    round_charge = models.IntegerField()
    shareable = models.IntegerField()
    income_head_id = models.IntegerField(blank=True, null=True)
    main_category_id = models.IntegerField(blank=True, null=True)
    service_category_id = models.IntegerField(blank=True, null=True)
    default = models.IntegerField()
    group_id = models.IntegerField(blank=True, null=True)
    bed_charge = models.IntegerField()
    is_teleconsultation = models.IntegerField()
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    sms_billing = models.IntegerField()
    discount_grp_id = models.IntegerField()
    discount_per_id = models.IntegerField()
    is_emergency_registration = models.PositiveIntegerField()
    group_item = models.IntegerField()
    is_service_charge = models.IntegerField()
    opd_service_charge_percent = models.FloatField(blank=True, null=True)
    ipd_service_charge_percent = models.FloatField(blank=True, null=True)
    is_dialysis_charge = models.IntegerField()
    catalogue_id = models.PositiveIntegerField(blank=True, null=True)
    is_surgery = models.IntegerField()
    is_package_panel = models.IntegerField()
    rate_percent = models.FloatField()
    is_inventory_item = models.IntegerField(blank=True, null=True)
    is_zero_charge = models.IntegerField()
    is_medical_registration = models.IntegerField()
    is_anesthesia_charge = models.IntegerField()
    is_additional_cons_charge = models.IntegerField()
    show_in_revenue_report = models.IntegerField()
    time_basis_from = models.CharField(max_length=255, blank=True, null=True)
    time_basis_to = models.CharField(max_length=255, blank=True, null=True)
    is_procedure = models.IntegerField()
    is_physiotherapy = models.IntegerField()
    enable_rate_percent = models.IntegerField()
    is_tag_item = models.IntegerField()
    team_item = models.IntegerField()
    package_duration = models.PositiveIntegerField()
    ot_charge = models.IntegerField(blank=True, null=True)
    is_emergency_charge = models.IntegerField(blank=True, null=True)
    show_in_other_charge = models.IntegerField(blank=True, null=True)
    sharing_percent_limit = models.FloatField()
    enable_sharing_consultant = models.IntegerField()
    enable_sharing_refer_by_consultant = models.IntegerField()
    enable_sharing_service_refer_by_consultant = models.IntegerField()
    max_sharing_percent = models.FloatField()
    parent_id = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    applicability = models.PositiveIntegerField()
    bed_id = models.PositiveIntegerField(blank=True, null=True)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    is_bed_charge = models.IntegerField()
    is_performing = models.IntegerField()
    is_utilization = models.IntegerField(blank=True, null=True)
    item_pre_description = models.TextField(blank=True, null=True)
    ref_department_id = models.PositiveIntegerField(blank=True, null=True)
    is_consultant_charge = models.IntegerField()
    is_uk = models.IntegerField()
    insurance_service_id = models.PositiveIntegerField(blank=True, null=True)
    ssf_service = models.ForeignKey(ItemSsf, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items'


class ItemsGroup(models.Model):
    item_group = models.CharField(max_length=255)
    created_by = models.IntegerField()
    updated_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items_group'


class Jobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    queue = models.CharField(max_length=255)
    payload = models.TextField()
    attempts = models.PositiveIntegerField()
    reserved = models.PositiveIntegerField()
    reserved_at = models.PositiveIntegerField(blank=True, null=True)
    available_at = models.PositiveIntegerField()
    created_at = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'jobs'


class LeaveSetup(models.Model):
    day_date_type = models.CharField(max_length=4)
    leave_day = models.CharField(max_length=3)
    leave_date = models.DateTimeField(blank=True, null=True)
    remarks = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leave_setup'


class LeaveSetupException(models.Model):
    consultant_id = models.PositiveIntegerField()
    is_leave = models.CharField(max_length=1)
    day_date_type = models.CharField(max_length=4)
    leave_day = models.CharField(max_length=3)
    leave_date = models.DateTimeField(blank=True, null=True)
    remarks = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leave_setup_exception'


class Ledgers(models.Model):
    master_bill_id = models.IntegerField()
    bill_no = models.CharField(max_length=255, blank=True, null=True)
    discount_group = models.IntegerField(blank=True, null=True)
    discount_type = models.IntegerField(blank=True, null=True)
    debt_amt = models.DecimalField(max_digits=8, decimal_places=2)
    credit_amt = models.DecimalField(max_digits=8, decimal_places=2)
    refund_master_id = models.IntegerField()
    parent_id = models.IntegerField()
    child_id = models.IntegerField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    reference_bill_no = models.CharField(max_length=255, blank=True, null=True)
    is_discount = models.IntegerField()
    remarks = models.TextField()
    note = models.TextField()
    bill_type = models.CharField(max_length=1, blank=True, null=True)
    branch = models.PositiveIntegerField()
    revenue_center = models.IntegerField()
    payment_type = models.IntegerField()
    bank_id = models.PositiveIntegerField()
    card_no = models.CharField(max_length=255, blank=True, null=True)
    cheque_no = models.CharField(max_length=255, blank=True, null=True)
    partner_id = models.IntegerField(blank=True, null=True)
    rate_type = models.ForeignKey('PatientCategories', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ledgers'


class LocalCode(models.Model):
    code = models.CharField(max_length=191)
    disease = models.CharField(max_length=191)
    is_icd = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'local_code'


class MachineLogDetails(models.Model):
    machine_log_id = models.IntegerField()
    patient_id = models.IntegerField()
    sample_id = models.CharField(max_length=255)
    record_id = models.CharField(max_length=255, blank=True, null=True)
    host_code = models.CharField(max_length=255, blank=True, null=True)
    test_id = models.CharField(max_length=255)
    parameter_id = models.PositiveIntegerField()
    value = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    flag = models.CharField(max_length=255)
    status = models.IntegerField()
    error_log = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    branch = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'machine_log_details'


class MachineLogs(models.Model):
    machine_name = models.CharField(max_length=255)
    probe_id = models.IntegerField()
    uuid = models.CharField(max_length=255)
    data = models.TextField()
    sample_id = models.CharField(max_length=255)
    patient_id = models.IntegerField()
    status = models.IntegerField()
    error_log = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    result_date_time = models.TextField()

    class Meta:
        managed = False
        db_table = 'machine_logs'


class Machines(models.Model):
    machine_name = models.CharField(max_length=255)
    device_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'machines'


class MailMessages(models.Model):
    subject = models.TextField(blank=True, null=True)
    message = models.TextField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_messages'


class MailUsers(models.Model):
    mail_message = models.ForeignKey('Users', models.DO_NOTHING)
    from_user = models.ForeignKey('Users', models.DO_NOTHING, related_name='mailusers_from_user_set')
    to_user = models.ForeignKey('Users', models.DO_NOTHING, related_name='mailusers_to_user_set')
    status = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mail_users'


class MainCategories(models.Model):
    main_category = models.CharField(max_length=255)
    created_by = models.IntegerField()
    updated_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_categories'


class ManageExpireBreakage(models.Model):
    name = models.CharField(max_length=191, blank=True, null=True)
    status = models.PositiveIntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manage_expire_breakage'


class Manpower(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'manpower'


class MasterBills(models.Model):
    bill_no = models.CharField(max_length=255, blank=True, null=True)
    internal_no = models.IntegerField(blank=True, null=True)
    patient = models.ForeignKey('Patients', models.DO_NOTHING, blank=True, null=True)
    emergency_pat_id = models.IntegerField()
    dialysis_pat_id = models.IntegerField()
    refund_master_id = models.PositiveIntegerField(blank=True, null=True)
    refund_status = models.IntegerField()
    reference_bill_id = models.IntegerField(blank=True, null=True)
    pan = models.CharField(max_length=255, blank=True, null=True)
    claim_code = models.CharField(max_length=255, blank=True, null=True)
    print_count = models.IntegerField()
    tender_amt = models.IntegerField()
    amt_wo_tax = models.FloatField(blank=True, null=True)
    amt_w_tax = models.FloatField(blank=True, null=True)
    amt_bd = models.FloatField(blank=True, null=True)
    amt_ad = models.FloatField(blank=True, null=True)
    master_discount = models.FloatField(blank=True, null=True)
    master_tax = models.FloatField(blank=True, null=True)
    master_total = models.FloatField(blank=True, null=True)
    consultant = models.PositiveIntegerField()
    ref_consultant = models.IntegerField(blank=True, null=True)
    discount_group_id = models.PositiveIntegerField()
    discount_group_percent_id = models.PositiveIntegerField(blank=True, null=True)
    discount_type_percent = models.PositiveIntegerField()
    payment_type = models.PositiveIntegerField(blank=True, null=True)
    bank_id = models.PositiveIntegerField()
    card_no = models.CharField(max_length=255, blank=True, null=True)
    cheque_no = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at_nepali_date = models.CharField(max_length=10)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    ref_hospital = models.CharField(max_length=255)
    ird_status = models.IntegerField()
    ref_hospital_id = models.IntegerField()
    has_opd = models.IntegerField()
    amount = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    taxable_amt = models.FloatField(blank=True, null=True)
    tax = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    credit_status = models.IntegerField()
    in_pat_id = models.IntegerField()
    branch = models.PositiveIntegerField()
    revenue_center = models.IntegerField(blank=True, null=True)
    category_type = models.PositiveIntegerField()
    discharge_status = models.IntegerField()
    lock_status = models.IntegerField()
    remarks = models.CharField(max_length=255, blank=True, null=True)
    urgent_status = models.IntegerField()
    gateway_ref = models.CharField(max_length=255, blank=True, null=True)
    epay_vendor_id = models.IntegerField(blank=True, null=True)
    online_status = models.IntegerField()
    is_teleconsultation = models.IntegerField()
    batch_id = models.PositiveIntegerField()
    online_purchase = models.IntegerField()
    partner_id = models.IntegerField(blank=True, null=True)
    department_id = models.IntegerField()
    journal_id = models.IntegerField(blank=True, null=True)
    round_off = models.FloatField(blank=True, null=True)
    doctor_discount_per = models.PositiveIntegerField(blank=True, null=True)
    doctor_discount_total_amt = models.FloatField(blank=True, null=True)
    site_id = models.PositiveIntegerField(blank=True, null=True)
    transaction_date = models.DateTimeField(blank=True, null=True)
    account_posting_status = models.IntegerField()
    admitted_date = models.DateTimeField(blank=True, null=True)
    cancel_status = models.IntegerField(blank=True, null=True)
    cashcredit = models.CharField(max_length=100, blank=True, null=True)
    discharged_date = models.DateTimeField(blank=True, null=True)
    doctor_discount = models.FloatField()
    hospital_discount = models.FloatField()
    norv_bill_no = models.CharField(max_length=100, blank=True, null=True)
    patage = models.IntegerField(blank=True, null=True)
    patno = models.CharField(max_length=100, blank=True, null=True)
    patage_type = models.CharField(max_length=1)
    bill_no_short = models.CharField(max_length=20, blank=True, null=True)
    bill_no_sequence = models.IntegerField(blank=True, null=True)
    fiscal_year = models.CharField(max_length=4, blank=True, null=True)
    employee_id = models.PositiveIntegerField(blank=True, null=True)
    ssf_no = models.CharField(max_length=255, blank=True, null=True)
    insurance_no = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_bills'
        unique_together = (('bill_no', 'branch'),)


class MasterCreditNotes(models.Model):
    master_credit_note_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    supplier_id = models.PositiveIntegerField(blank=True, null=True)
    msp_opening_stocks_id = models.PositiveIntegerField()
    msp_closing_stocks_id = models.PositiveIntegerField()
    credit_note_no = models.CharField(max_length=191, blank=True, null=True)
    master_purchases_return_id = models.IntegerField(blank=True, null=True)
    vendor_credit_note_no = models.CharField(max_length=191, blank=True, null=True)
    supplier_bill_no = models.CharField(max_length=191, blank=True, null=True)
    supplier_bill_date = models.CharField(max_length=191, blank=True, null=True)
    total_quantity = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    discount_amount = models.FloatField(blank=True, null=True)
    discount_per = models.FloatField(blank=True, null=True)
    tax_per = models.FloatField(blank=True, null=True)
    tax_amount = models.FloatField(blank=True, null=True)
    other_charges = models.FloatField()
    cc = models.PositiveIntegerField()
    total_amount = models.FloatField(blank=True, null=True)
    payment_type = models.IntegerField(blank=True, null=True)
    master_credit_note_remarks = models.TextField(blank=True, null=True)
    master_credit_note_cancel_remarks = models.TextField(blank=True, null=True)
    credit_note_good_in_date = models.DateField(blank=True, null=True)
    credit_note_good_in_nepali_date = models.CharField(max_length=191, blank=True, null=True)
    master_credit_note_cancel_status = models.IntegerField()
    master_credit_note_created_by = models.PositiveIntegerField()
    master_credit_note_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_credit_notes'


class MasterExpiredReturns(models.Model):
    master_expired_returns_id = models.AutoField(primary_key=True)
    expired_returns_no = models.CharField(max_length=191)
    total_qty = models.PositiveIntegerField()
    master_expired_returns_remarks = models.TextField(blank=True, null=True)
    master_expired_returns_created_by = models.PositiveIntegerField()
    master_expired_returns_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_expired_returns'


class MasterFluidManagement(models.Model):
    patient_id = models.IntegerField()
    inpatient_id = models.IntegerField()
    total_intake = models.FloatField()
    total_output = models.FloatField()
    insensible_loses = models.FloatField()
    total_balance = models.FloatField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    er_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'master_fluid_management'


class MasterMedication(models.Model):
    status = models.CharField(max_length=10)
    patient_id = models.IntegerField()
    ipd_id = models.IntegerField()
    ordered_at = models.CharField(max_length=191, blank=True, null=True)
    ordered_by = models.IntegerField(blank=True, null=True)
    requisition_no = models.CharField(max_length=191, blank=True, null=True)
    approved_at = models.CharField(max_length=191, blank=True, null=True)
    approved_by = models.IntegerField(blank=True, null=True)
    received_at = models.CharField(max_length=191, blank=True, null=True)
    received_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    other_order = models.TextField(blank=True, null=True)
    investigation = models.TextField(blank=True, null=True)
    plan_and_concern = models.TextField(blank=True, null=True)
    doctor_round_note = models.TextField(blank=True, null=True)
    allergies_and_adr = models.TextField(blank=True, null=True)
    er_id = models.IntegerField()
    prescribed_date = models.DateField()
    dialysis_pat_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'master_medication'


class MasterPurchasesReturns(models.Model):
    master_purchases_return_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    mpr_opening_stocks_id = models.PositiveIntegerField()
    mpr_closing_stocks_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    supplier_id = models.PositiveIntegerField()
    purchases_return_no = models.CharField(max_length=191)
    return_status = models.IntegerField()
    cancel_status = models.IntegerField()
    is_salable = models.IntegerField()
    opening_return_flag = models.IntegerField()
    total_return_qty = models.PositiveIntegerField()
    sub_total = models.FloatField()
    courier_charge = models.FloatField()
    discount = models.FloatField()
    tax_amount = models.FloatField()
    total_return_amount = models.FloatField()
    adjustment_amount = models.FloatField()
    master_purchases_return_remarks = models.TextField(blank=True, null=True)
    credit_note = models.CharField(max_length=191, blank=True, null=True)
    credit_remark = models.TextField(blank=True, null=True)
    master_purchases_returns_created_by = models.PositiveIntegerField()
    master_purchases_returns_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    reverted_date = models.CharField(max_length=191, blank=True, null=True)
    credit_note_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'master_purchases_returns'


class MasterRefunds(models.Model):
    master_bill = models.OneToOneField(MasterBills, models.DO_NOTHING, blank=True, null=True)
    pan = models.CharField(max_length=255, blank=True, null=True)
    print_count = models.IntegerField()
    remarks = models.TextField()
    bill_no = models.CharField(max_length=255)
    gross_total = models.FloatField()
    amount = models.FloatField()
    tax_amount = models.FloatField()
    discount_amount = models.FloatField()
    bill_total = models.FloatField()
    refund_status = models.PositiveIntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at_nepali_date = models.CharField(max_length=10)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    branch = models.PositiveIntegerField()
    payment_type = models.PositiveIntegerField(blank=True, null=True)
    deduction_amount = models.FloatField()
    deduction_by = models.IntegerField()
    deduction_percent = models.FloatField()
    dialysis_pat_id = models.PositiveIntegerField(blank=True, null=True)
    discount_group = models.IntegerField()
    discount_type = models.IntegerField()
    emergency_pat_id = models.PositiveIntegerField(blank=True, null=True)
    in_pat_id = models.PositiveIntegerField(blank=True, null=True)
    patno = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_refunds'


class MasterReturnMedication(models.Model):
    status = models.CharField(max_length=10)
    patient_id = models.IntegerField()
    ipd_id = models.IntegerField()
    returned_at = models.CharField(max_length=191, blank=True, null=True)
    returned_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    er_id = models.IntegerField()
    dialysis_pat_id = models.IntegerField()
    medication_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'master_return_medication'


class MasterReturns(models.Model):
    master_returns_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    mr_opening_stocks_id = models.PositiveIntegerField()
    mr_closing_stocks_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    return_to_store = models.PositiveIntegerField()
    returns_no = models.CharField(max_length=191)
    total_qty = models.PositiveIntegerField()
    issue_return_status = models.PositiveIntegerField()
    expiry_return_status = models.PositiveIntegerField()
    master_returns_remarks = models.TextField(blank=True, null=True)
    master_returns_created_by = models.PositiveIntegerField()
    master_returns_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_returns'


class MasterStockIssues(models.Model):
    master_stock_issues_id = models.AutoField(primary_key=True)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    store = models.ForeignKey('Stores', models.DO_NOTHING)
    msi_opening_stocks_id = models.PositiveIntegerField()
    msi_closing_stocks_id = models.PositiveIntegerField()
    received_from_store = models.PositiveIntegerField()
    stock_issues_remarks = models.TextField(blank=True, null=True)
    stock_issue_no = models.CharField(max_length=191)
    master_stock_issue_cancel_status = models.IntegerField()
    master_stock_issues_created_by = models.PositiveIntegerField()
    master_stock_issues_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_stock_issues'


class MasterStockPurchases(models.Model):
    master_stock_purchases_id = models.AutoField(primary_key=True)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    store = models.ForeignKey('Stores', models.DO_NOTHING)
    supplier = models.ForeignKey('Suppliers', models.DO_NOTHING, blank=True, null=True)
    purchases_order = models.ForeignKey('PurchaseOrders', models.DO_NOTHING, blank=True, null=True)
    msp_opening_stocks_id = models.PositiveIntegerField()
    msp_closing_stocks_id = models.PositiveIntegerField()
    stock_purchases_no = models.CharField(max_length=191, blank=True, null=True)
    supplier_bill_no = models.CharField(max_length=191, blank=True, null=True)
    supplier_bill_date = models.CharField(max_length=191, blank=True, null=True)
    purchases_order_no = models.CharField(max_length=191, blank=True, null=True)
    total_quantity = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    discount_amount = models.FloatField(blank=True, null=True)
    discount_per = models.FloatField(blank=True, null=True)
    tax_per = models.FloatField(blank=True, null=True)
    tax_amount = models.FloatField(blank=True, null=True)
    other_charges = models.FloatField()
    adjustment_amount = models.FloatField()
    total_amount = models.FloatField(blank=True, null=True)
    payment_type = models.IntegerField(blank=True, null=True)
    master_stock_purchases_remarks = models.TextField(blank=True, null=True)
    master_stock_purchases_cancel_remarks = models.TextField(blank=True, null=True)
    stock_purchases_good_in_date = models.DateField(blank=True, null=True)
    stock_purchases_good_in_nepali_date = models.CharField(max_length=191, blank=True, null=True)
    master_stock_purchases_cancel_status = models.IntegerField()
    master_stock_purchases_created_by = models.PositiveIntegerField()
    master_stock_purchases_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)
    exchange_rate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_stock_purchases'


class MasterStockReturns(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_stock_returns'


class MasterTemplates(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_templates'


class MaternityRegisterSummaries(models.Model):
    inpatient_id = models.IntegerField()
    patient_id = models.IntegerField(blank=True, null=True)
    anc_no = models.CharField(max_length=255, blank=True, null=True)
    admission_date = models.DateField()
    admission_time = models.TimeField(blank=True, null=True)
    ethnicity = models.IntegerField(blank=True, null=True)
    gravida = models.CharField(max_length=255, blank=True, null=True)
    lmp = models.DateField(blank=True, null=True)
    edd = models.DateField(blank=True, null=True)
    no_of_anc = models.CharField(max_length=255, blank=True, null=True)
    weeks_of_gestation = models.CharField(max_length=255, blank=True, null=True)
    fhs_on_admission = models.CharField(max_length=255, blank=True, null=True)
    husband_name = models.CharField(max_length=255, blank=True, null=True)
    referral_in = models.CharField(max_length=255)
    admission_diagnosis = models.CharField(max_length=255, blank=True, null=True)
    place_of_delivery = models.CharField(max_length=255)
    type_of_delivery = models.CharField(max_length=255)
    blood_transfussion_for = models.CharField(max_length=255, blank=True, null=True)
    eoc = models.CharField(max_length=255, blank=True, null=True)
    other_oc = models.CharField(max_length=255, blank=True, null=True)
    non_ob_morbidity = models.CharField(max_length=255, blank=True, null=True)
    obstetric_procedure = models.CharField(max_length=255, blank=True, null=True)
    no_of_babies = models.CharField(max_length=255)
    outcome_of_woman = models.CharField(max_length=255, blank=True, null=True)
    date_of_discharge = models.DateField()
    referral_out = models.CharField(max_length=255, blank=True, null=True)
    vitamin_a = models.IntegerField(db_column='vitamin_A')  # Field name made lowercase.
    hiv_status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maternity_register_summaries'


class Media(models.Model):
    model_id = models.PositiveIntegerField()
    model_type = models.CharField(max_length=255)
    collection_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    disk = models.CharField(max_length=255)
    size = models.PositiveIntegerField()
    manipulations = models.TextField()
    custom_properties = models.TextField()
    order_column = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'media'


class MedicalDetails(models.Model):
    visit_id = models.IntegerField()
    patient_id = models.IntegerField()
    infectious_disease_status = models.IntegerField()
    pneumonia_status = models.IntegerField()
    pneumonia_duration = models.IntegerField(blank=True, null=True)
    pneumonia_duration_unit = models.CharField(max_length=191, blank=True, null=True)
    tb_status = models.IntegerField(db_column='TB_status')  # Field name made lowercase.
    tb_duration = models.IntegerField(db_column='TB_duration', blank=True, null=True)  # Field name made lowercase.
    tb_duration_unit = models.CharField(db_column='TB_duration_unit', max_length=191, blank=True, null=True)  # Field name made lowercase.
    jaundice_status = models.IntegerField()
    jaundice_duration = models.IntegerField(blank=True, null=True)
    jaundice_duration_unit = models.CharField(max_length=191, blank=True, null=True)
    asthma_status = models.IntegerField()
    asthma_duration = models.IntegerField(blank=True, null=True)
    asthma_duration_unit = models.CharField(max_length=191, blank=True, null=True)
    malaria_status = models.IntegerField()
    malaria_duration = models.IntegerField(blank=True, null=True)
    malaria_duration_unit = models.CharField(max_length=191, blank=True, null=True)
    kalazar_status = models.IntegerField()
    kalazar_duration = models.IntegerField(blank=True, null=True)
    kalazar_duration_unit = models.CharField(max_length=191, blank=True, null=True)
    other_infectious_status = models.IntegerField()
    other_infectious_remarks = models.CharField(max_length=191, blank=True, null=True)
    medical_condition_status = models.IntegerField()
    p_diabetes_status = models.IntegerField()
    p_diabetes_duration = models.IntegerField(blank=True, null=True)
    p_diabetes_duration_unit = models.CharField(max_length=191, blank=True, null=True)
    p_htn_status = models.IntegerField()
    p_htn_duration = models.IntegerField(blank=True, null=True)
    p_htn_duration_unit = models.CharField(max_length=191, blank=True, null=True)
    p_thyroid_status = models.IntegerField()
    p_thyroid_duration = models.IntegerField(blank=True, null=True)
    p_thyroid_duration_unit = models.CharField(max_length=191, blank=True, null=True)
    p_heartattack_status = models.IntegerField()
    p_heartattack_duration = models.IntegerField(blank=True, null=True)
    p_heartattack_duration_unit = models.CharField(max_length=191, blank=True, null=True)
    p_stroke_status = models.IntegerField()
    p_stroke_duration = models.IntegerField(blank=True, null=True)
    p_stroke_duration_unit = models.CharField(max_length=191, blank=True, null=True)
    p_other_medical_status = models.IntegerField()
    p_other_medical_remarks = models.CharField(max_length=191, blank=True, null=True)
    accident_status = models.IntegerField()
    accident_remarks = models.CharField(max_length=191, blank=True, null=True)
    alcohol_status = models.IntegerField()
    alcohol_remarks = models.CharField(max_length=191, blank=True, null=True)
    smoking_status = models.IntegerField()
    smoking_remarks = models.CharField(max_length=191, blank=True, null=True)
    max_bp_recorded = models.CharField(max_length=191, blank=True, null=True)
    food_habit = models.IntegerField(blank=True, null=True)
    traveltoepidemicarea_status = models.IntegerField()
    traveltoepidemicarea_remarks = models.CharField(max_length=191, blank=True, null=True)
    otherchronicaldisease_status = models.IntegerField()
    otherchronicaldisease_remarks = models.CharField(max_length=191, blank=True, null=True)
    mental_status = models.IntegerField()
    mental_remarks = models.CharField(max_length=191, blank=True, null=True)
    trauma_status = models.IntegerField()
    trauma_remarks = models.CharField(max_length=191, blank=True, null=True)
    surgery_status = models.IntegerField()
    surgery_remarks = models.CharField(max_length=191, blank=True, null=True)
    bloodtransfusion_status = models.IntegerField()
    bloodtransfusion_remarks = models.CharField(max_length=191, blank=True, null=True)
    radiation_status = models.IntegerField()
    radiation_remarks = models.CharField(max_length=191, blank=True, null=True)
    allergy_status = models.IntegerField()
    allergy_remarks = models.CharField(max_length=191, blank=True, null=True)
    dyslipidemia_status = models.IntegerField()
    dyslipidemia_remarks = models.CharField(max_length=191, blank=True, null=True)
    others_status = models.IntegerField()
    others_remarks = models.CharField(max_length=191, blank=True, null=True)
    hyper_family_status = models.IntegerField()
    hyper_family_remarks = models.CharField(max_length=191, blank=True, null=True)
    hyper_family_check = models.TextField(blank=True, null=True)
    diabetes_family_status = models.IntegerField()
    diabetes_family_remarks = models.CharField(max_length=191, blank=True, null=True)
    diabetes_family_check = models.TextField(blank=True, null=True)
    thyroid_family_status = models.IntegerField()
    thyroid_family_remarks = models.CharField(max_length=191, blank=True, null=True)
    thyroid_family_check = models.TextField(blank=True, null=True)
    obesity_family_status = models.IntegerField()
    obesity_family_remarks = models.CharField(max_length=191, blank=True, null=True)
    obesity_family_check = models.TextField(blank=True, null=True)
    cancer_family_status = models.IntegerField()
    cancer_family_remarks = models.CharField(max_length=191, blank=True, null=True)
    cancer_family_check = models.TextField(blank=True, null=True)
    su_death_family_status = models.IntegerField()
    su_death_family_remarks = models.CharField(max_length=191, blank=True, null=True)
    su_death_family_check = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    ipd_id = models.IntegerField()
    last_menstraul_period = models.CharField(max_length=100, blank=True, null=True)
    er_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medical_details'


class MedicalOfficerRecords(models.Model):
    pat = models.ForeignKey('Patients', models.DO_NOTHING, blank=True, null=True)
    in_pat = models.ForeignKey(InPatients, models.DO_NOTHING, blank=True, null=True)
    emergency_pat = models.ForeignKey(EmergencyRegistration, models.DO_NOTHING, blank=True, null=True)
    dialysis_pat = models.ForeignKey(DialysisPatients, models.DO_NOTHING, blank=True, null=True)
    doctor = models.ForeignKey(Doctors, models.DO_NOTHING, blank=True, null=True)
    doctor_name = models.CharField(max_length=255)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='updated_by', related_name='medicalofficerrecords_updated_by_set', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(db_comment=' 0:Active\n                  1: Cancel\n                  ')

    class Meta:
        managed = False
        db_table = 'medical_officer_records'


class MedicalRegistration(models.Model):
    patient_id = models.PositiveIntegerField(blank=True, null=True)
    master_bill_id = models.PositiveIntegerField(blank=True, null=True)
    bill_no = models.CharField(max_length=255)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    refund_status = models.IntegerField()
    moja_no = models.CharField(max_length=255)
    deleted_at = models.DateTimeField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    bmi = models.FloatField(blank=True, null=True)
    passport_issue_date = models.DateTimeField(blank=True, null=True)
    passport_expiry_date = models.DateTimeField(blank=True, null=True)
    passport_issue_place = models.CharField(max_length=255, blank=True, null=True)
    visa_issue_date = models.DateTimeField(blank=True, null=True)
    religion = models.CharField(max_length=255, blank=True, null=True)
    applied_position_id = models.PositiveIntegerField(blank=True, null=True)
    other = models.CharField(max_length=255, blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    country_travelling = models.CharField(max_length=255, blank=True, null=True)
    visa_number = models.CharField(max_length=255, blank=True, null=True)
    passport_number = models.CharField(max_length=255, blank=True, null=True)
    slip_no = models.CharField(max_length=255, blank=True, null=True)
    report_expiry_date = models.DateTimeField(blank=True, null=True)
    manpower = models.CharField(max_length=255, blank=True, null=True)
    date_examined = models.DateTimeField(blank=True, null=True)
    mofa_number = models.CharField(max_length=255, blank=True, null=True)
    is_gcc_update = models.IntegerField()
    is_verify = models.IntegerField()
    is_verified_by = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medical_registration'


class MedicationFrequency(models.Model):
    frequency = models.CharField(max_length=191)
    frequency_unit = models.IntegerField()
    frequency_duration_unit = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medication_frequency'


class MedicationOrderLists(models.Model):
    visit_id = models.IntegerField()
    patient_id = models.IntegerField()
    ipd_id = models.IntegerField()
    er_id = models.IntegerField()
    dialysis_pat_id = models.IntegerField()
    medication_id = models.IntegerField(blank=True, null=True)
    master_medication_id = models.IntegerField(blank=True, null=True)
    order_qty = models.IntegerField(blank=True, null=True)
    requisition_no = models.CharField(max_length=191, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medication_order_lists'


class Medicines(models.Model):
    medicine_name = models.CharField(max_length=191)
    catalogue_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_antibotic = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medicines'


class MembershipDiscountToTestPivot(models.Model):
    member_type = models.ForeignKey('Membertypes', models.DO_NOTHING)
    test = models.ForeignKey('Tests', models.DO_NOTHING)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    discount = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'membership_discount_to_test_pivot'


class Membertypes(models.Model):
    type = models.CharField(max_length=255)
    discount = models.IntegerField()
    status = models.IntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'membertypes'


class MiTestSettings(models.Model):
    test_name = models.CharField(max_length=255)
    test_id = models.IntegerField()
    parameter_id = models.IntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mi_test_settings'


class MicrobiologyOrganisms(models.Model):
    organisms = models.CharField(max_length=255)
    font_style = models.IntegerField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'microbiology_organisms'


class MigDepartments(models.Model):
    id = models.PositiveIntegerField()
    department = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    section_id = models.IntegerField(blank=True, null=True)
    order_column = models.PositiveIntegerField()
    active = models.IntegerField()
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

    class Meta:
        managed = False
        db_table = 'mig_departments'


class MigMember(models.Model):
    patient_id = models.IntegerField(primary_key=True)
    start_date = models.DateTimeField(blank=True, null=True)
    bill_date = models.DateTimeField(blank=True, null=True)
    test_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mig_member'


class MigPricePatientCats(models.Model):
    id = models.PositiveIntegerField()
    item_id = models.PositiveIntegerField(blank=True, null=True)
    patient_cat_id = models.PositiveIntegerField(blank=True, null=True)
    net_amount = models.FloatField()
    total_tax = models.FloatField()
    total_amount = models.FloatField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    branch = models.PositiveIntegerField()
    hospital_share = models.FloatField()
    hospital = models.FloatField()
    hospital_percentage = models.FloatField()
    department = models.FloatField()
    department_percentage = models.FloatField()
    anesthesist = models.FloatField()
    anesthesist_percentage = models.FloatField()
    fund = models.FloatField()
    fund_percentage = models.FloatField()
    depreciation = models.FloatField()
    depreciation_percentage = models.FloatField()
    instrument = models.FloatField()
    instrument_percentage = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mig_price_patient_cats'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class MisDashboardDataLog(models.Model):
    collection = models.FloatField()
    billing = models.FloatField()
    services = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mis_dashboard_data_log'


class MobileAppUsers(models.Model):
    device_id = models.CharField(max_length=255)
    device_type = models.CharField(max_length=255)
    device_name = models.CharField(max_length=255)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    module = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=255)
    status = models.CharField(max_length=1)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    fcm_token = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mobile_app_users'


class Municipalities(models.Model):
    id = models.BigAutoField(primary_key=True)
    municipality = models.CharField(max_length=255)
    district_id = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    imu_municipality_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'municipalities'


class NepalPayLogs(models.Model):
    request_from = models.CharField(max_length=255)
    patient_id = models.PositiveIntegerField()
    in_pat_id = models.PositiveIntegerField(blank=True, null=True)
    emergency_pat_id = models.PositiveIntegerField(blank=True, null=True)
    dialysis_pat_id = models.PositiveIntegerField(blank=True, null=True)
    validation_trace_id = models.CharField(max_length=255, blank=True, null=True)
    bill_no = models.CharField(max_length=255)
    amt = models.FloatField()
    qr_response_code = models.CharField(max_length=255, blank=True, null=True)
    pay_response_code = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    verified_by = models.IntegerField(blank=True, null=True)
    verified_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    request = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nepal_pay_logs'


class NepaliMonths(models.Model):
    fiscal_year_id = models.PositiveBigIntegerField()
    fiscal_year = models.CharField(max_length=255)
    month_name = models.CharField(max_length=255)
    year_name = models.CharField(max_length=255)
    from_date = models.CharField(max_length=255)
    to_date = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nepali_months'


class NervousSystems(models.Model):
    visit_id = models.IntegerField()
    medicaldetails_id = models.IntegerField()
    patient_id = models.IntegerField()
    gait = models.TextField(blank=True, null=True)
    muscles_atropy = models.TextField(blank=True, null=True)
    state_of_conciousness = models.TextField(blank=True, null=True)
    twiching_abnormal_movement = models.TextField(blank=True, null=True)
    purpilary_light_reflex = models.TextField(blank=True, null=True)
    strength_facial_muscultur = models.TextField(blank=True, null=True)
    hearing = models.TextField(blank=True, null=True)
    proximal_myopathy = models.IntegerField()
    proximal_myopathy_remarks = models.TextField(blank=True, null=True)
    babinski_response = models.IntegerField()
    chvosteks_sign = models.IntegerField()
    gag_reflex = models.TextField(blank=True, null=True)
    carpal_tunnel_syndrome = models.IntegerField()
    tongue_lip_movement = models.TextField(blank=True, null=True)
    ability_to_smell_taste = models.TextField(blank=True, null=True)
    sensory_exam = models.IntegerField()
    sensory_exam_remarks = models.TextField(blank=True, null=True)
    sensation = models.TextField(blank=True, null=True)
    tendon_reflex = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    ipd_id = models.IntegerField()
    er_id = models.IntegerField()
    planter_reflex = models.TextField(blank=True, null=True)
    power_rt_ul = models.IntegerField(blank=True, null=True)
    power_rt_ll = models.IntegerField(blank=True, null=True)
    power_lt_ul = models.IntegerField(blank=True, null=True)
    power_lt_ll = models.IntegerField(blank=True, null=True)
    carnial_nerve_exam = models.TextField(blank=True, null=True)
    motor_function = models.TextField(blank=True, null=True)
    gcs = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nervous_systems'


class NoteType(models.Model):
    note_type = models.CharField(max_length=191)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'note_type'


class Notifications(models.Model):
    title = models.CharField(max_length=255, db_collation='utf8mb4_unicode_ci')
    body = models.CharField(max_length=255, db_collation='utf8mb4_unicode_ci')
    notification_action = models.CharField(max_length=255, db_collation='utf8mb4_unicode_ci')
    expiry = models.CharField(max_length=255, db_collation='utf8mb4_unicode_ci')
    status = models.CharField(max_length=255, db_collation='utf8mb4_unicode_ci')
    user_id = models.BigIntegerField()
    notification_type = models.CharField(max_length=255, db_collation='utf8mb4_unicode_ci')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    patient_id = models.IntegerField(blank=True, null=True)
    in_pat_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notifications'


class NurseShiftNotes(models.Model):
    in_pat_id = models.IntegerField()
    pat_id = models.IntegerField()
    note = models.TextField()
    type = models.IntegerField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    er_id = models.IntegerField()
    note_type_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nurse_shift_notes'


class Nurses(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nurses'


class OauthAccessTokens(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    client_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=191, blank=True, null=True)
    scopes = models.TextField(blank=True, null=True)
    revoked = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_access_tokens'


class OauthAuthCodes(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    user_id = models.PositiveBigIntegerField()
    client_id = models.PositiveBigIntegerField()
    scopes = models.TextField(blank=True, null=True)
    revoked = models.IntegerField()
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_auth_codes'


class OauthClients(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=191)
    secret = models.CharField(max_length=100, blank=True, null=True)
    provider = models.CharField(max_length=191, blank=True, null=True)
    redirect = models.TextField()
    personal_access_client = models.IntegerField()
    password_client = models.IntegerField()
    revoked = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_clients'


class OauthPersonalAccessClients(models.Model):
    id = models.BigAutoField(primary_key=True)
    client_id = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_personal_access_clients'


class OauthRefreshTokens(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    access_token_id = models.CharField(max_length=100)
    revoked = models.IntegerField()
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_refresh_tokens'


class ObsGynos(models.Model):
    visit_id = models.IntegerField()
    medicaldetails_id = models.IntegerField()
    patient_id = models.IntegerField()
    birth = models.DateField(blank=True, null=True)
    delivery = models.DateField(blank=True, null=True)
    menopause = models.TextField(blank=True, null=True)
    c_section = models.TextField(blank=True, null=True)
    menarache_age = models.TextField(blank=True, null=True)
    mensuration_cycle = models.TextField(blank=True, null=True)
    children = models.IntegerField()
    children_remarks = models.TextField(blank=True, null=True)
    pregnency = models.TextField(blank=True, null=True)
    son = models.TextField(blank=True, null=True)
    daughter = models.TextField(blank=True, null=True)
    last_mensuration = models.TextField(blank=True, null=True)
    regular = models.IntegerField()
    mensuration_duration = models.TextField(blank=True, null=True)
    abortion = models.IntegerField()
    abortion_remarks = models.TextField(blank=True, null=True)
    vaginal_discharge = models.IntegerField()
    vaginal_discharge_remarks = models.TextField(blank=True, null=True)
    skin_lension = models.TextField(blank=True, null=True)
    provisional_diagonosis = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    ipd_id = models.IntegerField()
    er_id = models.IntegerField()
    pv_bleeding = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'obs_gynos'


class Observations(models.Model):
    medicaldetails_id = models.IntegerField()
    visit_id = models.IntegerField()
    patient_id = models.IntegerField()
    complaint_notes = models.TextField(blank=True, null=True)
    history_notes = models.TextField(blank=True, null=True)
    examine_notes = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    ipd_id = models.IntegerField()
    past_history = models.TextField(blank=True, null=True)
    er_id = models.IntegerField()
    allergies = models.TextField(blank=True, null=True)
    severity = models.CharField(max_length=191, blank=True, null=True)
    gc = models.CharField(max_length=191, blank=True, null=True)
    pilccod = models.CharField(max_length=191, blank=True, null=True)
    family_history = models.TextField(blank=True, null=True)
    gynae_history = models.TextField(blank=True, null=True)
    past_inv_report = models.TextField(blank=True, null=True)
    personal_social_history = models.TextField(blank=True, null=True)
    present_inv_report = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'observations'


class OnlineItems(models.Model):
    item_id = models.IntegerField()
    test_id = models.IntegerField()
    item_name = models.CharField(max_length=255)
    test_name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    department_id = models.IntegerField()
    active = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'online_items'


class OnlinePurchase(models.Model):
    patient_id = models.IntegerField()
    master_bill_id = models.IntegerField()
    status = models.IntegerField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'online_purchase'


class OpeningStocks(models.Model):
    opening_stocks_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    opening_stocks_tot_stock_qty = models.PositiveIntegerField()
    opening_stocks_remarks = models.TextField(blank=True, null=True)
    opening_stocks_created_by = models.PositiveIntegerField()
    opening_stocks_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    store = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'opening_stocks'


class OperationLogs(models.Model):
    instance = models.CharField(max_length=255)
    bill_no = models.CharField(max_length=255)
    patient_id = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField()
    remarks = models.TextField()
    branch = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operation_logs'


class OpticExamination(models.Model):
    patient_id = models.IntegerField()
    visit_id = models.IntegerField()
    eom = models.CharField(max_length=191, blank=True, null=True)
    cover_test = models.TextField(blank=True, null=True)
    lids_le = models.TextField(blank=True, null=True)
    lids_re = models.TextField(blank=True, null=True)
    conjunctiva_le = models.TextField(blank=True, null=True)
    conjunctiva_re = models.TextField(blank=True, null=True)
    cormea_le = models.TextField(blank=True, null=True)
    cormea_re = models.TextField(blank=True, null=True)
    ac_le = models.TextField(blank=True, null=True)
    ac_re = models.TextField(blank=True, null=True)
    pupils_le = models.TextField(blank=True, null=True)
    pupils_re = models.TextField(blank=True, null=True)
    lens_le = models.TextField(blank=True, null=True)
    lens_re = models.TextField(blank=True, null=True)
    vitreous_le = models.TextField(blank=True, null=True)
    vitreous_re = models.TextField(blank=True, null=True)
    retina_le = models.TextField(blank=True, null=True)
    retina_re = models.TextField(blank=True, null=True)
    optic_disc_le = models.TextField(blank=True, null=True)
    optic_disc_re = models.TextField(blank=True, null=True)
    cdr_le = models.TextField(blank=True, null=True)
    cdr_re = models.TextField(blank=True, null=True)
    image_1_le = models.TextField(blank=True, null=True)
    image_2_le = models.TextField(blank=True, null=True)
    image_1_re = models.TextField(blank=True, null=True)
    image_2_re = models.TextField(blank=True, null=True)
    examination_checkbox = models.TextField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'optic_examination'


class OpticEyeRefraction(models.Model):
    patient_id = models.IntegerField()
    visit_id = models.IntegerField()
    dry_re_sph = models.CharField(max_length=191, blank=True, null=True)
    dry_re_cyl = models.CharField(max_length=191, blank=True, null=True)
    dry_re_axis = models.CharField(max_length=191, blank=True, null=True)
    wg_re_sph = models.CharField(max_length=191, blank=True, null=True)
    wg_re_cyl = models.CharField(max_length=191, blank=True, null=True)
    wg_re_axis = models.CharField(max_length=191, blank=True, null=True)
    dry_le_sph = models.CharField(max_length=191, blank=True, null=True)
    dry_le_cyl = models.CharField(max_length=191, blank=True, null=True)
    dry_le_axis = models.CharField(max_length=191, blank=True, null=True)
    wg_le_sph = models.CharField(max_length=191, blank=True, null=True)
    wg_le_cyl = models.CharField(max_length=191, blank=True, null=True)
    wg_le_axis = models.CharField(max_length=191, blank=True, null=True)
    wet_re_sph = models.CharField(max_length=191, blank=True, null=True)
    wet_re_cyl = models.CharField(max_length=191, blank=True, null=True)
    wet_re_axis = models.CharField(max_length=191, blank=True, null=True)
    wet_le_sph = models.CharField(max_length=191, blank=True, null=True)
    wet_le_cyl = models.CharField(max_length=191, blank=True, null=True)
    wet_le_axis = models.CharField(max_length=191, blank=True, null=True)
    add_re_sph = models.CharField(max_length=191, blank=True, null=True)
    add_re_vision = models.CharField(max_length=191, blank=True, null=True)
    add_re_distance = models.CharField(max_length=191, blank=True, null=True)
    add_le_sph = models.CharField(max_length=191, blank=True, null=True)
    add_le_vision = models.CharField(max_length=191, blank=True, null=True)
    add_le_distance = models.CharField(max_length=191, blank=True, null=True)
    acceptance_re_sph = models.CharField(max_length=191, blank=True, null=True)
    acceptance_re_cyl = models.CharField(max_length=191, blank=True, null=True)
    acceptance_re_axis = models.CharField(max_length=191, blank=True, null=True)
    acceptance_re_vision = models.CharField(max_length=191, blank=True, null=True)
    acceptance_le_sph = models.CharField(max_length=191, blank=True, null=True)
    acceptance_le_cyl = models.CharField(max_length=191, blank=True, null=True)
    acceptance_le_axis = models.CharField(max_length=191, blank=True, null=True)
    acceptance_le_vision = models.CharField(max_length=191, blank=True, null=True)
    ipd_dipd = models.CharField(max_length=191, blank=True, null=True)
    ipd_nipd = models.CharField(max_length=191, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    wg_re_value = models.CharField(max_length=191, blank=True, null=True)
    wog_re_value = models.CharField(max_length=191, blank=True, null=True)
    wg_le_value = models.CharField(max_length=191, blank=True, null=True)
    wog_le_value = models.CharField(max_length=191, blank=True, null=True)
    wog_flag = models.IntegerField(blank=True, null=True)
    addition_flag = models.CharField(max_length=191, blank=True, null=True)
    wg_flag = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'optic_eye_refraction'


class OpticHistory(models.Model):
    patient_id = models.IntegerField()
    visit_id = models.IntegerField()
    visit_date = models.DateField()
    visit_type = models.CharField(max_length=191, blank=True, null=True)
    past_history = models.TextField(blank=True, null=True)
    prior_surgery = models.TextField(blank=True, null=True)
    current_medications = models.TextField(blank=True, null=True)
    systemic_disease = models.TextField(blank=True, null=True)
    allergy = models.TextField(blank=True, null=True)
    additional_information = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'optic_history'


class OpticIopGonio(models.Model):
    patient_id = models.IntegerField()
    visit_id = models.IntegerField()
    time = models.CharField(max_length=191, blank=True, null=True)
    method = models.CharField(max_length=191, blank=True, null=True)
    right_iop = models.FloatField(blank=True, null=True)
    top_od = models.CharField(max_length=191, blank=True, null=True)
    left_od = models.CharField(max_length=191, blank=True, null=True)
    bottom_od = models.CharField(max_length=191, blank=True, null=True)
    right_od = models.CharField(max_length=191, blank=True, null=True)
    left_iop = models.FloatField(blank=True, null=True)
    top_os = models.CharField(max_length=191, blank=True, null=True)
    left_os = models.CharField(max_length=191, blank=True, null=True)
    bottom_os = models.CharField(max_length=191, blank=True, null=True)
    right_os = models.CharField(max_length=191, blank=True, null=True)
    glaucoma_comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'optic_iop_gonio'


class OpticRefraction(models.Model):
    patient_id = models.IntegerField()
    visit_id = models.IntegerField()
    dry_re_sph = models.CharField(max_length=191, blank=True, null=True)
    dry_re_sph_value = models.FloatField(blank=True, null=True)
    dry_re_cyl = models.CharField(max_length=191, blank=True, null=True)
    dry_re_cyl_value = models.FloatField(blank=True, null=True)
    dry_re_axis = models.FloatField(blank=True, null=True)
    dry_re_vision = models.CharField(max_length=191, blank=True, null=True)
    dry_le_sph = models.CharField(max_length=191, blank=True, null=True)
    dry_le_sph_value = models.FloatField(blank=True, null=True)
    dry_le_cyl = models.CharField(max_length=191, blank=True, null=True)
    dry_le_cyl_value = models.FloatField(blank=True, null=True)
    dry_le_axis = models.FloatField(blank=True, null=True)
    dry_le_vision = models.CharField(max_length=191, blank=True, null=True)
    dry_add_re = models.CharField(max_length=191, blank=True, null=True)
    dry_add_re_value = models.FloatField(blank=True, null=True)
    dry_add_re_vision = models.CharField(max_length=191, blank=True, null=True)
    dry_add_le = models.CharField(max_length=191, blank=True, null=True)
    dry_add_le_value = models.FloatField(blank=True, null=True)
    dry_add_le_vision = models.CharField(max_length=191, blank=True, null=True)
    dry_ipd_dipd = models.CharField(max_length=191, blank=True, null=True)
    dry_ipd_nipd = models.CharField(max_length=191, blank=True, null=True)
    dry_note = models.TextField(blank=True, null=True)
    wet_re_sph = models.CharField(max_length=191, blank=True, null=True)
    wet_re_sph_value = models.FloatField(blank=True, null=True)
    wet_re_cyl = models.CharField(max_length=191, blank=True, null=True)
    wet_re_cyl_value = models.FloatField(blank=True, null=True)
    wet_re_axis = models.FloatField(blank=True, null=True)
    wet_re_vision = models.CharField(max_length=191, blank=True, null=True)
    wet_le_sph = models.CharField(max_length=191, blank=True, null=True)
    wet_le_sph_value = models.FloatField(blank=True, null=True)
    wet_le_cyl = models.CharField(max_length=191, blank=True, null=True)
    wet_le_cyl_value = models.FloatField(blank=True, null=True)
    wet_le_axis = models.FloatField(blank=True, null=True)
    wet_le_vision = models.CharField(max_length=191, blank=True, null=True)
    wet_add_re = models.CharField(max_length=191, blank=True, null=True)
    wet_add_re_value = models.FloatField(blank=True, null=True)
    wet_add_re_vision = models.CharField(max_length=191, blank=True, null=True)
    wet_add_le = models.CharField(max_length=191, blank=True, null=True)
    wet_add_le_value = models.FloatField(blank=True, null=True)
    wet_add_le_vision = models.CharField(max_length=191, blank=True, null=True)
    wet_ipd_dipd = models.CharField(max_length=191, blank=True, null=True)
    wet_ipd_nipd = models.CharField(max_length=191, blank=True, null=True)
    wet_note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'optic_refraction'


class OrganismPanel(models.Model):
    antibiotic_id = models.IntegerField()
    panel_id = models.IntegerField()
    data_entry_type = models.IntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organism_panel'


class Organisms(models.Model):
    org_name = models.CharField(max_length=255)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_default = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'organisms'


class OtNotes(models.Model):
    patient_id = models.IntegerField()
    in_pat_id = models.IntegerField()
    department_id = models.IntegerField()
    department_name = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    date_eng = models.CharField(max_length=255)
    note = models.TextField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ot_notes'


class OtRegisterAnesthetistAssistants(models.Model):
    assistant_id = models.IntegerField()
    ot_register_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ot_register_anesthetist_assistants'


class OtRegisterAnesthetists(models.Model):
    anesthetist_id = models.IntegerField()
    ot_register_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ot_register_anesthetists'


class OtRegisterAssistants(models.Model):
    assistant_id = models.IntegerField()
    ot_register_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ot_register_assistants'


class OtRegisterSurgeons(models.Model):
    surgeon_id = models.IntegerField()
    ot_register_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ot_register_surgeons'


class OtpLog(models.Model):
    mobile_number = models.CharField(max_length=255)
    otp_code = models.IntegerField()
    otp_status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    device_id = models.CharField(max_length=100, blank=True, null=True)
    otp_type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'otp_log'


class OutsourceVendors(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'outsource_vendors'


class PLedgers(models.Model):
    patient_id = models.PositiveIntegerField(blank=True, null=True)
    inpatient_id = models.PositiveIntegerField(blank=True, null=True)
    discount_group_id = models.PositiveIntegerField(blank=True, null=True)
    discount_group_percent_id = models.PositiveIntegerField(blank=True, null=True)
    branch_id = models.PositiveIntegerField()
    p_master_bill_id = models.IntegerField()
    p_master_refund_id = models.IntegerField()
    bill_no = models.CharField(max_length=191, blank=True, null=True)
    reference_bill_no = models.CharField(max_length=191, blank=True, null=True)
    receipt_no = models.CharField(max_length=191, blank=True, null=True)
    dr_amt = models.FloatField()
    cr_amt = models.FloatField()
    bill_type = models.CharField(max_length=1)
    insurance_flag = models.IntegerField()
    payment_type = models.IntegerField()
    bank_id = models.IntegerField(blank=True, null=True)
    card_no = models.CharField(max_length=191, blank=True, null=True)
    cheque_no = models.CharField(max_length=191, blank=True, null=True)
    is_discount = models.IntegerField()
    remarks = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    revenue_center = models.IntegerField()
    parent_id = models.IntegerField()
    child_id = models.IntegerField()
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_ledgers'


class PPatientLedgers(models.Model):
    patient_id = models.PositiveIntegerField()
    inpatient_id = models.IntegerField(blank=True, null=True)
    discount_group_id = models.PositiveIntegerField(blank=True, null=True)
    discount_group_percent_id = models.PositiveIntegerField(blank=True, null=True)
    branch_id = models.PositiveIntegerField()
    p_master_bill_id = models.IntegerField()
    p_master_refund_id = models.IntegerField()
    reference_bill_no = models.CharField(max_length=191, blank=True, null=True)
    receipt_no = models.CharField(max_length=191, blank=True, null=True)
    dr_amt = models.FloatField()
    cr_amt = models.FloatField()
    bill_type = models.CharField(max_length=1)
    insurance_flag = models.IntegerField()
    payment_type = models.IntegerField()
    bank_id = models.IntegerField(blank=True, null=True)
    card_no = models.CharField(max_length=191, blank=True, null=True)
    cheque_no = models.CharField(max_length=191, blank=True, null=True)
    remarks = models.TextField()
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_patient_ledgers'


class PPharmacyBillDetails(models.Model):
    pharmacy_bill_detail_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    pharmacy_master_bill_id = models.PositiveIntegerField()
    stock_issue_id = models.PositiveIntegerField()
    batch = models.CharField(max_length=191)
    store_id = models.PositiveIntegerField()
    patient_id = models.PositiveIntegerField()
    refund_status = models.CharField(max_length=1)
    cancel_status = models.CharField(max_length=1)
    catalogue_type_id = models.PositiveIntegerField()
    catalogue_id = models.PositiveIntegerField()
    cost_price = models.FloatField()
    rate = models.FloatField()
    total_stock_quantity = models.PositiveIntegerField()
    quantity = models.IntegerField()
    total_remaining_quantity = models.PositiveIntegerField()
    amount = models.FloatField()
    discount_percentage = models.FloatField()
    discount = models.FloatField()
    is_taxable = models.IntegerField()
    taxable_amt = models.FloatField()
    tax_per = models.FloatField()
    tax = models.FloatField()
    total = models.FloatField()
    refunded_by = models.PositiveIntegerField(blank=True, null=True)
    refunded_at = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    refund_quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'p_pharmacy_bill_details'


class PPharmacyMasterBills(models.Model):
    pharmacy_master_bill_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    bill_no = models.CharField(max_length=191)
    patient_id = models.PositiveIntegerField()
    inpatient_id = models.PositiveIntegerField(blank=True, null=True)
    reference_master_bill_id = models.PositiveIntegerField(blank=True, null=True)
    refunded_master_bill_id = models.PositiveIntegerField(blank=True, null=True)
    store_id = models.PositiveIntegerField()
    consultant = models.PositiveIntegerField(blank=True, null=True)
    ref_hospital_id = models.IntegerField(blank=True, null=True)
    claim_code = models.CharField(max_length=191, blank=True, null=True)
    pan = models.CharField(max_length=191, blank=True, null=True)
    patient_name = models.TextField(blank=True, null=True)
    refund_status = models.IntegerField()
    cancel_status = models.IntegerField()
    ird_status = models.IntegerField()
    print_count = models.IntegerField()
    tender_amt = models.FloatField()
    return_amt = models.FloatField()
    amount = models.FloatField()
    discount = models.FloatField()
    taxable_amt = models.FloatField()
    tax = models.FloatField()
    total = models.FloatField()
    discount_group_id = models.PositiveIntegerField(blank=True, null=True)
    discount_group_percent_id = models.PositiveIntegerField(blank=True, null=True)
    discount_type_percent = models.PositiveIntegerField()
    payment_type = models.PositiveIntegerField(blank=True, null=True)
    bank_id = models.PositiveIntegerField()
    card_no = models.CharField(max_length=191, blank=True, null=True)
    cheque_no = models.CharField(max_length=191, blank=True, null=True)
    reference_number = models.CharField(max_length=191, blank=True, null=True)
    remarks = models.CharField(max_length=191, blank=True, null=True)
    created_at_nepali_date = models.CharField(max_length=10)
    refunded_by = models.PositiveIntegerField(blank=True, null=True)
    refunded_at = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    pos_setup_id = models.PositiveIntegerField()
    visit_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_pharmacy_master_bills'
        unique_together = (('bill_no', 'branch_id'),)


class PPharmacyMasterRefunds(models.Model):
    pharmacy_master_refund_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    pharmacy_master_bill_id = models.PositiveIntegerField()
    pharmacy_refund_store_id = models.PositiveIntegerField()
    pharmacy_refund_bill_no = models.CharField(max_length=191)
    pharmacy_refund_remarks = models.TextField(blank=True, null=True)
    print_count = models.IntegerField()
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    inpatient_id = models.PositiveIntegerField(blank=True, null=True)
    patient_id = models.PositiveIntegerField(blank=True, null=True)
    payment_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'p_pharmacy_master_refunds'


class PPharmacyRefundDetails(models.Model):
    phar_refund_detail_id = models.AutoField(primary_key=True)
    pharmacy_master_refund_id = models.PositiveIntegerField()
    pharmacy_bill_detail_id = models.PositiveIntegerField()
    catalogue_type_id = models.PositiveIntegerField()
    catalogue_generic_id = models.PositiveIntegerField()
    catalogue_id = models.IntegerField()
    cost_price = models.FloatField()
    rate = models.FloatField()
    quantity = models.IntegerField()
    amount = models.FloatField()
    discount_percentage = models.FloatField()
    discount = models.FloatField()
    is_taxable = models.IntegerField()
    taxable_amt = models.FloatField()
    expiry_date = models.CharField(max_length=191)
    tax_per = models.FloatField()
    tax = models.FloatField()
    total = models.FloatField()
    store_id = models.PositiveIntegerField()
    profit_percent = models.FloatField()
    batch = models.CharField(max_length=191, blank=True, null=True)
    cancel_status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_pharmacy_refund_details'


class PackageBillDetails(models.Model):
    package_bill_detail_id = models.AutoField(primary_key=True)
    s_master_bill_id = models.PositiveIntegerField(blank=True, null=True)
    s_bill_detail_id = models.PositiveIntegerField(blank=True, null=True)
    bill_detail_id = models.PositiveIntegerField(blank=True, null=True)
    master_bill_id = models.PositiveIntegerField(blank=True, null=True)
    package_item_id = models.PositiveIntegerField()
    item_id = models.PositiveIntegerField()
    is_sharable = models.PositiveIntegerField()
    refund_status = models.PositiveIntegerField()
    total_amt = models.FloatField()
    item_name = models.CharField(max_length=255)
    item_package = models.CharField(max_length=255)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    cancel_status = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    additional_consultant = models.PositiveIntegerField()
    available_free_qty = models.IntegerField()
    consultant_incharge = models.PositiveIntegerField()
    deduction_status = models.IntegerField()
    free_qty = models.IntegerField()
    performing_consultant = models.PositiveIntegerField()
    refer_by_consultant = models.PositiveIntegerField()
    service_refer_by_consultant = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'package_bill_details'


class PackageTestPivot(models.Model):
    package_id = models.PositiveIntegerField()
    test_id = models.PositiveIntegerField()
    item_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_package_panel = models.IntegerField()
    opd_weightage = models.FloatField(blank=True, null=True)
    ipd_weightage = models.FloatField(blank=True, null=True)
    opd_price = models.FloatField(blank=True, null=True)
    ipd_price = models.FloatField(blank=True, null=True)
    status = models.IntegerField()
    is_substitute = models.PositiveIntegerField()
    parent_item_id = models.PositiveIntegerField()
    free_qty = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'package_test_pivot'


class PackageWiseBudgets(models.Model):
    package = models.ForeignKey(Items, models.DO_NOTHING)
    source_name = models.CharField(max_length=255)
    patient_qty = models.IntegerField()
    service_qty = models.IntegerField()
    amount = models.FloatField()
    fiscalyear = models.CharField(max_length=255)
    month = models.CharField(max_length=255)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='updated_by', related_name='packagewisebudgets_updated_by_set', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    department_id = models.PositiveIntegerField()
    per_day_amount = models.FloatField()
    per_day_patient_qty = models.FloatField()
    per_day_service_qty = models.FloatField()

    class Meta:
        managed = False
        db_table = 'package_wise_budgets'


class PanelReceiptAdjustments(models.Model):
    panel_receipt = models.ForeignKey('PanelReceipts', models.DO_NOTHING)
    master_bill = models.ForeignKey(MasterBills, models.DO_NOTHING, blank=True, null=True)
    adjustment = models.FloatField()
    tds = models.FloatField()
    discount = models.FloatField()
    net_amount = models.FloatField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'panel_receipt_adjustments'


class PanelReceipts(models.Model):
    panel = models.ForeignKey('PatientCategories', models.DO_NOTHING, blank=True, null=True)
    adjustment = models.FloatField()
    tds = models.FloatField()
    discount = models.FloatField()
    net_amount = models.FloatField()
    period = models.PositiveIntegerField(blank=True, null=True)
    voucher_no = models.CharField(max_length=255, blank=True, null=True)
    reference_number = models.CharField(max_length=255, blank=True, null=True)
    cheque_no = models.CharField(max_length=255, blank=True, null=True)
    cheque_date = models.CharField(max_length=255, blank=True, null=True)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    adjustment_amount = models.FloatField()
    patient_category_id = models.PositiveIntegerField()
    received_amount = models.FloatField()
    status = models.IntegerField()
    tds_amount = models.FloatField()

    class Meta:
        managed = False
        db_table = 'panel_receipts'


class ParameterFormulas(models.Model):
    parameter = models.ForeignKey('Parameters', models.DO_NOTHING)
    gender_id = models.IntegerField()
    formula = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parameter_formulas'


class Parameters(models.Model):
    result_head = models.CharField(max_length=255)
    display_order = models.PositiveIntegerField(blank=True, null=True)
    value_type = models.CharField(max_length=255, blank=True, null=True)
    title = models.IntegerField(blank=True, null=True)
    online_status = models.IntegerField()
    test = models.ForeignKey('Tests', models.DO_NOTHING, blank=True, null=True)
    unit = models.ForeignKey('Units', models.DO_NOTHING, blank=True, null=True)
    unit_name = models.CharField(max_length=255, blank=True, null=True)
    work_list = models.IntegerField()
    active = models.IntegerField()
    full_row = models.IntegerField()
    q_range = models.TextField()
    children_critical_max = models.CharField(max_length=10, blank=True, null=True)
    children_critical_min = models.CharField(max_length=10, blank=True, null=True)
    female_critical_max = models.CharField(max_length=10, blank=True, null=True)
    female_critical_min = models.CharField(max_length=10, blank=True, null=True)
    male_critical_max = models.CharField(max_length=10, blank=True, null=True)
    male_critical_min = models.CharField(max_length=10, blank=True, null=True)
    standard_critical_max = models.CharField(max_length=10, blank=True, null=True)
    standard_critical_min = models.CharField(max_length=10, blank=True, null=True)
    standard_min = models.CharField(max_length=10, blank=True, null=True)
    standard_max = models.CharField(max_length=10, blank=True, null=True)
    male_min = models.CharField(max_length=10, blank=True, null=True)
    male_max = models.CharField(max_length=10, blank=True, null=True)
    female_min = models.CharField(max_length=10, blank=True, null=True)
    female_max = models.CharField(max_length=10, blank=True, null=True)
    children_min = models.CharField(max_length=10, blank=True, null=True)
    children_max = models.CharField(max_length=10, blank=True, null=True)
    clinical_status = models.IntegerField()
    short_code = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    susceptibility = models.IntegerField()
    branch = models.PositiveIntegerField()
    formula_status = models.IntegerField()
    formula = models.CharField(max_length=255)
    decimals = models.CharField(max_length=255)
    formula_max_limit = models.CharField(max_length=255)
    is_multiple = models.IntegerField()
    code = models.CharField(max_length=100, blank=True, null=True)
    default_value = models.CharField(max_length=255, blank=True, null=True)
    test_method_id = models.IntegerField(blank=True, null=True)
    having_multi_formula = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'parameters'


class PartnerDetails(models.Model):
    partner_id = models.IntegerField()
    discount_percent_id = models.IntegerField()
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partner_details'


class Partners(models.Model):
    partner_name = models.CharField(max_length=255)
    active = models.IntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    partner_code = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_credit_client = models.IntegerField()
    account_id = models.IntegerField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    letter_head = models.IntegerField()
    email = models.CharField(max_length=255, blank=True, null=True)
    parent_partner_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'partners'


class PasswordResets(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'password_resets'


class PatientActivities(models.Model):
    date = models.DateTimeField()
    patient_id = models.PositiveIntegerField()
    in_pat_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    consultant = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    er_id = models.PositiveIntegerField()
    rate_type = models.CharField(max_length=255, blank=True, null=True)
    add_consultant = models.CharField(max_length=255, blank=True, null=True)
    dialysis_pat_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'patient_activities'


class PatientAdmissionType(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_admission_type'


class PatientCategories(models.Model):
    category = models.CharField(max_length=255)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    multiplier = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    active = models.IntegerField()
    currency = models.ForeignKey(Currencies, models.DO_NOTHING, blank=True, null=True)
    rate_type = models.CharField(max_length=255)
    is_inherit = models.CharField(max_length=255)
    formula = models.CharField(max_length=255, blank=True, null=True)
    inherit = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    is_exception = models.CharField(max_length=255)
    partner_id = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=100)
    paytype = models.IntegerField(blank=True, null=True)
    discount_type_id = models.PositiveIntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=100, blank=True, null=True)
    is_party = models.IntegerField()
    payment_mode = models.IntegerField()
    bipanna_nagarik = models.IntegerField()
    health_insurance = models.IntegerField()
    zero_ticket_charge = models.IntegerField()
    autoload_discount = models.IntegerField()
    discount_group = models.ForeignKey(DiscountGroups, models.DO_NOTHING, blank=True, null=True)
    discount_group_percent = models.ForeignKey(DiscountGroupPercent, models.DO_NOTHING, blank=True, null=True)
    acc_account = models.ForeignKey(AccAccounts, models.DO_NOTHING, blank=True, null=True)
    acc_cost_center_id = models.PositiveIntegerField(blank=True, null=True)
    partner_login_enable = models.IntegerField()
    partner_pan_no = models.CharField(max_length=255, blank=True, null=True)
    effective_date_from = models.CharField(max_length=255, blank=True, null=True)
    effective_date_to = models.CharField(max_length=255, blank=True, null=True)
    effective = models.CharField(max_length=255)
    set_credit_limit = models.IntegerField()
    credit_limit = models.FloatField()
    is_employee = models.IntegerField()
    is_default_sharing_inherit = models.IntegerField()
    sharing_inherit_from = models.PositiveIntegerField(blank=True, null=True)
    is_non_cat = models.PositiveIntegerField(blank=True, null=True)
    panel_category = models.IntegerField()
    primary_rate_type_id = models.IntegerField()
    sharing_inherit_from_ipd = models.PositiveIntegerField(blank=True, null=True)
    sharing_inherit_from_opd = models.PositiveIntegerField(blank=True, null=True)
    panel_type = models.IntegerField(blank=True, null=True)
    is_ssf = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'patient_categories'


class PatientClinicalRecords(models.Model):
    patient_id = models.IntegerField()
    history = models.TextField(blank=True, null=True)
    complaints = models.TextField(blank=True, null=True)
    diagnosis = models.TextField(blank=True, null=True)
    risk_factor = models.TextField(blank=True, null=True)
    procedures = models.TextField(blank=True, null=True)
    hospital = models.TextField(blank=True, null=True)
    department_id = models.IntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    record_created = models.DateField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    age = models.IntegerField()
    age_type = models.CharField(max_length=1, blank=True, null=True)
    morbidity_type = models.IntegerField()
    in_patient_id = models.PositiveBigIntegerField(blank=True, null=True)
    branch = models.IntegerField()
    height = models.CharField(max_length=255, blank=True, null=True)
    weight = models.CharField(max_length=255, blank=True, null=True)
    bmi = models.CharField(max_length=255, blank=True, null=True)
    master_bill_id = models.IntegerField(blank=True, null=True)
    bp = models.CharField(max_length=255, blank=True, null=True)
    pulse = models.CharField(max_length=255, blank=True, null=True)
    spo2 = models.CharField(max_length=255, blank=True, null=True)
    temp = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_clinical_records'


class PatientDepositRefund(models.Model):
    in_pat_id = models.IntegerField()
    patient_id = models.PositiveIntegerField(blank=True, null=True)
    emergency_pat_id = models.IntegerField()
    dialysis_pat_id = models.IntegerField()
    s_masterbill_id = models.IntegerField()
    ref_masterbill_id = models.IntegerField()
    p_billreceipt_id = models.PositiveIntegerField()
    bill_no = models.CharField(max_length=255)
    refund_amount = models.FloatField(blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField()
    branch = models.PositiveIntegerField()
    revenue_center = models.IntegerField(blank=True, null=True)
    deposit_type = models.IntegerField()
    ref_deposit_bill_id = models.IntegerField()
    pat_deposit_type = models.IntegerField()
    store_id = models.IntegerField()
    cancel_status = models.IntegerField()
    is_dialysis_transfered = models.IntegerField()
    is_emergency_transfered = models.IntegerField()
    patno = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_deposit_refund'


class PatientDeposits(models.Model):
    in_pat_id = models.IntegerField()
    patient_id = models.PositiveIntegerField(blank=True, null=True)
    emergency_pat_id = models.IntegerField()
    dialysis_pat_id = models.IntegerField()
    s_masterbill_id = models.IntegerField()
    ref_masterbill_id = models.IntegerField()
    bill_no = models.CharField(max_length=255)
    deposit_amount = models.FloatField(blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    payment_type = models.PositiveIntegerField(blank=True, null=True)
    bank_id = models.PositiveIntegerField()
    card_no = models.CharField(max_length=255, blank=True, null=True)
    cheque_no = models.CharField(max_length=255, blank=True, null=True)
    branch = models.PositiveIntegerField()
    revenue_center = models.IntegerField(blank=True, null=True)
    deposit_type = models.IntegerField()
    cancel_status = models.IntegerField()
    pat_deposit_type = models.IntegerField()
    store_id = models.IntegerField()
    ref_code = models.CharField(max_length=255, blank=True, null=True)
    pos_id = models.PositiveIntegerField(blank=True, null=True)
    deposit_by = models.CharField(max_length=191, blank=True, null=True)
    is_dialysis_transfered = models.IntegerField()
    is_emergency_transfered = models.IntegerField()
    patno = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_deposits'


class PatientExercise(models.Model):
    patient_id = models.IntegerField()
    visit_id = models.IntegerField()
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    checked_status = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_exercise'


class PatientFollowups(models.Model):
    patient_id = models.IntegerField()
    visit_id = models.IntegerField()
    ipd_id = models.IntegerField()
    er_id = models.IntegerField()
    schedule_list_id = models.IntegerField()
    tem_patient_id = models.IntegerField()
    doc_id = models.IntegerField()
    doctor_name = models.CharField(max_length=191)
    appointment_date = models.DateField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_followups'


class PatientFormFields(models.Model):
    pid = models.PositiveIntegerField()
    form_element_id = models.PositiveIntegerField()
    value = models.TextField()
    status = models.IntegerField()
    masterbill_id = models.PositiveIntegerField()
    bill_date = models.DateField()
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_form_fields'


class PatientGuardian(models.Model):
    patient_id = models.IntegerField()
    relation = models.CharField(max_length=191, blank=True, null=True)
    name = models.CharField(max_length=191, blank=True, null=True)
    gender = models.CharField(max_length=191, blank=True, null=True)
    occupation = models.CharField(max_length=191, blank=True, null=True)
    address = models.CharField(max_length=191, blank=True, null=True)
    email = models.CharField(max_length=191, blank=True, null=True)
    contact = models.CharField(max_length=191, blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    ipd_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'patient_guardian'


class PatientInfoModificationLogs(models.Model):
    patient_id = models.IntegerField()
    old_info = models.TextField()
    new_info = models.TextField()
    image_mod_status = models.IntegerField()
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_info_modification_logs'


class PatientLedgers(models.Model):
    in_pat_id = models.IntegerField()
    master_bill_id = models.IntegerField()
    pat_id = models.IntegerField()
    s_masterbill_id = models.IntegerField()
    ref_master_id = models.IntegerField()
    deposit_id = models.IntegerField()
    deposit_refund_id = models.IntegerField()
    bill_no = models.CharField(max_length=255, blank=True, null=True)
    reference_bill_no = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.IntegerField()
    child_id = models.IntegerField()
    discount_group = models.IntegerField()
    discount_type = models.IntegerField()
    debt_amt = models.DecimalField(max_digits=8, decimal_places=2)
    credit_amt = models.DecimalField(max_digits=8, decimal_places=2)
    bill_type = models.CharField(max_length=1)
    remarks = models.TextField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    branch = models.PositiveIntegerField()
    revenue_center = models.IntegerField(blank=True, null=True)
    payment_type = models.IntegerField()
    bank_id = models.IntegerField()
    card_no = models.CharField(max_length=255)
    cheque_no = models.CharField(max_length=255)
    rate_type = models.ForeignKey(PatientCategories, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_ledgers'


class PatientMedication(models.Model):
    visit_id = models.IntegerField()
    patient_id = models.IntegerField()
    drug_name = models.CharField(max_length=191)
    drug_id = models.IntegerField(blank=True, null=True)
    dose = models.CharField(max_length=191)
    dose_unit = models.CharField(max_length=191)
    type = models.CharField(max_length=191)
    types_unit = models.CharField(max_length=191)
    continue_status = models.IntegerField()
    frequency_id = models.IntegerField(blank=True, null=True)
    frequency = models.CharField(max_length=191)
    route = models.CharField(max_length=191, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    duration = models.CharField(max_length=191)
    duration_unit = models.CharField(max_length=191)
    total_qty = models.CharField(max_length=191)
    total_qty_unit = models.CharField(max_length=191)
    order_id = models.IntegerField()
    sos = models.IntegerField()
    sos_instruction = models.CharField(max_length=191, blank=True, null=True)
    sos_add_instruction = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    ipd_id = models.IntegerField()
    master_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    reorder_qty = models.CharField(max_length=191, blank=True, null=True)
    actual_qty = models.CharField(max_length=191, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    batch_no = models.CharField(max_length=191, blank=True, null=True)
    expiry_date = models.CharField(max_length=191, blank=True, null=True)
    prescriber = models.CharField(max_length=191, blank=True, null=True)
    stopped_by = models.IntegerField()
    stopped_at = models.CharField(max_length=191, blank=True, null=True)
    return_qty = models.CharField(max_length=191, blank=True, null=True)
    master_return_id = models.IntegerField()
    medication_time = models.CharField(max_length=191)
    er_id = models.IntegerField()
    is_takeaway = models.IntegerField()
    takeaway_quantity = models.BigIntegerField()
    is_external = models.IntegerField()
    is_self = models.IntegerField()
    prescribed_date = models.DateField()
    requisition_no = models.CharField(max_length=191, blank=True, null=True)
    dialysis_pat_id = models.IntegerField()
    is_nebu_medicine = models.IntegerField()
    ot_template = models.IntegerField()
    cardex_remarks = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_exchanged = models.IntegerField()
    order_qty = models.IntegerField(blank=True, null=True)
    prescribed_consultant = models.CharField(max_length=191, blank=True, null=True)
    referenced_pm_id = models.IntegerField(blank=True, null=True)
    show_in_discharge_summary = models.IntegerField()
    order_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_medication'


class PatientMemberPivot(models.Model):
    patient = models.ForeignKey('Patients', models.DO_NOTHING, blank=True, null=True)
    discount_group_percent = models.ForeignKey(DiscountGroupPercent, models.DO_NOTHING, blank=True, null=True)
    valid_from = models.DateField(blank=True, null=True)
    valid_until = models.DateField(blank=True, null=True)
    enable = models.IntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    member_no = models.CharField(max_length=255, blank=True, null=True)
    never_expiry = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'patient_member_pivot'


class PatientObsGynae(models.Model):
    visit_id = models.IntegerField()
    patient_id = models.IntegerField()
    ipd_id = models.IntegerField()
    er_id = models.IntegerField()
    dialysis_id = models.IntegerField()
    lmp = models.TextField(blank=True, null=True)
    cycle_length = models.TextField(blank=True, null=True)
    flow_days = models.TextField(blank=True, null=True)
    pads = models.TextField(blank=True, null=True)
    gravida = models.TextField(blank=True, null=True)
    parity = models.TextField(blank=True, null=True)
    abortion = models.TextField(blank=True, null=True)
    gastation = models.TextField(blank=True, null=True)
    symptoms = models.TextField(blank=True, null=True)
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    ob_details = models.TextField(blank=True, null=True)
    contraceptive_history = models.TextField(blank=True, null=True)
    personal_history = models.TextField(blank=True, null=True)
    medical_surgical_history = models.TextField(blank=True, null=True)
    husband_name = models.CharField(max_length=191, blank=True, null=True)
    age = models.CharField(max_length=191, blank=True, null=True)
    occupation = models.CharField(max_length=191, blank=True, null=True)
    married_since = models.CharField(max_length=191, blank=True, null=True)
    sub_fertility = models.CharField(max_length=191, blank=True, null=True)
    husband_personal_history = models.TextField(blank=True, null=True)
    medical_history = models.TextField(blank=True, null=True)
    husband_semen_analysis = models.TextField(blank=True, null=True)
    past_inv_report_and_treatments = models.TextField(blank=True, null=True)
    husband_marriage_status = models.CharField(max_length=191, blank=True, null=True)
    wife_marriage_status = models.CharField(max_length=191, blank=True, null=True)
    lmp_remark = models.TextField(blank=True, null=True)
    wife_past_inv_report_and_treatments = models.TextField(blank=True, null=True)
    is_pregnant = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'patient_obs_gynae'


class PatientPortalLog(models.Model):
    instance = models.CharField(max_length=255)
    remarks = models.TextField()
    created_by = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_portal_log'


class PatientRelationPivot(models.Model):
    rel_id = models.IntegerField()
    inpat_id = models.IntegerField()
    pat_id = models.IntegerField()
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    type = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_relation_pivot'


class PatientServiceAppointment(models.Model):
    pat = models.ForeignKey('Patients', models.DO_NOTHING, blank=True, null=True)
    in_pat = models.ForeignKey(InPatients, models.DO_NOTHING, blank=True, null=True)
    emergency_pat = models.ForeignKey(EmergencyRegistration, models.DO_NOTHING, blank=True, null=True)
    dialysis_pat = models.ForeignKey(DialysisPatients, models.DO_NOTHING, blank=True, null=True)
    appointment_date = models.DateField()
    appointment_no = models.CharField(max_length=255, blank=True, null=True)
    item = models.ForeignKey(Items, models.DO_NOTHING)
    item_name = models.CharField(max_length=255)
    dept = models.ForeignKey(Departments, models.DO_NOTHING)
    st_hh = models.IntegerField(db_column='st_HH')  # Field name made lowercase.
    st_mm = models.IntegerField()
    st_fulltime = models.CharField(max_length=255)
    ed_hh = models.IntegerField(db_column='ed_HH')  # Field name made lowercase.
    ed_mm = models.IntegerField()
    ed_fulltime = models.CharField(max_length=255)
    s_billdetail = models.ForeignKey('SBilldetails', models.DO_NOTHING, blank=True, null=True)
    billdetail = models.ForeignKey(BillDetails, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='updated_by', related_name='patientserviceappointment_updated_by_set', blank=True, null=True)
    status = models.IntegerField(db_comment=' 0:Pending\n                  1: Completed\n                  2: Waiting\n                  3: Cancelled\n                  4: Scheduled for Next Date')
    queue_no = models.IntegerField()
    from_call_center = models.IntegerField(db_comment='1: Indicator from call center')
    temp_pat_id = models.PositiveIntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_service_appointment'


class PatientTags(models.Model):
    tag_name = models.CharField(max_length=255)
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    tag_color = models.CharField(max_length=255)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_tags'


class PatientTests(models.Model):
    visit_id = models.IntegerField()
    patient_id = models.IntegerField()
    test_name = models.CharField(max_length=191)
    test_id = models.IntegerField()
    panel = models.IntegerField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    billing_status = models.IntegerField()
    ipd_id = models.IntegerField()
    s_bill_detail_id = models.CharField(max_length=255)
    er_id = models.IntegerField()
    is_procedure = models.CharField(max_length=191)
    is_physiotherapy = models.CharField(max_length=191)
    is_package = models.CharField(max_length=191)
    bill_detail_id = models.IntegerField(blank=True, null=True)
    cancelled_at = models.DateTimeField(blank=True, null=True)
    cancelled_by = models.PositiveIntegerField()
    remarks = models.CharField(max_length=255, blank=True, null=True)
    prescribed_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'patient_tests'


class PatientVaccination(models.Model):
    patient_id = models.IntegerField()
    visit_id = models.IntegerField()
    ipd_id = models.IntegerField()
    er_id = models.IntegerField()
    dialysis_pat_id = models.IntegerField()
    vaccine = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    dose = models.CharField(max_length=191, blank=True, null=True)
    frequency = models.CharField(max_length=191, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    route = models.CharField(max_length=191, blank=True, null=True)
    vaccine_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'patient_vaccination'


class Patients(models.Model):
    visit_count = models.PositiveIntegerField()
    patient_index = models.BigIntegerField(blank=True, null=True)
    mname = models.CharField(max_length=255, blank=True, null=True)
    fname = models.CharField(max_length=255, blank=True, null=True)
    lname = models.CharField(max_length=255, blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    dob = models.CharField(max_length=50, blank=True, null=True)
    dob_ad = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    bloodgroup = models.CharField(db_column='bloodGroup', max_length=255, blank=True, null=True)  # Field name made lowercase.
    maritalstatus = models.CharField(db_column='maritalStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    zone = models.IntegerField(blank=True, null=True)
    district = models.IntegerField(blank=True, null=True)
    vdc = models.IntegerField(blank=True, null=True)
    ward = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    phoneno = models.CharField(db_column='phoneNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mobileno = models.CharField(db_column='mobileNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(max_length=255, blank=True, null=True)
    consultantname = models.CharField(db_column='consultantName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    patient_cat = models.ForeignKey(PatientCategories, models.DO_NOTHING, blank=True, null=True)
    member_id = models.IntegerField(blank=True, null=True)
    insurance_no = models.CharField(max_length=255, blank=True, null=True)
    ssf_no = models.CharField(max_length=255, blank=True, null=True)
    ethinicity_code = models.IntegerField(blank=True, null=True)
    created_at_bs = models.CharField(max_length=10, blank=True, null=True)
    age_type = models.CharField(max_length=1, blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    education = models.CharField(max_length=191, blank=True, null=True)
    company_name = models.CharField(max_length=191, blank=True, null=True)
    category_id = models.IntegerField()
    branch = models.PositiveIntegerField()
    province_id = models.IntegerField()
    province_district_id = models.IntegerField()
    roll_no = models.IntegerField(blank=True, null=True)
    year_id = models.IntegerField(blank=True, null=True)
    batch_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField(blank=True, null=True)
    program_year_id = models.IntegerField(blank=True, null=True)
    print_count = models.IntegerField()
    is_activate = models.IntegerField()
    otp_code = models.IntegerField(blank=True, null=True)
    otp_code_expire = models.DateTimeField(blank=True, null=True)
    otp_status = models.IntegerField()
    passport_no = models.CharField(max_length=255, blank=True, null=True)
    country_issued = models.CharField(max_length=255, blank=True, null=True)
    municipality_id = models.IntegerField(blank=True, null=True)
    is_registered = models.IntegerField()
    is_set_dob = models.IntegerField()
    age_status = models.IntegerField()
    dob_status = models.IntegerField()
    name_title = models.IntegerField(blank=True, null=True)
    employee_id = models.CharField(max_length=255, blank=True, null=True)
    fullname = models.CharField(max_length=100, blank=True, null=True)
    is_death = models.IntegerField()
    is_dental = models.IntegerField()
    last_login = models.DateTimeField(blank=True, null=True)
    mig_stat = models.IntegerField(blank=True, null=True)
    mother_pat_id = models.IntegerField(blank=True, null=True)
    temp_mobile = models.CharField(max_length=100, blank=True, null=True)
    death_time = models.DateTimeField(blank=True, null=True)
    document = models.CharField(max_length=255, blank=True, null=True)
    document_type = models.IntegerField()
    document_uploaded_at = models.DateTimeField(blank=True, null=True)
    is_parent = models.IntegerField()
    kyc_expired_at = models.DateTimeField(blank=True, null=True)
    kyc_verify_at = models.DateTimeField(blank=True, null=True)
    merge_count = models.IntegerField()
    merged_at = models.DateTimeField(blank=True, null=True)
    merged_by = models.PositiveIntegerField()
    nationality_id = models.PositiveIntegerField(blank=True, null=True)
    parent_id = models.PositiveIntegerField()
    verify_kyc = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'patients'


class PaymentLogs(models.Model):
    source = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    response_type = models.CharField(max_length=255, blank=True, null=True)
    payment_method = models.ForeignKey('PaymentMethod', models.DO_NOTHING, blank=True, null=True)
    payment_method_name = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.PositiveIntegerField(blank=True, null=True)
    patient_id = models.PositiveIntegerField(blank=True, null=True)
    response = models.JSONField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_logs'


class PaymentMethod(models.Model):
    phar_payment_method_id = models.IntegerField(blank=True, null=True)
    payment_mode = models.CharField(max_length=255)
    editable = models.IntegerField()
    active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    payment_method_type = models.CharField(max_length=255, blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    payment_credentials = models.JSONField(blank=True, null=True)
    is_dynamic_qr = models.IntegerField()
    payment_group = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_method'


class PaymentReceipt(models.Model):
    item_id = models.IntegerField()
    patient_id = models.IntegerField()
    receipt_no = models.CharField(max_length=255)
    date = models.DateField()
    time = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    master_bill = models.ForeignKey(MasterBills, models.DO_NOTHING, blank=True, null=True)
    is_paid = models.IntegerField()
    book_cancel = models.IntegerField()
    book_cancel_date = models.DateTimeField(blank=True, null=True)
    source = models.PositiveIntegerField(db_comment='1: Wellness, 2: Appointment')
    payment_transaction_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'payment_receipt'


class PaymentTransactions(models.Model):
    temp_patient_id = models.IntegerField()
    epay_vendor_id = models.IntegerField()
    gateway_ref = models.CharField(max_length=255)
    epay_status = models.IntegerField()
    invoice_status = models.IntegerField()
    total_amount = models.FloatField()
    transaction_amount = models.FloatField(blank=True, null=True)
    response_data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    schedule_list_id = models.IntegerField()
    merchantcode = models.CharField(db_column='MerchantCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refid = models.CharField(db_column='RefId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tokenid = models.CharField(db_column='TokenId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    msisdn = models.CharField(db_column='Msisdn', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payment_transactions'


class PdfUploads(models.Model):
    file_name = models.CharField(max_length=191)
    f_name = models.CharField(max_length=191)
    uploaded_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pdf_uploads'


class PermissionRole(models.Model):
    permission = models.OneToOneField('Permissions', models.DO_NOTHING, primary_key=True)  # The composite primary key (permission_id, role_id) found, that is not supported. The first column is selected.
    role = models.ForeignKey('Roles', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'permission_role'
        unique_together = (('permission', 'role'),)


class PermissionUser(models.Model):
    user_id = models.IntegerField()
    accessible_id = models.IntegerField()
    accessible_type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'permission_user'


class Permissions(models.Model):
    name = models.CharField(unique=True, max_length=255)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    catagory = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissions'


class PharPivotMasterBillPaymentTypes(models.Model):
    payment_id = models.PositiveIntegerField(blank=True, null=True)
    pharmacy_master_bill_id = models.PositiveIntegerField()
    bank_id = models.PositiveIntegerField()
    card_no = models.CharField(max_length=191, blank=True, null=True)
    reference_number = models.CharField(max_length=191, blank=True, null=True)
    amount = models.CharField(max_length=191)
    cheque_no = models.CharField(max_length=191, blank=True, null=True)
    bill_type = models.CharField(max_length=191, blank=True, null=True)
    payment_type = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    pharmacy_master_refund_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'phar_pivot_master_bill_payment_types'


class PharStockLog(models.Model):
    created_by = models.PositiveIntegerField(blank=True, null=True)
    catalogue_id = models.PositiveIntegerField(blank=True, null=True)
    batch = models.CharField(max_length=191, blank=True, null=True)
    remark = models.CharField(max_length=191, blank=True, null=True)
    type = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phar_stock_log'


class PharmacyBillReceipts(models.Model):
    receipt_no = models.CharField(max_length=191)
    patient_id = models.IntegerField()
    inpatient_id = models.IntegerField(blank=True, null=True)
    amount = models.FloatField()
    type = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pharmacy_bill_receipts'


class PharmacyConfigs(models.Model):
    name = models.CharField(max_length=191)
    value = models.TextField()
    type = models.CharField(max_length=191)
    description = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'pharmacy_configs'


class PharmacyCounter(models.Model):
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    module = models.CharField(max_length=191)
    counter_name = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=8)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pharmacy_counter'


class PharmacyMedicineQueues(models.Model):
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    pharmacy_master_bill = models.ForeignKey(PPharmacyMasterBills, models.DO_NOTHING)
    token_number = models.IntegerField()
    status = models.IntegerField()
    received_by = models.PositiveIntegerField(blank=True, null=True)
    received_at = models.DateTimeField(blank=True, null=True)
    to_be_dispatched_at = models.DateTimeField(blank=True, null=True)
    call_at = models.DateTimeField(blank=True, null=True)
    counter_name = models.CharField(max_length=191, blank=True, null=True)
    dispatched_by = models.PositiveIntegerField(blank=True, null=True)
    dispatched_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pharmacy_medicine_queues'


class PharmacyServiceBillDetails(models.Model):
    pharmacy_s_bill_detail_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    pharmacy_s_master_bill_id = models.PositiveIntegerField()
    pharmacy_master_bill_id = models.PositiveIntegerField(blank=True, null=True)
    batch = models.CharField(max_length=191)
    patient_id = models.PositiveIntegerField(blank=True, null=True)
    in_pat_id = models.PositiveIntegerField(blank=True, null=True)
    store_id = models.PositiveIntegerField()
    refund_status = models.CharField(max_length=1)
    cancel_status = models.CharField(max_length=1)
    catalogue_type_id = models.PositiveIntegerField()
    catalogue_id = models.PositiveIntegerField()
    cost_price = models.FloatField()
    rate = models.FloatField()
    expiry_date = models.CharField(max_length=191)
    total_stock_quantity = models.PositiveIntegerField()
    total_sales_quantity = models.PositiveIntegerField()
    quantity = models.IntegerField()
    refund_quantity = models.PositiveIntegerField()
    total_remaining_quantity = models.PositiveIntegerField()
    amount = models.FloatField()
    discount_percentage = models.PositiveIntegerField()
    discount = models.FloatField()
    is_taxable = models.IntegerField()
    taxable_amt = models.FloatField()
    tax_per = models.FloatField()
    tax = models.FloatField()
    total = models.FloatField()
    refunded_by = models.PositiveIntegerField(blank=True, null=True)
    refunded_at = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    master_medication_id = models.PositiveIntegerField(blank=True, null=True)
    patient_med_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pharmacy_service_bill_details'


class PharmacyServiceBilldetailStockissues(models.Model):
    pharmacy_s_billdetail_stockissue_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    pharmacy_s_master_bill_id = models.PositiveIntegerField()
    pharmacy_s_bill_detail_id = models.PositiveIntegerField()
    stock_issue_id = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    pharmacy_s_billdetail_stockissue_created_by = models.PositiveIntegerField()
    pharmacy_s_billdetail_stockissue_updated_by = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pharmacy_service_billdetail_stockissues'


class PharmacyServiceMasterBills(models.Model):
    pharmacy_s_master_bill_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    bill_no = models.CharField(unique=True, max_length=191)
    patient_id = models.PositiveIntegerField(blank=True, null=True)
    in_pat_id = models.PositiveIntegerField(blank=True, null=True)
    pharmacy_master_bill_id = models.PositiveIntegerField(blank=True, null=True)
    reference_s_master_bill_id = models.PositiveIntegerField(blank=True, null=True)
    store_id = models.PositiveIntegerField()
    consultant = models.PositiveIntegerField(blank=True, null=True)
    ref_hospital_id = models.IntegerField(blank=True, null=True)
    pan = models.CharField(max_length=191, blank=True, null=True)
    refund_status = models.IntegerField()
    cancel_status = models.IntegerField()
    print_count = models.IntegerField()
    amount = models.FloatField()
    discount = models.FloatField()
    taxable_amt = models.FloatField()
    tax = models.FloatField()
    total = models.FloatField()
    discount_group_id = models.PositiveIntegerField(blank=True, null=True)
    discount_group_percent_id = models.PositiveIntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=191, blank=True, null=True)
    created_at_nepali_date = models.CharField(max_length=10)
    refunded_by = models.PositiveIntegerField(blank=True, null=True)
    refunded_at = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    master_medication_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'pharmacy_service_master_bills'


class PharmacyServiceMasterRefunds(models.Model):
    pharmacy_s_master_refund_id = models.AutoField(primary_key=True)
    pharmacy_s_master_bill_id = models.PositiveIntegerField()
    pharmacy_s_refund_store_id = models.PositiveIntegerField()
    pharmacy_s_refund_bill_no = models.CharField(max_length=191)
    pharmacy_s_refund_remarks = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pharmacy_service_master_refunds'


class PharmacyShortCodes(models.Model):
    branch_id = models.PositiveIntegerField()
    short_code = models.CharField(unique=True, max_length=191)
    description = models.TextField()
    status = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pharmacy_short_codes'


class PharmacyShortcuts(models.Model):
    command = models.CharField(max_length=191)
    key_binding = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    status = models.PositiveIntegerField()
    updated_by = models.DateTimeField()
    created_by = models.DateTimeField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pharmacy_shortcuts'


class PisAppMenus(models.Model):
    name = models.CharField(max_length=191, blank=True, null=True)
    display_name = models.CharField(max_length=191, blank=True, null=True)
    url = models.CharField(max_length=191, blank=True, null=True)
    order = models.PositiveIntegerField(blank=True, null=True)
    active = models.PositiveIntegerField()
    tab = models.PositiveIntegerField()
    logo = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pis_app_menus'


class PisCheckInOut(models.Model):
    id = models.BigAutoField(primary_key=True)
    in_out_date = models.DateField()
    in_out_time = models.TimeField()
    status = models.CharField(max_length=191)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    in_status = models.IntegerField()
    out_status = models.IntegerField()
    created_by_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pis_check_in_out'


class PisDepartments(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey('Users', models.DO_NOTHING)
    status = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pis_departments'


class PisDesignations(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(PisDepartments, models.DO_NOTHING)
    audit = models.ForeignKey('Users', models.DO_NOTHING)
    status = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pis_designations'


class PisEmployeeSalaryHeads(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING)
    earning_heads = models.ForeignKey('PisSalaryEarningHeads', models.DO_NOTHING, blank=True, null=True)
    deducation_heads = models.ForeignKey('PisSalaryDeductionHeads', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pis_employee_salary_heads'


class PisFailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=191)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pis_failed_jobs'


class PisHolidays(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=191)
    from_date = models.DateField()
    to_date = models.DateField()
    total_days = models.BigIntegerField()
    status = models.IntegerField()
    audit = models.ForeignKey('Users', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pis_holidays'


class PisLeaveTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    short_code = models.CharField(max_length=191)
    name = models.CharField(max_length=191)
    color_code = models.CharField(max_length=191)
    icon = models.CharField(max_length=191)
    status = models.IntegerField()
    audit = models.ForeignKey('Users', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pis_leave_types'


class PisPermissionCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=191, blank=True, null=True)
    status = models.IntegerField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pis_permission_category'


class PisPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)
    description = models.CharField(max_length=191, blank=True, null=True)
    permission_category = models.ForeignKey(PisPermissionCategory, models.DO_NOTHING)
    created_by = models.ForeignKey('Users', models.DO_NOTHING)
    status = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pis_permissions'


class PisRolePermission(models.Model):
    id = models.BigAutoField(primary_key=True)
    role = models.ForeignKey('PisRoles', models.DO_NOTHING)
    permission = models.ForeignKey(PisPermissions, models.DO_NOTHING)
    created_by = models.ForeignKey('Users', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pis_role_permission'


class PisRoles(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=191, blank=True, null=True)
    status = models.IntegerField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pis_roles'


class PisSalaryDeductionHeads(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING)
    applicable_after_tax = models.IntegerField()
    deduction_heads = models.CharField(max_length=191)
    default_percent = models.DecimalField(max_digits=10, decimal_places=2)
    applicable_to_basic_gross = models.IntegerField()
    description = models.CharField(max_length=191, blank=True, null=True)
    grouping_category = models.IntegerField()
    grouping_category_captions = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pis_salary_deduction__heads'


class PisSalaryEarningHeads(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING)
    is_basic = models.IntegerField()
    applicable_after_tax = models.IntegerField()
    earning_heads = models.CharField(max_length=191)
    description = models.CharField(max_length=191, blank=True, null=True)
    grouping_category = models.IntegerField()
    grouping_category_captions = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pis_salary_earning_heads'


class PisShiftTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    from_time = models.TimeField()
    to_time = models.TimeField()
    shift_title = models.CharField(max_length=191)
    weekend = models.CharField(max_length=191, blank=True, null=True)
    color_code = models.CharField(max_length=191)
    created_by = models.ForeignKey('Users', models.DO_NOTHING)
    is_default = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pis_shift_types'


class PisTaxSetup(models.Model):
    id = models.BigAutoField(primary_key=True)
    fiscal_year = models.CharField(max_length=191)
    is_married = models.IntegerField()
    tax_banding = models.CharField(max_length=191)
    tax_percentage = models.IntegerField()
    tax_amount = models.BigIntegerField()
    audit = models.ForeignKey('Users', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pis_tax_setup'


class PisUserDocuments(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=191)
    employee = models.ForeignKey('Users', models.DO_NOTHING)
    size = models.IntegerField(blank=True, null=True)
    extension = models.CharField(max_length=191, blank=True, null=True)
    file_path = models.CharField(max_length=191, blank=True, null=True)
    thumbnail = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pis_user_documents'


class PisUserRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    role = models.ForeignKey(PisRoles, models.DO_NOTHING)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, related_name='pisuserrole_created_by_set')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pis_user_role'


class PisUserShiftDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    from_time = models.TimeField(blank=True, null=True)
    to_time = models.TimeField(blank=True, null=True)
    shift = models.ForeignKey(PisShiftTypes, models.DO_NOTHING)
    is_custom = models.PositiveBigIntegerField()
    status = models.IntegerField()
    audit_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pis_user_shift_details'


class PisUsersDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    gender = models.CharField(max_length=191)
    contact_number = models.CharField(max_length=191)
    province = models.CharField(max_length=191)
    city = models.CharField(max_length=191)
    zip_code = models.CharField(max_length=191, blank=True, null=True)
    address_line_1 = models.CharField(max_length=191)
    address_line_2 = models.CharField(max_length=191, blank=True, null=True)
    pan_no = models.PositiveBigIntegerField(blank=True, null=True)
    joining_date = models.DateField()
    emergency_contact_name = models.CharField(max_length=191)
    emergency_contact_number = models.CharField(max_length=191)
    relationship = models.CharField(max_length=191, blank=True, null=True)
    bank_name = models.CharField(max_length=191, blank=True, null=True)
    account_name = models.CharField(max_length=191, blank=True, null=True)
    account_number = models.CharField(max_length=191, blank=True, null=True)
    audit = models.ForeignKey('Users', models.DO_NOTHING, related_name='pisusersdetail_audit_set')
    avatar = models.CharField(max_length=191, blank=True, null=True)
    dob = models.DateField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pis_users_detail'


class PivotAccChequePrintTemplates(models.Model):
    key = models.CharField(max_length=191)
    x_coordinate = models.IntegerField()
    y_coordinate = models.IntegerField()
    width = models.IntegerField()
    character_padding = models.IntegerField()
    font_size = models.IntegerField()
    inherit_font_size_from_parent = models.IntegerField()
    acc_cheque_print_templates_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pivot_acc_cheque_print_templates'


class PivotAdditionalSpecimenSample(models.Model):
    sample_collection = models.ForeignKey('SampleCollection', models.DO_NOTHING, blank=True, null=True)
    additional_specimen = models.ForeignKey(AdditionalSpecimen, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pivot_additional_specimen_sample'


class PivotBillDetailSharing(models.Model):
    bill = models.ForeignKey(BillDetails, models.DO_NOTHING, blank=True, null=True)
    s_bill = models.ForeignKey('SBilldetails', models.DO_NOTHING, blank=True, null=True)
    consultant_type = models.IntegerField()
    doctor_discount_percent = models.FloatField()
    doctor_discount_amount = models.FloatField()

    class Meta:
        managed = False
        db_table = 'pivot_bill_detail_sharing'


class PivotBilldetailStockissues(models.Model):
    pivot_billdetail_stockissue_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    pharmacy_master_bill_id = models.PositiveIntegerField()
    pharmacy_bill_detail_id = models.PositiveIntegerField()
    stock_issue_id = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    pivot_billdetail_stockissue_created_by = models.PositiveIntegerField()
    pivot_billdetail_stockissue_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    pharmacy_master_refund_id = models.PositiveIntegerField()
    phar_refund_detail_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'pivot_billdetail_stockissues'


class PivotBipannaPatients(models.Model):
    pat_id = models.IntegerField()
    discount_group_id = models.IntegerField()
    discount_percent_id = models.IntegerField()
    balance = models.FloatField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    rate_type_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pivot_bipanna_patients'


class PivotBranchPrint(models.Model):
    branch_id = models.PositiveIntegerField()
    print_info = models.TextField(blank=True, null=True)
    branch_column_name = models.CharField(max_length=191, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pivot_branch_print'


class PivotCatalogueGeneric(models.Model):
    catalogue_id = models.PositiveIntegerField()
    generic_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'pivot_catalogue_generic'


class PivotChildItems(models.Model):
    parent_item_id = models.IntegerField()
    child_item_id = models.IntegerField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pivot_child_items'


class PivotClosingStockDetailStockPurchases(models.Model):
    closing_stock_details_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    stock_purchases_id = models.PositiveIntegerField()
    master_stock_purchases_id = models.PositiveIntegerField()
    master_stock_issues_id = models.PositiveIntegerField()
    stock_issue_id = models.PositiveIntegerField()
    closing_stocks_id = models.PositiveIntegerField()
    actual_qty = models.IntegerField()
    reconcile_qty = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pivot_closing_stock_detail_stock_purchases'


class PivotDepartmentUsers(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(Departments, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pivot_department_users'


class PivotDepartmentVerify(models.Model):
    user_id = models.IntegerField()
    department_id = models.IntegerField()
    active = models.IntegerField()
    description = models.TextField()
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pivot_department_verify'


class PivotDischargeSummaryDoctors(models.Model):
    discharge_summary_id = models.IntegerField()
    designation_id = models.IntegerField()
    designation_name = models.CharField(max_length=255)
    doctor_id = models.IntegerField()
    doctor_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pivot_discharge_summary_doctors'


class PivotDischargeSummaryIcdCode(models.Model):
    discharge_summary_id = models.IntegerField()
    disease_code_id = models.IntegerField()
    disease_code = models.CharField(max_length=255)
    disease = models.CharField(max_length=255)
    confirmed = models.IntegerField()
    is_icd = models.IntegerField()
    show_in_discharge_summary = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pivot_discharge_summary_icd_code'


class PivotDischargeSummaryMedicines(models.Model):
    discharge_summary_id = models.IntegerField()
    drug_name = models.CharField(max_length=255)
    drug_type = models.CharField(max_length=255)
    dose = models.CharField(max_length=255)
    frequency = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    drug_id = models.IntegerField()
    duration = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    route = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pivot_discharge_summary_medicines'


class PivotDischargeSummaryOperations(models.Model):
    discharge_summary_id = models.IntegerField()
    operation_date = models.CharField(max_length=255)
    procedure = models.CharField(max_length=255)
    findings = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=255)
    minor_type = models.CharField(max_length=255, blank=True, null=True)
    infection = models.TextField()

    class Meta:
        managed = False
        db_table = 'pivot_discharge_summary_operations'


class PivotDiscountPercentTemplate(models.Model):
    discount_group_id = models.PositiveIntegerField()
    discount_percent_id = models.PositiveIntegerField()
    discount_template_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'pivot_discount_percent_template'


class PivotDiscounttypeHeads(models.Model):
    discount_group_percent_id = models.IntegerField()
    discount_name = models.CharField(max_length=255, blank=True, null=True)
    main_category_id = models.IntegerField(blank=True, null=True)
    main_category = models.CharField(max_length=255, blank=True, null=True)
    hospital_discount = models.IntegerField()
    department_discount = models.IntegerField()
    anesthesist_discount = models.IntegerField()
    fund_discount = models.IntegerField()
    depreciation_discount = models.IntegerField()
    instrument_discount = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    discount_percentage = models.FloatField()
    appliance_discount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pivot_discounttype_heads'


class PivotDoctorDesignations(models.Model):
    doctor_id = models.PositiveIntegerField(blank=True, null=True)
    designation_id = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pivot_doctor_designations'


class PivotItemBranch(models.Model):
    branch_id = models.PositiveIntegerField()
    item_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'pivot_item_branch'


class PivotMasterBillSharing(models.Model):
    master_bill = models.ForeignKey(MasterBills, models.DO_NOTHING)
    s_master_bill = models.ForeignKey('SMasterbills', models.DO_NOTHING)
    consultant_type = models.IntegerField()
    doctor_discount_total_percent = models.FloatField()
    doctor_discount_total_amount = models.FloatField()

    class Meta:
        managed = False
        db_table = 'pivot_master_bill_sharing'


class PivotMasterBillsNotes(models.Model):
    master_bill = models.ForeignKey(MasterBills, models.DO_NOTHING)
    debit = models.FloatField()
    credit = models.FloatField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    cancel_status = models.IntegerField()
    dialysis_pat_id = models.IntegerField()
    emergency_pat_id = models.IntegerField()
    in_pat_id = models.IntegerField()
    note_no = models.CharField(max_length=255, blank=True, null=True)
    patient_id = models.IntegerField()
    patno = models.CharField(max_length=100, blank=True, null=True)
    source = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pivot_master_bills_notes'


class PivotNewbornChildDetails(models.Model):
    maternity_register_id = models.IntegerField()
    delivery_date = models.DateField()
    delivery_time = models.TimeField()
    baby_gender = models.CharField(max_length=255)
    baby_weight = models.CharField(max_length=255)
    outcome_of_baby = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pivot_newborn_child_details'


class PivotParameterIntensitySetup(models.Model):
    item_id = models.IntegerField()
    test_id = models.IntegerField()
    parameter_id = models.IntegerField()
    class_field = models.CharField(db_column='class', max_length=255, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    min_val = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    max_val = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    explanation = models.TextField(blank=True, null=True)
    display_order = models.IntegerField()
    branch = models.PositiveIntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pivot_parameter_intensity_setup'


class PivotParameterRefRanges(models.Model):
    item_id = models.IntegerField()
    test_id = models.IntegerField()
    parameter_id = models.IntegerField()
    age_type = models.CharField(max_length=255)
    age_min_limit = models.PositiveIntegerField(blank=True, null=True)
    age_max_limit = models.PositiveIntegerField(blank=True, null=True)
    male_min = models.CharField(max_length=255, blank=True, null=True)
    male_max = models.CharField(max_length=255, blank=True, null=True)
    female_min = models.CharField(max_length=255, blank=True, null=True)
    female_max = models.CharField(max_length=255, blank=True, null=True)
    display_order = models.IntegerField()
    branch = models.PositiveIntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    q_range = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pivot_parameter_ref_ranges'


class PivotPatientBatch(models.Model):
    pat_id = models.PositiveIntegerField()
    batch_id = models.PositiveIntegerField()
    sms_status = models.IntegerField()
    report_sms = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pivot_patient_batch'


class PivotPatientClinicalRecords(models.Model):
    patient_clinical_record_id = models.IntegerField()
    disease_code_id = models.IntegerField()
    disease_code = models.CharField(max_length=255)
    disease = models.CharField(max_length=255)
    is_icd = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pivot_patient_clinical_records'


class PivotPatientSms(models.Model):
    patient_id = models.IntegerField()
    bill_id = models.IntegerField()
    invoice_sms = models.IntegerField()
    report_sms = models.IntegerField()
    repeat_sms = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    unsend_status = models.IntegerField()
    batch_id = models.PositiveIntegerField()
    created_by = models.PositiveIntegerField()
    doctor_leave_sms = models.IntegerField()
    instance = models.TextField()
    message = models.TextField()
    mobileno = models.CharField(db_column='mobileNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    schedule_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pivot_patient_sms'


class PivotPatientTags(models.Model):
    patient_id = models.IntegerField()
    tag_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pivot_patient_tags'


class PivotPaymentMethodDetail(models.Model):
    master_bill_id = models.PositiveIntegerField()
    payment_type_id = models.PositiveIntegerField()
    payment_name = models.CharField(max_length=255, blank=True, null=True)
    ref_number = models.CharField(max_length=255)
    vendor = models.PositiveIntegerField()
    amount = models.FloatField()
    pos_id = models.IntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    in_pat_id = models.PositiveIntegerField(blank=True, null=True)
    revenue_center = models.PositiveIntegerField(blank=True, null=True)
    chq_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    rectno = models.CharField(max_length=100, blank=True, null=True)
    is_refund = models.IntegerField(blank=True, null=True)
    ptype = models.CharField(max_length=100, blank=True, null=True)
    pat_deposit_type = models.IntegerField(blank=True, null=True)
    emergency_pat_id = models.IntegerField(blank=True, null=True)
    dialysis_pat_id = models.IntegerField(blank=True, null=True)
    reference_id = models.IntegerField(blank=True, null=True)
    reference_no = models.CharField(max_length=100, blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    card_holder_name = models.CharField(max_length=255, blank=True, null=True)
    cost_center_id = models.PositiveIntegerField(blank=True, null=True)
    deposit_by = models.CharField(max_length=255, blank=True, null=True)
    drawn_on_bank = models.PositiveIntegerField(blank=True, null=True)
    is_dialysis_transfered = models.IntegerField()
    is_emergency_transfered = models.IntegerField()
    patient_id = models.IntegerField(blank=True, null=True)
    patno = models.CharField(max_length=100, blank=True, null=True)
    print_count = models.IntegerField()
    remarks = models.CharField(max_length=255, blank=True, null=True)
    schedule_list_id = models.PositiveIntegerField()
    status = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    voucher_no = models.CharField(max_length=255, blank=True, null=True)
    cancellation_remarks = models.CharField(max_length=255, blank=True, null=True)
    cancelled_at = models.DateTimeField(blank=True, null=True)
    cancelled_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pivot_payment_method_detail'


class PivotPeriodUser(models.Model):
    user_id = models.IntegerField()
    period_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_preferred = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pivot_period_user'


class PivotPharmacyMasterbillConsultants(models.Model):
    pharmacy_master_bill_id = models.BigIntegerField()
    consultant_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'pivot_pharmacy_masterbill_consultants'


class PivotPregnancySummaries(models.Model):
    discharge_summary_id = models.IntegerField()
    date = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    baby_weight = models.CharField(max_length=255)
    week_gestation = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    birth_delete_status = models.IntegerField()
    abortus = models.CharField(max_length=255, blank=True, null=True)
    baby_height = models.CharField(max_length=255, blank=True, null=True)
    birth_certificate_no = models.CharField(max_length=255, blank=True, null=True)
    bloodgroup = models.CharField(db_column='bloodGroup', max_length=255, blank=True, null=True)  # Field name made lowercase.
    child_ipd_id = models.IntegerField(blank=True, null=True)
    child_pat_id = models.IntegerField(blank=True, null=True)
    father_name = models.CharField(max_length=255, blank=True, null=True)
    gestation = models.CharField(max_length=255, blank=True, null=True)
    gravida = models.CharField(max_length=255, blank=True, null=True)
    in_pat_id = models.IntegerField(blank=True, null=True)
    parity = models.CharField(max_length=255, blank=True, null=True)
    pat_id = models.IntegerField(blank=True, null=True)
    pregnancy_remarks = models.TextField(blank=True, null=True)
    pregnancy_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pivot_pregnancy_summaries'


class PivotPremiumFloor(models.Model):
    panel_category = models.PositiveIntegerField()
    room_type_id = models.PositiveIntegerField()
    floor_id = models.PositiveIntegerField()
    group1 = models.FloatField()
    group2 = models.FloatField()
    group3 = models.FloatField()
    procedure_percent = models.FloatField()
    surgery_percent = models.FloatField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pivot_premium_floor'


class PivotPurchasereturnStockpurchases(models.Model):
    pivot_purchasereturn_stockpurchase_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    master_purchases_return_id = models.PositiveIntegerField()
    purchase_return_id = models.PositiveIntegerField()
    stock_purchases_id = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    pivot_purchasereturn_stockpurchase_created_by = models.PositiveIntegerField()
    pivot_purchasereturn_stockpurchase_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pivot_purchasereturn_stockpurchases'


class PivotReportPatients(models.Model):
    bill_no = models.CharField(max_length=255)
    sample_no = models.CharField(max_length=255)
    patient_id = models.IntegerField()
    report_status = models.IntegerField()
    email_status = models.IntegerField()
    email_status_new = models.IntegerField()
    sms_status = models.IntegerField()
    sms_status_new = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    footer_template = models.IntegerField()
    report_header = models.IntegerField()
    branch = models.PositiveIntegerField()
    template_wise_signature_status = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'pivot_report_patients'


class PivotResultEntryType2Images(models.Model):
    type2_parameter_id = models.IntegerField()
    result_entry_type2_id = models.IntegerField()
    image_path = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pivot_result_entry_type2_images'


class PivotResultEntryType2Parameters(models.Model):
    result_entry_type2_id = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    show_in_discharge_summary = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pivot_result_entry_type2_parameters'


class PivotRoomAmenities(models.Model):
    room_id = models.IntegerField()
    amenities_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pivot_room_amenities'


class PivotServiceContractImages(models.Model):
    asset_id = models.IntegerField()
    accession_number = models.CharField(max_length=191, blank=True, null=True)
    is_complete = models.IntegerField()
    name = models.CharField(max_length=191, blank=True, null=True)
    url = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    path = models.CharField(max_length=191, blank=True, null=True)
    contract_type = models.CharField(max_length=191, blank=True, null=True)
    original_name = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pivot_service_contract_images'


class PivotStockPurchaseSupplierDiscountBonus(models.Model):
    stock_purchases_id = models.IntegerField()
    bonus_qty = models.CharField(max_length=191, blank=True, null=True)
    discount = models.CharField(max_length=191, blank=True, null=True)
    supplier_manufacture_discount_id = models.IntegerField()
    catalogue_cost_price = models.CharField(max_length=191, blank=True, null=True)
    cp_before_tax = models.CharField(max_length=191, blank=True, null=True)
    cp_before_tax_chg = models.CharField(max_length=191, blank=True, null=True)
    cost_price = models.CharField(max_length=191, blank=True, null=True)
    cost_price_chg = models.CharField(max_length=191, blank=True, null=True)
    item_bonus_qty = models.CharField(max_length=191, blank=True, null=True)
    bonus_qty_chg = models.CharField(max_length=191, blank=True, null=True)
    discount_per = models.CharField(max_length=191, blank=True, null=True)
    discount_per_chg = models.CharField(max_length=191, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pivot_stock_purchase_supplier_discount_bonus'


class PivotStockPurchases(models.Model):
    pivot_stock_purchases_id = models.AutoField(primary_key=True)
    stock_purchases = models.ForeignKey('StockPurchases', models.DO_NOTHING)
    stock_purchases_no = models.CharField(max_length=191)
    catalogue = models.ForeignKey(Catalogues, models.DO_NOTHING)
    batch = models.CharField(max_length=191)
    free_status = models.IntegerField()
    expiry_date = models.CharField(max_length=191)
    never_expiry = models.IntegerField()
    cost_price = models.FloatField()
    selling_price = models.FloatField()
    profit_percent = models.FloatField()
    pivot_purchases_created_by = models.PositiveIntegerField()
    pivot_purchases_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pivot_stock_purchases'


class PivotStoreUsers(models.Model):
    user_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    is_primary = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pivot_store_users'


class PivotSubjectiveTemplate(models.Model):
    template = models.ForeignKey('SubjectiveTemplates', models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    newline = models.IntegerField()
    order = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pivot_subjective_template'


class PivotSubjectiveTemplatesReports(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    subjective_template_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pivot_subjective_templates_reports'


class PivotTestTats(models.Model):
    test_id = models.IntegerField()
    branch_id = models.IntegerField()
    tat = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'pivot_test_tats'


class PivotTestTemplates(models.Model):
    test_id = models.IntegerField()
    template_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pivot_test_templates'


class PivotUserBranch(models.Model):
    user_id = models.IntegerField()
    branch_id = models.IntegerField()
    primary = models.IntegerField()
    r_center_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pivot_user_branch'


class PivotUserCompany(models.Model):
    user_id = models.IntegerField()
    company_id = models.IntegerField()
    primary = models.IntegerField()
    r_center_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pivot_user_company'


class PivotWardConsultation(models.Model):
    room_type_id = models.IntegerField()
    template_id = models.IntegerField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pivot_ward_consultation'


class Pivotpatient(models.Model):
    parent_id = models.IntegerField()
    child_id = models.IntegerField()
    relation_name = models.CharField(max_length=255)
    relation_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pivotpatient'


class PosSetup(models.Model):
    name = models.CharField(max_length=255)
    bank_id = models.PositiveIntegerField()
    is_hospital = models.PositiveIntegerField()
    is_pharmacy = models.PositiveIntegerField()
    active = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_setup'


class PricePatientCats(models.Model):
    item = models.ForeignKey(Items, models.DO_NOTHING, blank=True, null=True)
    patient_cat = models.ForeignKey(PatientCategories, models.DO_NOTHING, blank=True, null=True)
    net_amount = models.FloatField()
    total_tax = models.FloatField()
    total_amount = models.FloatField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    branch = models.PositiveIntegerField()
    hospital_share = models.FloatField()
    hospital = models.FloatField()
    hospital_percentage = models.FloatField()
    department = models.FloatField()
    department_percentage = models.FloatField()
    anesthesist = models.FloatField()
    anesthesist_percentage = models.FloatField()
    fund = models.FloatField()
    fund_percentage = models.FloatField()
    depreciation = models.FloatField()
    depreciation_percentage = models.FloatField()
    instrument = models.FloatField()
    instrument_percentage = models.FloatField()
    appliance = models.FloatField()
    appliance_percentage = models.FloatField()
    ipd_rate = models.FloatField(blank=True, null=True)
    rate_group_id = models.PositiveIntegerField(blank=True, null=True)
    start_date = models.CharField(max_length=255, blank=True, null=True)
    end_date = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.IntegerField()
    is_scheduled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'price_patient_cats'


class PricePatientCatsSchedules(models.Model):
    price_patient_cats = models.ForeignKey(PricePatientCats, models.DO_NOTHING)
    schedule_amount = models.FloatField()
    schedule_from = models.DateField(blank=True, null=True)
    schedule_to = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'price_patient_cats_schedules'


class PriceTemplates(models.Model):
    template_name = models.CharField(max_length=255)
    item_id = models.IntegerField()
    publish_date = models.DateTimeField()
    status = models.IntegerField()
    patient_category = models.IntegerField()
    rate = models.FloatField()
    currency = models.CharField(max_length=255)
    sharing_amt = models.FloatField()
    hospital_amt = models.FloatField()
    sharing = models.PositiveIntegerField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'price_templates'


class PrintLogs(models.Model):
    patient = models.ForeignKey(Patients, models.DO_NOTHING, blank=True, null=True)
    instance = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'print_logs'


class ProcedureDetail(models.Model):
    procedure_master_id = models.PositiveIntegerField()
    department = models.ForeignKey(Departments, models.DO_NOTHING, blank=True, null=True)
    item = models.ForeignKey(Items, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procedure_detail'


class ProcedureMaster(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'procedure_master'


class ProcedureWiseBudgets(models.Model):
    procedure = models.ForeignKey(Items, models.DO_NOTHING)
    source_name = models.CharField(max_length=255)
    patient_qty = models.IntegerField()
    per_day_patient_qty = models.FloatField()
    service_qty = models.IntegerField()
    per_day_service_qty = models.FloatField()
    amount = models.FloatField()
    per_day_amount = models.FloatField()
    fiscalyear = models.CharField(max_length=255)
    month = models.CharField(max_length=255)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='updated_by', related_name='procedurewisebudgets_updated_by_set', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procedure_wise_budgets'


class ProgramYears(models.Model):
    program_year = models.CharField(max_length=255)
    is_active = models.IntegerField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'program_years'


class Programs(models.Model):
    program = models.CharField(max_length=255)
    is_active = models.IntegerField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programs'


class Projectsetups(models.Model):
    slug = models.CharField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    value = models.TextField()
    path = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'projectsetups'


class ProvinceDistricts(models.Model):
    district = models.CharField(max_length=255)
    province_id = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    imu_district_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'province_districts'


class Provinces(models.Model):
    province = models.CharField(max_length=255)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provinces'


class PurchaseOrderCatalogues(models.Model):
    purchase_order_catalogue_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    purchase_order_id = models.PositiveIntegerField()
    catalogue_id = models.PositiveIntegerField()
    purchase_order_catalogue_quantity = models.IntegerField()
    rate = models.FloatField()
    purchase_order_catalogue_status = models.IntegerField()
    purchase_order_catalogue_remarks = models.TextField(blank=True, null=True)
    purchase_order_catalogue_created_by = models.PositiveIntegerField()
    purchase_order_catalogue_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    manufacture_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_order_catalogues'


class PurchaseOrders(models.Model):
    purchase_order_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    user_role_id = models.PositiveIntegerField()
    supplier_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    requisition_id = models.IntegerField()
    purchase_order_no = models.CharField(max_length=191)
    purchase_order_status = models.IntegerField()
    user_role_name = models.CharField(max_length=191)
    purchase_order_delivery_site = models.CharField(max_length=191)
    purchase_order_delivery_date = models.DateTimeField()
    purchase_order_date = models.DateField()
    purchase_order_approved_by = models.CharField(max_length=191)
    purchase_order_prepared_by = models.CharField(max_length=191)
    purchase_order_remarks = models.TextField(blank=True, null=True)
    purchase_order_created_by = models.PositiveIntegerField()
    purchase_order_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_orders'


class PurchaseReturns(models.Model):
    purchase_return_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    pr_opening_stocks_id = models.PositiveIntegerField()
    pr_closing_stocks_id = models.PositiveIntegerField()
    master_purchases_return_id = models.PositiveIntegerField()
    stock_purchases_id = models.PositiveIntegerField()
    catalogue_type_id = models.PositiveIntegerField()
    catalogue_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    batch = models.CharField(max_length=191)
    return_quantity = models.IntegerField()
    expiry_date = models.CharField(max_length=191)
    cost_price = models.FloatField()
    selling_price = models.FloatField()
    profit_percent = models.FloatField()
    purchase_return_status = models.IntegerField()
    cancel_status = models.IntegerField()
    is_courier_charge = models.IntegerField()
    courier_charge = models.FloatField()
    purchase_return_remarks = models.TextField(blank=True, null=True)
    purchase_return_created_by = models.PositiveIntegerField()
    purchase_return_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    reverted_date = models.CharField(max_length=191, blank=True, null=True)
    p_bonus_return_quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'purchase_returns'


class QmsCounters(models.Model):
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    module = models.CharField(max_length=191)
    counter_name = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=8)
    current_token = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qms_counters'


class Rate(models.Model):
    currency_id = models.IntegerField()
    code = models.CharField(max_length=255)
    rate = models.CharField(max_length=255)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rate'


class RateGroups(models.Model):
    title = models.CharField(max_length=255)
    order = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    is_covid = models.IntegerField(blank=True, null=True)
    is_critical = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rate_groups'


class RateTypeRooms(models.Model):
    room_type = models.ForeignKey('RoomTypes', models.DO_NOTHING)
    rate_type = models.ForeignKey(PatientCategories, models.DO_NOTHING)
    amount = models.FloatField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='updated_by', related_name='ratetyperooms_updated_by_set', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    rate_group_id = models.PositiveIntegerField()
    department_id = models.PositiveIntegerField(blank=True, null=True)
    item_id = models.PositiveIntegerField(blank=True, null=True)
    is_scheduled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rate_type_rooms'


class RateTypeRoomsSchedules(models.Model):
    rate_type_rooms = models.ForeignKey(RateTypeRooms, models.DO_NOTHING)
    schedule_amount = models.FloatField()
    schedule_from = models.DateField(blank=True, null=True)
    schedule_to = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rate_type_rooms_schedules'


class ReceiptMasters(models.Model):
    receipt_no = models.CharField(max_length=255)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'receipt_masters'


class ReferredBy(models.Model):
    patient_id = models.IntegerField()
    referred_by = models.CharField(max_length=191, blank=True, null=True)
    name = models.CharField(max_length=191, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    ipd_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'referred_by'


class RefundDetails(models.Model):
    master_refund = models.ForeignKey(MasterRefunds, models.DO_NOTHING, blank=True, null=True)
    bill_detail = models.OneToOneField(BillDetails, models.DO_NOTHING, blank=True, null=True)
    created_by = models.PositiveIntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    branch = models.PositiveIntegerField()
    amount = models.FloatField(blank=True, null=True)
    created_at_date = models.DateField(blank=True, null=True)
    deduction_percent = models.FloatField()
    deduction_status = models.IntegerField()
    is_package = models.IntegerField()
    package_bill_detail_id = models.PositiveIntegerField()
    quantity = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'refund_details'


class Relationship(models.Model):
    relation = models.CharField(max_length=255)
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'relationship'


class ReorderEmailLogs(models.Model):
    reorder_email_id = models.IntegerField(blank=True, null=True)
    stock_purchases_id = models.IntegerField(blank=True, null=True)
    stock_purchases_no = models.CharField(max_length=191, blank=True, null=True)
    stock_issue_id = models.IntegerField(blank=True, null=True)
    stock_issue_no = models.CharField(max_length=191, blank=True, null=True)
    catalogue_id = models.IntegerField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reorder_email_logs'


class ReorderEmails(models.Model):
    email = models.CharField(max_length=191, blank=True, null=True)
    name = models.CharField(max_length=191, blank=True, null=True)
    status = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reorder_emails'


class ReportComment(models.Model):
    description = models.TextField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    sample_collection_no = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    branch = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'report_comment'


class ReportDispatch(models.Model):
    s_master_bill_id = models.IntegerField()
    master_bill_id = models.IntegerField()
    patient_id = models.IntegerField()
    bill_no = models.CharField(max_length=255)
    status = models.IntegerField()
    report_data = models.TextField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_dispatch'


class ReportFooter(models.Model):
    test = models.ForeignKey('Tests', models.DO_NOTHING)
    department = models.ForeignKey(Departments, models.DO_NOTHING)
    flag_status = models.IntegerField()
    active = models.CharField(max_length=1)
    description = models.TextField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    base64 = models.TextField(blank=True, null=True)
    parameter_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_footer'


class ReportSignature(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    alignment = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    base64 = models.TextField()
    active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField()
    company_id = models.IntegerField(blank=True, null=True)
    period_id = models.IntegerField(blank=True, null=True)
    not_applicable_ds = models.IntegerField()
    not_applicable_opd = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'report_signature'


class ReportTypes(models.Model):
    type_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_types'


class RequestCallback(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    doctor_id = models.IntegerField()
    department_id = models.IntegerField()
    date = models.DateField()
    followup_status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'request_callback'


class RequisitionDetail(models.Model):
    branch_id = models.PositiveIntegerField()
    requisition_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    to_store_id = models.PositiveIntegerField()
    catalogue_id = models.PositiveIntegerField()
    quantity = models.IntegerField()
    status = models.IntegerField()
    reorder_level = models.IntegerField(blank=True, null=True)
    pacs_size = models.IntegerField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requisition_detail'


class Requisitions(models.Model):
    branch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    to_store_id = models.PositiveIntegerField()
    requisition_no = models.CharField(max_length=191)
    requisition_date = models.DateField()
    requester = models.CharField(max_length=191)
    status = models.IntegerField()
    remarks = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requisitions'


class RespiratorySystems(models.Model):
    visit_id = models.IntegerField()
    medicaldetails_id = models.IntegerField()
    patient_id = models.IntegerField()
    respiratory_rate = models.IntegerField(blank=True, null=True)
    breath_sound = models.TextField(blank=True, null=True)
    added_sound = models.IntegerField()
    added_sound_remark = models.TextField(blank=True, null=True)
    xray_finding = models.TextField(blank=True, null=True)
    spiro_findings = models.TextField(blank=True, null=True)
    others = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    ipd_id = models.IntegerField()
    er_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'respiratory_systems'


class ResultEntries(models.Model):
    sample_code = models.CharField(max_length=255)
    samplecollection_id = models.PositiveIntegerField()
    patient = models.ForeignKey(Patients, models.DO_NOTHING, blank=True, null=True)
    test = models.ForeignKey('Tests', models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(Departments, models.DO_NOTHING, blank=True, null=True)
    parameter = models.ForeignKey(Parameters, models.DO_NOTHING, blank=True, null=True)
    is_panel = models.IntegerField()
    panel_id = models.PositiveIntegerField(blank=True, null=True)
    title = models.IntegerField()
    value = models.CharField(max_length=255, blank=True, null=True)
    machine_value = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    verified_by = models.IntegerField(blank=True, null=True)
    verified_at = models.DateTimeField(blank=True, null=True)
    verify = models.IntegerField()
    provision_verified_by = models.IntegerField()
    provision_verified_at = models.DateTimeField()
    status = models.FloatField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    old_status = models.IntegerField()
    order = models.IntegerField()
    in_pat_id = models.IntegerField()
    flag = models.CharField(max_length=1, blank=True, null=True)
    machine_entry_status = models.IntegerField()
    ref_min = models.CharField(max_length=255, blank=True, null=True)
    ref_max = models.CharField(max_length=255, blank=True, null=True)
    q_range = models.TextField(blank=True, null=True)
    branch = models.PositiveIntegerField()
    unit_id = models.IntegerField(blank=True, null=True)
    unit_name = models.CharField(max_length=255, blank=True, null=True)
    result_head = models.CharField(max_length=255, blank=True, null=True)
    test_method = models.PositiveIntegerField(blank=True, null=True)
    old_value = models.CharField(max_length=255, blank=True, null=True)
    flag_status = models.CharField(max_length=255, blank=True, null=True)
    quant_result = models.CharField(max_length=255, blank=True, null=True)
    ratio = models.CharField(max_length=255, blank=True, null=True)
    emergency_pat_id = models.PositiveIntegerField(blank=True, null=True)
    is_image = models.IntegerField()
    organism_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'result_entries'
        unique_together = (('sample_code', 'samplecollection_id', 'patient', 'test', 'parameter', 'old_status'),)


class ResultEntryType2(models.Model):
    sample_code = models.CharField(max_length=255)
    sample_collection_id = models.IntegerField()
    patient_id = models.IntegerField()
    test_id = models.IntegerField()
    template_id = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=255)
    department_id = models.CharField(max_length=255)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    verify = models.IntegerField()
    provision_verified_by = models.IntegerField()
    provision_verified_at = models.DateTimeField()
    verified_by = models.IntegerField(blank=True, null=True)
    verified_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    in_pat_id = models.IntegerField()
    branch = models.PositiveIntegerField()
    ref_no = models.CharField(max_length=255)
    sample_source = models.CharField(max_length=255)
    report_heading = models.CharField(max_length=255, blank=True, null=True)
    emergency_pat_id = models.IntegerField()
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'result_entry_type2_'


class ResultEntryType3(models.Model):
    sample_code = models.CharField(max_length=255)
    sample_collection_id = models.IntegerField()
    patient_id = models.IntegerField()
    test_id = models.IntegerField()
    template_id = models.IntegerField()
    ref_no = models.CharField(max_length=255)
    art_site = models.CharField(max_length=255)
    specimen_id = models.IntegerField()
    pcr = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    hiv_load_method_used = models.CharField(max_length=255, blank=True, null=True)
    date_of_analysis = models.DateField(blank=True, null=True)
    anti_hiv_result = models.IntegerField(blank=True, null=True)
    risk = models.IntegerField(blank=True, null=True)
    other_risk = models.TextField(blank=True, null=True)
    cause_of_investigation = models.IntegerField(blank=True, null=True)
    other_cause_of_investigation = models.TextField(blank=True, null=True)
    comment_clinical_history = models.TextField(blank=True, null=True)
    eid_method_used = models.IntegerField(blank=True, null=True)
    other_eid_method_used_comment = models.TextField(blank=True, null=True)
    test_result = models.IntegerField(blank=True, null=True)
    test_result_optional = models.IntegerField(blank=True, null=True)
    comment_test_result = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    verify = models.IntegerField()
    verified_by = models.IntegerField(blank=True, null=True)
    verified_at = models.DateTimeField(blank=True, null=True)
    provision_verified_by = models.IntegerField(blank=True, null=True)
    provision_verified_at = models.DateTimeField(blank=True, null=True)
    department_id = models.IntegerField()
    nic_sentinel_site = models.CharField(max_length=255, blank=True, null=True)
    nic_no = models.CharField(max_length=255, blank=True, null=True)
    nic_fever = models.IntegerField(blank=True, null=True)
    nic_fever_history = models.CharField(max_length=255, blank=True, null=True)
    nic_measured_temp = models.FloatField(blank=True, null=True)
    nic_cough = models.IntegerField(blank=True, null=True)
    nic_sore_throat = models.IntegerField(blank=True, null=True)
    nic_breathing_difficulty = models.IntegerField(blank=True, null=True)
    nic_clinical_symptoms_others = models.CharField(max_length=255, blank=True, null=True)
    nic_date_of_symptoms = models.CharField(max_length=255, blank=True, null=True)
    nic_travel_outside_nepal = models.IntegerField(blank=True, null=True)
    nic_place_name = models.CharField(max_length=255, blank=True, null=True)
    nic_choronic_resporatory_disease = models.IntegerField(blank=True, null=True)
    nic_asthma = models.IntegerField(blank=True, null=True)
    nic_diabetes = models.IntegerField(blank=True, null=True)
    nic_haematology_disease = models.IntegerField(blank=True, null=True)
    nic_chronic_cardiac_diseases = models.IntegerField(blank=True, null=True)
    nic_immunodeficiency_hiv = models.IntegerField(blank=True, null=True)
    nic_neuromuscular_disease = models.IntegerField(blank=True, null=True)
    nic_other_comorbidity = models.CharField(max_length=255, blank=True, null=True)
    nic_oxygen_therapy = models.IntegerField()
    nic_admission_to_icu = models.IntegerField()
    nic_intubation = models.IntegerField()
    nic_hs_others = models.IntegerField()
    nic_hs_other_detail = models.CharField(max_length=255, blank=True, null=True)
    nic_specimen_id = models.IntegerField(blank=True, null=True)
    nic_specimen_name = models.CharField(max_length=255, blank=True, null=True)
    nic_specimen_collection_date = models.CharField(max_length=255, blank=True, null=True)
    nic_test_result = models.IntegerField()
    nic_other_detail_test_result = models.IntegerField(blank=True, null=True)
    nic_discharged = models.IntegerField()
    nic_discharge_date = models.CharField(max_length=255, blank=True, null=True)
    nic_died = models.IntegerField()
    nic_date_of_death = models.CharField(max_length=255, blank=True, null=True)
    nic_mfd_by = models.CharField(max_length=255, blank=True, null=True)
    nic_lot_no = models.CharField(max_length=255, blank=True, null=True)
    nic_influenza_a = models.CharField(max_length=255, blank=True, null=True)
    nic_influenza_b = models.CharField(max_length=255, blank=True, null=True)
    nic_influenza_a_h1 = models.CharField(max_length=255, blank=True, null=True)
    nic_influenza_a_h3 = models.CharField(max_length=255, blank=True, null=True)
    nic_influenza_a_pdm09 = models.CharField(max_length=255, blank=True, null=True)
    nic_influenza_a_h5a = models.CharField(max_length=255, blank=True, null=True)
    nic_influenza_a_h5b = models.CharField(max_length=255, blank=True, null=True)
    nic_influenza_a_h7n9 = models.CharField(max_length=255, blank=True, null=True)
    nic_rapid_diagnostic_test = models.CharField(max_length=255, blank=True, null=True)
    nic_sub_type_test_date = models.CharField(max_length=255, blank=True, null=True)
    nic_ct_value = models.CharField(max_length=255, blank=True, null=True)
    nic_ct_value_sub_type = models.CharField(max_length=255, blank=True, null=True)
    revision_status = models.IntegerField()
    revised_by = models.IntegerField(blank=True, null=True)
    revised_at = models.CharField(max_length=255, blank=True, null=True)
    nic_week = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'result_entry_type3_'


class RevenueCenter(models.Model):
    branch_id = models.IntegerField()
    revenue_center = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    website = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    slogan = models.CharField(max_length=255, blank=True, null=True)
    pan_no = models.CharField(max_length=255, blank=True, null=True)
    vat_no = models.CharField(max_length=255, blank=True, null=True)
    short_name = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'revenue_center'


class RevenueWiseBudgets(models.Model):
    source_code = models.CharField(max_length=255)
    source_name = models.CharField(max_length=255)
    patient_qty = models.IntegerField()
    per_day_patient_qty = models.FloatField()
    service_qty = models.IntegerField()
    per_day_service_qty = models.FloatField()
    amount = models.FloatField()
    per_day_amount = models.FloatField()
    fiscalyear = models.IntegerField()
    month = models.IntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'revenue_wise_budgets'


class RevertLogs(models.Model):
    revert_log_id = models.AutoField(primary_key=True)
    revert_no = models.CharField(max_length=191)
    master_stock_issues_id = models.PositiveIntegerField()
    catalogue_name = models.CharField(max_length=191)
    catalogue_id = models.PositiveIntegerField()
    expiry_date = models.CharField(max_length=191)
    batch = models.CharField(max_length=191)
    catalogue_type_name = models.CharField(max_length=191)
    catalogue_type_id = models.PositiveIntegerField()
    revert_store_id = models.PositiveIntegerField()
    revert_store_name = models.CharField(max_length=191)
    revert_from_store_id = models.PositiveIntegerField()
    revert_from_store_name = models.CharField(max_length=191)
    stock_issue_id = models.PositiveIntegerField()
    stock_issue_no = models.CharField(max_length=191)
    stock_purchases_id = models.PositiveIntegerField()
    stock_purchases_no = models.CharField(max_length=191)
    stock_issues_revert_remarks = models.CharField(max_length=191, blank=True, null=True)
    revert_quantity = models.CharField(max_length=191)
    revert_by = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'revert_logs'


class RoleUser(models.Model):
    user_id = models.PositiveIntegerField(primary_key=True)  # The composite primary key (user_id, role_id) found, that is not supported. The first column is selected.
    role = models.ForeignKey('Roles', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'role_user'
        unique_together = (('user_id', 'role'),)


class Roles(models.Model):
    name = models.CharField(unique=True, max_length=255)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='updated_by', related_name='roles_updated_by_set', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    report_access_days = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'roles'


class RoomTypes(models.Model):
    ward = models.CharField(max_length=255)
    room_type = models.CharField(max_length=255)
    rate = models.FloatField()
    tax_amount = models.FloatField()
    total_amount = models.FloatField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    ward_id = models.IntegerField()
    status = models.IntegerField()
    remarks = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    branch = models.PositiveIntegerField()
    rate_group_id = models.IntegerField()
    department_type_id = models.IntegerField(blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True)
    is_emergency = models.IntegerField()
    is_dialysis = models.IntegerField()
    alos_standard = models.PositiveIntegerField(blank=True, null=True)
    alos_status = models.IntegerField()
    end_date = models.DateField(blank=True, null=True)
    insurance_shortname = models.CharField(max_length=255, blank=True, null=True)
    is_covid = models.IntegerField()
    is_critical = models.IntegerField()
    is_ot_room = models.CharField(max_length=2)
    show_in_mis_reports = models.IntegerField()
    start_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room_types'


class RunningNumber(models.Model):
    sc_id = models.IntegerField()
    department_id = models.IntegerField()
    running_no = models.CharField(max_length=255)
    created_by = models.IntegerField()
    updated_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'running_number'


class SBilldetails(models.Model):
    in_pat_id = models.IntegerField()
    cancel_status = models.CharField(max_length=1)
    patient_id = models.PositiveIntegerField(blank=True, null=True)
    emergency_pat_id = models.IntegerField()
    dialysis_pat_id = models.IntegerField()
    s_master_bill_id = models.PositiveIntegerField(blank=True, null=True)
    item_id = models.PositiveIntegerField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    discount_percentage = models.PositiveIntegerField()
    discount = models.FloatField(blank=True, null=True)
    taxable_amt = models.FloatField(blank=True, null=True)
    tax = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    department_id = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField()
    remarks = models.CharField(max_length=255, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    bill_type = models.IntegerField()
    branch = models.PositiveIntegerField()
    category_type = models.PositiveIntegerField()
    status = models.IntegerField()
    master_bill_id = models.IntegerField()
    surgery_discount_flag = models.IntegerField()
    anesthesia_discount_flag = models.IntegerField()
    doctor_id = models.IntegerField(blank=True, null=True)
    group_item_id = models.IntegerField()
    group_item_name = models.CharField(max_length=255, blank=True, null=True)
    ipd_bed_details_id = models.PositiveIntegerField()
    free_pack_detail_id = models.PositiveIntegerField(blank=True, null=True, db_comment='s_billdetail_id of package from where it was free')
    is_pharmacy_item = models.IntegerField(blank=True, null=True)
    package_date_from = models.DateTimeField(blank=True, null=True)
    package_date_to = models.DateTimeField(blank=True, null=True)
    service_charge_amount = models.FloatField(blank=True, null=True)
    free_qty = models.IntegerField()
    additional_consultant = models.PositiveIntegerField()
    consultant_incharge = models.PositiveIntegerField()
    created_at_date = models.DateField(blank=True, null=True)
    dialysis_bill_id = models.PositiveIntegerField()
    doctor_discount = models.FloatField()
    doctor_percentage = models.FloatField()
    doctype = models.CharField(max_length=100, blank=True, null=True)
    emergency_bill_id = models.PositiveIntegerField()
    emergency_charge_amount = models.FloatField()
    has_emergency_charge = models.IntegerField()
    hospital_discount = models.FloatField()
    hospital_percentage = models.FloatField()
    inv_billed_status = models.IntegerField()
    inv_service_bill_ref_id = models.IntegerField(blank=True, null=True)
    is_dialysis_transfered = models.IntegerField()
    is_emergency_transfered = models.IntegerField()
    is_inventory_item = models.IntegerField(blank=True, null=True)
    is_medication = models.IntegerField()
    is_service_charge = models.IntegerField()
    is_transfer_bed = models.IntegerField()
    labno = models.CharField(max_length=100, blank=True, null=True)
    package_id = models.PositiveIntegerField(blank=True, null=True)
    partner_id = models.IntegerField(blank=True, null=True)
    patno = models.CharField(max_length=100, blank=True, null=True)
    performing_consultant = models.PositiveIntegerField()
    prev_bill_id = models.PositiveIntegerField()
    rate_group = models.CharField(max_length=100, blank=True, null=True)
    refer_by_consultant = models.PositiveIntegerField()
    room_type_id = models.PositiveIntegerField(blank=True, null=True)
    service_charge_percent = models.PositiveIntegerField()
    service_refer_by_consultant = models.PositiveIntegerField()
    sno = models.IntegerField(blank=True, null=True)
    surgery_booking_id = models.PositiveIntegerField()
    surgery_item_type = models.CharField(max_length=255, blank=True, null=True)
    surgerycode = models.CharField(max_length=100, blank=True, null=True)
    item_name = models.CharField(max_length=255)
    actual_created_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    ssf_adjustment_remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_billdetails'


class SMasterbills(models.Model):
    in_pat_id = models.IntegerField()
    bill_no = models.CharField(unique=True, max_length=255, blank=True, null=True)
    patient_id = models.PositiveIntegerField(blank=True, null=True)
    emergency_pat_id = models.IntegerField()
    dialysis_pat_id = models.IntegerField()
    cancel_status = models.IntegerField()
    pan = models.CharField(max_length=255, blank=True, null=True)
    print_count = models.IntegerField()
    tender_amt = models.IntegerField()
    amount = models.FloatField()
    discount = models.FloatField()
    taxable_amt = models.FloatField()
    tax = models.FloatField()
    total = models.FloatField()
    consultant = models.PositiveIntegerField()
    discount_group_id = models.PositiveIntegerField()
    discount_group_percent_id = models.PositiveIntegerField(blank=True, null=True)
    discount_type_percent = models.PositiveIntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at_nepali_date = models.CharField(max_length=10)
    ref_hospital = models.CharField(max_length=255)
    master_bill_id = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    ref_hospital_id = models.IntegerField()
    branch = models.PositiveIntegerField()
    category_type = models.PositiveIntegerField()
    lock_status = models.IntegerField()
    is_pharmacy_bill = models.CharField(max_length=255, blank=True, null=True)
    pharmacy_bill_no = models.CharField(max_length=255, blank=True, null=True)
    ref_consultant = models.IntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    cashcredit = models.CharField(max_length=100, blank=True, null=True)
    doctor_discount = models.FloatField()
    hospital_discount = models.FloatField()
    ims_location = models.PositiveIntegerField()
    norv_bill_no = models.CharField(max_length=100, blank=True, null=True)
    partner_id = models.IntegerField(blank=True, null=True)
    patno = models.CharField(max_length=100, blank=True, null=True)
    site_id = models.IntegerField(blank=True, null=True)
    transaction_date = models.DateTimeField(blank=True, null=True)
    actual_created_at = models.DateTimeField(blank=True, null=True)
    bill_no_sequence = models.IntegerField(blank=True, null=True)
    fiscal_year = models.CharField(max_length=4, blank=True, null=True)
    ssf_no = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_masterbills'


class Salutation(models.Model):
    title_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'salutation'


class SampleCollection(models.Model):
    code = models.CharField(max_length=12, blank=True, null=True)
    running_no = models.IntegerField(blank=True, null=True)
    bill_detail_id = models.PositiveIntegerField(blank=True, null=True)
    ref_bill_no = models.CharField(max_length=255)
    s_bill_detail_id = models.IntegerField()
    test = models.ForeignKey('Tests', models.DO_NOTHING, blank=True, null=True)
    test_note = models.IntegerField()
    department = models.ForeignKey(Departments, models.DO_NOTHING, blank=True, null=True)
    master_bill_id = models.PositiveIntegerField(blank=True, null=True)
    s_masterbill_id = models.IntegerField()
    status = models.FloatField()
    package_id = models.IntegerField()
    is_package = models.IntegerField()
    abnormal_status = models.CharField(max_length=1)
    patient = models.ForeignKey(Patients, models.DO_NOTHING, blank=True, null=True)
    cancel = models.IntegerField()
    uncollect_status = models.IntegerField()
    remark = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    collected_by = models.PositiveIntegerField(blank=True, null=True)
    collected_at = models.DateTimeField(blank=True, null=True)
    received_by = models.PositiveIntegerField(blank=True, null=True)
    received_at = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    in_out = models.IntegerField()
    in_pat_id = models.IntegerField()
    machine_entry_status = models.IntegerField(blank=True, null=True)
    branch = models.PositiveIntegerField()
    load_status = models.IntegerField()
    batch_id = models.PositiveIntegerField()
    form_no = models.CharField(max_length=255, blank=True, null=True)
    reference_collected_date = models.DateField(blank=True, null=True)
    online_purchase = models.IntegerField()
    bill_no = models.CharField(max_length=400, blank=True, null=True)
    panel_id = models.PositiveIntegerField()
    imu_swab_id = models.CharField(max_length=255, blank=True, null=True)
    additional_verify = models.IntegerField()
    email_dispatch_status = models.IntegerField()
    emergency_pat_id = models.IntegerField()
    print_dispatch_status = models.IntegerField()
    service_ref_id = models.IntegerField(blank=True, null=True)
    show_in_discharge_summary = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sample_collection'


class SampleStore(models.Model):
    sample_no = models.CharField(max_length=12)
    freezer_id = models.PositiveIntegerField()
    description = models.TextField()
    status = models.CharField(max_length=1)
    check_in_date = models.DateTimeField()
    check_in_by = models.IntegerField()
    check_out_date = models.DateTimeField(blank=True, null=True)
    check_out_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sample_store'


class ScheduleLists(models.Model):
    pat_id = models.PositiveIntegerField()
    type_id = models.PositiveIntegerField()
    walk_in_status = models.SmallIntegerField()
    schedule_id = models.PositiveIntegerField()
    pat_status = models.IntegerField()
    st_hh = models.IntegerField(db_column='st_HH')  # Field name made lowercase.
    st_mm = models.IntegerField()
    st_hhmm = models.SmallIntegerField(db_column='st_HHmm')  # Field name made lowercase.
    st_fulltime = models.CharField(max_length=255)
    ed_hh = models.IntegerField(db_column='ed_HH')  # Field name made lowercase.
    ed_mm = models.IntegerField()
    ed_hhmm = models.SmallIntegerField(db_column='ed_HHmm')  # Field name made lowercase.
    ed_fulltime = models.CharField(max_length=255)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    dept_id = models.IntegerField()
    doc_id = models.IntegerField()
    visit_status = models.SmallIntegerField()
    initial_pat_type = models.SmallIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    cancel_status = models.IntegerField()
    scheduled_sms = models.IntegerField()
    verified_sms = models.IntegerField()
    appointment_date = models.DateField(blank=True, null=True)
    notify_status = models.IntegerField()
    teleconsultation_status = models.IntegerField()
    video_link = models.CharField(max_length=255, blank=True, null=True)
    app_taken_at = models.CharField(max_length=255, blank=True, null=True)
    online_paid_status = models.IntegerField(db_comment='0 as default, 1 for unpaid online appointment and 2 for paid online appointment')
    viber_number = models.CharField(max_length=255, blank=True, null=True)
    conference_link = models.CharField(max_length=255, blank=True, null=True)
    skype_link = models.CharField(max_length=255, blank=True, null=True)
    is_immigration = models.IntegerField()
    no_of_patients = models.PositiveIntegerField()
    schedule_list_id = models.PositiveIntegerField()
    app_code = models.CharField(max_length=200, blank=True, null=True)
    app_from_date = models.DateTimeField(blank=True, null=True)
    app_to_date = models.DateTimeField(blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    is_waiting = models.IntegerField()
    master_bill_id = models.PositiveIntegerField(blank=True, null=True)
    purposeofvisit = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    app_taken_device = models.CharField(max_length=255)
    country = models.IntegerField()
    emergency_pat_id = models.PositiveIntegerField(blank=True, null=True)
    in_pat_id = models.PositiveIntegerField(blank=True, null=True)
    locker_no = models.IntegerField(blank=True, null=True)
    reported_time = models.DateTimeField(blank=True, null=True)
    screening_status = models.IntegerField()
    serial_no = models.IntegerField(blank=True, null=True)
    uk_patients = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'schedule_lists'


class Schedules(models.Model):
    doc_id = models.IntegerField()
    base_plan_id = models.IntegerField()
    dept_id = models.IntegerField()
    doc_name = models.CharField(max_length=255)
    dept_name = models.CharField(max_length=255)
    day_start_time_hh = models.IntegerField(db_column='day_start_time_HH')  # Field name made lowercase.
    day_start_time_mm = models.IntegerField()
    day_end_time_hh = models.IntegerField(db_column='day_end_time_HH')  # Field name made lowercase.
    day_end_time_mm = models.IntegerField()
    day = models.PositiveIntegerField()
    leave_status = models.IntegerField()
    status = models.IntegerField()
    date = models.DateField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_waiting = models.IntegerField(blank=True, null=True)
    timegap = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedules'


class Sections(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    active = models.IntegerField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sections'


class ServiceApprovals(models.Model):
    service_name = models.CharField(max_length=255)
    service_type = models.CharField(max_length=255)
    charges = models.JSONField()
    speciality_id = models.PositiveIntegerField(blank=True, null=True)
    department_id = models.PositiveIntegerField(blank=True, null=True)
    status = models.IntegerField()
    requested_by = models.IntegerField()
    approved_by = models.IntegerField(blank=True, null=True)
    approved_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_approvals'


class ServiceCategories(models.Model):
    service_category = models.CharField(max_length=255)
    created_by = models.IntegerField()
    updated_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_ot = models.IntegerField(blank=True, null=True)
    ot_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'service_categories'


class ServiceContract(models.Model):
    asset_id = models.IntegerField(blank=True, null=True)
    accession_number = models.CharField(max_length=191, blank=True, null=True)
    start_date = models.CharField(max_length=191, blank=True, null=True)
    end_date = models.CharField(max_length=191, blank=True, null=True)
    is_recurring = models.IntegerField()
    frequency = models.CharField(max_length=191, blank=True, null=True)
    frequency_type = models.CharField(max_length=191, blank=True, null=True)
    is_complete = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    insurance_period = models.CharField(max_length=191, blank=True, null=True)
    insurance_period_type = models.CharField(max_length=191, blank=True, null=True)
    contract_type = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_contract'


class ServiceDetail(models.Model):
    service_master_id = models.PositiveIntegerField()
    department = models.ForeignKey(Departments, models.DO_NOTHING, blank=True, null=True)
    item = models.ForeignKey(Items, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_detail'


class ServiceMaster(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'service_master'


class ServiceWiseBudgets(models.Model):
    item = models.ForeignKey(Items, models.DO_NOTHING)
    source_name = models.CharField(max_length=255)
    patient_qty = models.IntegerField()
    per_day_patient_qty = models.FloatField()
    service_qty = models.IntegerField()
    per_day_service_qty = models.FloatField()
    amount = models.FloatField()
    per_day_amount = models.FloatField()
    fiscalyear = models.IntegerField()
    month = models.IntegerField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='updated_by', related_name='servicewisebudgets_updated_by_set', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    source_code = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'service_wise_budgets'


class Sessions(models.Model):
    id = models.CharField(unique=True, max_length=255)
    user_id = models.IntegerField(blank=True, null=True)
    ip_address = models.CharField(max_length=45, blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    payload = models.TextField()
    last_activity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sessions'


class ShortCodes(models.Model):
    short_codes = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'short_codes'


class SignatureTemplateDetails(models.Model):
    sig_temp_id = models.IntegerField()
    alignment = models.CharField(max_length=1)
    full_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255)
    base64 = models.TextField()
    active = models.CharField(max_length=255)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    display_order = models.IntegerField(blank=True, null=True)
    report_signature_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'signature_template_details'


class SignatureTemplates(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    online_report_status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    branch = models.PositiveIntegerField()
    order_column = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'signature_templates'


class SiteReferralPersons(models.Model):
    site_id = models.PositiveIntegerField()
    full_name = models.CharField(max_length=255)
    mobileno = models.CharField(db_column='mobileNo', max_length=255)  # Field name made lowercase.
    email = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'site_referral_persons'


class Sites(models.Model):
    name = models.CharField(max_length=255)
    status = models.IntegerField()
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    district_id = models.PositiveIntegerField()
    site_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sites'


class Sms(models.Model):
    smstoken = models.CharField(db_column='smsToken', max_length=255)  # Field name made lowercase.
    smsurl = models.CharField(db_column='smsURL', max_length=255)  # Field name made lowercase.
    smssender = models.CharField(db_column='smsSender', max_length=255)  # Field name made lowercase.
    smsvendorid = models.IntegerField(db_column='smsVendorId')  # Field name made lowercase.
    smsvendor = models.CharField(db_column='smsVendor', max_length=255)  # Field name made lowercase.
    smsmessage = models.TextField(db_column='smsMessage')  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    dry_run = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sms'


class SmsLogs(models.Model):
    status_code = models.CharField(max_length=255)
    instance = models.CharField(max_length=255)
    user_id = models.IntegerField()
    pat_id = models.IntegerField()
    pat_name = models.CharField(max_length=255)
    remarks = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    schedule_list_id = models.IntegerField()
    mobile_no = models.CharField(max_length=255, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    pivot_patient_sms_id = models.IntegerField(blank=True, null=True)
    batch_id = models.IntegerField(blank=True, null=True)
    ip_address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_logs'


class SmsVendor(models.Model):
    vendor_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_vendor'


class Source(models.Model):
    source = models.CharField(max_length=191)
    type = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'source'


class Specialities(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    active = models.IntegerField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_online = models.IntegerField(blank=True, null=True)
    show_in_mis_reports = models.IntegerField()
    speciality_group_id = models.IntegerField()
    image = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'specialities'


class SpecialityGroup(models.Model):
    group_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'speciality_group'


class SpecialityHeads(models.Model):
    head_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    department_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'speciality_heads'


class Specimens(models.Model):
    specimen_name = models.CharField(max_length=255)
    tube_color = models.CharField(max_length=255)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'specimens'


class SsfClaimLogs(models.Model):
    ssf_no = models.CharField(max_length=255)
    patient_id = models.IntegerField()
    claim_no = models.CharField(max_length=255)
    claim_uuid = models.CharField(max_length=255)
    patient_uuid = models.CharField(max_length=255)
    request = models.TextField()
    response = models.TextField()
    type = models.CharField(max_length=255)
    success_status = models.CharField(max_length=1)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    ipd_id = models.PositiveIntegerField(blank=True, null=True)
    ssf_claim_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ssf_claim_logs'


class SsfClaims(models.Model):
    patient = models.ForeignKey(Patients, models.DO_NOTHING)
    ipd = models.ForeignKey(InPatients, models.DO_NOTHING, blank=True, null=True)
    master_bill = models.ForeignKey(MasterBills, models.DO_NOTHING, blank=True, null=True)
    s_masterbill = models.ForeignKey(SMasterbills, models.DO_NOTHING, blank=True, null=True)
    pharmacy_master_bill = models.ForeignKey(PPharmacyMasterBills, models.DO_NOTHING, blank=True, null=True)
    claim_no = models.CharField(max_length=255)
    claim_uuid = models.CharField(max_length=255, blank=True, null=True)
    total_amount = models.FloatField()
    ssf_liability_amount = models.FloatField()
    ssf_no = models.CharField(max_length=255)
    patient_uuid = models.CharField(max_length=255)
    is_booked = models.IntegerField()
    status = models.IntegerField(db_comment='0 : default, 1 : Successfully Claimed ,  2 : Successfully booked, 4 : Error while Claiming')
    disease_code_id = models.PositiveIntegerField(blank=True, null=True)
    billable_date = models.DateTimeField()
    nmc_no = models.CharField(max_length=255, blank=True, null=True)
    base64_doc = models.TextField(blank=True, null=True)
    reattachment_status = models.IntegerField()
    claim_submit_msg = models.TextField(blank=True, null=True)
    explanation = models.TextField(blank=True, null=True)
    mark_as_complete = models.IntegerField()
    resubmit_claim = models.IntegerField()
    claim_status = models.CharField(max_length=255, blank=True, null=True)
    confirmed_by = models.PositiveIntegerField(blank=True, null=True)
    scheme_type = models.IntegerField(blank=True, null=True, db_comment='1 : Accident Scheme, 2 : Medical Scheme')
    claim_submitted_date = models.DateTimeField(blank=True, null=True)
    patient_type = models.IntegerField(blank=True, null=True, db_comment='1 : OPD, 2 : IPD')
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ssf_claims'


class SsfPatientDetails(models.Model):
    patient = models.ForeignKey(Patients, models.DO_NOTHING, blank=True, null=True)
    ssf_no = models.CharField(max_length=255)
    ssf_uuid = models.CharField(max_length=255)
    medical_ipd_balance = models.FloatField(blank=True, null=True)
    medical_opd_balance = models.FloatField(blank=True, null=True)
    medical_allowed_money = models.FloatField(blank=True, null=True)
    medical_used_money = models.FloatField(blank=True, null=True)
    medical_inforce = models.IntegerField(blank=True, null=True)
    accident_ipd_balance = models.FloatField(blank=True, null=True)
    accident_opd_balance = models.FloatField(blank=True, null=True)
    accident_allowed_money = models.FloatField(blank=True, null=True)
    accident_used_money = models.FloatField(blank=True, null=True)
    accident_inforce = models.IntegerField(blank=True, null=True)
    img_path = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ssf_patient_details'


class StatusCommunications(models.Model):
    schedule_id = models.PositiveIntegerField()
    schedule_list_id = models.PositiveIntegerField()
    deleted_status = models.SmallIntegerField()
    status = models.IntegerField()
    remarks = models.TextField(blank=True, null=True)
    communication_through = models.IntegerField()
    communication_status = models.SmallIntegerField()
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_latest = models.IntegerField(blank=True, null=True)
    ip_address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'status_communications'


class StockIssues(models.Model):
    stock_issue_id = models.AutoField(primary_key=True)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    master_stock_issues = models.ForeignKey(MasterStockIssues, models.DO_NOTHING)
    stock_issue_no = models.CharField(max_length=191)
    master_stock_purchases = models.ForeignKey(MasterStockPurchases, models.DO_NOTHING)
    stock_purchases = models.ForeignKey('StockPurchases', models.DO_NOTHING)
    stock_purchases_no = models.CharField(max_length=191)
    si_opening_stocks_id = models.PositiveIntegerField()
    si_closing_stocks_id = models.PositiveIntegerField()
    catalogue = models.ForeignKey(Catalogues, models.DO_NOTHING)
    catalogue_type = models.ForeignKey(CatalogueTypes, models.DO_NOTHING)
    store = models.ForeignKey('Stores', models.DO_NOTHING)
    received_from_store = models.ForeignKey('Stores', models.DO_NOTHING, db_column='received_from_store', related_name='stockissues_received_from_store_set')
    batch = models.CharField(max_length=191)
    i_quantity = models.IntegerField()
    i_stock_quantity = models.IntegerField()
    i_revert_quantity = models.PositiveIntegerField()
    expiry_date = models.CharField(max_length=191)
    cost_price = models.FloatField()
    selling_price = models.FloatField()
    profit_percent = models.FloatField()
    stock_issue_status = models.IntegerField()
    stock_issue_created_by = models.PositiveIntegerField()
    stock_issue_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    batch_flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stock_issues'


class StockPurchases(models.Model):
    stock_purchases_id = models.AutoField(primary_key=True)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    supplier_id = models.PositiveIntegerField(blank=True, null=True)
    manufacture_id = models.IntegerField()
    master_stock_purchases = models.ForeignKey(MasterStockPurchases, models.DO_NOTHING)
    stock_purchases_no = models.CharField(max_length=191, blank=True, null=True)
    purchases_order = models.ForeignKey(PurchaseOrders, models.DO_NOTHING, blank=True, null=True)
    purchases_order_no = models.CharField(max_length=191, blank=True, null=True)
    sp_opening_stocks_id = models.PositiveIntegerField()
    sp_closing_stocks_id = models.PositiveIntegerField()
    catalogue_type = models.ForeignKey(CatalogueTypes, models.DO_NOTHING)
    catalogue = models.ForeignKey(Catalogues, models.DO_NOTHING)
    store = models.ForeignKey('Stores', models.DO_NOTHING)
    batch = models.CharField(max_length=191)
    bonus_quantity = models.PositiveIntegerField()
    p_quantity = models.IntegerField()
    p_stock_quantity = models.IntegerField()
    p_return_quantity = models.PositiveIntegerField()
    expiry_date = models.CharField(max_length=191)
    cp_before_tax = models.FloatField()
    is_courier_charge = models.IntegerField()
    cc_per = models.FloatField()
    cc = models.FloatField()
    discount_per = models.FloatField()
    discount_amount = models.FloatField()
    is_taxable = models.IntegerField()
    taxable_amt = models.FloatField()
    tax_per = models.FloatField()
    tax_amount = models.FloatField()
    cost_price = models.FloatField()
    selling_price = models.FloatField()
    profit_percent = models.FloatField()
    stock_purchases_remarks = models.TextField(blank=True, null=True)
    stock_purchases_status = models.IntegerField()
    purchase_return_status = models.IntegerField()
    stock_purchases_created_by = models.PositiveIntegerField()
    stock_purchases_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    foreign_rate = models.FloatField(blank=True, null=True)
    batch_flag = models.IntegerField()
    p_bonus_return_quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stock_purchases'


class StockReportLogs(models.Model):
    branch_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    data = models.TextField()
    date = models.DateField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_report_logs'


class StockReturns(models.Model):
    stock_return_id = models.AutoField(primary_key=True)
    catalogue_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    received_from_store = models.PositiveIntegerField()
    stock_purchase_id = models.PositiveIntegerField()
    batch = models.CharField(max_length=191)
    r_quantity = models.IntegerField()
    r_stock_quantity = models.IntegerField()
    expiry_date = models.CharField(max_length=191)
    issue_date = models.CharField(max_length=191)
    purchase_order_no = models.CharField(max_length=191)
    cost_price = models.FloatField()
    selling_price = models.FloatField()
    profit_percent = models.IntegerField()
    stock_return_remarks = models.CharField(max_length=191, blank=True, null=True)
    stock_return_created_by = models.PositiveIntegerField()
    stock_return_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_returns'


class StockUpdateLogs(models.Model):
    stock_update_log_id = models.AutoField(primary_key=True)
    branch_id = models.IntegerField()
    table_name = models.CharField(max_length=191)
    old_value = models.TextField()
    new_value = models.TextField()
    stock_update_log_created_by = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_update_logs'


class Stores(models.Model):
    store_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    store_name = models.CharField(max_length=191)
    store_description = models.TextField(blank=True, null=True)
    store_pos_status = models.IntegerField()
    store_main_status = models.IntegerField()
    store_status = models.IntegerField()
    store_created_by = models.PositiveIntegerField()
    store_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    lead_time = models.CharField(max_length=191, blank=True, null=True)
    delivery_day = models.CharField(max_length=191, blank=True, null=True)
    stock_days = models.CharField(max_length=191, blank=True, null=True)
    cost_center_id = models.IntegerField(blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    is_expired_store = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stores'


class SubjectiveTemplates(models.Model):
    test = models.ForeignKey('Tests', models.DO_NOTHING)
    department = models.ForeignKey(Departments, models.DO_NOTHING)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    heading = models.CharField(max_length=255)
    revenue_center = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subjective_templates'


class SugarProfile(models.Model):
    reported_date = models.CharField(max_length=191, blank=True, null=True)
    reported_time = models.CharField(max_length=191, blank=True, null=True)
    sugar_profile = models.CharField(max_length=191)
    value = models.CharField(max_length=191)
    treatment = models.CharField(max_length=191)
    nurse_name = models.CharField(max_length=191)
    patient_id = models.IntegerField()
    in_pat_id = models.IntegerField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    rbs = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sugar_profile'


class SupplierWiseManufactureDiscount(models.Model):
    supplier_id = models.PositiveIntegerField(blank=True, null=True)
    manufacture_id = models.PositiveIntegerField(blank=True, null=True)
    catalogue_id = models.PositiveIntegerField(blank=True, null=True)
    catalogue_type_id = models.PositiveIntegerField(blank=True, null=True)
    bonus_qty = models.PositiveIntegerField(blank=True, null=True)
    discount = models.PositiveIntegerField(blank=True, null=True)
    cost_price = models.FloatField()
    selling_price = models.FloatField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_wise_manufacture_discount'


class Suppliers(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    supplier_name = models.CharField(max_length=191)
    supplier_code = models.CharField(unique=True, max_length=191)
    supplier_address = models.CharField(max_length=191, blank=True, null=True)
    supplier_email = models.CharField(max_length=191, blank=True, null=True)
    supplier_description = models.TextField(blank=True, null=True)
    supplier_pan_vat = models.CharField(max_length=191)
    supplier_contact = models.CharField(max_length=191)
    supplier_status = models.IntegerField()
    supplier_created_by = models.PositiveIntegerField()
    supplier_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    acc_partner_id = models.IntegerField()
    acc_account_id = models.IntegerField()
    account_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suppliers'


class SurgeryBooking(models.Model):
    patient = models.ForeignKey(Patients, models.DO_NOTHING)
    in_patient = models.ForeignKey(InPatients, models.DO_NOTHING)
    opt_in_time = models.DateTimeField()
    opt_out_time = models.DateTimeField()
    anesthesia_start_time = models.DateTimeField()
    anesthesia_end_time = models.DateTimeField()
    ot_bed = models.ForeignKey(Beds, models.DO_NOTHING)
    surgery_type = models.CharField(max_length=255, blank=True, null=True)
    case_type_id = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    branch_id = models.PositiveIntegerField()
    total = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    refund_status = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    cancel_status = models.IntegerField(blank=True, null=True)
    discount = models.FloatField()
    doctor_discount = models.FloatField()
    hospital_discount = models.FloatField()
    ipd_beds = models.PositiveIntegerField()
    ipd_beds_id = models.PositiveIntegerField()
    service_charge = models.FloatField()
    surgery_no = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'surgery_booking'


class SusceptabilityResult(models.Model):
    result_entry_id = models.IntegerField()
    patient = models.ForeignKey(Patients, models.DO_NOTHING, blank=True, null=True)
    sample_collection = models.ForeignKey(SampleCollection, models.DO_NOTHING, blank=True, null=True)
    sample_code = models.CharField(max_length=255)
    test = models.ForeignKey('Tests', models.DO_NOTHING, blank=True, null=True)
    drug = models.ForeignKey(Drugs, models.DO_NOTHING, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    in_pat_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'susceptability_result'


class SusceptibilityResults(models.Model):
    value = models.CharField(max_length=255)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'susceptibility_results'


class SysLogs(models.Model):
    instance = models.CharField(max_length=255)
    remarks = models.TextField()
    branch = models.IntegerField()
    ip_address = models.CharField(max_length=255, blank=True, null=True)
    old_value = models.TextField(blank=True, null=True)
    new_value = models.TextField(blank=True, null=True)
    critical = models.IntegerField()
    access_log = models.IntegerField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    patient_id = models.CharField(max_length=255, blank=True, null=True)
    in_pat_id = models.CharField(max_length=255, blank=True, null=True)
    emergency_pat_id = models.CharField(max_length=255, blank=True, null=True)
    dialysis_pat_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_logs'


class TeamDoctors(models.Model):
    team_doc = models.ForeignKey(Doctors, models.DO_NOTHING, blank=True, null=True)
    doc = models.ForeignKey(Doctors, models.DO_NOTHING, related_name='teamdoctors_doc_set', blank=True, null=True)
    dontsend = models.IntegerField(blank=True, null=True)
    share_percentage = models.FloatField()
    enable_individual_sharing = models.IntegerField()
    send_sms = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'team_doctors'


class TempOTSchedulings(models.Model):
    patient = models.ForeignKey(Patients, models.DO_NOTHING, blank=True, null=True)
    in_pat = models.ForeignKey(InPatients, models.DO_NOTHING, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    mobile_number = models.CharField(max_length=255, blank=True, null=True)
    name_title = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    age_type = models.CharField(max_length=255, blank=True, null=True)
    blood_group = models.CharField(max_length=255, blank=True, null=True)
    dob = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    ot_in_time = models.DateTimeField(blank=True, null=True)
    ot_out_time = models.DateTimeField(blank=True, null=True)
    ot_room = models.CharField(max_length=255, blank=True, null=True)
    surgery = models.CharField(max_length=255, blank=True, null=True)
    surgeon = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    dob_ad = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField()
    surgery_booking_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_o_t_schedulings'


class TempPatients(models.Model):
    mname = models.CharField(max_length=255)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    age = models.IntegerField()
    bloodgroup = models.CharField(db_column='bloodGroup', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phoneno = models.CharField(db_column='phoneNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mobileno = models.CharField(db_column='mobileNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age_type = models.CharField(max_length=1)
    reg_status = models.SmallIntegerField()
    r_patid = models.IntegerField(db_column='r_patId')  # Field name made lowercase.
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    maritalstatus = models.CharField(db_column='maritalStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    opd_date = models.DateField(blank=True, null=True)
    online_status = models.IntegerField()
    district_id = models.IntegerField()
    department_id = models.IntegerField(blank=True, null=True)
    doctor_id = models.IntegerField(blank=True, null=True)
    form_status = models.IntegerField(blank=True, null=True)
    schedule_list_id = models.PositiveIntegerField()
    address = models.CharField(max_length=100, blank=True, null=True)
    hap_id = models.IntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    intake_date = models.DateField(blank=True, null=True)
    name_title = models.IntegerField(blank=True, null=True)
    province_district_id = models.IntegerField()
    municipality_id = models.IntegerField()
    appointment_country = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    is_batch = models.IntegerField(blank=True, null=True)
    is_waiting = models.IntegerField(blank=True, null=True)
    memberid = models.IntegerField(db_column='memberId', blank=True, null=True)  # Field name made lowercase.
    otp_code = models.IntegerField(blank=True, null=True)
    otp_code_expire = models.DateTimeField(blank=True, null=True)
    otp_status = models.IntegerField(blank=True, null=True)
    passport_no = models.CharField(max_length=100, blank=True, null=True)
    province_id = models.IntegerField(blank=True, null=True)
    schedule_id = models.PositiveIntegerField(blank=True, null=True)
    visit_count = models.IntegerField(blank=True, null=True)
    ward = models.PositiveIntegerField(blank=True, null=True)
    uk_address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_patients'


class TempTests(models.Model):
    patient_id = models.PositiveIntegerField()
    ipd_id = models.PositiveIntegerField()
    er_id = models.PositiveIntegerField()
    visit_id = models.PositiveIntegerField()
    created_by = models.PositiveIntegerField()
    test_name = models.CharField(max_length=191)
    temp = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_physiotherapy = models.IntegerField()
    is_procedure = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'temp_tests'


class Templates(models.Model):
    master_template_id = models.IntegerField()
    active = models.IntegerField()
    template_name = models.CharField(max_length=255)
    specimen_id = models.IntegerField()
    pcr = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    hiv_load_method_used = models.CharField(max_length=255, blank=True, null=True)
    comment_test_result = models.TextField()
    test_result_optional = models.IntegerField()
    test_result = models.IntegerField()
    other_eid_method_used_comment = models.TextField()
    eid_method_used = models.IntegerField()
    comment_clinical_history = models.TextField()
    other_cause_of_investigation = models.TextField()
    cause_of_investigation = models.IntegerField()
    other_risk = models.TextField()
    risk = models.IntegerField()
    anti_hiv_result = models.IntegerField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    viral_load_type = models.CharField(max_length=255, blank=True, null=True)
    units = models.CharField(max_length=255, blank=True, null=True)
    nic_sentinel_site = models.CharField(max_length=255, blank=True, null=True)
    nic_no = models.CharField(max_length=255, blank=True, null=True)
    nic_fever = models.IntegerField(blank=True, null=True)
    nic_fever_history = models.CharField(max_length=255, blank=True, null=True)
    nic_measured_temp = models.FloatField(blank=True, null=True)
    nic_cough = models.IntegerField(blank=True, null=True)
    nic_sore_throat = models.IntegerField(blank=True, null=True)
    nic_breathing_difficulty = models.IntegerField(blank=True, null=True)
    nic_clinical_symptoms_others = models.CharField(max_length=255, blank=True, null=True)
    nic_date_of_symptoms = models.CharField(max_length=255, blank=True, null=True)
    nic_travel_outside_nepal = models.IntegerField(blank=True, null=True)
    nic_place_name = models.CharField(max_length=255, blank=True, null=True)
    nic_choronic_resporatory_disease = models.IntegerField(blank=True, null=True)
    nic_asthma = models.IntegerField(blank=True, null=True)
    nic_diabetes = models.IntegerField(blank=True, null=True)
    nic_haematology_disease = models.IntegerField(blank=True, null=True)
    nic_chronic_cardiac_diseases = models.IntegerField(blank=True, null=True)
    nic_immunodeficiency_hiv = models.IntegerField(blank=True, null=True)
    nic_neuromuscular_disease = models.IntegerField(blank=True, null=True)
    nic_other_comorbidity = models.CharField(max_length=255, blank=True, null=True)
    nic_oxygen_therapy = models.IntegerField()
    nic_admission_to_icu = models.IntegerField()
    nic_intubation = models.IntegerField()
    nic_hs_others = models.IntegerField()
    nic_hs_other_detail = models.CharField(max_length=255, blank=True, null=True)
    nic_specimen_id = models.IntegerField(blank=True, null=True)
    nic_specimen_name = models.CharField(max_length=255, blank=True, null=True)
    nic_specimen_collection_date = models.CharField(max_length=255, blank=True, null=True)
    nic_test_result = models.IntegerField()
    nic_other_detail_test_result = models.IntegerField(blank=True, null=True)
    nic_discharged = models.IntegerField()
    nic_discharge_date = models.CharField(max_length=255, blank=True, null=True)
    nic_died = models.IntegerField()
    nic_date_of_death = models.CharField(max_length=255, blank=True, null=True)
    nic_mfd_by = models.CharField(max_length=255, blank=True, null=True)
    nic_lot_no = models.CharField(max_length=255, blank=True, null=True)
    nic_influenza_a = models.CharField(max_length=255, blank=True, null=True)
    nic_influenza_b = models.CharField(max_length=255, blank=True, null=True)
    nic_influenza_a_h1 = models.CharField(max_length=255, blank=True, null=True)
    nic_influenza_a_h3 = models.CharField(max_length=255, blank=True, null=True)
    nic_influenza_a_pdm09 = models.CharField(max_length=255, blank=True, null=True)
    nic_influenza_a_h5a = models.CharField(max_length=255, blank=True, null=True)
    nic_influenza_a_h5b = models.CharField(max_length=255, blank=True, null=True)
    nic_influenza_a_h7n9 = models.CharField(max_length=255, blank=True, null=True)
    nic_rapid_diagnostic_test = models.CharField(max_length=255, blank=True, null=True)
    nic_sub_type_test_date = models.CharField(max_length=255, blank=True, null=True)
    nic_ct_value = models.CharField(max_length=255, blank=True, null=True)
    nic_ct_value_sub_type = models.CharField(max_length=255, blank=True, null=True)
    nic_week = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'templates'


class TemplatewiseCategories(models.Model):
    patient_category_id = models.IntegerField()
    template_id = models.IntegerField()
    currency_id = models.CharField(max_length=255)
    room_type_id = models.IntegerField()
    net_amount = models.FloatField()
    total_tax = models.FloatField()
    total_amount = models.FloatField()
    status = models.IntegerField()
    hospital = models.FloatField()
    hospital_percentage = models.FloatField()
    department = models.FloatField()
    department_percentage = models.FloatField()
    anesthesist = models.FloatField()
    anesthesist_percentage = models.FloatField()
    fund = models.FloatField()
    fund_percentage = models.FloatField()
    depreciation = models.FloatField()
    depreciation_percentage = models.FloatField()
    instrument = models.FloatField()
    instrument_percentage = models.FloatField()
    appliance = models.FloatField()
    appliance_percentage = models.FloatField()
    branch = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    rate_group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'templatewise_categories'


class TestMappings(models.Model):
    department = models.ForeignKey(Departments, models.DO_NOTHING)
    test = models.ForeignKey('Tests', models.DO_NOTHING)
    parameter_id = models.IntegerField()
    device = models.ForeignKey(Devices, models.DO_NOTHING)
    device_test_code = models.CharField(max_length=255)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    round_off = models.CharField(max_length=3, blank=True, null=True)
    specimen = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_mappings'


class TestMethodPivot(models.Model):
    test = models.ForeignKey('Tests', models.DO_NOTHING, blank=True, null=True)
    method = models.ForeignKey('TestMethods', models.DO_NOTHING, blank=True, null=True)
    branch = models.PositiveIntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_method_pivot'


class TestMethods(models.Model):
    test_method = models.CharField(max_length=255)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_methods'


class TestOrderMaster(models.Model):
    customer_group_id = models.PositiveIntegerField()
    customer_type_id = models.PositiveIntegerField()
    status = models.PositiveIntegerField()
    cancel = models.IntegerField()
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    discard_message = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_order_master'


class TestOrderPivot(models.Model):
    test_order_master_id = models.PositiveIntegerField()
    test_id = models.PositiveIntegerField()
    test_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    cancel = models.IntegerField()
    patient_id = models.PositiveIntegerField()
    accept_status = models.PositiveIntegerField()
    discard_message = models.CharField(max_length=255, blank=True, null=True)
    status = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'test_order_pivot'


class TestPanelPivot(models.Model):
    child = models.ForeignKey('Tests', models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey('Tests', models.DO_NOTHING, related_name='testpanelpivot_parent_set', blank=True, null=True)
    display_order = models.PositiveIntegerField(blank=True, null=True)
    work_list = models.IntegerField()
    online_status = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_panel_pivot'


class TestParamsDetails(models.Model):
    test_code = models.CharField(primary_key=True, max_length=8)
    test_name = models.CharField(max_length=40)
    footer_details = models.CharField(max_length=9127)

    class Meta:
        managed = False
        db_table = 'test_params_details'


class TestSettings(models.Model):
    test_name = models.CharField(max_length=32, blank=True, null=True)
    test_id = models.IntegerField(blank=True, null=True)
    parameter_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_settings'


class TestSpecimenPivot(models.Model):
    test = models.ForeignKey('Tests', models.DO_NOTHING, blank=True, null=True)
    specimen = models.ForeignKey(Specimens, models.DO_NOTHING, blank=True, null=True)
    branch = models.PositiveIntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_specimen_pivot'


class Tests(models.Model):
    item = models.ForeignKey(Items, models.DO_NOTHING, blank=True, null=True)
    test_name = models.CharField(max_length=255)
    code = models.CharField(unique=True, max_length=255)
    cpt_code = models.CharField(max_length=255, blank=True, null=True)
    order_column = models.PositiveIntegerField()
    department = models.ForeignKey(Departments, models.DO_NOTHING, blank=True, null=True)
    susceptibility = models.IntegerField()
    panel = models.IntegerField()
    single_page = models.IntegerField()
    is_package = models.IntegerField()
    report_type = models.CharField(max_length=255)
    active = models.IntegerField()
    lab_item = models.IntegerField()
    iso_accredited = models.IntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_glucose_test = models.IntegerField()
    is_corona_test = models.IntegerField()
    panel_head = models.CharField(max_length=255, blank=True, null=True)
    is_package_panel = models.IntegerField()
    is_outsource = models.IntegerField()
    out_preferred_vendor = models.IntegerField(blank=True, null=True)
    out_ref_item_code = models.CharField(max_length=255, blank=True, null=True)
    out_price = models.IntegerField(blank=True, null=True)
    is_ecg = models.IntegerField()
    is_ana = models.IntegerField()
    direct_verify = models.IntegerField()
    enable_additional_verify = models.IntegerField()
    is_online = models.IntegerField(blank=True, null=True)
    modality_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tests'


class TestwiseDrugs(models.Model):
    test = models.ForeignKey(Tests, models.DO_NOTHING, blank=True, null=True)
    drugs = models.ForeignKey(Drugs, models.DO_NOTHING, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testwise_drugs'


class Triage(models.Model):
    triage_number = models.IntegerField()
    triage_colour_code = models.CharField(max_length=255)
    triage_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    text_color_code = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'triage'


class UkImmigrationDetails(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    certificate_no = models.CharField(unique=True, max_length=255, blank=True, null=True)
    patient_id = models.IntegerField(unique=True)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    country = models.CharField(max_length=255)
    city_town = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    accompanying_children_no = models.IntegerField()
    sputum_test = models.IntegerField(blank=True, null=True)
    chest_xray = models.IntegerField(blank=True, null=True)
    no_tb = models.IntegerField()
    family_contact_tb = models.IntegerField()
    pregnant = models.IntegerField()
    age_health_cond = models.IntegerField()
    chest_xray_cond = models.IntegerField()
    referral_letter_cond = models.IntegerField()
    status = models.IntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    approved_by = models.IntegerField(blank=True, null=True)
    visa_category = models.CharField(max_length=255, blank=True, null=True)
    uk_address = models.CharField(max_length=255, blank=True, null=True)
    cert_added_ip = models.CharField(max_length=255, blank=True, null=True)
    saved_by = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uk_immigration_details'


class UnidentifiedIps(models.Model):
    user_id = models.IntegerField()
    ip_address = models.CharField(max_length=255)
    fingerprint = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidentified_ips'


class UnitInventories(models.Model):
    unit_inventory_id = models.AutoField(primary_key=True)
    unit_inventory_name = models.CharField(max_length=191)
    unit_inventory_created_by = models.PositiveIntegerField()
    unit_inventory_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unit_inventories'


class Units(models.Model):
    unit = models.CharField(max_length=255)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'units'


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


class VaccinationHistory(models.Model):
    vaccine_id = models.CharField(max_length=191)
    vaccine_name = models.CharField(max_length=191)
    patient_id = models.IntegerField()
    vaccination_date = models.DateTimeField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    ipd_id = models.IntegerField()
    er_id = models.IntegerField()
    visit_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vaccination_history'


class Vaccinations(models.Model):
    vaccine_name = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vaccinations'


class Vdcs(models.Model):
    vdc = models.CharField(max_length=255)
    district = models.ForeignKey(Districts, models.DO_NOTHING, blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vdcs'


class VendorInventories(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    branch_id = models.PositiveIntegerField()
    vendor_name = models.CharField(max_length=191)
    vendor_country = models.CharField(max_length=191)
    vendor_address = models.CharField(max_length=191, blank=True, null=True)
    vendor_status = models.IntegerField()
    vendor_created_by = models.PositiveIntegerField()
    vendor_updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    compcode = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendor_inventories'


class VisaCategories(models.Model):
    category_name = models.CharField(unique=True, max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visa_categories'


class VisitTypes(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visit_types'


class Visits(models.Model):
    appointment_id = models.IntegerField(blank=True, null=True)
    appointment_no = models.CharField(max_length=191, blank=True, null=True)
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    master_bill_id = models.IntegerField(blank=True, null=True)
    pharmacy_status = models.IntegerField()
    labtest_status = models.IntegerField()
    bill_date = models.DateTimeField(blank=True, null=True)
    visit_start = models.DateTimeField(blank=True, null=True)
    visit_start_by = models.IntegerField(blank=True, null=True)
    visit_end = models.DateTimeField(blank=True, null=True)
    visit_end_by = models.IntegerField(blank=True, null=True)
    cancel = models.IntegerField()
    canceled_by = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField()
    appointment_date = models.DateTimeField()
    is_refunded = models.IntegerField()
    followup_date = models.DateTimeField(blank=True, null=True)
    dept_id = models.IntegerField()
    nepali_date = models.CharField(max_length=10)
    branch = models.PositiveIntegerField()
    opd_count = models.IntegerField()
    old_status = models.IntegerField()
    absent_status = models.IntegerField()
    is_teleconsultation = models.IntegerField()
    hap_id = models.CharField(max_length=255, blank=True, null=True)
    intake_date = models.DateField(blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    feedback_status = models.IntegerField()
    patno = models.CharField(max_length=100, blank=True, null=True)
    bill_detail_id = models.PositiveIntegerField(blank=True, null=True)
    doc_change_remarks = models.TextField(blank=True, null=True)
    emergency_pat_id = models.PositiveIntegerField(blank=True, null=True)
    in_pat_id = models.PositiveIntegerField(blank=True, null=True)
    is_doc_change = models.IntegerField()
    package_bill_detail_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visits'


class Vitals(models.Model):
    visit_id = models.IntegerField()
    patient_id = models.IntegerField()
    temp_f = models.FloatField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    head_cir = models.FloatField(blank=True, null=True)
    waist = models.IntegerField(blank=True, null=True)
    hip = models.IntegerField(blank=True, null=True)
    bp = models.CharField(max_length=191, blank=True, null=True)
    pulse = models.IntegerField(blank=True, null=True)
    respiration = models.IntegerField(blank=True, null=True)
    spo2 = models.IntegerField(blank=True, null=True)
    bmi = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    blood_group = models.CharField(max_length=191, blank=True, null=True)
    whratio = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    fathers_height_cm = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    fathers_height_ft = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    mothers_height_cm = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    mothers_height_ft = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    average_height_cm = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    average_height_ft = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    height_ft = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    weight_kg = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    ipd_id = models.IntegerField()
    vital_date = models.CharField(max_length=255, blank=True, null=True)
    vital_time = models.CharField(max_length=255, blank=True, null=True)
    jccol = models.CharField(max_length=191, blank=True, null=True)
    gc = models.CharField(max_length=191, blank=True, null=True)
    cvs = models.CharField(max_length=191, blank=True, null=True)
    chest = models.CharField(max_length=191, blank=True, null=True)
    cns = models.CharField(max_length=191, blank=True, null=True)
    p_a = models.CharField(max_length=191, blank=True, null=True)
    blood_sugar = models.IntegerField(blank=True, null=True)
    er_id = models.IntegerField()
    severity = models.CharField(max_length=191, blank=True, null=True)
    code_status = models.CharField(max_length=191, blank=True, null=True)
    spo2_method = models.CharField(max_length=191, blank=True, null=True)
    edema = models.CharField(max_length=191, blank=True, null=True)
    icterus = models.CharField(max_length=191, blank=True, null=True)
    bp_left = models.CharField(max_length=191, blank=True, null=True)
    bp_right = models.CharField(max_length=191, blank=True, null=True)
    bsa = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    chest_expiration = models.CharField(max_length=191, blank=True, null=True)
    chest_inspiration = models.CharField(max_length=191, blank=True, null=True)
    creatinine = models.CharField(max_length=191, blank=True, null=True)
    egfr = models.CharField(max_length=191, blank=True, null=True)
    urine_protein = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vitals'


class VoucherSubTypes(models.Model):
    parent_code = models.CharField(max_length=191, blank=True, null=True)
    parent = models.ForeignKey(AccTransactionTypes, models.DO_NOTHING, blank=True, null=True)
    code = models.CharField(max_length=191)
    name = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'voucher_sub_types'


class WardTypes(models.Model):
    ward_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    branch = models.PositiveIntegerField()
    code = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ward_types'


class Wards(models.Model):
    ward = models.CharField(max_length=255)
    vdc = models.ForeignKey(Vdcs, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wards'


class WebhookIntergrations(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    channel = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    webhook_url = models.CharField(max_length=191)
    token = models.CharField(max_length=100)
    created_by = models.ForeignKey(Users, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    updated_by = models.ForeignKey(Users, models.DO_NOTHING, db_column='updated_by', related_name='webhookintergrations_updated_by_set', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'webhook_intergrations'


class WellnessProfile(models.Model):
    profile_name = models.CharField(max_length=255)
    profile_info = models.CharField(max_length=255, blank=True, null=True)
    icon_url = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey(Users, models.DO_NOTHING, db_column='deleted_by', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wellness_profile'


class WellnessProfileParams(models.Model):
    profile_id = models.PositiveIntegerField()
    test_id = models.PositiveIntegerField()
    test_name = models.CharField(max_length=255)
    tube_label = models.CharField(max_length=255, blank=True, null=True)
    info_text = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey(Users, models.DO_NOTHING, db_column='deleted_by', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wellness_profile_params'


class WellnessProfileParamsDetails(models.Model):
    profil_params_id = models.PositiveIntegerField()
    diet_group_id = models.PositiveIntegerField()
    diet_group_name = models.CharField(max_length=255)
    variable_data = models.CharField(max_length=255)
    variable_value = models.CharField(max_length=255, blank=True, null=True)
    flag_type = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey(Users, models.DO_NOTHING, db_column='deleted_by', blank=True, null=True)
    profile_params_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'wellness_profile_params_details'


class WhatsappMessageLogs(models.Model):
    type = models.CharField(max_length=255, blank=True, null=True)
    patient_id = models.PositiveIntegerField(blank=True, null=True)
    doctor_id = models.PositiveIntegerField(blank=True, null=True)
    user_id = models.PositiveIntegerField()
    message_id = models.CharField(max_length=255, blank=True, null=True)
    recipient_no = models.CharField(max_length=255, blank=True, null=True)
    init_sent_at = models.DateTimeField(blank=True, null=True)
    sent_at = models.DateTimeField(blank=True, null=True)
    delivered_at = models.DateTimeField(blank=True, null=True)
    read_at = models.DateTimeField(blank=True, null=True)
    failed_at = models.DateTimeField(blank=True, null=True)
    fail_code_status = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'whatsapp_message_logs'


class Years(models.Model):
    year = models.CharField(max_length=255)
    is_active = models.IntegerField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'years'


class Zones(models.Model):
    zone = models.CharField(max_length=255)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zones'
