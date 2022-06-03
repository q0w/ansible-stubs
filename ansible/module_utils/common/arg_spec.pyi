from collections.abc import Iterable, Mapping, MutableMapping
from typing import Any

from ansible.module_utils.errors import AnsibleValidationErrorMultiple

class ValidationResult:
    _no_log_values: set[str]
    _unsupported_parameters: set[str]
    _validated_parameters: Mapping[str, Any]
    _deprecations: list[str]
    _warnings: list[str]
    _aliases: MutableMapping[str, Any]
    errors: AnsibleValidationErrorMultiple
    def __init__(self, parameters: Mapping[str, Any]): ...
    @property
    def validated_parameters(self) -> set[str]: ...
    @property
    def unsupported_parameters(self) -> Mapping[str, Any]: ...
    @property
    def error_messages(self) -> list[str]: ...

class ArgumentSpecValidator:
    def __init__(
        self,
        argument_spec: Mapping[str, Mapping[str, Any]],
        mutually_exclusive: list[tuple[str, ...]] | None = ...,
        required_together: list[tuple[str, ...]] | None = ...,
        required_one_of: list[tuple[str, ...]] | None = ...,
        required_if: list[tuple[str, str, tuple[str, ...], bool]] | None = ...,
        required_by: Mapping[str, Iterable[str]] | None = ...,
    ) -> None: ...
    def validate(self, parameters: Mapping[str, Any]) -> ValidationResult: ...

class ModuleArgumentSpecValidator(ArgumentSpecValidator): ...
