from Crypto.Cipher import DES
import binascii

flag = "ff7e3193db6975cfd4e62a3ac56cd5718f0dd9001d0c178794bd8462099eb7da0ad95ee95abe27fb"
potential = [(b'919199  ', b'109575  '), (b'919199  ', b'009565  '), (b'919199  ', b'119465  '), (b'919199  ', b'118575  '), (b'919199  ', b'018464  '), (b'919199  ', b'119575  '), (b'919199  ', b'019464  '), (b'919199  ', b'108575  '), (b'919199  ', b'009465  '), (b'919199  ', b'008575  '), (b'919199  ', b'108474  '), (b'919199  ', b'118474  '), (b'919199  ', b'119464  '), (b'919199  ', b'008474  '), (b'919199  ', b'019574  '), (b'919199  ', b'018565  '), (b'919199  ', b'109464  '), (b'919199  ', b'019474  '), (b'919199  ', b'008564  '), (b'919199  ', b'008574  '), (b'919199  ', b'018475  '), (b'919199  ', b'019575  '), (b'919199  ', b'019564  '), (b'919199  ', b'108565  '), (b'919199  ', b'009474  '), (b'919199  ', b'108574  '), (b'919199  ', b'018564  '), (b'919199  ', b'109574  '), (b'919199  ', b'108464  '), (b'919199  ', b'119564  '), (b'919199  ', b'019465  '), (b'919199  ', b'118464  '),
             (b'919199  ', b'018474  '), (b'919199  ', b'008464  '), (b'919199  ', b'009575  '), (b'919199  ', b'109474  '), (b'919199  ', b'018465  '), (b'919199  ', b'109465  '), (b'919199  ', b'118564  '), (b'919199  ', b'019565  '), (b'919199  ', b'108564  '), (b'919199  ', b'009564  '), (b'919199  ', b'118475  '), (b'919199  ', b'019475  '), (b'919199  ', b'119574  '), (b'919199  ', b'109565  '), (b'919199  ', b'109564  '), (b'919199  ', b'008475  '), (b'919199  ', b'009464  '), (b'919199  ', b'008465  '), (b'919199  ', b'018575  '), (b'919199  ', b'009574  '), (b'919199  ', b'008565  '), (b'919199  ', b'018574  '), (b'919199  ', b'118574  '), (b'919199  ', b'118565  '), (b'919199  ', b'009475  '), (b'919199  ', b'108475  '), (b'919199  ', b'119565  '), (b'919199  ', b'119475  '), (b'919199  ', b'119474  '), (b'919199  ', b'108465  '), (b'919199  ', b'109475  '), (b'919199  ', b'118465  ')]


def double_decrypt(cipher, key1, key2):
    cipher = binascii.unhexlify(cipher.encode())
    try:
        cipher2 = DES.new(key2, DES.MODE_ECB)
        decrypted_msg = cipher2.decrypt(cipher)
        cipher1 = DES.new(key1, DES.MODE_ECB)
        decrypted = cipher1.decrypt(decrypted_msg)
        return decrypted
    except:
        return("wrong key")


for pair in potential:
    print(double_decrypt(flag, pair[0], pair[1]))