# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import opal.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opal', '0027_auto_20170114_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allergies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('provisional', models.BooleanField(default=False, verbose_name=b'Suspected?')),
                ('details', models.CharField(max_length=255, blank=True)),
                ('drug_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_emergency_allergies_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('drug_fk', models.ForeignKey(blank=True, to='opal.Drug', null=True)),
                ('patient', models.ForeignKey(to='opal.Patient')),
                ('updated_by', models.ForeignKey(related_name='updated_emergency_allergies_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Demographics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('hospital_number', models.CharField(max_length=255, blank=True)),
                ('nhs_number', models.CharField(max_length=255, null=True, verbose_name=b'NHS Number', blank=True)),
                ('surname', models.CharField(max_length=255, blank=True)),
                ('first_name', models.CharField(max_length=255, blank=True)),
                ('middle_name', models.CharField(max_length=255, null=True, blank=True)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('religion', models.CharField(max_length=255, null=True, blank=True)),
                ('date_of_death', models.DateField(null=True, blank=True)),
                ('post_code', models.CharField(max_length=20, null=True, blank=True)),
                ('gp_practice_code', models.CharField(max_length=20, null=True, verbose_name=b'GP Practice Code', blank=True)),
                ('death_indicator', models.BooleanField(default=False)),
                ('title_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('marital_status_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('sex_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('birth_place_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('ethnicity_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('birth_place_fk', models.ForeignKey(blank=True, to='opal.Destination', null=True)),
                ('created_by', models.ForeignKey(related_name='created_emergency_demographics_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('ethnicity_fk', models.ForeignKey(blank=True, to='opal.Ethnicity', null=True)),
                ('marital_status_fk', models.ForeignKey(blank=True, to='opal.MaritalStatus', null=True)),
                ('patient', models.ForeignKey(to='opal.Patient')),
                ('sex_fk', models.ForeignKey(blank=True, to='opal.Gender', null=True)),
                ('title_fk', models.ForeignKey(blank=True, to='opal.Title', null=True)),
                ('updated_by', models.ForeignKey(related_name='updated_emergency_demographics_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('provisional', models.BooleanField(default=False, verbose_name=b'Provisional?')),
                ('details', models.CharField(max_length=255, blank=True)),
                ('date_of_diagnosis', models.DateField(null=True, blank=True)),
                ('condition_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('condition_fk', models.ForeignKey(blank=True, to='opal.Condition', null=True)),
                ('created_by', models.ForeignKey(related_name='created_emergency_diagnosis_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
                ('updated_by', models.ForeignKey(related_name='updated_emergency_diagnosis_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Investigation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('test', models.CharField(max_length=255)),
                ('date_ordered', models.DateField(null=True, blank=True)),
                ('details', models.CharField(max_length=255, blank=True)),
                ('microscopy', models.CharField(max_length=255, blank=True)),
                ('organism', models.CharField(max_length=255, blank=True)),
                ('sensitive_antibiotics', models.CharField(max_length=255, blank=True)),
                ('resistant_antibiotics', models.CharField(max_length=255, blank=True)),
                ('result', models.CharField(max_length=255, blank=True)),
                ('igm', models.CharField(max_length=20, blank=True)),
                ('igg', models.CharField(max_length=20, blank=True)),
                ('vca_igm', models.CharField(max_length=20, blank=True)),
                ('vca_igg', models.CharField(max_length=20, blank=True)),
                ('ebna_igg', models.CharField(max_length=20, blank=True)),
                ('hbsag', models.CharField(max_length=20, blank=True)),
                ('anti_hbs', models.CharField(max_length=20, blank=True)),
                ('anti_hbcore_igm', models.CharField(max_length=20, blank=True)),
                ('anti_hbcore_igg', models.CharField(max_length=20, blank=True)),
                ('rpr', models.CharField(max_length=20, blank=True)),
                ('tppa', models.CharField(max_length=20, blank=True)),
                ('viral_load', models.CharField(max_length=20, blank=True)),
                ('parasitaemia', models.CharField(max_length=20, blank=True)),
                ('hsv', models.CharField(max_length=20, blank=True)),
                ('vzv', models.CharField(max_length=20, blank=True)),
                ('syphilis', models.CharField(max_length=20, blank=True)),
                ('c_difficile_antigen', models.CharField(max_length=20, blank=True)),
                ('c_difficile_toxin', models.CharField(max_length=20, blank=True)),
                ('species', models.CharField(max_length=20, blank=True)),
                ('hsv_1', models.CharField(max_length=20, blank=True)),
                ('hsv_2', models.CharField(max_length=20, blank=True)),
                ('enterovirus', models.CharField(max_length=20, blank=True)),
                ('cmv', models.CharField(max_length=20, blank=True)),
                ('ebv', models.CharField(max_length=20, blank=True)),
                ('influenza_a', models.CharField(max_length=20, blank=True)),
                ('influenza_b', models.CharField(max_length=20, blank=True)),
                ('parainfluenza', models.CharField(max_length=20, blank=True)),
                ('metapneumovirus', models.CharField(max_length=20, blank=True)),
                ('rsv', models.CharField(max_length=20, blank=True)),
                ('adenovirus', models.CharField(max_length=20, blank=True)),
                ('norovirus', models.CharField(max_length=20, blank=True)),
                ('rotavirus', models.CharField(max_length=20, blank=True)),
                ('giardia', models.CharField(max_length=20, blank=True)),
                ('entamoeba_histolytica', models.CharField(max_length=20, blank=True)),
                ('cryptosporidium', models.CharField(max_length=20, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_emergency_investigation_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
                ('updated_by', models.ForeignKey(related_name='updated_emergency_investigation_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('category', models.CharField(max_length=255, blank=True)),
                ('hospital', models.CharField(max_length=255, blank=True)),
                ('ward', models.CharField(max_length=255, blank=True)),
                ('bed', models.CharField(max_length=255, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_emergency_location_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
                ('updated_by', models.ForeignKey(related_name='updated_emergency_location_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PastMedicalHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('year', models.CharField(max_length=4, blank=True)),
                ('details', models.CharField(max_length=255, blank=True)),
                ('condition_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('condition_fk', models.ForeignKey(blank=True, to='opal.Condition', null=True)),
                ('created_by', models.ForeignKey(related_name='created_emergency_pastmedicalhistory_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
                ('updated_by', models.ForeignKey(related_name='updated_emergency_pastmedicalhistory_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PatientConsultation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('test', models.CharField(max_length=255)),
                ('date_ordered', models.DateField(null=True, blank=True)),
                ('details', models.CharField(max_length=255, blank=True)),
                ('microscopy', models.CharField(max_length=255, blank=True)),
                ('organism', models.CharField(max_length=255, blank=True)),
                ('sensitive_antibiotics', models.CharField(max_length=255, blank=True)),
                ('resistant_antibiotics', models.CharField(max_length=255, blank=True)),
                ('result', models.CharField(max_length=255, blank=True)),
                ('igm', models.CharField(max_length=20, blank=True)),
                ('igg', models.CharField(max_length=20, blank=True)),
                ('vca_igm', models.CharField(max_length=20, blank=True)),
                ('vca_igg', models.CharField(max_length=20, blank=True)),
                ('ebna_igg', models.CharField(max_length=20, blank=True)),
                ('hbsag', models.CharField(max_length=20, blank=True)),
                ('anti_hbs', models.CharField(max_length=20, blank=True)),
                ('anti_hbcore_igm', models.CharField(max_length=20, blank=True)),
                ('anti_hbcore_igg', models.CharField(max_length=20, blank=True)),
                ('rpr', models.CharField(max_length=20, blank=True)),
                ('tppa', models.CharField(max_length=20, blank=True)),
                ('viral_load', models.CharField(max_length=20, blank=True)),
                ('parasitaemia', models.CharField(max_length=20, blank=True)),
                ('hsv', models.CharField(max_length=20, blank=True)),
                ('vzv', models.CharField(max_length=20, blank=True)),
                ('syphilis', models.CharField(max_length=20, blank=True)),
                ('c_difficile_antigen', models.CharField(max_length=20, blank=True)),
                ('c_difficile_toxin', models.CharField(max_length=20, blank=True)),
                ('species', models.CharField(max_length=20, blank=True)),
                ('hsv_1', models.CharField(max_length=20, blank=True)),
                ('hsv_2', models.CharField(max_length=20, blank=True)),
                ('enterovirus', models.CharField(max_length=20, blank=True)),
                ('cmv', models.CharField(max_length=20, blank=True)),
                ('ebv', models.CharField(max_length=20, blank=True)),
                ('influenza_a', models.CharField(max_length=20, blank=True)),
                ('influenza_b', models.CharField(max_length=20, blank=True)),
                ('parainfluenza', models.CharField(max_length=20, blank=True)),
                ('metapneumovirus', models.CharField(max_length=20, blank=True)),
                ('rsv', models.CharField(max_length=20, blank=True)),
                ('adenovirus', models.CharField(max_length=20, blank=True)),
                ('norovirus', models.CharField(max_length=20, blank=True)),
                ('rotavirus', models.CharField(max_length=20, blank=True)),
                ('giardia', models.CharField(max_length=20, blank=True)),
                ('entamoeba_histolytica', models.CharField(max_length=20, blank=True)),
                ('cryptosporidium', models.CharField(max_length=20, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_emergency_patientconsultation_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
                ('updated_by', models.ForeignKey(related_name='updated_emergency_patientconsultation_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SymptomComplex',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('test', models.CharField(max_length=255)),
                ('date_ordered', models.DateField(null=True, blank=True)),
                ('details', models.CharField(max_length=255, blank=True)),
                ('microscopy', models.CharField(max_length=255, blank=True)),
                ('organism', models.CharField(max_length=255, blank=True)),
                ('sensitive_antibiotics', models.CharField(max_length=255, blank=True)),
                ('resistant_antibiotics', models.CharField(max_length=255, blank=True)),
                ('result', models.CharField(max_length=255, blank=True)),
                ('igm', models.CharField(max_length=20, blank=True)),
                ('igg', models.CharField(max_length=20, blank=True)),
                ('vca_igm', models.CharField(max_length=20, blank=True)),
                ('vca_igg', models.CharField(max_length=20, blank=True)),
                ('ebna_igg', models.CharField(max_length=20, blank=True)),
                ('hbsag', models.CharField(max_length=20, blank=True)),
                ('anti_hbs', models.CharField(max_length=20, blank=True)),
                ('anti_hbcore_igm', models.CharField(max_length=20, blank=True)),
                ('anti_hbcore_igg', models.CharField(max_length=20, blank=True)),
                ('rpr', models.CharField(max_length=20, blank=True)),
                ('tppa', models.CharField(max_length=20, blank=True)),
                ('viral_load', models.CharField(max_length=20, blank=True)),
                ('parasitaemia', models.CharField(max_length=20, blank=True)),
                ('hsv', models.CharField(max_length=20, blank=True)),
                ('vzv', models.CharField(max_length=20, blank=True)),
                ('syphilis', models.CharField(max_length=20, blank=True)),
                ('c_difficile_antigen', models.CharField(max_length=20, blank=True)),
                ('c_difficile_toxin', models.CharField(max_length=20, blank=True)),
                ('species', models.CharField(max_length=20, blank=True)),
                ('hsv_1', models.CharField(max_length=20, blank=True)),
                ('hsv_2', models.CharField(max_length=20, blank=True)),
                ('enterovirus', models.CharField(max_length=20, blank=True)),
                ('cmv', models.CharField(max_length=20, blank=True)),
                ('ebv', models.CharField(max_length=20, blank=True)),
                ('influenza_a', models.CharField(max_length=20, blank=True)),
                ('influenza_b', models.CharField(max_length=20, blank=True)),
                ('parainfluenza', models.CharField(max_length=20, blank=True)),
                ('metapneumovirus', models.CharField(max_length=20, blank=True)),
                ('rsv', models.CharField(max_length=20, blank=True)),
                ('adenovirus', models.CharField(max_length=20, blank=True)),
                ('norovirus', models.CharField(max_length=20, blank=True)),
                ('rotavirus', models.CharField(max_length=20, blank=True)),
                ('giardia', models.CharField(max_length=20, blank=True)),
                ('entamoeba_histolytica', models.CharField(max_length=20, blank=True)),
                ('cryptosporidium', models.CharField(max_length=20, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_emergency_symptomcomplex_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
                ('updated_by', models.ForeignKey(related_name='updated_emergency_symptomcomplex_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('dose', models.CharField(max_length=255, blank=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('route_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('drug_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('frequency_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_emergency_treatment_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('drug_fk', models.ForeignKey(blank=True, to='opal.Drug', null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
                ('frequency_fk', models.ForeignKey(blank=True, to='opal.Drugfreq', null=True)),
                ('route_fk', models.ForeignKey(blank=True, to='opal.Drugroute', null=True)),
                ('updated_by', models.ForeignKey(related_name='updated_emergency_treatment_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
    ]
