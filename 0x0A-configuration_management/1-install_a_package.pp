# install flask from pip3

# Resource declaration
package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
}

# install dependency
package { 'Werkzeug':
    ensure   => '2.1.1',
    provider => 'pip3',
}
