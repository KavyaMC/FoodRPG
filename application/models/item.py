from dataclasses import dataclass, field


@dataclass(slots=True)
class Item:
    item_id: int
    item_name: str
    item_type: str
    attributes: dict = field(default_factory=dict)
    tags: list[str] = field(default_factory=list)

    def to_dict(self):
        return {
            "item_id": self.item_id,
            "item_name": self.item_name,
            "item_type": self.item_type,
            "attributes": self.attributes,
            "tags": self.tags,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            item_id=data["item_id"],
            item_name=data["item_name"],
            item_type=data["item_type"],
            attributes=data.get("attributes", {}),
            tags=data.get("tags", []),
        )
