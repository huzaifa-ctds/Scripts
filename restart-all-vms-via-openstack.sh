openstack server list | grep dev-hmb | awk '{ print $4 }' >serverlist
servers=$(cat serverlist)
for server in $servers
do
  echo openstack server reboot $server  
done
