from dataclasses import dataclass


@dataclass(slots=True)
class Player:
    SAVE_VERSION = 1

    player_name: str
    business_name: str
    business_category: str

    ownership_model: str = "Entrepreneur"

    def validate(self):
        fields = (
            ("Player Name", self.player_name),
            ("Business Name", self.business_name),
            ("Business Category", self.business_category),
        )

        for name, value in fields:
            if not value or not str(value).strip():
                raise ValueError(f"{name} is required.")

    def to_dict(self):
        return {
            "version": self.SAVE_VERSION,
            "player_name": self.player_name,
            "business_name": self.business_name,
            "business_category": self.business_category,
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
            business_category=data.get(
                "business_category",
                "",
            ),
            ownership_model=data.get(
                "ownership_model",
                "Entrepreneur",
            ),
        )

    def __str__(self):
        return f"{self.player_name} | {self.business_name} | {self.business_category}"
