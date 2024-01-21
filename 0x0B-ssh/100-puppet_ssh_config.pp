#make changes to ssh configuration file

file_line { 'host servers':
    ensure  => 'present',
    path    => '/etc/ssh/ssh_config',
    line    => 'Host *',
}

file_line { 'no PasswordAuthentication':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
}

file_line { 'IdentityFile':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
}