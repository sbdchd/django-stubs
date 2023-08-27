from collections.abc import Iterator, Sequence
from typing import Any, Optional, Union

from django.apps import AppConfig
from django.apps.registry import Apps
from django.db.models.base import Model
from django.db.models.fields import Field
from django.db.models.manager import Manager

class AppConfigStub(AppConfig): ...

class ModelState:
    name: str
    app_label: str
    fields: list[tuple[str, Field[Any, Any]]]
    options: dict[str, Any] = ...
    bases: tuple[type[Model]] = ...
    managers: list[tuple[str, Manager[Any]]] = ...
    def __init__(
        self,
        app_label: str,
        name: str,
        fields: list[tuple[str, Field[Any, Any]]],
        options: Optional[dict[str, Any]] = ...,
        bases: Optional[Sequence[Union[type[Model], str]]] = ...,
        managers: Optional[list[tuple[str, Manager[Any]]]] = ...,
    ) -> None: ...
    def clone(self) -> ModelState: ...
    def construct_managers(self) -> Iterator[tuple[str, Manager[Any]]]: ...
    @classmethod
    def from_model(cls, model: type[Model], exclude_rels: bool = ...) -> ModelState: ...
    def get_field_by_name(self, name: str) -> Field[Any, Any]: ...
    @property
    def name_lower(self) -> str: ...
    def render(self, apps: Apps) -> Any: ...

def get_related_models_tuples(model: type[Model]) -> set[tuple[str, str]]: ...
def get_related_models_recursive(model: type[Model]) -> set[tuple[str, str]]: ...

class ProjectState:
    is_delayed: bool
    models: dict[Any, Any]
    real_apps: list[str]
    def __init__(
        self,
        models: Optional[dict[tuple[str, str], ModelState]] = ...,
        real_apps: Optional[list[str]] = ...,
    ) -> None: ...
    def add_model(self, model_state: ModelState) -> None: ...
    @property
    def apps(self) -> StateApps: ...
    def clear_delayed_apps_cache(self) -> None: ...
    def clone(self) -> ProjectState: ...
    @property
    def concrete_apps(self) -> StateApps: ...
    @classmethod
    def from_apps(cls, apps: Apps) -> ProjectState: ...
    def reload_model(
        self, app_label: str, model_name: str, delay: bool = ...
    ) -> None: ...
    def reload_models(self, models: list[Any], delay: bool = ...) -> None: ...
    def remove_model(self, app_label: str, model_name: str) -> None: ...

class StateApps(Apps):
    real_models: list[ModelState]
    def __init__(
        self,
        real_apps: list[str],
        models: dict[tuple[str, str], ModelState],
        ignore_swappable: bool = ...,
    ) -> None: ...
    def bulk_update(self) -> Iterator[None]: ...
    def clone(self) -> StateApps: ...
    def render_multiple(self, model_states: list[ModelState]) -> None: ...
    def unregister_model(self, app_label: str, model_name: str) -> None: ...
