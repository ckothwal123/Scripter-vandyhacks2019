from google.cloud import texttospeech
import wave
from pydub import AudioSegment
#import libraries
from glob import iglob
import shutil
import os

def text_speech(database):
    voice_switcher = {
        "male": texttospeech.enums.SsmlVoiceGender.MALE,
        "female": texttospeech.enums.SsmlVoiceGender.FEMALE
    }
    i = 0
    infiles = []
    outfile = "rolePlay.wav"
    for dialouge, role in database:
        voice = voice_switcher.get(role, texttospeech.enums.SsmlVoiceGender.NEUTRAL)

        # Instantiates a client
        client = texttospeech.TextToSpeechClient()

        # Set the text input to be synthesized
        synthesis_input = texttospeech.types.SynthesisInput(text=dialouge)

        # Build the voice request, select the language code ("en-US") and the ssml
        # voice gender ("neutral")
        voice = texttospeech.types.VoiceSelectionParams(
            language_code='en-US',
            ssml_gender=voice)

        # Select the type of audio file you want returned
        audio_config = texttospeech.types.AudioConfig(

            audio_encoding=texttospeech.enums.AudioEncoding.MP3)

        # Perform the text-to-speech request on the text input with the selected
        # voice parameters and audio file type
        response = client.synthesize_speech(synthesis_input, voice, audio_config)

        infile = 'E:\\vandyHacks\\text-speech\processed_speech\\file' + '{}'.format(i) + '.mp3'
        # The response's audio_content is binary.
        with open(infile, 'wb') as out:
            # Write the response to the output file.
            out.write(response.audio_content)
            print('Audio content written to file {}'.format(infile))
        infiles.append(infile)
        i+=1

    final_audio = AudioSegment.empty()
    final_audio.converter = "E:\\vandyHacks\\ffmpeg-20191101-53c21c2-win64-static\\bin"
    for inF in infiles:
        final_audio = final_audio + AudioSegment.from_mp3(inF)
    final_audio.export("final.mp3", format="mp3")