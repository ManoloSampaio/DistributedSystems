from arcon import ArCodicionado
import time
import grpc
import concurrent.futures
import HAgrpc_pb2_grpc

port = input('Porta grpc:')
name = input('Object Name')
server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
HAgrpc_pb2_grpc.add_ActuatorGRPCServicer_to_server(
                                ArCodicionado('ar1','localhost',52000,45000), server)
server.add_insecure_port(f'[::]:{port}')
server.start()
server.wait_for_termination()