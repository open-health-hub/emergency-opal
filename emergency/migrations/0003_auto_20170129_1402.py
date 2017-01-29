# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0027_auto_20170114_1302'),
        ('emergency', '0002_auto_20170128_1539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientconsultation',
            old_name='details',
            new_name='initials',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='adenovirus',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='anti_hbcore_igg',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='anti_hbcore_igm',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='anti_hbs',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='c_difficile_antigen',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='c_difficile_toxin',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='cmv',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='cryptosporidium',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='date_ordered',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='ebna_igg',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='ebv',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='entamoeba_histolytica',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='enterovirus',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='giardia',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='hbsag',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='hsv',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='hsv_1',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='hsv_2',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='igg',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='igm',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='influenza_a',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='influenza_b',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='metapneumovirus',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='microscopy',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='norovirus',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='organism',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='parainfluenza',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='parasitaemia',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='resistant_antibiotics',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='result',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='rotavirus',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='rpr',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='rsv',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='sensitive_antibiotics',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='species',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='syphilis',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='test',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='tppa',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='vca_igg',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='vca_igm',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='viral_load',
        ),
        migrations.RemoveField(
            model_name='patientconsultation',
            name='vzv',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='adenovirus',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='anti_hbcore_igg',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='anti_hbcore_igm',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='anti_hbs',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='c_difficile_antigen',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='c_difficile_toxin',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='cmv',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='cryptosporidium',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='date_ordered',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='ebna_igg',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='ebv',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='entamoeba_histolytica',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='enterovirus',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='giardia',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='hbsag',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='hsv',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='hsv_1',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='hsv_2',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='igg',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='igm',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='influenza_a',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='influenza_b',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='metapneumovirus',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='microscopy',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='norovirus',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='organism',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='parainfluenza',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='parasitaemia',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='resistant_antibiotics',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='result',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='rotavirus',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='rpr',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='rsv',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='sensitive_antibiotics',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='species',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='syphilis',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='test',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='tppa',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='vca_igg',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='vca_igm',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='viral_load',
        ),
        migrations.RemoveField(
            model_name='symptomcomplex',
            name='vzv',
        ),
        migrations.AddField(
            model_name='patientconsultation',
            name='discussion',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='patientconsultation',
            name='reason_for_interaction_fk',
            field=models.ForeignKey(blank=True, to='opal.PatientConsultationReasonForInteraction', null=True),
        ),
        migrations.AddField(
            model_name='patientconsultation',
            name='reason_for_interaction_ft',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='patientconsultation',
            name='when',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='symptomcomplex',
            name='duration',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='symptomcomplex',
            name='symptoms',
            field=models.ManyToManyField(related_name='symptoms', to='opal.Symptom', blank=True),
        ),
        migrations.AlterField(
            model_name='symptomcomplex',
            name='details',
            field=models.TextField(null=True, blank=True),
        ),
    ]
