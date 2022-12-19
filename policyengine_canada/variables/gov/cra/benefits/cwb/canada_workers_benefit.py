from policyengine_canada.model_api import *


class canada_workers_benefit(Variable):
    value_type = float
    entity = Household
    label = "Canada workers benefit"
    definition_period = YEAR

    formula = sum_of_variables(
        ["canada_workers_benefit_base", "canada_workers_benefit_supplement"]
    )
