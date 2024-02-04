from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DormybobaRole(_message.Message):
    __slots__ = ["role_id", "role_name"]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_NAME_FIELD_NUMBER: _ClassVar[int]
    role_id: int
    role_name: str
    def __init__(self, role_id: _Optional[int] = ..., role_name: _Optional[str] = ...) -> None: ...

class Institute(_message.Message):
    __slots__ = ["institute_id", "institute_name"]
    INSTITUTE_ID_FIELD_NUMBER: _ClassVar[int]
    INSTITUTE_NAME_FIELD_NUMBER: _ClassVar[int]
    institute_id: int
    institute_name: str
    def __init__(self, institute_id: _Optional[int] = ..., institute_name: _Optional[str] = ...) -> None: ...

class AcademicType(_message.Message):
    __slots__ = ["type_id", "type_name"]
    TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    type_id: int
    type_name: str
    def __init__(self, type_id: _Optional[int] = ..., type_name: _Optional[str] = ...) -> None: ...

class GenerateVerificationCodeRequest(_message.Message):
    __slots__ = ["role_name"]
    ROLE_NAME_FIELD_NUMBER: _ClassVar[int]
    role_name: str
    def __init__(self, role_name: _Optional[str] = ...) -> None: ...

class GenerateVerificationCodeResponse(_message.Message):
    __slots__ = ["verification_code"]
    VERIFICATION_CODE_FIELD_NUMBER: _ClassVar[int]
    verification_code: int
    def __init__(self, verification_code: _Optional[int] = ...) -> None: ...

class GetRoleByVerificationCodeRequest(_message.Message):
    __slots__ = ["verification_code"]
    VERIFICATION_CODE_FIELD_NUMBER: _ClassVar[int]
    verification_code: int
    def __init__(self, verification_code: _Optional[int] = ...) -> None: ...

class GetRoleByVerificationCodeResponse(_message.Message):
    __slots__ = ["role"]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: DormybobaRole
    def __init__(self, role: _Optional[_Union[DormybobaRole, _Mapping]] = ...) -> None: ...

class CreateUserRequest(_message.Message):
    __slots__ = ["user_id", "institute_id", "role_id", "academic_type_id", "year", "group", "verification_code"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    INSTITUTE_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    ACADEMIC_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_CODE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    institute_id: int
    role_id: int
    academic_type_id: int
    year: int
    group: str
    verification_code: int
    def __init__(self, user_id: _Optional[str] = ..., institute_id: _Optional[int] = ..., role_id: _Optional[int] = ..., academic_type_id: _Optional[int] = ..., year: _Optional[int] = ..., group: _Optional[str] = ..., verification_code: _Optional[int] = ...) -> None: ...

class GetAllInstitutesResponse(_message.Message):
    __slots__ = ["institutes"]
    INSTITUTES_FIELD_NUMBER: _ClassVar[int]
    institutes: _containers.RepeatedCompositeFieldContainer[Institute]
    def __init__(self, institutes: _Optional[_Iterable[_Union[Institute, _Mapping]]] = ...) -> None: ...

class GetInstituteByNameRequest(_message.Message):
    __slots__ = ["institute_name"]
    INSTITUTE_NAME_FIELD_NUMBER: _ClassVar[int]
    institute_name: str
    def __init__(self, institute_name: _Optional[str] = ...) -> None: ...

class GetInstituteByNameResponse(_message.Message):
    __slots__ = ["institute"]
    INSTITUTE_FIELD_NUMBER: _ClassVar[int]
    institute: Institute
    def __init__(self, institute: _Optional[_Union[Institute, _Mapping]] = ...) -> None: ...

class GetAllAcademicTypesResponse(_message.Message):
    __slots__ = ["academic_types"]
    ACADEMIC_TYPES_FIELD_NUMBER: _ClassVar[int]
    academic_types: _containers.RepeatedCompositeFieldContainer[AcademicType]
    def __init__(self, academic_types: _Optional[_Iterable[_Union[AcademicType, _Mapping]]] = ...) -> None: ...

class GetAcademicTypeByNameRequest(_message.Message):
    __slots__ = ["type_name"]
    TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    type_name: str
    def __init__(self, type_name: _Optional[str] = ...) -> None: ...

class GetAcademicTypeByNameResponse(_message.Message):
    __slots__ = ["academic_type"]
    ACADEMIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    academic_type: AcademicType
    def __init__(self, academic_type: _Optional[_Union[AcademicType, _Mapping]] = ...) -> None: ...

class CreateMailingRequest(_message.Message):
    __slots__ = ["theme", "mailing_text", "at", "institute_id", "academic_type_id", "year"]
    THEME_FIELD_NUMBER: _ClassVar[int]
    MAILING_TEXT_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    INSTITUTE_ID_FIELD_NUMBER: _ClassVar[int]
    ACADEMIC_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    theme: str
    mailing_text: str
    at: _timestamp_pb2.Timestamp
    institute_id: int
    academic_type_id: int
    year: int
    def __init__(self, theme: _Optional[str] = ..., mailing_text: _Optional[str] = ..., at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., institute_id: _Optional[int] = ..., academic_type_id: _Optional[int] = ..., year: _Optional[int] = ...) -> None: ...

class CreateQueueRequest(_message.Message):
    __slots__ = ["title", "description", "open", "close"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    OPEN_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    open: _timestamp_pb2.Timestamp
    close: _timestamp_pb2.Timestamp
    def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., open: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., close: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AddPersonToQueueRequest(_message.Message):
    __slots__ = ["queue_id", "user_id"]
    QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    queue_id: int
    user_id: int
    def __init__(self, queue_id: _Optional[int] = ..., user_id: _Optional[int] = ...) -> None: ...

class AddPersonToQueueResponse(_message.Message):
    __slots__ = ["is_active"]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    is_active: bool
    def __init__(self, is_active: bool = ...) -> None: ...

class RemovePersonFromQueueRequest(_message.Message):
    __slots__ = ["queue_id", "user_id"]
    QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    queue_id: int
    user_id: int
    def __init__(self, queue_id: _Optional[int] = ..., user_id: _Optional[int] = ...) -> None: ...

class PersonCompleteQueueRequest(_message.Message):
    __slots__ = ["queue_id", "user_id"]
    QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    queue_id: int
    user_id: int
    def __init__(self, queue_id: _Optional[int] = ..., user_id: _Optional[int] = ...) -> None: ...

class PersonCompleteQueueResponse(_message.Message):
    __slots__ = ["is_queue_empty", "active_user_id"]
    IS_QUEUE_EMPTY_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_USER_ID_FIELD_NUMBER: _ClassVar[int]
    is_queue_empty: bool
    active_user_id: int
    def __init__(self, is_queue_empty: bool = ..., active_user_id: _Optional[int] = ...) -> None: ...

class AssignDefectRequest(_message.Message):
    __slots__ = ["defect_id"]
    DEFECT_ID_FIELD_NUMBER: _ClassVar[int]
    defect_id: str
    def __init__(self, defect_id: _Optional[str] = ...) -> None: ...

class AssignDefectResponse(_message.Message):
    __slots__ = ["assigned_user_id"]
    ASSIGNED_USER_ID_FIELD_NUMBER: _ClassVar[int]
    assigned_user_id: int
    def __init__(self, assigned_user_id: _Optional[int] = ...) -> None: ...
