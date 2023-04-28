# Kill a process

exec { 'killmenow':
  command  => 'pkill killmenow'
}
