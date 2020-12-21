#!/usr/bin/env bash
# puppet config nginx

exec { '/usr/bin/env apt-get -y update' : }
package { 'nginx':
  ensure => installed,
}
file { '/var/www/html/index.html' :
  content => 'Holberton School!',
}
-> file_line { 'header' :
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "\tadd_header X-Served-By ${hostname};",
  after  => 'server_name _;',
}
-> exec { 'Restaring Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
