#!/bin/bash

count=0

for file in ../recordings/230814/*.mp3
do
    if [ $count -ge 1 ]
    then
        break
    fi
    echo "Processing file: $file"
    output_file="${file%.mp3}.wav"
    ffmpeg -i "$file" -acodec pcm_s16le -ac 1 -ar 16000 "$output_file"
    transcription=$(./main "$output_file" | python -u removeTimestamps.py | python -u redact_names.py)

    # Save the prompt into a file
    echo "$transcription" > prompt.txt

    # Pass the prompt file to main program
    ./main -f prompt.txt -p "Put this transcription into a medical note. Note that this transcription is a conversation between a doctor and the patient, thus any mention of \"my, me, or I\" should not be ascribed to the patients case. It should have the following categories, if they are discussed: Chief Complaints,ROS (Review of symptoms),Medical history, Surgical history,Hospitalization/major diagnostic procedures,Family history,Social history,Medications,Allergies,Assessment - Discussion,Assessment - Plan,Assessment - Plan - Treatment,Assessment - Plan - Preventative Medicine. Transcription:" > "${file%.mp3}_free_processed.txt"
    let count=count+1
done
