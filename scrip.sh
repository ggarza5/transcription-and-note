#!/bin/bash

count=0

for file in ../recordings/230814/*.mp3
do
    if [ $count -ge 10 ]
    then
        break
    fi
    echo "Processing file: $file"
    output_file="${file%.mp3}.wav"
    ffmpeg -i "$file" -acodec pcm_s16le -ac 1 -ar 16000 "$output_file"
    ./main -m models/ggml-medium.en.bin -f "$output_file" | python -u removeTimestamps.py | python -u redact_names.py | python -u medical_note.py > "${file%.mp3}_processed.txt"
    let count=count+1
done
