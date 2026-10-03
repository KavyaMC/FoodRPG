from dataclasses import dataclass


@dataclass(slots=True)
class Player:
    SAVE_VERSION = 1
    DEFAULT_OWNERSHIP_MODEL = "Entrepreneur"

    player_name: str
    business_name: str
    business_type: str

    ownership_model: str = DEFAULT_OWNERSHIP_MODEL

    @classmethod
    def new(cls, player_name, business_name, business_type, defaults):
        return cls(
            player_name=player_name,
            business_name=business_name,
            business_type=business_type,
            ownership_model=defaults.get(
                "ownership_model",
                cls.DEFAULT_OWNERSHIP_MODEL,
            ),
        )

    def validate(self):
        fields = (
            ("Player Name", self.player_name),
            ("Business Name", self.business_name),
            ("Business Type", self.business_type),
        )

        for name, value in fields:
            if not value or not str(value).strip():
                raise ValueError(f"{name} is required.")

    def to_dict(self):
        return {
            "version": self.SAVE_VERSION,
            "player_name": self.player_name,
            "business_name": self.business_name,
            "business_type": self.business_type,
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
            business_type=data.get(
                "business_type",
                "",
            ),
            ownership_model=data.get(
                "ownership_model",
                cls.DEFAULT_OWNERSHIP_MODEL,
            ),
        )

    def __str__(self):
        return f"{self.player_name} | {self.business_name} | {self.business_type}"
