"""
Copyright 2020 The OneFlow Authors. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import unittest
from collections import OrderedDict

import numpy as np

from oneflow.test_utils.automated_test_util import *
from oneflow.test_utils.test_util import GenArgList

import oneflow as flow
import oneflow.unittest


@flow.unittest.skip_unless_1n1d()
class TestBatchNormModule(flow.unittest.TestCase):
    @autotest(
        auto_backward=True, rtol=1e-3, atol=1e-3, check_grad_use_random_data=False
    )
    def test_batchnorm1d_module_with_random_data(test_case):
        device = random_device()
        channel = random(1, 4).to(int)
        m = torch.nn.BatchNorm1d(
            num_features=channel,
            track_running_stats=random().to(bool),
            affine=random().to(bool),
        ).to(device)
        m.train(random())
        x = random_tensor(
            ndim=3, dim0=random(1, 4), dim1=channel, requires_grad=True
        ).to(device)
        y = m(x)
        return y

    @autotest(
        auto_backward=True, rtol=1e-3, atol=1e-3, check_grad_use_random_data=False
    )
    def test_batchnorm2d_module_with_random_data(test_case):
        device = random_device()
        channel = random(1, 4).to(int)
        m = torch.nn.BatchNorm2d(
            num_features=channel,
            track_running_stats=random().to(bool),
            affine=random().to(bool),
        ).to(device)
        m.train(random())
        x = random_tensor(
            ndim=4, dim0=random(1, 4), dim1=channel, requires_grad=True
        ).to(device)
        y = m(x)
        return y

    @autotest(
        auto_backward=True, rtol=1e-3, atol=1e-3, check_grad_use_random_data=False
    )
    def test_batchnorm3d_module_with_random_data(test_case):
        device = random_device()
        channel = random(1, 4).to(int)
        m = torch.nn.BatchNorm3d(
            num_features=channel,
            track_running_stats=random().to(bool),
            affine=random().to(bool),
        ).to(device)
        m.train(random())
        x = random_tensor(ndim=5, dim1=channel, requires_grad=True).to(device)
        y = m(x)
        return y

    """
    @profile(torch.nn.BatchNorm1d) 
    def profile_BatchNorm1d(test_case):
        m1 = torch.nn.BatchNorm1d(100)
        m2 = torch.nn.BatchNorm1d(100, affine=False)
        input1 = torch.ones(20, 100)
        input2 = torch.ones(20, 100)
        out1=m1(input1)
        out2=m2(input2)

    @profile(torch.nn.BatchNorm2d) 
    def profile_BatchNorm2d(test_case):
        m1 = torch.nn.BatchNorm2d(10)
        m2 = torch.nn.BatchNorm2d(10, affine=False)
        print(type(m1),type(m2))
        input1 = torch.ones(2, 10, 8, 3)
        input2 = torch.ones(2, 10, 8, 3)
        out1=m1(input1)
        out2=m2(input2)

    @profile(torch.nn.BatchNorm3d) 
    def profile_BatchNorm3d(test_case):
        m1 = torch.nn.BatchNorm3d(10)
        m2 = torch.nn.BatchNorm3d(10, affine=False)
        input1 = torch.ones(2, 10, 5, 8, 4)
        input2 = torch.ones(2, 10, 5, 8, 4)
        out1=m1(input1)
        out2=m2(input2)
    """


if __name__ == "__main__":
    unittest.main()
