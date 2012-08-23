from quantum.db.db_base_plugin_v2 import QuantumDbPluginV2


class CatalystQuantumPluginV2(QuantumDbPluginV2):

    def create_network(self, context, network):
        return super(CatalystQuantumPluginV2, self).create_network(context, network)

    def update_network(self, context, id, network):
        return super(CatalystQuantumPluginV2, self).update_network(context, id, network)

    def delete_network(self, context, id):
        super(CatalystQuantumPluginV2, self).delete_network(context, id)

    def create_port(self, context, port):
        return super(CatalystQuantumPluginV2, self).create_port(context, port)

    def update_port(self, context, id, port):
        return super(CatalystQuantumPluginV2, self).update_port(context, id, port)

    def delete_port(self, context, id):
        super(CatalystQuantumPluginV2, self).delete_port(context, id)
