import os
import whisper
import torch
import time

model = whisper.load_model("base")

def transribe(fileName):

    # Add directory into content folder
    checkDownLoadFolder = os.path.exists("download")
    if not checkDownLoadFolder:
        os.mkdir("download")

    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(fileName)

    outputTextsArr = []
    while audio.size > 0:
        start = time.time()

        tirmedAudio = whisper.pad_or_trim(audio)
        # trimedArray.append(tirmedAudio)
        startIdx = tirmedAudio.size
        audio = audio[startIdx:]

        # make log-Mel spectrogram and move to the same device as the model
        mel = whisper.log_mel_spectrogram(tirmedAudio).to(model.device)

        # detect the spoken language
        _, probs = model.detect_language(mel)
        # print(f"Detected language: {max(probs, key=probs.get)}")

        # decode the audio
        options = whisper.DecodingOptions(fp16 = False)
        result = whisper.decode(model, mel, options)

        # print the recognized text
        outputTextsArr.append(result.text)

        print(time.time() - start)


    outputTexts = ' '.join(outputTextsArr)
    print(outputTexts)

    # Write into a text file
    with open(f"download/{fileName}.txt", "w", encoding="UTF-8") as f:
        f.write(f"▼ Transcription of {fileName}\n")
        f.write(outputTexts)