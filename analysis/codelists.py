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
