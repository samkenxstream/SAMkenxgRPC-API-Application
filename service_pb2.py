# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='service.proto',
  package='data',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rservice.proto\x12\x04\x64\x61ta\"+\n\x07GetData\x12\x0c\n\x04time\x18\x01 \x01(\t\x12\x12\n\nmeterusage\x18\x02 \x01(\x02\x32>\n\nCreateData\x12\x30\n\x0eLoadtimeseries\x12\r.data.GetData\x1a\r.data.GetData\"\x00\x62\x06proto3'
)




_GETDATA = _descriptor.Descriptor(
  name='GetData',
  full_name='data.GetData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='data.GetData.time', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='meterusage', full_name='data.GetData.meterusage', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=66,
)

DESCRIPTOR.message_types_by_name['GetData'] = _GETDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetData = _reflection.GeneratedProtocolMessageType('GetData', (_message.Message,), {
  'DESCRIPTOR' : _GETDATA,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:data.GetData)
  })
_sym_db.RegisterMessage(GetData)



_CREATEDATA = _descriptor.ServiceDescriptor(
  name='CreateData',
  full_name='data.CreateData',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=68,
  serialized_end=130,
  methods=[
  _descriptor.MethodDescriptor(
    name='Loadtimeseries',
    full_name='data.CreateData.Loadtimeseries',
    index=0,
    containing_service=None,
    input_type=_GETDATA,
    output_type=_GETDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CREATEDATA)

DESCRIPTOR.services_by_name['CreateData'] = _CREATEDATA

# @@protoc_insertion_point(module_scope)
