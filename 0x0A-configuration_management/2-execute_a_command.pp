# A manifest that kills a process named killmenow

# Resource declaration
exec { 'killmenow':
    command => 'pkill killmenow',
    path    => '/usr/bin', # Corrected the path
}
