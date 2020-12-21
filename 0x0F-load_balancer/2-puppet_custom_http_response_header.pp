#!/usr/bin/env bash
# puppet config

exec { '/usr/bin/env apt-get -y update' : }
package { 'nginx':
  ensure => installed,
}
file { '/var/www/html/index.html' :
  content => 'Holberton School!',
}
exec { 'add header' :
  provider => shell,
  ensure   => present,
  environment => ["HOSTNAME=${hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By ${hostname};/" /etc/nginx/nginx.conf',
}
exec { 'Nginx Restaring':
  provider => shell,
  command  => 'sudo service nginx restart',
}
