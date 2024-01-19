#install flask package

exec {'install_flask':
i    command => 'pip3 install Flask==2.1.0',
}