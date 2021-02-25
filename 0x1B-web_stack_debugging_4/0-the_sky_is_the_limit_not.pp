#increases the open file limit for nginx
exec { 'limit vers l infini':
command => 'sed -i "s/15/4069/g" /etc/default/nginx | service nginx restart',
path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
