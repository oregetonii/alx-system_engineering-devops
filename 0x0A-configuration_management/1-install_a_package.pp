#Installs flask package from pip3
package { 'flask':
ensure   => '2.1.0',
provider => 'pip',
}
class manage-python {
class {'pyhton':}
}
