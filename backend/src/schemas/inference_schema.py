from typing import List, Optional

from pydantic import BaseModel, Field
from src.translation import translation_mapping_custom_options


class InferenceSchema(BaseModel):
    # categorical
    manufacturer: str
    model: str
    fuel: str
    chassis: str
    sold_by: str
    gearbox: str

    # numerical
    km: int
    power: int
    engine: int
    year: int

    # description
    description: str

    # image
    image_url: str

    # optional equipments
    audio_and_technology: Optional[List[str]] = None
    comfort_and_optional_equipment: Optional[List[str]] = None
    electronics_and_assistance_systems: Optional[List[str]] = None
    performance: Optional[List[str]] = None
    safety: Optional[List[str]] = None

    def translate_optional_fields(self) -> dict:
        def translate_list(lst):
            return [translation_mapping_custom_options.get(item, item).lower() for item in lst]

        translated_fields = {
            "Audio and technology": translate_list(self.audio_and_technology) if self.audio_and_technology else [],
            "Comfort and optional equipment": translate_list(self.comfort_and_optional_equipment) if self.comfort_and_optional_equipment else [],
            "Electronics and assistance systems": (
                translate_list(self.electronics_and_assistance_systems) if self.electronics_and_assistance_systems else []
            ),
            "Performance": translate_list(self.performance) if self.performance else [],
            "Safety": translate_list(self.safety) if self.safety else [],
        }
        return translated_fields


class InferenceResponseSchema(BaseModel):
    prediction: float = Field(..., example=10000)
