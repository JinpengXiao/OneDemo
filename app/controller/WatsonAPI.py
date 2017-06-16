'''
Created on Jun 10, 2017

@author: xiao jinpeng
'''
import config
from os import remove
from watson_developer_cloud.text_to_speech_v1 import TextToSpeechV1

def text2speech(fileName='',message=''):
    print('*********Testing No.3*********')
    
    if (fileName == ''):
        fileName = '/Users/IBM_ADMIN/workspace/ProjectForPython/FirstDemo/tmp/output.wav'
        print(fileName)
        
    if (message == ''):
        message = 'Hello World'
        
    try:
        remove(fileName)
    except:
        print('there is no file exist')
        
    #use watson api to Transfer the text to speech
    text_to_speech = TextToSpeechV1(
        username = config.bluemix_username,
        password = config.bluemix_password,
        x_watson_learning_opt_out = True)       #Optional Flag
    
    with open(fileName, 'wb') as audio_file:
        audio_file.write(text_to_speech.synthesize(message, accept='audio/wav', voice=config.bluemix_watsonvoice))
        