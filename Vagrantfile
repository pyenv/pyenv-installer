VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.box = "ubuntu/trusty64"

    config.vm.synced_folder "vagrant-salt/", "/srv/salt/"
    config.vm.provision :salt do |saltCnf|
        saltCnf.verbose = true
        saltCnf.minion_config = './vagrant-salt/minion'
        saltCnf.run_highstate = true
        saltCnf.bootstrap_options = '-D'
        saltCnf.temp_config_dir = '/tmp'
    end
end
