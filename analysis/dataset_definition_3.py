from ehrql import create_dataset
from ehrql.tables.core import clinical_events, patients
from ehrql import codelist_from_csv
from codelists import asthma_codelist, hba1c_codelist

# Clinical Events
# Finding patient demographics
# Finding each patient's ethnicity
dataset = create_dataset()

ethnicity_codelist = codelist_from_csv(
    "codelists/nhsd-primary-care-domain-refsets-ethnall_cod.csv",
    column="code",
    category_column="term",
)

dataset.latest_ethnicity_code = (
    clinical_events.where(clinical_events.snomedct_code.is_in(ethnicity_codelist))
    .where(clinical_events.date.is_on_or_before("2023-01-01"))
    .sort_by(clinical_events.date)
    .last_for_patient()
    .snomedct_code
)
dataset.latest_ethnicity_group = dataset.latest_ethnicity_code.to_category(
    ethnicity_codelist
)
dataset.define_population(patients.exists_for_patient())

# Does each patient have an event matching some criteria?
# Does each patient have a clinical event matching a code in a codelist?
dataset = create_dataset()

# asthma_codelist = codelist_from_csv(
#     "codelists/opensafely-asthma-diagnosis-snomed.csv",
#     column="id",
#     category_column="name",
# )

dataset.has_had_asthma_diagnosis = clinical_events.where(
        clinical_events.snomedct_code.is_in(asthma_codelist)
).exists_for_patient()
dataset.define_population(patients.exists_for_patient())

# Does each patient have a clinical event matching a code in a codelist in a time period?
dataset = create_dataset()
dataset.has_recent_asthma_diagnosis = clinical_events.where(
        clinical_events.snomedct_code.is_in(asthma_codelist)
).where(
        clinical_events.date.is_on_or_between("2022-07-01", "2023-01-01")
).exists_for_patient()
dataset.define_population(patients.exists_for_patient())

# What is the first/last event matching some criteria?
# What is the earliest/latest clinical event matching some criteria?
dataset = create_dataset()

dataset.first_asthma_diagnosis_date = clinical_events.where(
        clinical_events.snomedct_code.is_in(asthma_codelist)
).where(
        clinical_events.date.is_on_or_after("2022-07-01")
).sort_by(
        clinical_events.date
).first_for_patient().date

dataset.last_asthma_diagnosis_date = clinical_events.where(
        clinical_events.snomedct_code.is_in(asthma_codelist)
).where(
        clinical_events.date.is_on_or_after("2022-07-01")
).sort_by(
        clinical_events.date
).last_for_patient().date

dataset.define_population(patients.exists_for_patient())

# Getting properties of an event matching some criteria🔗
# What is the code of the first/last clinical event matching some criteria?
dataset = create_dataset()
dataset.configure_dummy_data(population_size=200)

hba1c_events = clinical_events.where(
        clinical_events.snomedct_code.is_in(hba1c_codelist)
).where(
        # Note: filter out NULL numeric values before sorting
        clinical_events.numeric_value.is_not_null()
).where(
        clinical_events.date.is_on_or_after("2022-07-01")
)

earliest_min_hba1c_event = hba1c_events.sort_by(
        clinical_events.numeric_value, clinical_events.date
).first_for_patient()

earliest_max_hba1c_event = hba1c_events.sort_by(
        # Note the leading minus sign to sort numeric_value in reverse order
        -clinical_events.numeric_value, clinical_events.date
).first_for_patient()

latest_min_hba1c_event = hba1c_events.sort_by(
        # Note the leading minus sign to sort numeric_value in reverse order
        -clinical_events.numeric_value, clinical_events.date
).last_for_patient()

latest_max_hba1c_event = hba1c_events.sort_by(
        clinical_events.numeric_value, clinical_events.date
).last_for_patient()

dataset.date_of_first_min_hba1c_observed = earliest_min_hba1c_event.date
dataset.date_of_first_max_hba1c_observed = earliest_max_hba1c_event.date
dataset.date_of_last_min_hba1c_observed = latest_min_hba1c_event.date
dataset.date_of_last_max_hba1c_observed = latest_max_hba1c_event.date

dataset.value_of_first_min_hba1c_observed = earliest_min_hba1c_event.numeric_value
dataset.value_of_first_max_hba1c_observed = earliest_max_hba1c_event.numeric_value
dataset.value_of_last_min_hba1c_observed = latest_min_hba1c_event.numeric_value
dataset.value_of_last_max_hba1c_observed = latest_max_hba1c_event.numeric_value

dataset.define_population(patients.exists_for_patient())

# Getting properties of an event matching some criteria🔗
# What is the code and date of the first/last clinical event matching some criteria?
dataset = create_dataset()
dataset.configure_dummy_data(population_size=200)
first_asthma_diagnosis = clinical_events.where(
        clinical_events.snomedct_code.is_in(asthma_codelist)
).where(
        clinical_events.date.is_on_or_after("2022-07-01")
).sort_by(
        clinical_events.date
).first_for_patient()
dataset.first_asthma_diagnosis_code = first_asthma_diagnosis.snomedct_code
dataset.first_asthma_diagnosis_date = first_asthma_diagnosis.date
dataset.define_population(patients.exists_for_patient())