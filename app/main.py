from app.cafe import Cafe
from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError
from typing import Dict, Any


def go_to_cafe(visitor: Dict[str, Any], cafe: Cafe) -> None:
    try:
        message = cafe.visit_cafe(visitor)
        print(message)
    except (NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError) as error:
        print(error)
