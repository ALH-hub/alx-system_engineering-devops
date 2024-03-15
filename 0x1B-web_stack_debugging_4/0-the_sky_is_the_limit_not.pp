#increase the amount of traffic to handle
#increase file limit
exec { 'nginx-fix':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

#nginx restart
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
