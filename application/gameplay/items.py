from dataclasses import dataclass

@dataclass
class Item:
    id:int
    name:str
    type:str
    attributes:dict

