from os import remove, listdir
from shutil import move
import numpy as np
import qrcode
from PIL import Image, ImageFont, ImageDraw 

class sticker:
  def __init__(self, xy):
      self.x = int(xy.split(',')[0])
      self.y = int(xy.split(',')[1])
      self.font = ImageFont.truetype('Inter-Medium.ttf', 25)      

      # self.generate('-+=qrcode=+-')      
      # img2_test = Image.open('./img/_-+=qrcode=+-.jpg')
      # img_tes = self.merge(img1_test, img2_test ,round((img1_test.shape[1]/2)-(img2_test.shape[1]/2)), round(400-(img2_test.shape[0]/2)))
      # cv2.imwrite('./img/{}.jpg'.format('-+=qrcode=+-'), img_tes)
      # remove('./img/{}.jpg'.format('_-+=qrcode=+-'))
      # remove('./img/{}.jpg'.format('-+=qrcode=+-'))

  def generate(self, data):
    qr = qrcode.QRCode(
      version=1,
      box_size=16,
      border=0
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('./img/_{}.jpg'.format(data))

  def merge(self, background, overlay, x, y):
    background_width = background.shape[1]
    background_height = background.shape[0]
    if x >= background_width or y >= background_height:
      return background
    h, w = overlay.shape[0], overlay.shape[1]
    if x + w > background_width:
      w = background_width - x
      overlay = overlay[:, :w]
    if y + h > background_height:
      h = background_height - y
      overlay = overlay[:h]
    if overlay.shape[2] < 4:
      overlay = np.concatenate([
          overlay,
          np.ones((overlay.shape[0], overlay.shape[1], 1), dtype = overlay.dtype) * 255
        ],
        axis = 2,
      )
    overlay_image = overlay[..., :3]
    mask = overlay[..., 3:] / 255.0
    background[y:y+h, x:x+w] = (1.0 - mask) * background[y:y+h, x:x+w] + mask * overlay_image
    return background
  
  def get(self, name):
    img1_test = np.load('img1.npy')
    img1_test = Image.fromarray(np.uint8(img1_test)).convert('RGB')
    img1 =  img1_test
    img1_editable = ImageDraw.Draw(img1)
    img1_editable.text((self.x,self.y), f'{name}', (0, 0, 0), font=self.font)
    img1 = img1.__array__()
    img2 = Image.open('./img/_{}.jpg'.format(name)).convert('RGB').__array__()
    img = self.merge(img1, img2 ,round((img1.shape[1]/2)-(img2.shape[1]/2)), round(400-(img2.shape[0]/2)))
    img = Image.fromarray(np.uint8(img))
    img.save(f'./img/{name}.jpg', dpi=(300, 300))    
    remove('./img/_{}.jpg'.format(name))

  def clear(self):
    files = listdir('./img')
    if len(files) != 0:
      for file in files:
        try:
          move('./img/{}'.format(file), './history')
        except:
          remove('./img/{}'.format(file))


# if __name__ == '__main__':  
#   img2 = Image.open('./history/ISN1401871.jpg').convert('RGB')
#   print(img2.resize((189,265)))
  # import matplotlib.pyplot as plt
  # img = np.load('img1.npy')
  # img = Image.fromarray(np.uint8(img)).convert('RGB')
  # font = ImageFont.truetype('Inter-Medium.ttf', 23)
  # img_editable = ImageDraw.Draw(img)
  # img_editable.text((232,580), "ISN1234567", (0, 0, 0), font=font)
  # img = img.__array__()
  # print(img.shape)
  # plt.imshow(img)
  # plt.show()
  

  # qr = qrcode.QRCode(
  #   version=1,
  #   box_size=15,
  #   border=0
  # )
  # qr.add_data('ISN1234567')
  # qr.make()
  # b= np.array(qr.get_matrix())
  # img = qr.make_image(fill='black', back_color='white')
  # img = img.get_image()
  # b= np.array(img)
  # img = Image.fromarray(np.uint8(img)).convert('RGB')
  # print(b.shape)
  # plt.imshow(b)
  # plt.show()

  # img = Image.open('pic.png').__array__()
  # np.save('pic.npy',img)
  # img = np.load('pic.npy')  
  # print(img.shape)
  

  # from time import sleep
  # sticker = sticker('228,574')
  # data = ['ISN1234567', 'IS31234468', 'ISN1534569']
  # data = ['ISN1234567']
  # for x in data:
    # sticker.clear()
    # sticker.generate(x)
    # sticker.get(x)
    # sleep(1)


  # sticker.clear()
  # move('./img/ISN1044760.jpg', './history')

  # QRcode.generate(data)
  # sticker.get(data)
  # plt.imshow(sticker.get(data), cmap='gray')
  # plt.show()
  # cv2.imshow('template', img)
  # k = cv2.waitKey(0)
  # if k == 27:	
  #   cv2.destroyAllWindows()







