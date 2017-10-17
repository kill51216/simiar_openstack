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


from oslo_log import log
from oslo_utils import importutils
from similar.common import config
from similar import version

import similar.conf


profiler = importutils.try_import('osprofiler.opts')


CONF = similar.conf.CONF


def parse_args(argv, default_config_files=None, configure_db=True,
               init_rpc=True):
    log.register_options(CONF)
    # if CONF.similar.debug:
    #    extra_default_log_levels = ['similarclient=DEBUG']
    # else:
    #    extra_default_log_levels = ['similarclient=WARN']
    # log.set_defaults(default_log_levels=log.get_default_log_levels() +
    #                 extra_default_log_levels)
    log.set_defaults(default_log_levels=log.get_default_log_levels())
    if profiler:
        profiler.set_defaults(CONF)
    config.set_middleware_defaults()
    CONF(argv[1:],
         project='similar',
         version=version.version_string(),
         default_config_files=default_config_files)