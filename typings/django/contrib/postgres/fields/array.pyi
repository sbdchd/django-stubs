from typing import (
    Any,
    Generic,
    Iterable,
    List,
    Optional,
    Sequence,
    TypeVar,
    Union,
    overload,
)

from django.db.models.expressions import Combinable
from django.db.models.fields import (
    Field,
    _ErrorMessagesToOverride,
    _FieldChoices,
    _ValidatorCallable,
)
from typing_extensions import Literal

from .mixins import CheckFieldDefaultMixin

_T = TypeVar("_T")

class ArrayField(
    Generic[_T],
    CheckFieldDefaultMixin,
    Field[Union[Sequence[Any], Combinable], List[Any]],
):

    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    base_field: Any = ...
    size: Any = ...
    default_validators: Any = ...
    from_db_value: Any = ...
    @overload
    def __init__(
        self: ArrayField[List[Any]],
        base_field: Field,
        size: Optional[int] = ...,
        verbose_name: Optional[Union[str, bytes]] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Any = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Optional[_FieldChoices] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: ArrayField[Optional[List[Any]]],
        base_field: Field,
        size: Optional[int] = ...,
        verbose_name: Optional[Union[str, bytes]] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Any = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: Optional[str] = ...,
        unique_for_month: Optional[str] = ...,
        unique_for_year: Optional[str] = ...,
        choices: Optional[_FieldChoices] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: Optional[_ErrorMessagesToOverride] = ...,
    ) -> None: ...
    def __get__(self: ArrayField[_T], instance: Any, owner: Any) -> _T: ...
    def __set__(self: ArrayField[_T], instance: Any, value: _T) -> None: ...
    @property
    def description(self): ...
    def get_transform(self, name: Any): ...
