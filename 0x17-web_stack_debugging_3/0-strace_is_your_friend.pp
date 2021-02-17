# debugs apache 500 error
exec { 'replace a word' :
  command => 'sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php',
  path    =>  '/usr/local/bin/:/bin/'
}
