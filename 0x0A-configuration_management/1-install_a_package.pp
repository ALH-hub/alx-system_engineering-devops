#install flask package

package {'Flask':
    name     => 'Flask',
    ensure   => '2.1.0',
    provider => 'pip3',
}