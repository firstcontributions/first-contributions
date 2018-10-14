import grpc
import time

import chat_server_grpc_pb2, chat_server_grpc_pb2_grpc
import threading
import Queue


def generate_input_messages():
    """
    :return:
    """
    new_msg = raw_input("->")
    return chat_server_grpc_pb2.Request(message=str(new_msg))
    # for msg in msgs:
    #     time.sleep(2)
    #     yield chat_server_grpc_pb2.Request(message=msg)


class ReadThread(threading.Thread):
    """
    read thread, read data from the console
    """
    def __init__(self, stub, response_queue):
        """

        :param stub: stub object from grpc
        :param response_queue:
        """
        threading.Thread.__init__(self)
        self.stub = stub
        self.response_queue = response_queue

    def run(self):
        """
        method to execute to run the thread
        :return:
        """
        print("Enter new messages: ")
        response = self.stub.Communicate(generate_input_messages())
        self.response_queue.put(response)


class WriteThread(threading.Thread):
    """
    write thread, write data to the console
    """
    def __init__(self, stub, response_queue):
        """
        initialize the write thread
        """
        threading.Thread.__init__(self)
        self.stub = stub
        self.response_queue = response_queue

    def run(self):
        """
        method to execute to run the thread
        :return:
        """
        while True:
            response = self.response_queue.get(block=True)
            print(response.message)


def run():
    """

    :return:
    """
    channel = grpc.insecure_channel('localhost:50051')
    stub = chat_server_grpc_pb2_grpc.ChatServerStub(channel)
    print("Chat server-----------")

    response_queue = Queue.Queue()

    # this implementation is incorrect as it attempts to read and write using 2 threads in the same terminal
    read_thread = ReadThread(stub, response_queue)
    read_thread.start()

    write_thread = WriteThread(stub, response_queue)
    write_thread.start()


if __name__ == '__main__':
    run()