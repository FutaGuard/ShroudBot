from dataclasses import dataclass, field
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Token:
    """
    :method POST
    :path /api/v1/token
    """
    token: str = field(hash=False, repr=True, compare=False, default=None)
