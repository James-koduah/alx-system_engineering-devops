# Add a nginx header
Exec {
  path => ['/bin', '/usr/bin'],
}

exec { 'add nginx header' :
  command => 'sudo apt-get -y update;
  sudo apt-get -y install nginx;
  sudo sed -i "/server_name _;/a add_header X-Served-By \$HOSTNAME;" /etc/nginx/sites-available/default;
  sudo service nginx restart
}
