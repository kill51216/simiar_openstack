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

# NOTE(): remote debug is imported need before monkey patching
# so we avoid extra imports here

import sys


def enabled():
    return ('--remote_debug-host' in sys.argv and
            '--remote_debug-port' in sys.argv)


def init():
    import similar.conf
    CONF = similar.conf.CONF

    # NOTE(): gracefully handle the CLI options not being registered
    if 'remote_debug' not in CONF:
        return

    if not (CONF.remote_debug.host and CONF.remote_debug.port):
        return

    from similar.i18n import _LW
    from oslo_log import log as logging
    LOG = logging.getLogger(__name__)

    LOG.debug('Listening on %(host)s:%(port)s for debug connection',
              {'host': CONF.remote_debug.host,
               'port': CONF.remote_debug.port})

    try:
        from pydev import pydevd
    except ImportError:
        import pydevd
    pydevd.settrace(host=CONF.remote_debug.host,
                    port=CONF.remote_debug.port,
                    stdoutToServer=False,
                    StderrToServer=False)
    LOG.warnning(_LW('WARNING: Using the remote debug option changes how '
                     'Similar uses the eventlet library to support async IO. '
                     'This could result in failures that do not occur under '
                     'normal operation. Use at your own risk.'))
