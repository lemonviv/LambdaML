import argparse

import os
import sys
import torch
import torch.distributed as dist
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from math import ceil
from torch.multiprocessing import Process

sys.path.append("../")
# sys.path.append("../../../")
# sys.path.append("../../../")

from ec2.trainer import Trainer
from ec2.data_partition import partition_cifar10

from pytorch_model.resnet import ResNet50


def dist_is_initialized():
    if dist.is_available():
        if dist.is_initialized():
            return True
    return False


def run(args):
    """ Distributed Synchronous SGD Example """
    device = torch.device('cuda' if torch.cuda.is_available() and not args.no_cuda else 'cpu')
    torch.manual_seed(1234)

    train_loader, bsz, test_loader = partition_cifar10(args.batch_size, args.root, download=True)
    num_batches = ceil(len(train_loader.dataset) / float(bsz))

    model = ResNet50()
    optimizer = optim.SGD(model.parameters(), lr=args.learning_rate, momentum=0.9)

    trainer = Trainer(model, optimizer, train_loader, test_loader, args, device)

    trainer.fit(args.epochs, is_dist=dist_is_initialized())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--backend', type=str, default='gloo', help='Name of the backend to use.')
    parser.add_argument(
        '-i',
        '--init-method',
        type=str,
        default='tcp://127.0.0.1:23456',
        help='URL specifying how to initialize the package.')
    parser.add_argument('-s', '--world-size', type=int, default=1, help='Number of processes participating in the job.')
    parser.add_argument('-r', '--rank', type=int, default=0, help='Rank of the current process.')
    parser.add_argument('--epochs', type=int, default=20)
    parser.add_argument('--no-cuda', action='store_true')
    parser.add_argument('-lr', '--learning-rate', type=float, default=1e-3)
    parser.add_argument('--root', type=str, default='data')
    parser.add_argument('--batch-size', type=int, default=32*10)
    args = parser.parse_args()
    print(args)

    if args.world_size > 1:
        dist.init_process_group(backend=args.backend, init_method=args.init_method, world_size=args.world_size, rank=args.rank)

    run(args)


if __name__ == '__main__':
    main()


# def init_processes(rank, size, fn, backend='gloo'):
#     """ Initialize the distributed environment. """
#     os.environ['MASTER_ADDR'] = '127.0.0.1'
#     os.environ['MASTER_PORT'] = '29500'
#     dist.init_process_group(backend, rank=rank, world_size=size)
#     fn(rank, size)


# def run_local():
#     size = 2
#     processes = []
#     for rank in range(size):
#         p = Process(target=init_processes, args=(rank, size, run))
#         p.start()
#         processes.append(p)

#     for p in processes:
#         p.join()
