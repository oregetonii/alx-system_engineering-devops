#Manifest that kills a process named killmenow
exec { 'killmenow':
command => '/bin/pkill -f killmenow',
unless  => '/bin/pgrep -f killmenow',
}
