from ehrql.tables.core import patients

# Patients
# Finding patient demographics
# Finding each patient's sexfrom ehrql import create_dataset, case, when
dataset = create_dataset()
dataset.sex = patients.sex
dataset.define_population(patients.exists_for_patient())

# Finding each patient's date of birth
dataset = create_dataset()
dataset.date_of_birth = patients.date_of_birth
dataset.define_population(patients.exists_for_patient())

# Finding each patient's age
dataset = create_dataset()
dataset.age = patients.age_on("2023-01-01")
dataset.define_population(patients.exists_for_patient())

# Assigning each patient an age band
dataset = create_dataset()
age = patients.age_on("2023-01-01")
dataset.age_band = case(
        when(age < 20).then("0-19"),
        when(age < 40).then("20-39"),
        when(age < 60).then("40-59"),
        when(age < 80).then("60-79"),
        when(age >= 80).then("80+"),
        otherwise="missing",
)
dataset.define_population(patients.exists_for_patient())

# Finding each patient's date of death in their primary care record
dataset = create_dataset()
dataset.configure_dummy_data(population_size=200)
dataset.date_of_death = patients.date_of_death
dataset.define_population(patients.exists_for_patient())


# ONS Deaths
# Finding patient demographics🔗
# Finding each patient's date, underlying_cause_of_death, and first noted additional medical condition noted on the death certificate from ONS records
from ehrql import create_dataset
from ehrql.tables.core import ons_deaths, patients

dataset = create_dataset()
dataset.date_of_death = ons_deaths.date
dataset.underlying_cause_of_death = ons_deaths.underlying_cause_of_death
dataset.cause_of_death = ons_deaths.cause_of_death_01
dataset.define_population(patients.exists_for_patient())

# Finding patients with a particular cause of death
# from ehrql import create_dataset, codelist_from_csv
# from ehrql.tables.core import ons_deaths, patients

# dataset = create_dataset()

# cause_of_death_X_codelist = codelist_from_csv("XXX", column="YYY")

# dataset.died_with_X = ons_deaths.cause_of_death_is_in(cause_of_death_X_codelist)
# dataset.define_population(patients.exists_for_patient())

# Addresses
# Finding attributes related to each patient's address as of a given date
# Finding each patient's IMD rank
from ehrql import create_dataset
from ehrql.tables.tpp import addresses, patients

dataset = create_dataset()
dataset.imd = addresses.for_patient_on("2023-01-01").imd_rounded
dataset.define_population(patients.exists_for_patient())

# Calculating each patient's IMD quintile and/or decile
from ehrql import create_dataset
from ehrql.tables.tpp import addresses, patients

dataset = create_dataset()

patient_address = addresses.for_patient_on("2023-01-01")
dataset.imd_quintile = patient_address.imd_quintile
dataset.imd_decile = patient_address.imd_decile
dataset.define_population(patients.exists_for_patient())

# Finding each patient's rural/urban classification
from ehrql import create_dataset
from ehrql.tables.tpp import addresses, patients

dataset = create_dataset()
dataset.rural_urban = addresses.for_patient_on("2023-01-01").rural_urban_classification
dataset.define_population(patients.exists_for_patient())
# The meaning of this value is as follows:
# 1 - Urban major conurbation
# 2 - Urban minor conurbation
# 3 - Urban city and town
# 4 - Urban city and town in a sparse setting
# 5 - Rural town and fringe
# 6 - Rural town and fringe in a sparse setting
# 7 - Rural village and dispersed
# 8 - Rural village and dispersed in a sparse setting

# Finding each patient's MSOA
from ehrql import create_dataset
from ehrql.tables.tpp import addresses, patients

dataset = create_dataset()
dataset.msoa_code = addresses.for_patient_on("2023-01-01").msoa_code
dataset.define_population(patients.exists_for_patient())

# Finding multiple attributes of each patient's address
from ehrql import create_dataset
from ehrql.tables.tpp import addresses, patients

dataset = create_dataset()
address = addresses.for_patient_on("2023-01-01")
dataset.imd_rounded = address.imd_rounded
dataset.rural_urban_classification = address.rural_urban_classification
dataset.msoa_code = address.msoa_code
dataset.define_population(patients.exists_for_patient())
