# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wcf.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\twcf.proto\x12\x03wcf\"\xff\x03\n\x07Request\x12\x1c\n\x04\x66unc\x18\x01 \x01(\x0e\x32\x0e.wcf.Functions\x12\x1b\n\x05\x65mpty\x18\x02 \x01(\x0b\x32\n.wcf.EmptyH\x00\x12\r\n\x03str\x18\x03 \x01(\tH\x00\x12\x1b\n\x03txt\x18\x04 \x01(\x0b\x32\x0c.wcf.TextMsgH\x00\x12\x1c\n\x04\x66ile\x18\x05 \x01(\x0b\x32\x0c.wcf.PathMsgH\x00\x12\x1d\n\x05query\x18\x06 \x01(\x0b\x32\x0c.wcf.DbQueryH\x00\x12\x1e\n\x01v\x18\x07 \x01(\x0b\x32\x11.wcf.VerificationH\x00\x12\x1c\n\x01m\x18\x08 \x01(\x0b\x32\x0f.wcf.MemberMgmtH\x00\x12\x1a\n\x03xml\x18\t \x01(\x0b\x32\x0b.wcf.XmlMsgH\x00\x12\x1b\n\x03\x64\x65\x63\x18\n \x01(\x0b\x32\x0c.wcf.DecPathH\x00\x12\x1b\n\x02tf\x18\x0b \x01(\x0b\x32\r.wcf.TransferH\x00\x12\x12\n\x04ui64\x18\x0c \x01(\x04\x42\x02\x30\x01H\x00\x12\x0e\n\x04\x66lag\x18\r \x01(\x08H\x00\x12\x1d\n\x03\x61tt\x18\x0e \x01(\x0b\x32\x0e.wcf.AttachMsgH\x00\x12\x1b\n\x02\x61m\x18\x0f \x01(\x0b\x32\r.wcf.AudioMsgH\x00\x12\x1b\n\x02rt\x18\x10 \x01(\x0b\x32\r.wcf.RichTextH\x00\x12\x19\n\x02pm\x18\x11 \x01(\x0b\x32\x0b.wcf.PatMsgH\x00\x12\x1d\n\x02\x66m\x18\x12 \x01(\x0b\x32\x0f.wcf.ForwardMsgH\x00\x42\x05\n\x03msg\"\xc7\x02\n\x08Response\x12\x1c\n\x04\x66unc\x18\x01 \x01(\x0e\x32\x0e.wcf.Functions\x12\x10\n\x06status\x18\x02 \x01(\x05H\x00\x12\r\n\x03str\x18\x03 \x01(\tH\x00\x12\x1b\n\x05wxmsg\x18\x04 \x01(\x0b\x32\n.wcf.WxMsgH\x00\x12\x1e\n\x05types\x18\x05 \x01(\x0b\x32\r.wcf.MsgTypesH\x00\x12$\n\x08\x63ontacts\x18\x06 \x01(\x0b\x32\x10.wcf.RpcContactsH\x00\x12\x1b\n\x03\x64\x62s\x18\x07 \x01(\x0b\x32\x0c.wcf.DbNamesH\x00\x12\x1f\n\x06tables\x18\x08 \x01(\x0b\x32\r.wcf.DbTablesH\x00\x12\x1b\n\x04rows\x18\t \x01(\x0b\x32\x0b.wcf.DbRowsH\x00\x12\x1b\n\x02ui\x18\n \x01(\x0b\x32\r.wcf.UserInfoH\x00\x12\x1a\n\x03ocr\x18\x0b \x01(\x0b\x32\x0b.wcf.OcrMsgH\x00\x42\x05\n\x03msg\"\x07\n\x05\x45mpty\"\xbe\x01\n\x05WxMsg\x12\x0f\n\x07is_self\x18\x01 \x01(\x08\x12\x10\n\x08is_group\x18\x02 \x01(\x08\x12\x0e\n\x02id\x18\x03 \x01(\x04\x42\x02\x30\x01\x12\x0c\n\x04type\x18\x04 \x01(\r\x12\n\n\x02ts\x18\x05 \x01(\r\x12\x0e\n\x06roomid\x18\x06 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x07 \x01(\t\x12\x0e\n\x06sender\x18\x08 \x01(\t\x12\x0c\n\x04sign\x18\t \x01(\t\x12\r\n\x05thumb\x18\n \x01(\t\x12\r\n\x05\x65xtra\x18\x0b \x01(\t\x12\x0b\n\x03xml\x18\x0c \x01(\t\"7\n\x07TextMsg\x12\x0b\n\x03msg\x18\x01 \x01(\t\x12\x10\n\x08receiver\x18\x02 \x01(\t\x12\r\n\x05\x61ters\x18\x03 \x01(\t\")\n\x07PathMsg\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x10\n\x08receiver\x18\x02 \x01(\t\"G\n\x06XmlMsg\x12\x10\n\x08receiver\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\x05\"a\n\x08MsgTypes\x12\'\n\x05types\x18\x01 \x03(\x0b\x32\x18.wcf.MsgTypes.TypesEntry\x1a,\n\nTypesEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x87\x01\n\nRpcContact\x12\x0c\n\x04wxid\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0e\n\x06remark\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x05 \x01(\t\x12\x10\n\x08province\x18\x06 \x01(\t\x12\x0c\n\x04\x63ity\x18\x07 \x01(\t\x12\x0e\n\x06gender\x18\x08 \x01(\x05\"0\n\x0bRpcContacts\x12!\n\x08\x63ontacts\x18\x01 \x03(\x0b\x32\x0f.wcf.RpcContact\"\x18\n\x07\x44\x62Names\x12\r\n\x05names\x18\x01 \x03(\t\"$\n\x07\x44\x62Table\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03sql\x18\x02 \x01(\t\"(\n\x08\x44\x62Tables\x12\x1c\n\x06tables\x18\x01 \x03(\x0b\x32\x0c.wcf.DbTable\"\"\n\x07\x44\x62Query\x12\n\n\x02\x64\x62\x18\x01 \x01(\t\x12\x0b\n\x03sql\x18\x02 \x01(\t\"8\n\x07\x44\x62\x46ield\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x0e\n\x06\x63olumn\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\x0c\"%\n\x05\x44\x62Row\x12\x1c\n\x06\x66ields\x18\x01 \x03(\x0b\x32\x0c.wcf.DbField\"\"\n\x06\x44\x62Rows\x12\x18\n\x04rows\x18\x01 \x03(\x0b\x32\n.wcf.DbRow\"5\n\x0cVerification\x12\n\n\x02v3\x18\x01 \x01(\t\x12\n\n\x02v4\x18\x02 \x01(\t\x12\r\n\x05scene\x18\x03 \x01(\x05\"+\n\nMemberMgmt\x12\x0e\n\x06roomid\x18\x01 \x01(\t\x12\r\n\x05wxids\x18\x02 \x01(\t\"D\n\x08UserInfo\x12\x0c\n\x04wxid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06mobile\x18\x03 \x01(\t\x12\x0c\n\x04home\x18\x04 \x01(\t\"#\n\x07\x44\x65\x63Path\x12\x0b\n\x03src\x18\x01 \x01(\t\x12\x0b\n\x03\x64st\x18\x02 \x01(\t\"4\n\x08Transfer\x12\x0c\n\x04wxid\x18\x01 \x01(\t\x12\x0c\n\x04tfid\x18\x02 \x01(\t\x12\x0c\n\x04taid\x18\x03 \x01(\t\"9\n\tAttachMsg\x12\x0e\n\x02id\x18\x01 \x01(\x04\x42\x02\x30\x01\x12\r\n\x05thumb\x18\x02 \x01(\t\x12\r\n\x05\x65xtra\x18\x03 \x01(\t\"\'\n\x08\x41udioMsg\x12\x0e\n\x02id\x18\x01 \x01(\x04\x42\x02\x30\x01\x12\x0b\n\x03\x64ir\x18\x02 \x01(\t\"y\n\x08RichText\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x63\x63ount\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x0e\n\x06\x64igest\x18\x04 \x01(\t\x12\x0b\n\x03url\x18\x05 \x01(\t\x12\x10\n\x08thumburl\x18\x06 \x01(\t\x12\x10\n\x08receiver\x18\x07 \x01(\t\"&\n\x06PatMsg\x12\x0e\n\x06roomid\x18\x01 \x01(\t\x12\x0c\n\x04wxid\x18\x02 \x01(\t\"(\n\x06OcrMsg\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0e\n\x06result\x18\x02 \x01(\t\".\n\nForwardMsg\x12\x0e\n\x02id\x18\x01 \x01(\x04\x42\x02\x30\x01\x12\x10\n\x08receiver\x18\x02 \x01(\t*\xf2\x05\n\tFunctions\x12\x11\n\rFUNC_RESERVED\x10\x00\x12\x11\n\rFUNC_IS_LOGIN\x10\x01\x12\x16\n\x12\x46UNC_GET_SELF_WXID\x10\x10\x12\x16\n\x12\x46UNC_GET_MSG_TYPES\x10\x11\x12\x15\n\x11\x46UNC_GET_CONTACTS\x10\x12\x12\x15\n\x11\x46UNC_GET_DB_NAMES\x10\x13\x12\x16\n\x12\x46UNC_GET_DB_TABLES\x10\x14\x12\x16\n\x12\x46UNC_GET_USER_INFO\x10\x15\x12\x16\n\x12\x46UNC_GET_AUDIO_MSG\x10\x16\x12\x11\n\rFUNC_SEND_TXT\x10 \x12\x11\n\rFUNC_SEND_IMG\x10!\x12\x12\n\x0e\x46UNC_SEND_FILE\x10\"\x12\x11\n\rFUNC_SEND_XML\x10#\x12\x15\n\x11\x46UNC_SEND_EMOTION\x10$\x12\x16\n\x12\x46UNC_SEND_RICH_TXT\x10%\x12\x15\n\x11\x46UNC_SEND_PAT_MSG\x10&\x12\x14\n\x10\x46UNC_FORWARD_MSG\x10\'\x12\x18\n\x14\x46UNC_ENABLE_RECV_TXT\x10\x30\x12\x19\n\x15\x46UNC_DISABLE_RECV_TXT\x10@\x12\x16\n\x12\x46UNC_EXEC_DB_QUERY\x10P\x12\x16\n\x12\x46UNC_ACCEPT_FRIEND\x10Q\x12\x16\n\x12\x46UNC_RECV_TRANSFER\x10R\x12\x14\n\x10\x46UNC_REFRESH_PYQ\x10S\x12\x18\n\x14\x46UNC_DOWNLOAD_ATTACH\x10T\x12\x19\n\x15\x46UNC_GET_CONTACT_INFO\x10U\x12\x13\n\x0f\x46UNC_REVOKE_MSG\x10V\x12\x17\n\x13\x46UNC_REFRESH_QRCODE\x10W\x12\x16\n\x12\x46UNC_DECRYPT_IMAGE\x10`\x12\x11\n\rFUNC_EXEC_OCR\x10\x61\x12\x19\n\x15\x46UNC_ADD_ROOM_MEMBERS\x10p\x12\x19\n\x15\x46UNC_DEL_ROOM_MEMBERS\x10q\x12\x19\n\x15\x46UNC_INV_ROOM_MEMBERS\x10rB\r\n\x0b\x63om.iamteerb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wcf_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\013com.iamteer'
  _REQUEST.fields_by_name['ui64']._options = None
  _REQUEST.fields_by_name['ui64']._serialized_options = b'0\001'
  _WXMSG.fields_by_name['id']._options = None
  _WXMSG.fields_by_name['id']._serialized_options = b'0\001'
  _MSGTYPES_TYPESENTRY._options = None
  _MSGTYPES_TYPESENTRY._serialized_options = b'8\001'
  _ATTACHMSG.fields_by_name['id']._options = None
  _ATTACHMSG.fields_by_name['id']._serialized_options = b'0\001'
  _AUDIOMSG.fields_by_name['id']._options = None
  _AUDIOMSG.fields_by_name['id']._serialized_options = b'0\001'
  _FORWARDMSG.fields_by_name['id']._options = None
  _FORWARDMSG.fields_by_name['id']._serialized_options = b'0\001'
  _FUNCTIONS._serialized_start=2414
  _FUNCTIONS._serialized_end=3168
  _REQUEST._serialized_start=19
  _REQUEST._serialized_end=530
  _RESPONSE._serialized_start=533
  _RESPONSE._serialized_end=860
  _EMPTY._serialized_start=862
  _EMPTY._serialized_end=869
  _WXMSG._serialized_start=872
  _WXMSG._serialized_end=1062
  _TEXTMSG._serialized_start=1064
  _TEXTMSG._serialized_end=1119
  _PATHMSG._serialized_start=1121
  _PATHMSG._serialized_end=1162
  _XMLMSG._serialized_start=1164
  _XMLMSG._serialized_end=1235
  _MSGTYPES._serialized_start=1237
  _MSGTYPES._serialized_end=1334
  _MSGTYPES_TYPESENTRY._serialized_start=1290
  _MSGTYPES_TYPESENTRY._serialized_end=1334
  _RPCCONTACT._serialized_start=1337
  _RPCCONTACT._serialized_end=1472
  _RPCCONTACTS._serialized_start=1474
  _RPCCONTACTS._serialized_end=1522
  _DBNAMES._serialized_start=1524
  _DBNAMES._serialized_end=1548
  _DBTABLE._serialized_start=1550
  _DBTABLE._serialized_end=1586
  _DBTABLES._serialized_start=1588
  _DBTABLES._serialized_end=1628
  _DBQUERY._serialized_start=1630
  _DBQUERY._serialized_end=1664
  _DBFIELD._serialized_start=1666
  _DBFIELD._serialized_end=1722
  _DBROW._serialized_start=1724
  _DBROW._serialized_end=1761
  _DBROWS._serialized_start=1763
  _DBROWS._serialized_end=1797
  _VERIFICATION._serialized_start=1799
  _VERIFICATION._serialized_end=1852
  _MEMBERMGMT._serialized_start=1854
  _MEMBERMGMT._serialized_end=1897
  _USERINFO._serialized_start=1899
  _USERINFO._serialized_end=1967
  _DECPATH._serialized_start=1969
  _DECPATH._serialized_end=2004
  _TRANSFER._serialized_start=2006
  _TRANSFER._serialized_end=2058
  _ATTACHMSG._serialized_start=2060
  _ATTACHMSG._serialized_end=2117
  _AUDIOMSG._serialized_start=2119
  _AUDIOMSG._serialized_end=2158
  _RICHTEXT._serialized_start=2160
  _RICHTEXT._serialized_end=2281
  _PATMSG._serialized_start=2283
  _PATMSG._serialized_end=2321
  _OCRMSG._serialized_start=2323
  _OCRMSG._serialized_end=2363
  _FORWARDMSG._serialized_start=2365
  _FORWARDMSG._serialized_end=2411
# @@protoc_insertion_point(module_scope)
