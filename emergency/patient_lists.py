"""
Defining OPAL PatientLists
"""
from opal import core
from opal.models import Episode
from obs.models import Observation
from emergency import models

class AllPatientsList(core.patient_lists.PatientList):
    display_name = 'All Patients'

    schema = [
        models.Demographics,
        models.Diagnosis,
        models.Treatment
    ]

    def get_queryset(self):
        return Episode.objects.all()

class PatientsForTriageList(core.patient_lists.TaggedPatientList):
    display_name = 'Patients For Triage'

    tag = 'triage'

    schema = [
        models.Demographics,
        models.Location,
        Observation,
        models.EmergencyDepartmentTriage
    ]
