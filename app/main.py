from typing import List, Dict, Any
from app.cafe import Cafe
from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError

def go_to_cafe(friends: List[Dict[str, Any]], cafe: Cafe) -> str:
    result = []
    for friend in friends:
        try:
            message = cafe.visit_cafe(friend)
            result.append(message)
        except NotVaccinatedError:
            result.append(f"{friend['name']} is not vaccinated.")
        except OutdatedVaccineError:
            result.append(f"{friend['name']}'s vaccine is outdated.")
        except NotWearingMaskError:
            result.append(f"{friend['name']} is not wearing a mask.")
    return "\n".join(result)
