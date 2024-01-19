#Creation of a file called school in /tmp
#file with permission 0744
#owner and group set to www-data
#contains 'I love Puppet'

file {'school':
        path    => '/tmp/school',
        mode    => '0744',
        owner   => 'www-data',
        group   => 'www-data',
        content => 'I love Puppet',
}