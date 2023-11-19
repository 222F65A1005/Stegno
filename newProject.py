import pyfiglet
ascii_banner = pyfiglet.figlet_format("STEGANOGRAPHY - ENCRYPTION")
print(ascii_banner)
import cv2
loc=input("Enter the path of image (with extension) -> ")
image=cv2.imread(loc)
txt=input("Enter the data that you want to Encrypt (add '$' at the END of your statement) :- ")
ls=(list(txt))
for i in range(0,len(ls)):
     data=ord(ls[i])
     image[0,i,0]=data
lc=input("Enter saving location (Extension should be .png) ->")
cv2.imwrite(lc,image)
print("Data Encrypted")
input("")
import pyfiglet
ascii_banner = pyfiglet.figlet_format("STEGANOGRAPHY - DECRYPTION")
print(ascii_banner)
import cv2
d=[]
loc=input("Enter the path of image (with extension) -> ")
image=cv2.imread(loc)
x,y,z=image.shape
for i in range(0,y):
     b=chr(image[0,i,0])
     #print (b)
     if(b=='$'):
          break
     else:
          d.append(b)
d=''.join(d)
print(d)
input()
print("You can close the window now.")
