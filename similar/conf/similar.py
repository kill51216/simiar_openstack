#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_config import cfg

similar_group = cfg.OptGroup(
    'similar',
    title='Similar Options',
    help='Configuration options for the Similar service'
)

similar_opts = [
    cfg.BoolOpt('debug',
                default=False,
                help='Enable or disable debug logging with similarclient')
]


def register_opts(conf):
    conf.register_group(similar_group)
    conf.register_opts(similar_opts, group=similar_group)


def list_opts():
    return {similar_group: similar_opts}
