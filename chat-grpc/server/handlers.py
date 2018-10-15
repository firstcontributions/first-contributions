import chat_server_grpc_pb2, chat_server_grpc_pb2_grpc as chat_server_grpc


class ChatServerService(chat_server_grpc.ChatServerServicer):

    def __init__(self):
        """

        """
        pass

    def Communicate(self, request, context):
        """

        :param request:
        :param context:
        :return:
        """
        return chat_server_grpc_pb2.Response(message=request.message)

    # def Communicate(self, request_iterator, context):
    #     """
    #
    #     :param request_iterator: request_iterator as this is the request streaming rpc, response is also
    #     streaming rpc
    #     :param context:
    #     :return: response is also streamed
    #     """
    #     for request in request_iterator:
    #         # simply ping
    #         yield chat_server_grpc_pb2.Response(message=request.message)

