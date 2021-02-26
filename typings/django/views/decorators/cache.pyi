from typing import Any, Callable, Optional, TypeVar

_F = TypeVar("_F", bound=Callable[..., Any])

def cache_page(
    timeout: float, *, cache: Optional[Any] = ..., key_prefix: Optional[Any] = ...
) -> Callable[..., Any]: ...
def cache_control(**kwargs: Any) -> Callable[..., Any]: ...
def never_cache(view_func: _F) -> _F: ...
