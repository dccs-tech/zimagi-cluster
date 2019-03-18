from systems.command import profile


class Provisioner(profile.BaseProvisioner):

    def priority(self):
        return 2


    def ensure(self, name, config):
        networks = self.profile.pop_values('network', config)
        groups = self.profile.pop_values('group_names', config)

        def process(network):
            self.command.exec_local('subnet save', {
                'network_name': network,
                'subnet_name': name,
                'subnet_fields': config,
                'group_names': groups
            })
        if not networks:
            self.command.error("Subnet {} requires 'network' field".format(name))

        self.command.run_list(networks, process)


    def describe(self, subnet):
        return { 'network': subnet.network.name }