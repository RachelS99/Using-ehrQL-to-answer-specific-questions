from ehrql import codelist_from_csv

asthma_codelist = codelist_from_csv(
    "codelists/opensafely-asthma-diagnosis-snomed.csv",
    column="id",
    category_column="name",
)
ethnicity_codelist = codelist_from_csv(
    "codelists/nhsd-primary-care-domain-refsets-ethnall_cod.csv",
    column="code",
    category_column="term",
)
hba1c_codelist = codelist_from_csv(
    "codelists/opensafely-glycated-haemoglobin-hba1c-tests.csv",
    column="code",
    category_column="term",
)
pain_symptoms_codelist = codelist_from_csv(
    "codelists/opensafely-symptoms-pain.csv",
    column="code",
    category_column="term",
)
falls_codelist = codelist_from_csv(
    "codelists/user-RachelS99-falls.csv",
    column="CTV3Code",
    category_column="Description",
)
learning_disability_codelist = codelist_from_csv(
    "codelists/user-RachelS99-learning_disability.csv",
    column="code",
    category_column="term",
)
doac_codes = codelist_from_csv(
    "codelists/opensafely-direct-acting-oral-anticoagulants-doac.csv",
    system="snomed",
    column='id',
    category_column="code",
)
learning_disability_codelist = codelist_from_csv(
    "codelists/nhsd-primary-care-domain-refsets-mildfrail_cod.csv",
    column="code",
    category_column="term",
)
learning_disability_codelist = codelist_from_csv(
    "codelists/nhsd-primary-care-domain-refsets-modfrail_cod.csv",
    column="code",
    category_column="term",
)
learning_disability_codelist = codelist_from_csv(
    "codelists/nhsd-primary-care-domain-refsets-sevfrail_cod.csv",
    column="code",
    category_column="term",
)