from quantum.tests.unit import test_db_plugin
from catalyst.common import config


class CatalystPluginTestBase(object):
    def setUp(self):
        # Make sure at each test a new instance of the plugin is returned
        test_db_plugin.QuantumManager._instance = None

        self._tenant_id = 'test-tenant'

        json_deserializer = test_db_plugin.JSONDeserializer()
        self._deserializers = {
            'application/json': json_deserializer,
        }

        plugin = 'catalyst.plugin.CatalystPluginV2'
        config.CONF.set_override('core_plugin', plugin)
        self.api = test_db_plugin.APIRouter()
        self._skip_native_bulk = False


class TestNetworksV2(CatalystPluginTestBase, test_db_plugin.TestNetworksV2):
    pass


class TestPortsV2(CatalystPluginTestBase, test_db_plugin.TestPortsV2):
    pass
