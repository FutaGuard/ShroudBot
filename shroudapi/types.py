from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List, Optional, Union


@dataclass_json
@dataclass
class Token:
    """
    :method POST
    :path /api/v1/token
    """
    token: str = field(hash=False, repr=True, compare=False, default=None)


@dataclass_json
@dataclass
class EmailAliases:
    address: str = field(hash=False, repr=True, compare=False, default=None)
    enabled: bool = field(hash=False, repr=True, compare=False, default=None)
    title: Optional[str] = field(hash=False, repr=True, compare=False, default=None)
    notes: Optional[str] = field(hash=False, repr=True, compare=False, default=None)
    forwarded: int = field(hash=False, repr=True, compare=False, default=None)
    blocked: int = field(hash=False, repr=True, compare=False, default=None)
    blocked_addrresses: Optional[List[str]] = field(hash=False, repr=True, compare=False, default=None)


@dataclass_json
@dataclass
class Alias:
    """
    :method GET
    :path /api/v1/aliases
    """
    email_aliases: Optional[Union[List[EmailAliases], bool]] = field(hash=False, repr=True, compare=False, default=None)
    page_number: int = field(hash=False, repr=True, compare=False, default=None)
    page_size: int = field(hash=False, repr=True, compare=False, default=None)
    total_entries: int = field(hash=False, repr=True, compare=False, default=None)
    total_pages: int = field(hash=False, repr=True, compare=False, default=None)


@dataclass_json
@dataclass
class Domains:
    """
    :method GET
    :path /api/v1/domains
    """
    @dataclass_json
    @dataclass
    class Domain:
        domain: str = field(hash=False, repr=True, compare=False, default=None)

    domains: Optional[Union[List[Domain], bool]] = field(hash=False, repr=True, compare=False, default=None)
    page_number: int = field(hash=False, repr=True, compare=False, default=None)
    page_size: int = field(hash=False, repr=True, compare=False, default=None)
    total_entries: int = field(hash=False, repr=True, compare=False, default=None)
    total_pages: int = field(hash=False, repr=True, compare=False, default=None)
