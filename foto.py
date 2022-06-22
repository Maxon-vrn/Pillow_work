from PIL import Image


def convert():
    # convert png>jpeg and save
    foto = Image.open('./test_rostov/foto/benefit.png')
    rgb_im = foto.convert('RGB')
    rgb_im.save('denefit.jpg') 
#convert()


def past(img1,img2):
    foto1 = img1.copy()
    foto2 = img2.copy()

    foto1.paste(foto2,(0, 220))
    foto1.save('./foto/fon_pillow_paste.jpg',quality=95)

    img1.close()
    img2.close()

img1 = Image.open('./test_rostov/foto/denefit.jpg')
img2 = Image.open('./test_rostov/foto/106044_benefit.jpeg') 

past(img1,img2)