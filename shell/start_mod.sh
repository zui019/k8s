#/bin/bash
list1='br_netfilter ip6_udp_tunnel ip_set ip_set_hash_ip
ip_set_hash_net iptable_filter iptable_mangle iptable_nat
iptable_raw nf_conntrack nf_conntrack_ipv4 nf_conntrack_netlink
nf_defrag_ipv4 nf_nat nf_nat_ipv4 nf_nat_masquerade_ipv4 nfnetlink udp_tunnel
veth vxlan x_tables xt_addrtype xt_comment xt_conntrack xt_mark xt_multiport
xt_nat xt_recent xt_set xt_statistic xt_tcpudp'
for i in $list1;
do
 echo `'modprobe'  $i`;
done
