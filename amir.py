BITS = ('0', '1')
ASCII_BITS = 7

def display_bits(b):
    """converts list of {0, 1}* to string"""
    return ''.join([BITS[e] for e in b])

def seq_to_bits(seq):
    return [0 if b == '0' else 1 for b in seq]

def pad_bits(bits, pad):
    """pads seq with leading 0s up to length pad"""
    assert len(bits) <= pad
    return [0] * (pad - len(bits)) + bits
        
def convert_to_bits(n):
    """converts an integer `n` to bit array"""
    result = []
    if n == 0:
        return [0]
    while n > 0:
        result = [(n % 2)] + result
        n = int(n / 2)
    return result

def string_to_bits(s):
    def chr_to_bit(c):
        return pad_bits(convert_to_bits(ord(c)), ASCII_BITS)
    return [b for group in 
            map(chr_to_bit, s)
            for b in group]

def bits_to_char(b):
    assert len(b) == ASCII_BITS
    value = 0
    for e in b:
        value = (value * 2) + e
    return chr(value)

def list_to_string(p):
    return ''.join(p)

def bits_to_string(b):
    return ''.join([bits_to_char(b[i:i + ASCII_BITS]) 
                    for i in range(0, len(b), ASCII_BITS)])
    
def otp(m, k):
    assert len(m) == len(k)
    return[( mm+ kk) % 2 for mm, kk in zip(m, k)]
    
#Set own plaintext M1,M2 and Key 
  
m1 = "The Program"
print("Data type returned by function string_to_bits is " + str(type(string_to_bits(m1))))
print("\n" + m1 + " in binary python list is "+ str(string_to_bits(m1))+ " a.k.a 0b"+ display_bits(string_to_bits(m1)))

m2 = "Hello World"
print("\n" + m2 + " in binary python list is "+ str(string_to_bits(m2))+ " a.k.a 0b"+ display_bits(string_to_bits(m2)))

k = "Study Smart"

print ("\nKEY      : " + k )
print ("M1       : " + m1 )
print ("M2       : " + m2 )

#Perform the encryption to get the C1 and C2
#Perform cryptoanalysis
#Automate the cryptoanalysis

C1 = otp(string_to_bits(m1), string_to_bits(k))              #C1 (m1 XOR key)    
C2 = otp(string_to_bits(m2), string_to_bits(k))              #C2 (m2 XOR key)

OTP = otp ( C1 , C2 )                                        #one time pad C1 XOR C1

print ( "\nEncryption" )

print ("\nKey       : " + display_bits(string_to_bits(k)))   #display key in binary
print ("M1 is     : " + display_bits(string_to_bits(m1)))    #display m1 in binary
print ("C1 is     : " + display_bits((C1)))                  #display C1 (m1 XOR key)

print ("\nKey       : " + display_bits(string_to_bits(k)))   #display key in binary
print ("M2 is     : " + display_bits(string_to_bits(m2)))    #display m2 in binary
print ("C2 is     : " + display_bits((C2)))                  #display C2 (m2 XOR key)

print ("\nC1 is     : " + display_bits((C1)))                #display C1 in binary
print ("C2 is     : " + display_bits((C2)))                  #display C2 in binary
print ("otp(C1,C2): " + display_bits((OTP)))                 #display one time pad C1 with C2 (C1 XOR C2)

print ( "\nDecryption" )

decrypt_C1 = otp( (C1), string_to_bits(k))                   # C1 XOR key : to get back m1 
decrypt_C2 = otp( (C2), string_to_bits(k))                   # C2 XOR key : to get back m2
C1_decryptstring = bits_to_string (decrypt_C1)               # to get decrypted C1 in string 
C2_decryptstring = bits_to_string (decrypt_C2)               # to get decrypted C2 in string 
                     
print ("\nKey       : " + display_bits(string_to_bits(k)))   # display key in binary 
print ("C1 is     : " + display_bits( (C1)))                 # display C1 in binary                                  
print ("M1 is     : " + display_bits(decrypt_C1))            # display m1 in binary   

print ("\nKey       : " + display_bits(string_to_bits(k)))   # display key in binary
print ("C2 is     : " + display_bits( (C2)))                 # display C2 in binary  
print ("M2 is     : " + display_bits(decrypt_C2))            # display m2 in binary 

print ("\nMessage 1 is: " + C1_decryptstring)                # display decrypted C1 in text 
print ("Message 2 is: " + C2_decryptstring)                  # display decrypted C2 in text 
print ("\n")
