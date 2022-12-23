from policyengine_canada.model_api import *


class benefits(Variable):
    value_type = float
    entity = Household
    label = "benfits"
    unit = CAD
    definition_period = YEAR
    adds = [
        "canada_child_benefit",
        "child_disability_benefit",
        "canada_workers_benefit",
        "dental_benefit",
        #        "old_age_security_pension",
    ]
