# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gateway.proto

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
  name='gateway.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\rgateway.proto\"\xd5\x01\n\x0eGatewayRequest\x12\x31\n\x0crequest_type\x18\x01 \x01(\x0e\x32\x1b.GatewayRequest.RequestType\x12\r\n\x05value\x18\x02 \x01(\t\x12\x14\n\x0c\x63lient_ident\x18\x03 \x01(\x05\x12\x0b\n\x03\x61ux\x18\x04 \x01(\t\"^\n\x0bRequestType\x12\x0e\n\nReadStatus\x10\x00\x12\x0e\n\nReadSensor\x10\x01\x12\r\n\tModStatus\x10\x02\x12\x0b\n\x07ModOnOf\x10\x03\x12\x13\n\x0f\x44iscoverComands\x10\x05\"[\n\x0fGadgetsResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0csensor_ident\x18\x03 \x01(\x05\x12\x14\n\x0c\x63lient_ident\x18\x04 \x01(\x05\"6\n\x0cGadgetsIdent\x12\x0c\n\x04nome\x18\x01 \x01(\t\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x03\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_GATEWAYREQUEST_REQUESTTYPE = _descriptor.EnumDescriptor(
  name='RequestType',
  full_name='GatewayRequest.RequestType',
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
      name='DiscoverComands', index=4, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=137,
  serialized_end=231,
)
_sym_db.RegisterEnumDescriptor(_GATEWAYREQUEST_REQUESTTYPE)


_GATEWAYREQUEST = _descriptor.Descriptor(
  name='GatewayRequest',
  full_name='GatewayRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_type', full_name='GatewayRequest.request_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='GatewayRequest.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_ident', full_name='GatewayRequest.client_ident', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aux', full_name='GatewayRequest.aux', index=3,
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
    _GATEWAYREQUEST_REQUESTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=231,
)


_GADGETSRESPONSE = _descriptor.Descriptor(
  name='GadgetsResponse',
  full_name='GadgetsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='GadgetsResponse.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='GadgetsResponse.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sensor_ident', full_name='GadgetsResponse.sensor_ident', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_ident', full_name='GadgetsResponse.client_ident', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=233,
  serialized_end=324,
)


_GADGETSIDENT = _descriptor.Descriptor(
  name='GadgetsIdent',
  full_name='GadgetsIdent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nome', full_name='GadgetsIdent.nome', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ip', full_name='GadgetsIdent.ip', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='GadgetsIdent.port', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=326,
  serialized_end=380,
)

_GATEWAYREQUEST.fields_by_name['request_type'].enum_type = _GATEWAYREQUEST_REQUESTTYPE
_GATEWAYREQUEST_REQUESTTYPE.containing_type = _GATEWAYREQUEST
DESCRIPTOR.message_types_by_name['GatewayRequest'] = _GATEWAYREQUEST
DESCRIPTOR.message_types_by_name['GadgetsResponse'] = _GADGETSRESPONSE
DESCRIPTOR.message_types_by_name['GadgetsIdent'] = _GADGETSIDENT

GatewayRequest = _reflection.GeneratedProtocolMessageType('GatewayRequest', (_message.Message,), dict(
  DESCRIPTOR = _GATEWAYREQUEST,
  __module__ = 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:GatewayRequest)
  ))
_sym_db.RegisterMessage(GatewayRequest)

GadgetsResponse = _reflection.GeneratedProtocolMessageType('GadgetsResponse', (_message.Message,), dict(
  DESCRIPTOR = _GADGETSRESPONSE,
  __module__ = 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:GadgetsResponse)
  ))
_sym_db.RegisterMessage(GadgetsResponse)

GadgetsIdent = _reflection.GeneratedProtocolMessageType('GadgetsIdent', (_message.Message,), dict(
  DESCRIPTOR = _GADGETSIDENT,
  __module__ = 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:GadgetsIdent)
  ))
_sym_db.RegisterMessage(GadgetsIdent)


# @@protoc_insertion_point(module_scope)
