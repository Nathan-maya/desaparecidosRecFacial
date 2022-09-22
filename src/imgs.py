# import the necessary packages
import sys
import numpy as np
import urllib.request
import cv2
import os
import uuid
from skimage.io import imread, imshow
from skimage.transform import resize
from skimage.util import img_as_ubyte
from fetchApi import buscar_dados

__all__ = ["stuff", "to", "export"]

images = []
# METHOD #1: OpenCV, NumPy, and urllib


# os.makedirs('./images/')

def download_imgs():
  try:
      data = buscar_dados()

      for urls in data:
          # download the image URL and display it
          nome = str(urls['nome']).replace(' ', '').lower()
          print(urls['nome'])
          os.makedirs('./images/' + nome)

          for url in urls['img']:
          # print(url)
              urllib.request.urlretrieve(
              url, './images/'+nome+'/'+'photo'+str(uuid.uuid4())+'.jpg')
      print("Imagem salva! =)")
  except:
      erro = sys.exc_info()
      if(not FileExistsError()):
        print("Ocorreu um erro:", erro)

