#make changes to ssh configuration file

file { '~/.ssh/config':
    ensure  => file,
    mode    => '0600',
    content => "Host *\n  IdentityFile ~/.ssh/school\n  PasswordAuthentication no\n",
}