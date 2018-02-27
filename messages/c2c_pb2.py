# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: c2c.proto

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
  name='c2c.proto',
  package='tud.seemuh.nfcgate.network.c2c',
  syntax='proto2',
  serialized_pb=_b('\n\tc2c.proto\x12\x1etud.seemuh.nfcgate.network.c2c\"\x8a\x01\n\x07NFCData\x12G\n\x0b\x64\x61ta_source\x18\x01 \x02(\x0e\x32\x32.tud.seemuh.nfcgate.network.c2c.NFCData.DataSource\x12\x12\n\ndata_bytes\x18\x02 \x02(\x0c\"\"\n\nDataSource\x12\n\n\x06READER\x10\x00\x12\x08\n\x04\x43\x41RD\x10\x01\"\x19\n\x07\x41nticol\x12\x0e\n\x06\x43ONFIG\x18\x01 \x02(\x0c\"\xa9\x02\n\x06Status\x12?\n\x04\x63ode\x18\x01 \x02(\x0e\x32\x31.tud.seemuh.nfcgate.network.c2c.Status.StatusCode\"\xdd\x01\n\nStatusCode\x12\x11\n\rKEEPALIVE_REQ\x10\x00\x12\x11\n\rKEEPALIVE_REP\x10\x01\x12\x0e\n\nCARD_FOUND\x10\x02\x12\x10\n\x0c\x43\x41RD_REMOVED\x10\x03\x12\x10\n\x0cREADER_FOUND\x10\x04\x12\x12\n\x0eREADER_REMOVED\x10\x05\x12\x0f\n\x0bNFC_NO_CONN\x10\x06\x12\x13\n\x0fINVALID_MSG_FMT\x10\x07\x12\x13\n\x0fNOT_IMPLEMENTED\x10\x08\x12\x13\n\x0fUNKNOWN_MESSAGE\x10\t\x12\x11\n\rUNKNOWN_ERROR\x10\n')
)



_NFCDATA_DATASOURCE = _descriptor.EnumDescriptor(
  name='DataSource',
  full_name='tud.seemuh.nfcgate.network.c2c.NFCData.DataSource',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='READER', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CARD', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=150,
  serialized_end=184,
)
_sym_db.RegisterEnumDescriptor(_NFCDATA_DATASOURCE)

_STATUS_STATUSCODE = _descriptor.EnumDescriptor(
  name='StatusCode',
  full_name='tud.seemuh.nfcgate.network.c2c.Status.StatusCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='KEEPALIVE_REQ', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KEEPALIVE_REP', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CARD_FOUND', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CARD_REMOVED', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READER_FOUND', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READER_REMOVED', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NFC_NO_CONN', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_MSG_FMT', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_IMPLEMENTED', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_MESSAGE', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_ERROR', index=10, number=10,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=290,
  serialized_end=511,
)
_sym_db.RegisterEnumDescriptor(_STATUS_STATUSCODE)


_NFCDATA = _descriptor.Descriptor(
  name='NFCData',
  full_name='tud.seemuh.nfcgate.network.c2c.NFCData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data_source', full_name='tud.seemuh.nfcgate.network.c2c.NFCData.data_source', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_bytes', full_name='tud.seemuh.nfcgate.network.c2c.NFCData.data_bytes', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _NFCDATA_DATASOURCE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=184,
)


_ANTICOL = _descriptor.Descriptor(
  name='Anticol',
  full_name='tud.seemuh.nfcgate.network.c2c.Anticol',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='CONFIG', full_name='tud.seemuh.nfcgate.network.c2c.Anticol.CONFIG', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=186,
  serialized_end=211,
)


_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='tud.seemuh.nfcgate.network.c2c.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='tud.seemuh.nfcgate.network.c2c.Status.code', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STATUS_STATUSCODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=214,
  serialized_end=511,
)

_NFCDATA.fields_by_name['data_source'].enum_type = _NFCDATA_DATASOURCE
_NFCDATA_DATASOURCE.containing_type = _NFCDATA
_STATUS.fields_by_name['code'].enum_type = _STATUS_STATUSCODE
_STATUS_STATUSCODE.containing_type = _STATUS
DESCRIPTOR.message_types_by_name['NFCData'] = _NFCDATA
DESCRIPTOR.message_types_by_name['Anticol'] = _ANTICOL
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NFCData = _reflection.GeneratedProtocolMessageType('NFCData', (_message.Message,), dict(
  DESCRIPTOR = _NFCDATA,
  __module__ = 'c2c_pb2'
  # @@protoc_insertion_point(class_scope:tud.seemuh.nfcgate.network.c2c.NFCData)
  ))
_sym_db.RegisterMessage(NFCData)

Anticol = _reflection.GeneratedProtocolMessageType('Anticol', (_message.Message,), dict(
  DESCRIPTOR = _ANTICOL,
  __module__ = 'c2c_pb2'
  # @@protoc_insertion_point(class_scope:tud.seemuh.nfcgate.network.c2c.Anticol)
  ))
_sym_db.RegisterMessage(Anticol)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), dict(
  DESCRIPTOR = _STATUS,
  __module__ = 'c2c_pb2'
  # @@protoc_insertion_point(class_scope:tud.seemuh.nfcgate.network.c2c.Status)
  ))
_sym_db.RegisterMessage(Status)


# @@protoc_insertion_point(module_scope)
