#!/usr/bin/perl
 
 
use HTTP::Request;
use LWP::Simple;
use LWP::UserAgent;
 
 
if ($^O =~ /MSWin32/) {system("cls"); system("color a");
}else { system(""); }
print "\t \n";
 
open(tarrget,"<$ARGV[0]") or die "$!";
while(<tarrget>){
chomp($_);
$target = $_;
if($target !~ /http:\/\//)
{
$target = "http://$target";
}
 
$website = $target."/index.php?option=com_jdownloads&Itemid=0&view=upload";
 
$req=HTTP::Request->new(GET=>$website);
$ua=LWP::UserAgent->new();
$ua->timeout(30);
$response=$ua->request($req);
if($response->content=~ /Soumettre/ ||
   $response->content=~ /Submit/    
 
)
 {
 $Messageee ="GOOD";
open (TEXT, '>>GOOD.txt');
print TEXT "$target => $Messageee\n";
close (TEXT);
}
else {
$Messageee = "ERROR";
}
print ">> $target => $Messageee\n";
}
