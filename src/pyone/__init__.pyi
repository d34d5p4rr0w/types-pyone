# Stub file for pyone module
import xmlrpc.client
from typing import Any, Dict, Optional, Protocol, Tuple, Union
from xmlrpc.client import Transport, _Marshallable

from _typeshed import SizedBuffer
from aenum import IntEnum
from six import string_types

from . import bindings

# Exceptions as defined in the XML-API reference
class OneException(Exception): ...

class OneAuthenticationException(OneException): ...

class OneAuthorizationException(OneException): ...

class OneNoExistsException(OneException): ...

class OneActionException(OneException): ...

class OneApiException(OneException): ...

class OneInternalException(OneException): ...

# Constants, naming follows those in Open Nebula Ruby API
DATASTORE_TYPES: IntEnum
DATASTORE_STATES: IntEnum
DISK_TYPES: IntEnum
HISTORY_ACTION: IntEnum
HOST_STATES: IntEnum
HOST_STATUS: IntEnum
IMAGE_STATES: IntEnum
IMAGE_TYPES: IntEnum
LCM_STATE: IntEnum
MARKETPLACEAPP_STATES: IntEnum
MARKETPLACEAPP_TYPES: IntEnum
PAGINATED_POOLS: IntEnum
REMOVE_VNET_ATTRS: IntEnum
VM_STATE: IntEnum

class OneImagePoolMethod(Protocol):
    def info(self, resources: int, begin: int, end: int) -> bindings.IMAGE_POOLSub: ...


class OneTemplateMethod(Protocol):
    def instantiate(self, template_id: int, name: str, hold: bool, extra: str) -> int: ...


class OneVMMethod(Protocol):
    def info(self, vm_id: int) -> bindings.VMSub: ...
    def action(self, name: str, vm_id: int) -> None: ...


class OneServer(xmlrpc.client.ServerProxy):
    def __init__(self, uri: str, session: str, timeout: Optional[int] = None, https_verify: bool = True, **options: Any): ...
    def _ServerProxy__request(self, methodname: str, params: Tuple) -> Any: ...
    def _do_request(self, method: str, params: Tuple) -> Any: ...
    def _cast_parms(self, params: Tuple) -> Tuple: ...
    def __response(self, raw_response: Any) -> Any: ...
    def server_retry_interval(self) -> int: ...
    def server_close(self) -> None: ...

    @property
    def imagepool(self) -> OneImagePoolMethod: ...

    @property
    def template(self) -> OneTemplateMethod: ...

    @property
    def vm(self) -> OneVMMethod: ...

class RequestsTransport(xmlrpc.client.Transport):
    user_agent: str
    use_https: bool
    https_verify: bool

    def set_https(self, https: bool = False) -> None: ...
    def set_https_verify(self, https_verify: bool) -> None: ...
    def request(self, host: Union[str, Tuple[str, Dict[str, str]]], handler: str, request_body: SizedBuffer, verbose: bool = ...) -> Tuple[_Marshallable, ...]: ...
    def parse_response(self, response: Any) -> Any: ...
    def _build_url(self, host: str, handler: str) -> str: ...
