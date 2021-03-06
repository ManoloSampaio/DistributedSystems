# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='app.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\tapp.proto\"\x8b\x02\n\x0bRequest_APP\x12.\n\x0crequest_type\x18\x01 \x01(\x0e\x32\x18.Request_APP.RequestType\x12\r\n\x05value\x18\x02 \x01(\x02\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0b\n\x03\x61ux\x18\x04 \x01(\t\"\xa1\x01\n\x0bRequestType\x12\x0e\n\nReadStatus\x10\x00\x12\x0e\n\nReadSensor\x10\x01\x12\r\n\tModStatus\x10\x02\x12\x0b\n\x07ModOnOf\x10\x03\x12\x13\n\x0f\x44iscoverComands\x10\x04\x12\x0f\n\x0bListObjects\x10\x05\x12\x12\n\x0eVerifyActuator\x10\x06\x12\x10\n\x0cVerifySensor\x10\x07\x12\n\n\x06LogOut\x10\x08\"\x89\x02\n\x0cResponse_APP\x12\x31\n\rresponse_type\x18\x01 \x01(\x0e\x32\x1a.Response_APP.ResponseType\x12\x13\n\x0bobject_name\x18\x02 \x01(\t\x12\x15\n\robject_result\x18\x03 \x01(\x02\x12\x13\n\x0blist_object\x18\x04 \x01(\t\x12\x15\n\ron_off_status\x18\x05 \x01(\t\x12\x16\n\x0eobject_comands\x18\x06 \x03(\t\"V\n\x0cResponseType\x12\n\n\x06Status\x10\x00\x12\x11\n\rON_OFF_status\x10\x01\x12\x12\n\x0eServer_Message\x10\x02\x12\x13\n\x0fObject_commands\x10\x03\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_REQUEST_APP_REQUESTTYPE = _descriptor.EnumDescriptor(
  name='RequestType',
  full_name='Request_APP.RequestType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ReadStatus', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ReadSensor', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ModStatus', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ModOnOf', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DiscoverComands', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ListObjects', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VerifyActuator', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VerifySensor', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LogOut', index=8, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=120,
  serialized_end=281,
)
_sym_db.RegisterEnumDescriptor(_REQUEST_APP_REQUESTTYPE)

_RESPONSE_APP_RESPONSETYPE = _descriptor.EnumDescriptor(
  name='ResponseType',
  full_name='Response_APP.ResponseType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Status', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ON_OFF_status', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Server_Message', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Object_commands', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=463,
  serialized_end=549,
)
_sym_db.RegisterEnumDescriptor(_RESPONSE_APP_RESPONSETYPE)


_REQUEST_APP = _descriptor.Descriptor(
  name='Request_APP',
  full_name='Request_APP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_type', full_name='Request_APP.request_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='Request_APP.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Request_APP.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aux', full_name='Request_APP.aux', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REQUEST_APP_REQUESTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=281,
)


_RESPONSE_APP = _descriptor.Descriptor(
  name='Response_APP',
  full_name='Response_APP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response_type', full_name='Response_APP.response_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='object_name', full_name='Response_APP.object_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='object_result', full_name='Response_APP.object_result', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='list_object', full_name='Response_APP.list_object', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='on_off_status', full_name='Response_APP.on_off_status', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='object_comands', full_name='Response_APP.object_comands', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RESPONSE_APP_RESPONSETYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=284,
  serialized_end=549,
)

_REQUEST_APP.fields_by_name['request_type'].enum_type = _REQUEST_APP_REQUESTTYPE
_REQUEST_APP_REQUESTTYPE.containing_type = _REQUEST_APP
_RESPONSE_APP.fields_by_name['response_type'].enum_type = _RESPONSE_APP_RESPONSETYPE
_RESPONSE_APP_RESPONSETYPE.containing_type = _RESPONSE_APP
DESCRIPTOR.message_types_by_name['Request_APP'] = _REQUEST_APP
DESCRIPTOR.message_types_by_name['Response_APP'] = _RESPONSE_APP

Request_APP = _reflection.GeneratedProtocolMessageType('Request_APP', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST_APP,
  __module__ = 'app_pb2'
  # @@protoc_insertion_point(class_scope:Request_APP)
  ))
_sym_db.RegisterMessage(Request_APP)

Response_APP = _reflection.GeneratedProtocolMessageType('Response_APP', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE_APP,
  __module__ = 'app_pb2'
  # @@protoc_insertion_point(class_scope:Response_APP)
  ))
_sym_db.RegisterMessage(Response_APP)


# @@protoc_insertion_point(module_scope)
