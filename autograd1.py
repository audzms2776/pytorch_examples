import torch
from torch.autograd import Variable

x = Variable(torch.Tensor([1]), requires_grad=True)
w = Variable(torch.Tensor([2]), requires_grad=True)
b = Variable(torch.Tensor([3]), requires_grad=True)

y = w * x + b

y.backward()

print(x.grad, w.grad, b.grad)
