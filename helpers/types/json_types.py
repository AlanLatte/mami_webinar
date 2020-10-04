from typing import Any, List, Mapping, Union

_JSONType0 = Union[str, int, float, bool, None, Mapping[str, Any], List[Any]]  # type: ignore
_JSONType1 = Union[
    str, int, float, bool, None, Mapping[str, _JSONType0], List[_JSONType0],
]
_JSONType2 = Union[
    str, int, float, bool, None, Mapping[str, _JSONType1], List[_JSONType1],
]
_JSONType3 = Union[
    str, int, float, bool, None, Mapping[str, _JSONType2], List[_JSONType2],
]
JSON = Union[
    str, int, float, bool, None, Mapping[str, _JSONType3], List[_JSONType3],
]
JSON_MAPPING = Mapping[str, JSON]
