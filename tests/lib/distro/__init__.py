# Copyright (c) 2020 SUSE LINUX GmbH
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""The Hardware module should take care of the operating system abstraction
through images.
libcloud will provide a common set of cloud-agnostic objects such as Node[s]
We might extend the Node object to have an easy way to run arbitrary commands
on the node such as Node.execute().
There will be a challenge where those arbitrary commands differ between OS's;
this is an abstraction that is not yet well figured out, but will likely
take the form of cloud-init or similar bringing the target node to an
expected state."""

from tests import config
from tests.lib.distro.opensuse import openSUSE_k8s
from tests.lib.distro.sles import SLES_CaaSP


def get_distro():
    if config.DISTRO == 'openSUSE_k8s':
        return openSUSE_k8s
    elif config.DISTRO == 'SLES_CaaSP':
        return SLES_CaaSP
    else:
        raise Exception('Unknown distro {}'.format(config.DISTRO))
