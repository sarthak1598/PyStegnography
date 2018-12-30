

# This program/script is a simple stegnographic approach to hide the  sensitive data inside the images

# THE following modules are utilized in the code for encoding and encrypting the data inside the images 

# modules : Image , stepic and ezpycrypto 


# the code will first encrypt the message to be hidden in the image using ezpycrypto 
# then after this that message would be hidden in the image 


# The hidden mechanism is simple as:\

#       Stepic provides a Python module and also a command-line interface to hide arbitrary data within images.
#       It slightly modifies the colours of pixels in the image to store the data. 
#       These modifications can't be detected by the humans but can be detected by programs.
#       FINALLY AFTER A LOT OF COMMENTRY THIS= IS THE CODE:)


from PIL import Image # for handling the image operations

import stepic
import ezPyCrypto

image = Image.open("im_name.jpg") # passing the image path to be opened

encrypt_key = ezPyCrypto.key(2048)  #  Creating the RSA encryption key of 2048 bit size.

enc = k.encStringToAscii('Message to be hidden in the image') #  encrypting the message with the rsa key  
im1=stepic.encode(enc)  # encoding the message 
im1.save('stegoimg.jpg','JPEG')  # saving image after procedure completion

print enc # will prints the string to ascii converted data  

