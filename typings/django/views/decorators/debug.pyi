from typing import Any, Callable

def sensitive_variables(*variables: Any) -> Callable[..., Any]: ...
def sensitive_post_parameters(*parameters: Any) -> Callable[..., Any]: ...
