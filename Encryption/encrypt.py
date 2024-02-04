
from cryptochaos import logistic

def encrypt_data(data,r):
   r_min, r_max = 3.6, 4.0
   k = r_min + (r % (r_max - r_min))
   encrypted_text = logistic.logistic_encrypt(data,k)

   return encrypted_text

def decrypt_data(data,r):
   r_min, r_max = 3.6, 4.0
   k = r_min + (r % (r_max - r_min))
   decrypted_text = logistic.logistic_decrypt(data,k)
   return decrypted_text