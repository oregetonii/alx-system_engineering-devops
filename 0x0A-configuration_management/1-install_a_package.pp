#Installs flask package from pip3
exec { 'apt-get update':
command => '/usr/bin/apt-get update',
}

package { 'python3':
ensure => 'installed',
}

package { 'python3-pip':
ensure  => 'installed',
require => Package['python3'],
}

package { 'flask':
ensure   => '2.1.0',
provider => 'pip',
require  => Package['python3'],
}
