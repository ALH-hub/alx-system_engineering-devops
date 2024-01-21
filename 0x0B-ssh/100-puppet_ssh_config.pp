#make changes to ssh configuration file

file { '/home/oumate/.ssh/config':
    ensure  => file,
    owner   => 'oumate',
    group   => 'oumate',
    mode    => '0600',
    content => "Host *\n  IdentityFile ~/.ssh/school\n  PasswordAuthentication no\n",
}