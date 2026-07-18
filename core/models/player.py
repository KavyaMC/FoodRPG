from dataclasses import dataclass


@dataclass(slots=True)
class Player:
    SAVE_VERSION = 1

    player_name: str

    business_name: str

    business_sector: str
    business_category: str
    business_type: str
    business_model: str

    ownership_model: str = "Entrepreneur"

    def validate(self):
        fields = (
            ("Player Name", self.player_name),
            ("Business Name", self.business_name),
            ("Business Sector", self.business_sector),
            ("Business Category", self.business_category),
            ("Business Type", self.business_type),
            ("Business Model", self.business_model),
            ("Ownership Model", self.ownership_model),
        )

        for name, value in fields:
            if not value or not str(value).strip():
                raise ValueError(f"{name} is required.")

    def to_dict(self):
        return {
            "version": self.SAVE_VERSION,
            "player_name": self.player_name,
            "business_name": self.business_name,
            "business_sector": self.business_sector,
            "business_category": self.business_category,
            "business_type": self.business_type,
            "business_model": self.business_model,
            "ownership_model": self.ownership_model,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            player_name=data.get(
                "player_name",
                "",
            ),
            business_name=data.get(
                "business_name",
                "",
            ),
            business_sector=data.get(
                "business_sector",
                "",
            ),
            business_category=data.get(
                "business_category",
                "",
            ),
            business_type=data.get(
                "business_type",
                "",
            ),
            business_model=data.get(
                "business_model",
                "",
            ),
            ownership_model=data.get(
                "ownership_model",
                "Entrepreneur",
            ),
        )

    def __str__(self):
        return f"{self.player_name} | {self.business_name} | {self.business_type}"
