# puppet_install_flask.pp

# Use a variable for the Flask version for easier maintenance
$flask_version = '2.1.0'

# Install python3-pip package
package { 'python3-pip':
  ensure => present,
}

# Install Flask using pip3
exec { 'install_flask':
  command => "/usr/bin/pip3 install flask==${flask_version}",
  path    => ['/usr/bin'],
  unless  => "/usr/local/bin/flask --version | grep -q '${flask_version}'",
  require => Package['python3-pip'],
}
