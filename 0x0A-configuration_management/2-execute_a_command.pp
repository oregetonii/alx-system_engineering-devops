#Manifest that kills a process named killmenow
exec { 'pkill killmenow':
command => '/usr/bin/pkill -f killmenow',
unless  => '/usr/bin/pgrep -f killmenow',
}
