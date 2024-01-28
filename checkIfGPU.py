# import torch

# print(torch.cuda.is_available())
# print(torch.cuda.current_device())
# print(torch.cuda.get_device_name(0))
import torch

print("Is CUDA available: ", torch.cuda.is_available())

if torch.cuda.is_available():
    print("Current CUDA device: ", torch.cuda.current_device())
    print("CUDA device name: ", torch.cuda.get_device_name(0))
else:
    print("CUDA is not available. PyTorch will use CPU.")

print("PyTorch version: ", torch.__version__)