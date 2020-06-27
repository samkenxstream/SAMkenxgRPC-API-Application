import grpc
import time
from concurrent import futures
import service_pb2_grpc
import service_pb2
import logging

_ONE_DAY_IN_SECONDS = 60 * 60 * 24



# create a class to define the server functions, derived from service_pb2_grpc.CreateDataServicer
class CreateDataServicer(service_pb2_grpc.CreateDataServicer):
# the index.html is exposed here
# the request and response are of the data type service_pb2.TimeseriesDataResponse

    def Loadtimeseries(self, request, context):
        result = service_pb2.GetData()
        result.time, result.meterusage = request.time, request.meterusage
        return result

        
#create a gRPC server

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
# use the generated function `add_CreateDataServicer_to_server`
# to add the defined class to the server
    service_pb2_grpc.add_CreateDataServicer_to_server(CreateDataServicer(), server)
# listen on port 50051
    print('Starting server. Listening on port 50051.')
    server.add_insecure_port('[::]:50051')
    server.start()
# since server.start() will not block,
# a sleep-loop is added to keep alive
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        logging.debug('GRPC stop')
        server.stop(0)
if __name__ == '__main__':
    serve()