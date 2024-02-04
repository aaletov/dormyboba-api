# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import v1api_pb2 as v1api__pb2


class DormybobaCoreStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GenerateVerificationCode = channel.unary_unary(
                '/api.DormybobaCore/GenerateVerificationCode',
                request_serializer=v1api__pb2.GenerateVerificationCodeRequest.SerializeToString,
                response_deserializer=v1api__pb2.GenerateVerificationCodeResponse.FromString,
                )
        self.GetRoleByVerificationCode = channel.unary_unary(
                '/api.DormybobaCore/GetRoleByVerificationCode',
                request_serializer=v1api__pb2.GetRoleByVerificationCodeRequest.SerializeToString,
                response_deserializer=v1api__pb2.GetRoleByVerificationCodeResponse.FromString,
                )
        self.CreateUser = channel.unary_unary(
                '/api.DormybobaCore/CreateUser',
                request_serializer=v1api__pb2.CreateUserRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetAllInstitutes = channel.unary_unary(
                '/api.DormybobaCore/GetAllInstitutes',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=v1api__pb2.GetAllInstitutesResponse.FromString,
                )
        self.GetInstituteByName = channel.unary_unary(
                '/api.DormybobaCore/GetInstituteByName',
                request_serializer=v1api__pb2.GetInstituteByNameRequest.SerializeToString,
                response_deserializer=v1api__pb2.GetInstituteByNameResponse.FromString,
                )
        self.GetAllAcademicTypes = channel.unary_unary(
                '/api.DormybobaCore/GetAllAcademicTypes',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=v1api__pb2.GetAllAcademicTypesResponse.FromString,
                )
        self.GetAcademicTypeByName = channel.unary_unary(
                '/api.DormybobaCore/GetAcademicTypeByName',
                request_serializer=v1api__pb2.GetAcademicTypeByNameRequest.SerializeToString,
                response_deserializer=v1api__pb2.GetAcademicTypeByNameResponse.FromString,
                )
        self.CreateMailing = channel.unary_unary(
                '/api.DormybobaCore/CreateMailing',
                request_serializer=v1api__pb2.CreateMailingRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.CreateQueue = channel.unary_unary(
                '/api.DormybobaCore/CreateQueue',
                request_serializer=v1api__pb2.CreateQueueRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.AddPersonToQueue = channel.unary_unary(
                '/api.DormybobaCore/AddPersonToQueue',
                request_serializer=v1api__pb2.AddPersonToQueueRequest.SerializeToString,
                response_deserializer=v1api__pb2.AddPersonToQueueResponse.FromString,
                )
        self.RemovePersonFromQueue = channel.unary_unary(
                '/api.DormybobaCore/RemovePersonFromQueue',
                request_serializer=v1api__pb2.RemovePersonFromQueueRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.PersonCompleteQueue = channel.unary_unary(
                '/api.DormybobaCore/PersonCompleteQueue',
                request_serializer=v1api__pb2.PersonCompleteQueueRequest.SerializeToString,
                response_deserializer=v1api__pb2.PersonCompleteQueueResponse.FromString,
                )
        self.AssignDefect = channel.unary_unary(
                '/api.DormybobaCore/AssignDefect',
                request_serializer=v1api__pb2.AssignDefectRequest.SerializeToString,
                response_deserializer=v1api__pb2.AssignDefectResponse.FromString,
                )


class DormybobaCoreServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GenerateVerificationCode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRoleByVerificationCode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllInstitutes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetInstituteByName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllAcademicTypes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAcademicTypeByName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateMailing(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateQueue(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddPersonToQueue(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemovePersonFromQueue(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PersonCompleteQueue(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AssignDefect(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DormybobaCoreServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GenerateVerificationCode': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateVerificationCode,
                    request_deserializer=v1api__pb2.GenerateVerificationCodeRequest.FromString,
                    response_serializer=v1api__pb2.GenerateVerificationCodeResponse.SerializeToString,
            ),
            'GetRoleByVerificationCode': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRoleByVerificationCode,
                    request_deserializer=v1api__pb2.GetRoleByVerificationCodeRequest.FromString,
                    response_serializer=v1api__pb2.GetRoleByVerificationCodeResponse.SerializeToString,
            ),
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=v1api__pb2.CreateUserRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetAllInstitutes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllInstitutes,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=v1api__pb2.GetAllInstitutesResponse.SerializeToString,
            ),
            'GetInstituteByName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetInstituteByName,
                    request_deserializer=v1api__pb2.GetInstituteByNameRequest.FromString,
                    response_serializer=v1api__pb2.GetInstituteByNameResponse.SerializeToString,
            ),
            'GetAllAcademicTypes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllAcademicTypes,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=v1api__pb2.GetAllAcademicTypesResponse.SerializeToString,
            ),
            'GetAcademicTypeByName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAcademicTypeByName,
                    request_deserializer=v1api__pb2.GetAcademicTypeByNameRequest.FromString,
                    response_serializer=v1api__pb2.GetAcademicTypeByNameResponse.SerializeToString,
            ),
            'CreateMailing': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateMailing,
                    request_deserializer=v1api__pb2.CreateMailingRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'CreateQueue': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateQueue,
                    request_deserializer=v1api__pb2.CreateQueueRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'AddPersonToQueue': grpc.unary_unary_rpc_method_handler(
                    servicer.AddPersonToQueue,
                    request_deserializer=v1api__pb2.AddPersonToQueueRequest.FromString,
                    response_serializer=v1api__pb2.AddPersonToQueueResponse.SerializeToString,
            ),
            'RemovePersonFromQueue': grpc.unary_unary_rpc_method_handler(
                    servicer.RemovePersonFromQueue,
                    request_deserializer=v1api__pb2.RemovePersonFromQueueRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'PersonCompleteQueue': grpc.unary_unary_rpc_method_handler(
                    servicer.PersonCompleteQueue,
                    request_deserializer=v1api__pb2.PersonCompleteQueueRequest.FromString,
                    response_serializer=v1api__pb2.PersonCompleteQueueResponse.SerializeToString,
            ),
            'AssignDefect': grpc.unary_unary_rpc_method_handler(
                    servicer.AssignDefect,
                    request_deserializer=v1api__pb2.AssignDefectRequest.FromString,
                    response_serializer=v1api__pb2.AssignDefectResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.DormybobaCore', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DormybobaCore(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GenerateVerificationCode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.DormybobaCore/GenerateVerificationCode',
            v1api__pb2.GenerateVerificationCodeRequest.SerializeToString,
            v1api__pb2.GenerateVerificationCodeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRoleByVerificationCode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.DormybobaCore/GetRoleByVerificationCode',
            v1api__pb2.GetRoleByVerificationCodeRequest.SerializeToString,
            v1api__pb2.GetRoleByVerificationCodeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.DormybobaCore/CreateUser',
            v1api__pb2.CreateUserRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllInstitutes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.DormybobaCore/GetAllInstitutes',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            v1api__pb2.GetAllInstitutesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetInstituteByName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.DormybobaCore/GetInstituteByName',
            v1api__pb2.GetInstituteByNameRequest.SerializeToString,
            v1api__pb2.GetInstituteByNameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllAcademicTypes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.DormybobaCore/GetAllAcademicTypes',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            v1api__pb2.GetAllAcademicTypesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAcademicTypeByName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.DormybobaCore/GetAcademicTypeByName',
            v1api__pb2.GetAcademicTypeByNameRequest.SerializeToString,
            v1api__pb2.GetAcademicTypeByNameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateMailing(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.DormybobaCore/CreateMailing',
            v1api__pb2.CreateMailingRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateQueue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.DormybobaCore/CreateQueue',
            v1api__pb2.CreateQueueRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddPersonToQueue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.DormybobaCore/AddPersonToQueue',
            v1api__pb2.AddPersonToQueueRequest.SerializeToString,
            v1api__pb2.AddPersonToQueueResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemovePersonFromQueue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.DormybobaCore/RemovePersonFromQueue',
            v1api__pb2.RemovePersonFromQueueRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PersonCompleteQueue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.DormybobaCore/PersonCompleteQueue',
            v1api__pb2.PersonCompleteQueueRequest.SerializeToString,
            v1api__pb2.PersonCompleteQueueResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AssignDefect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.DormybobaCore/AssignDefect',
            v1api__pb2.AssignDefectRequest.SerializeToString,
            v1api__pb2.AssignDefectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
