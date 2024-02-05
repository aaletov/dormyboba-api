import sys
from pathlib import Path
sys.path.append(Path(__file__).resolve().parent.parent)
print('\n'.join(sys.path)) ###
import v1api_pb2
import v1api_pb2_grpc