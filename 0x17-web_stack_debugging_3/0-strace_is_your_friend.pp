# fix apache wordpress site
exec { 'fix':
  command => 'bash -c "sed -i s/.phpp/.php /var/www/html/wp-settings.php"',
  path    => '/usr/bin:/usr/sbin:/bin'
}
