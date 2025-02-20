import sys
from gtts import gTTS from
pydub import AudioSegment
import os
# Set paths for ffmpeg and ffprobe 
ffmpeg_path ="C:\\ffmpeg\\ffmpeg-7.0.1-full_build\\bin\\ffmpeg.exe"
ffprobe_path ="C:\\ffmpeg\\ffmpeg-7.0.1-full_build\\bin\\ffprobe.exe"
# Apply these paths to pydub
AudioSegment.converter = ffmpeg_path
AudioSegment.ffmpeg = ffmpeg_path
AudioSegment.ffprobe = ffprobe_path 
def convert_to_speech(text, language):
 try:
  tts = gTTS(text=text, lang=language, slow=False)
tts.save("output.mp3") 
print("Speech has been
successfully generated.") except Exception as e:
 print(f"Failed to generate speech: {e}", file=sys.stderr)
if _name_ == "_main_":
 if len(sys.argv) > 1: text = sys.argv[1]
language = sys.argv[2] if len(sys.argv) > 2 else "en"
convert_to_speech(text, language)
 else: 
 print("Please provide the text and language as command-line arguments.")
