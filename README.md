# Pentest Tools Framework (exploits, Scanner, Password.)

<h4 align="center"><img src="https://raw.githubusercontent.com/3xploit-db/Pentest-Tools-Framework/master/core/logo/logo.jpg" width="300px" height="300px">

</a>
<h4 align="center">Details</h4>                
<p align="center">
  </a>
  <a href="https://ru.m.wikipedia.org/wiki/python">
    <img src="https://img.shields.io/badge/language-python-blue.svg">
 </a>
  <a href="https://github.com/3xploit-db/Pentest-Tools-Framework">
    <img src="https://img.shields.io/badge/version-V.2.2[Beta]-green.svg">
 </a>
   <a href="https://t.me/WongNdesoCok">
   <img src="https://img.shields.io/badge/telegram--blue.svg">
   </a>
  <a href="https://github.com/3xploit-db/Pentest-Tools-Framework/releases">
   <img src="https://img.shields.io/badge/release-V.2.1[Beta]-red.svg">
   </a>
   <a href="https://github.com/3xploit-db/Pentest-Tools-Framework/blob/master/LICENSE">
   <img src="https://img.shields.io/badge/LICENSE-red.svg">
   </a>
 </a>
</p>
<center><table><tr>
<td><img src="core/logo/help.jpg" width="250px" height="250px"></td>
<td><img src="core/logo/exploit.jpg" width="250px" height="250px"></td>
<td><img src="core/logo/Scanner.jpg" width="250px" height="250px"></td>
 </tr></table></center>


# NEWS Modules PTF UPDATE!
> PTF OPtions


            -------------------------------------------------------------------------------------
            |                                  Global Option                                    |
            -------------------------------------------------------------------------------------
            |  Command                                      Description                         |
            |-----------------------------------------------------------------------------------|
            | show modules                    |  Look this modules                              |
            | show options                    |  Show Current Options Of Selected Module        |
            | ipconfig                        |  Network Informasion                            |
            | shell                           |  Execution Command Shell >[ctrl+C exit shell ]  |
            | use                             |  Select Tipe Module For Use                     |
            | set                             |  Select Modules For Use                         |
            | run                             |  Excute modules                                 |
            | update                          |  Update Pentest Framework                       |
            | banner                          |  PTF Banner                                     |
            | about                           |  Informasion Tools                              |
            | credits                         |  Credits && Thanks                              |
            | clear                           |  Clean Pentest input/output                     |
            | exit                            |  Exit the progam                                |
            -------------------------------------------------------------------------------------


> Modules

<img src="https://img.shields.io/badge/exploits-46-red.svg">

            +-----------------------------------------------------------------------------------------------------------------------------------+
            | EXPLOITS                                                                                                                          |
            -------------------------------------------------------------------------------------------------------------------------------------
            |     COMMANDS                                 Rank                                   Description                                   |
            -------------------------------------------------------------------------------------------------------------------------------------
            | exploit/abrt_privilege_escalation        | normal    |   ABRT - sosreport Privilege Escalation                                    |
            | exploit/web_delivery                     | good      |   Script Web Delivery                                                      |
            | exploit/apache                           | good      |   Apache exploit                                                           |
            | exploit/shellshock                       | good      |   cgi-bin/vulnerable shellshock                                            |
            | exploit/davtest                          | good      |   Testing tool for webdav server                                           |
            | exploit/auto_sql                         | good      |   auto with sqlmap                                                         |
            | exploit/ldap_buffer_overflow             | normal    |   Apache module mod_rewrite LDAP protocol Buffer Overflow                  |
            | exploit/vbulletin_rce                    | good      |   vBulletin 5.x 0day pre-quth RCE exploit                                  |
            | exploit/cmsms_showtime2_rce              | normal    |   CMS Made Simple (CMSMS) Showtime2 File Upload RCE                        |
            | exploit/awind_snmp_exec                  | good      |   AwindInc SNMP Service Command Injection                                  |
            | exploit/webmin_packageup_rce             | excellent |   Webmin Package Updates Remote Command Execution                          |
            | exploit/samsung_knox_smdm_url            | good      |   Samsung Galaxy KNOX Android Browser RCE                                  |
            | exploit/cisco_dcnm_upload_2019           | excellent |   Cisco Data Center Network Manager Unauthenticated Remote Code Execution  |
            | exploit/zenworks_configuration           | excellent |   Novell ZENworks Configuration Management Arbitrary File Upload           |
            | exploit/cisco_ucs_rce                    | excellent |   Cisco UCS Director Unauthenticated Remote Code Execution                 |
            | exploit/sonicwall                        | normal    |   Sonicwall SRA <= v8.1.0.2-14sv remote exploit                            |
            | exploit/bluekeep                         | good      |   cve 2019 0708 bluekeep rce                                               |
            | exploit/eternalblue                      | good      |   MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption           |
            | exploit/inject_html                      | normal    |   Inject Html code in all visited webpage                                  |
            | exploit/robots                           | normal    |   robots.txt Detected                                                      |
            | exploit/jenkins_script_console           | good      |   Jenkins-CI Script-Console Java Execution                                 |
            | exploit/php_thumb_shell_upload           | good      |   php shell uploads                                                        |
            | exploit/cpanel_bruteforce                | normal    |   cpanel bruteforce                                                        |
            | exploit/cms_rce                          | normal    |   CMS Made Simple 2.2.7 - (Authenticated) Remote Code Execution            |
            | exploit/joomla_com_hdflayer              | manual    |   joomla exploit hdflayer                                                  |
            | exploit/wp_symposium_shell_upload        | good      |   symposium shell upload                                                   |
            | exploit/joomla0day_com_myngallery        | good      |   exploits com myngallery                                                  |
            | exploit/jm_auto_change_pswd              | normal    |   vulnerability                                                            |
            | exploit/android_remote_access            | expert    |   Remote Acces Administrator (RAT)                                         |
            | exploit/power_dos                        | manual    |   Denial Of Service                                                        |
            | exploit/tp_link_dos                      | normal    |   TP_LINK DOS, 150M Wireless Lite N Router, Model No. TL-WR740N            |
            | exploit/joomla_com_foxcontact            | high      |   joomla foxcontact                                                        |
            | exploit/joomla_simple_shell              | high      |   joomla simple shell                                                      |
            | exploit/joomla_comfields_sqli_rce        | high      |   Joomla Component Fields SQLi Remote Code Execution                       |
            | exploit/inject_javascript                | normal    |   Inject Javascript code in all visited webpage                            |
            | exploit/dns_bruteforce                   | high      |   Dns Bruteforce with nmap                                                 |
            | exploit/dos_attack                       | normal    |   hping3 dos attack                                                        |
            | exploit/shakescreen                      | high      |   Shaking Web Browser content                                              |
            | exploit/bypass_waf                       | normal    |   bypass WAf                                                               |
            | exploit/enumeration                      | high      |   simple enumeration                                                       |
            | exploit/restrict_anonymous               | normal    |   obtain credentials                                                       |
            | exploit/openssl_heartbleed               | high      |   dump openssl_heartbleed                                                  |
            | exploit/samba                            | good      |   Samba EXploits                                                           |
            | exploit/smb                              | good      |   Albitary samba exploit                                                   |
            | exploit/webview_addjavascriptinterface   | good      |   Android Browser and WebView addJavascriptInterface Code Execution        |
            -------------------------------------------------------------------------------------------------------------------------------------


<img src="https://img.shields.io/badge/scanners-59-red.svg">

            +------------------------------------------------------------------------------------------------------------------------------------+
            | SCANNERS                                                                                                                           |
            --------------------------------------------------------------------------------------------------------------------------------------
            |     COMMANDS                                         Rank                                   Description                            |
            --------------------------------------------------------------------------------------------------------------------------------------
            | scanner/enumiax                                    | good   |       protocol username enumeration                                  |
            | scanner/wordpress_user_dislosure                   | normal |       wordpress 5.3 User Disclosure                                  |
            | scanner/botnet_scanning                            | normal |       Bootnet Scanning, first need to find the botnet IP             |
            | scanner/check_ssl_certificate                      | normal |       SSL Certificate                                                |
            | scanner/http_services                              | normal |       Gather page titles from HTTP services                          |
            | scanner/dnsrecon                                   | normal |       Record enumeration                                             |
            | scanner/sslscan                                    | normal |       SSL Scanner                                                    |
            | scanner/ssl_cert                                   | normal |       Nmap script ssl-cert                                           |
            | scanner/dns_zone_transfer                          | normal |       Dns Zone transfer                                              |
            | scanner/dns_bruteforce                             | normal |       Dns Bruteforce                                                 |
            | scanner/zone_walking                               | normal |       Zone walking                                                   |
            | scanner/web_services                               | normal |       Get HTTP headers of web services                               |
            | scanner/http_enum                                  | normal |       Find web apps from known paths                                 |
            | scanner/ddos_reflectors                            | normal |       Scan for UDP DDOS reflectors                                   |
            | scanner/grabbing_detection                         | normal |       Lighter banner grabbing detection                              |
            | scanner/discovery                                  | normal |       Scan selected ports - ignore discovery                         |
            | scanner/bluekeep                                   | good   |       CVE-2019-0708 BlueKeep Microsoft Remote Desktop RCE Check      |
            | scanner/drupal_scan                                | good   |       drupal scanner                                                 |
            | scanner/eternalblue                                | good   |       SMB RCE Detection                                              |
            | scanner/header                                     | good   |       header Scanner with nmap                                       |
            | scanner/firewalk                                   | good   |       firewalk                                                       |
            | scanner/whois                                      | high   |       whois                                                          |
            | scanner/dmitry                                     | good   |       Information Gathering Tool                                     |
            | scanner/admin_finder                               | normal |       Admin finder                                                   |
            | scanner/heartbleed                                 | normal |       heartbleed scanner vulnerability                               |
            | scanner/wordpress_scan                             | normal |       wordpress scanner                                              |
            | scanner/ssl_scanning                               | good   |       SSL Vulnerability Scanning                                     |
            | scanner/dns_bruteforce                             | normal |       dns bruteforce                                                 |
            | scanner/nmap_scanner                               | normal |       port scanners nmap                                             |
            | scanner/https_discover                             | normal |       https discover                                                 |
            | scanner/smb_scanning                               | good   |       scan vulnerable SMB server                                     |
            | scanner/joomla_vulnerability_scanners              | high   |       vulnerability                                                  |
            | scanner/mysql_empty_password                       | good   |       mysql empty password Detected                                  |
            | scanner/joomla_scanners_v.2                        | good   |       joomla scaning                                                 |
            | scanner/joomla_scanners_v3                         | normal |       joomla scaning                                                 |
            | scanner/jomscan_v4                                 | good   |       scan joomla                                                    |
            | scanner/webdav_scan                                | normal |       webdav scan vulnerable                                         |
            | scanner/joomla_sqli_scanners                       | high   |       vulnerability scanners                                         |
            | scanner/lfi_scanners                               | good   |       lfi bug scan                                                   |
            | scanner/port_scanners                              | manual |       port scan                                                      |
            | scanner/dir_search                                 | high   |       directory webscan                                              |
            | scanner/dir_bruteforce                             | good   |       directory Scanning                                             |
            | scanner/wordpress_user_scan                        | good   |       get wordpress username                                         |
            | scanner/cms_war                                    | high   |       FULL SCAN ALL WEBSITES                                         |
            | scanner/usr_pro_wordpress_auto_find                | norma  |       find user vulnerability                                        |
            | scanner/nmap_vuln                                  | normal |       vulnerability Scanner                                          |
            | scanner/xss_scaner                                 | normal |       Detected vulnerability xss                                     |
            | scanner/spaghetti                                  | high   |       Web Application Security Scanner                               |
            | scanner/dnslookup                                  | normal |       dnslookup scan                                                 |
            | scanner/reverse_dns                                | normal |       Reverse Dns Lookup                                             |
            | scanner/domain_map                                 | normal |       scanner domain map                                             |
            | scanner/dns_report                                 | normal |       dns report                                                     |
            | scanner/find_shared_dns                            | normal |       find shared dns                                                |
            | scanner/golismero                                  | normal |       scan vulnerability with golismero                              |
            | scanner/dns_propagation                            | low    |       dns propagation                                                |
            | scanner/find_records                               | normal |       find records                                                   |
            | scanner/cloud_flare                                | normal |       cloud flare                                                    |
            | scanner/extract_links                              | normal |       links extract                                                  |
            | scanner/web_robot                                  | normal |       web robots scanner                                             |
            | scanner/enumeration                                | normal |       http-enumeration                                               |
            | scanner/ip_locator                                 | good   |       ip Detected LOcator                                            |
            --------------------------------------------------------------------------------------------------------------------------------------


<img src="https://img.shields.io/badge/POST-8-red.svg">

            +----------------------------------------------------------------------------------------------------------+
            | POST                                                                                                     |
            ------------------------------------------------------------------------------------------------------------
            |     COMMANDS                                        Rank                 Description                     |
            ------------------------------------------------------------------------------------------------------------
            |  post/enumeration                                 | normal |     http-enumeration                        |
            |  post/vbulletin                                   | high   |     exploits                                |
            |  post/wordpress_user_scan                         | good   |     scanners                                |
            |  post/dir_search                                  | high   |     scanners                                |
            |  post/cms_war                                     | high   |     scanners                                |
            |  post/usr_pro_wordpress_auto_find                 | normal |     scanners                                |
            |  post/android_remote_access                       | good   |     exploits                                |
            |  post/samba                                       | good   |     exploits                                |
            ------------------------------------------------------------------------------------------------------------


<img src="https://img.shields.io/badge/Password-7-red.svg">


            +----------------------------------------------------------------------------------------------------------+
            | PASSWORD                                                                                                 |
            ------------------------------------------------------------------------------------------------------------
            |     COMMANDS                                        Rank                 Description                     |
            ------------------------------------------------------------------------------------------------------------
            | password/base64_decode                            | good  |      base64 decode                           |
            | password/md5_decrypt                              | good  |      md5 decrypt                             |
            | password/sha1_decrypt                             | good  |      sha1 decrypt                            |
            | password/sha256_decrypt                           | good  |      sha256 decrypt                          |
            | password/sha384_decrypt                           | good  |      sha384 decrypt                          |
            | password/sha512_decrypt                           | good  |      sha512 decrypt                          |
            | password/ssh_bruteforce                           | good  |      ssh password bruteforce                 |
            ------------------------------------------------------------------------------------------------------------

<img src="https://img.shields.io/badge/listeners-14-red.svg">


            +------------------------------------------------------------------------------------------------------------------------------------+
            | LISTENERS MODULES                                                                                                      |
            --------------------------------------------------------------------------------------------------------------------------------------
            |     COMMANDS                                         Rank                                   Description                |
            --------------------------------------------------------------------------------------------------------------------------------------
            |  android_meterpreter_reverse_tcp                    | good  |      Android Meterpreter, Android Reverse TCP Stager                 |
            |  android_meterpreter_reverse_https                  | good  |      Android Meterpreter, Android Reverse HTTPS Stager               |
            |  java_jsp_shell_reverse_tcp                         | good  |      Java JSP Command Shell, Reverse TCP Inline                      |
            |  linux_x64_meterpreter_reverse_https                | good  |      linux/x64/meterpreter_reverse_https                             |
            |  linux_x64_meterpreter_reverse_tcp                  | good  |      Linux Meterpreter, Reverse TCP Inline                           |
            |  linux_x64_shell_reverse_tcp                        | good  |      Linux Command Shell, Reverse TCP Stager                         |
            |  osx_x64_meterpreter_reverse_https                  | good  |      OSX Meterpreter, Reverse HTTPS Inline                           |
            |  osx_x64_meterpreter_reverse_tcp                    | good  |      OSX Meterpreter, Reverse TCP Inline                             |
            |  php_meterpreter_reverse_tcp                        | good  |      PHP Meterpreter, PHP Reverse TCP Stager                         |
            |  python_meterpreter_reverse_https                   | good  |      Python Meterpreter Shell, Reverse HTTPS Inline                  |
            |  python_meterpreter_reverse_tcp                     | good  |      python/meterpreter_reverse_tcp                                  |
            |  windows_x64_meterpreter_reverse_https              | good  |      Windows Meterpreter Shell, Reverse HTTPS Inline (x64)           |
            |  windows_x64_meterpreter_reverse_tcp                | good  |      Windows Meterpreter Shell, Reverse TCP Inline x64               |
            |  cmd_windows_reverse_powershell                     | good  |      Windows Command Shell, Reverse TCP (via Powershell)             |
            +------------------------------------------------------------------------------------------------------------------------------------+

# About Pentest Tools Framework

    INFO: Pentest Tools Framework is a database of exploits, Scanners
    and tools for penetration testing. Pentest is a powerful
    framework includes a lot of tools for beginners. You can explore
    kernel vulnerabilities, network vulnerabilities.

# How to install PTF(Pentest Tools Framework)

> root@kali~# cd Pentest-Tools-Framework

> root@kali~# pip install -r requirements.txt

> root@kali~# python install.py

> root@kali~# PTF



    INFO: After running install.py you should
    select your backbox/kali linux /parrot Os , all computer OS,

# About Pentest Tools Framework modules

> Exploits

    INFO: A computer program, piece of code,
    or sequence of commands that exploit vulnerabilities
    in software and are used to carry out an attack on a
    computer system. The purpose of the attack can be as a
    seizure of control over the system, and the violation
    of its functioning!

>Scanners

    INFO: The program that scans the specified Internet resource,
    archive or website. Also network scanners can scan open ports or
    your local network and IPs!


# Why  Pentest Tools Framework?

> Pentest Tools Framework is a free software

    INFO: This is a good platform
    to start exploring vulnerabilities!

> Simple UX/UI interface for beginners

    INFO: Pentest Tools Framework has simple UX/UI for beginners!
    It is easy to understand and it will be easier
    for you to master the Pentest Tools Framework.

> A lot of tools for beginners

    INFO: Pentest Tools Framework has еру following modules
    exploits - scanners - password
    This is enough for beginners.
### Donate!

(I love coffee and am very addicted to coffee:v)
<br><a href="https://www.buymeacoffee.com/pikpikcu"><img src="https://cdn.buymeacoffee.com/buttons/default-black.png" alt="Buy Me A Coffee" height="50px"></a>

# Credits & Thanks


<table><tr>
<td> [Nmap Security Scanners] <a href="https://nmap.org">
    <img src="https://nmap.org/images/sitelogo.png">
 </a></td>
<td> [Metasploit-framework] <a href="https://github.com/rapid7/metasploit-framework">
    <img src="https://media.trustradius.com/vendor-logos/Jt/nm/DMQHRCTTH9CT-180x180.JPEG">
 </a></td>
<td> [exploit-db] <a href="https://www.exploit-db.com">
     <img src="https://pentest.tonyng.net/wp-content/uploads/2017/11/edb-2015-theme-logo641.png">
</a></td>
  <td> [offensive-security] <a href="https://github.com/offensive-security/exploitdb">
     <img src="https://www.offensive-security.com/wp-content/uploads/2015/09/Offsec-Red-Site-Logo-2015-3001.png">
</a>
  </td>
 </tr></table></center>


# END
