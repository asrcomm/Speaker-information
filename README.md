# Speaker-information

1. Extract the audio from the video using extract_audio.py script
2. In case to compress or resample (to 16kHz) or change the number of channels of the audio:
  
  
 ffmpeg -i original_audio.wav -ac 1 -ar 16000 modified_audio.wav

   
Speaker_count.ipynb gives the speaker information
