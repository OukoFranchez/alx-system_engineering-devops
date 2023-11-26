# client configuration file with puppet

exec {'SSH configuration':
    command => "echo 'Host 54.172.129.154\n\tPasswordAuthentication no\n\tIdentityFile ~/.ssh/school' >> /etc/ssh/ssh_config",
    path => '/usr/bin'
}
