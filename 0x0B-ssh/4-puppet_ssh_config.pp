# ssh_config file using puppet
include stdlib

file_line { 'Turn off passwd auth':
  ensure => 'present',
  line   => 'PasswordAuthentication no',
  path   => '/etc/ssh/ssh_config',
  
}

file_line { 'Declare identity file':
  ensure => 'present',
  line   => 'IdentityFile /home/vagrant/.ssh/holberton',
  path   => '/etc/ssh/ssh_config',

}

