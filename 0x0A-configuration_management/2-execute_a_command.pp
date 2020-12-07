# a Puppet Manifest that kills a process
exec { 'killmenow':
  command  => 'pkill -f killmenow',
  provider => 'shell',
}
