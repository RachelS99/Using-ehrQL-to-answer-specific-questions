from ehrql import create_dataset
from ehrql.tables.core import clinical_events, patients
from ehrql import codelist_from_csv
from codelists import asthma_codelist, hba1c_codelist

# Performing arithmetic on numeric values of clinical events🔗
# Finding the mean observed value of clinical events matching some criteria
dataset = create_dataset()
dataset.configure_dummy_data(population_size=200)
dataset.mean_hba1c = clinical_events.where(
        clinical_events.snomedct_code.is_in(hba1c_codelist)
).where(
        clinical_events.date.is_on_or_after("2022-07-01")
).numeric_value.mean_for_patient()
dataset.define_population(patients.exists_for_patient())

# Finding events within a date range
# Finding events within a fixed date range
