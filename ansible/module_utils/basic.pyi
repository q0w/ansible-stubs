from collections.abc import Iterable, Mapping, MutableMapping
from typing import Any, NoReturn

from _typeshed import StrOrBytesPath

from ansible.module_utils.common.arg_spec import ModuleArgumentSpecValidator

def get_platform() -> str: ...
def missing_required_lib(library: str, reason: str | None = ..., url: str | None = ...) -> str: ...

class AnsibleModule:
    params: Mapping[str, Any]
    argument_spec: Mapping[str, Mapping[str, Any]]
    supports_check_mode: bool
    check_mode: bool
    bypass_checks: bool
    no_log: bool
    mutually_exclusive: list[tuple[str, ...]]
    required_together: list[tuple[str, ...]]
    required_one_of: list[tuple[str, ...]]
    add_file_commong_args: bool
    required_if: list[tuple[str, str, tuple[str, ...], bool]]
    required_by: Mapping[str, Iterable[str]]
    cleanup_files: list[StrOrBytesPath | int]
    run_command_environ_update: MutableMapping[str, str]
    aliases: MutableMapping[str, Any]
    no_log_values: set[str]
    validator: ModuleArgumentSpecValidator
    _selinux_enabled: bool
    def __init__(
        self,
        argument_spec: Mapping[str, Mapping[str, Any]],
        bypass_checks: bool = ...,
        no_log: bool = ...,
        mutually_exclusive: list[tuple[str, ...]] | None = ...,
        required_together: list[tuple[str, ...]] | None = ...,
        required_one_of: list[tuple[str, ...]] | None = ...,
        add_file_common_args: bool = ...,
        supports_check_mode: bool = ...,
        required_if: list[tuple[str, str, tuple[str, ...], bool]] | None = ...,
        required_by: Mapping[str, Iterable[str]] | None = ...,
    ) -> None: ...
    def fail_json(self, msg: str, **kwargs) -> NoReturn: ...
    def exit_json(self, **kwargs) -> NoReturn: ...
