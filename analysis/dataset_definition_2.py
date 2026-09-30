from ehrql import create_dataset
from ehrql.tables.tpp import practice_registrations, patients

# Practice Registrations
# Finding attributes related to each patient's GP practice as of a given date
# Finding each patient's practice's pseudonymised identifier
dataset = create_dataset()
dataset.practice = practice_registrations.for_patient_on("2023-01-01").practice_pseudo_id
dataset.define_population(patients.exists_for_patient())

# Finding each patient's practice's STP
from ehrql import create_dataset
from ehrql.tables.tpp import practice_registrations, patients

dataset = create_dataset()
dataset.stp = practice_registrations.for_patient_on("2023-01-01").practice_stp
dataset.define_population(patients.exists_for_patient())

# Finding each patient's practice's region
from ehrql import create_dataset
from ehrql.tables.tpp import practice_registrations, patients

dataset = create_dataset()
dataset.region = practice_registrations.for_patient_on("2023-01-01").practice_nuts1_region_name
dataset.define_population(patients.exists_for_patient())

# Finding multiple attributes of each patient's practice
from ehrql import create_dataset
from ehrql.tables.tpp import practice_registrations, patients

dataset = create_dataset()
registration = practice_registrations.for_patient_on("2023-01-01")
dataset.practice = registration.practice_pseudo_id
dataset.stp = registration.practice_stp
dataset.region = registration.practice_nuts1_region_name
dataset.define_population(patients.exists_for_patient())

# Excluding patients based on study dates🔗
# The following example ensures that the dataset only includes patients registered at a single practice for the entire duration of the study, plus at least 3 months prior to the study start.
from ehrql import create_dataset, codelist_from_csv, months
from ehrql.tables.tpp import patients, practice_registrations

study_start_date = "2022-01-01"
study_end_date = "2022-12-31"

dataset = create_dataset()

# find registrations that exist for the full study period, and at least 3 months
# prior
registrations = (
    practice_registrations.where(
        practice_registrations.start_date.is_on_or_before(study_start_date - months(3))
    )
    .except_where(
        practice_registrations.end_date.is_on_or_before(study_end_date)
    )
)

dataset.define_population(registrations.exists_for_patient())
