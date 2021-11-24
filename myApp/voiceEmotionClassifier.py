import tensorflow as tf
from tensorflow.keras import datasets, layers, models


import tensorflow.keras
import numpy as np
import librosa
import tensorflow as tf 


emotions = {
                            0: 'neutral_F',
                            1 : 'happiness_F',
                            2: 'sadness_F',
                            3: 'anger_F',
                            4: 'neutral_M',
                            5 : 'happiness_M',
                            6: 'sadness_M',
                            7: 'anger_M',
}
emo_list = list(emotions.values())


class livePredictions:
    """
    Main class of the application.
    """

    def __init__(self, path, file):
        """
        Init method is used to initialize the main parameters.
        """
        self.path = path
        self.file = file
    def load_model(self):
        """
        Method to load the chosen model.
        :param path: path to your h5 model.
        :return: summary of the model with the .summary() function.
        """
        self.loaded_model = tensorflow.keras.models.load_model(self.path)
        return self.loaded_model.summary()

    def makepredictions(self):
        """
        Method to process the files and create your features.
        """
        data, sampling_rate = librosa.load(self.file)
        mfccs = np.mean(librosa.feature.mfcc(y=data, sr=sampling_rate, n_mfcc=40).T, axis=0)
        x = np.expand_dims(mfccs, axis=1)
        x = np.expand_dims(x, axis=0)
        predictions = self.loaded_model.predict_classes(x)
        print(self.loaded_model.predict(x))
        #print("Prediction is", " ", self.convertclasstoemotion(predictions))

        return self.convertclasstoemotion(predictions)

    @staticmethod
    def convertclasstoemotion(pred):
        """
        Method to convert the predictions (int) into human readable strings.
        """
        
        label_conversion = { 
                            0: 'neutral_F',
                            1 : 'happiness_F',
                            2: 'sadness_F',
                            3: 'anger_F',
                            4: 'neutral_M',
                            5 : 'happiness_M',
                            6: 'sadness_M',
                            7: 'anger_M',
                           
                           
                           
                           }

        for key, value in label_conversion.items():
            if int(key) == pred:
                label = value
        return label


def voicePredict(voice_file):
  pred = livePredictions(path='testing10_model.h5',file=voice_file)
  
  pred.load_model()
  res = pred.makepredictions()

  if res=='neutral_F' or res== 'neutral_M':
    return "중립"
  elif res=='happiness_F' or res== 'happiness_M':
    return "행복"
  elif res=='sadness_F' or res== 'sadness_M':
    return "슬픔"
  elif res=='anger_F' or res== 'anger_M':
    return "분노"

    


