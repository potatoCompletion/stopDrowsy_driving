#from __future__ import division
import os
import dlib, cv2
import numpy as np

class Face_id(object):
      
        '''This class detect the user's face_id with images DB''' 
        def __init__(self):
          self.detector = dlib.get_frontal_face_detector()
          cwd = os.path.abspath(os.path.dirname(__file__))
          model_path = os.path.abspath(os.path.join(cwd, "trained_models/shape_predictor_68_face_landmarks.dat"))
          face_model_path=os.path.abspath(os.path.join(cwd,"trained_models/dlib_face_recognition_resnet_model_v1.dat"))
          self._predictor = dlib.shape_predictor(model_path)
          self._facerec=dlib.face_recognition_model_v1(face_model_path)
          self.img=None
          #self.detector = dlib.get_frontal_face_detector()
          #sp = dlib.shape_predictor('/home/semiwo/simple_face_recognition/models/shape_predictor_68_face_landmarks.dat')
          #facerec = dlib.face_recognition_model_v1('/home/semiwo/simple_face_recognition/models/dlib_face_recognition_resnet_model_v1.dat')

        '''def read_img(self,img_path): 
          img = cv2.imread(img_path)
          img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
          return img'''

        def encode_face(self,img):
          dets = self.detector(img, 1)

          if len(dets) == 0:
            return np.empty(0)

          for k, d in enumerate(dets):
            # print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(k, d.left(), d.top(), d.right(), d.bottom()))
            shape = self._predictor(img, d)
            face_descriptor = self._facerec.compute_face_descriptor(img, shape)

            return np.array(face_descriptor)
'''
  # main
  img1_path = '/home/semiwo/simple_face_recognition/IU.png' # iu

  # img2_path = '/Users/visualcamp/Pictures/00502318_20180518.JPG' # suz
  # img2_path = '/Users/visualcamp/Pictures/660190_v9_ba.jpg' # suz

  # img2_path = '/Users/visualcamp/Development/tf/GazeCapture/dataset/processed/00002/frames/00000.jpg'
  # img1_path = '/Users/visualcamp/Development/tf/GazeCapture/dataset/processed/03523/frames/02190.jpg'
  # img2_path = '/Users/visualcamp/Development/tf/GazeCapture/dataset/processed/03523/frames/00000.jpg'
  # img2_path = '/Users/visualcamp/Development/tf/GazeCapture/dataset/processed/02534/frames/00005.jpg'

  img1_path = '/home/semiwo/simple_face_recognition/IU.png' # me
  img1 = read_img(img1_path)
  img1_encoded = encode_face(img1)
  # img2 = read_img(img2_path)

  cap = cv2.VideoCapture(0)

  if not cap.isOpened():
    exit()

  while True:
    ret, img2 = cap.read()
    if not ret:
      break

    img2 = cv2.resize(img2, (640, img2.shape[0] * 640 // img2.shape[1]))
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    img2_encoded = encode_face(img2)

    if len(img2_encoded) == 0:
      continue

    dist = np.linalg.norm(img1_encoded - img2_encoded, axis=0)
  
    print('%s, Distance: %s' % (dist < 0.6, dist))'''
