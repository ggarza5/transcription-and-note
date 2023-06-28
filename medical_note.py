import os
import openai
import sys

openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the categories in the medical note
categories = [
    "Chief Complaints",
    "ROS (Review of symptoms)",
    "Medical history",
    "Surgical history",
    "Hospitalization/major diagnostic procedures",
    "Family history",
    "Social history",
    "Medications",
    "Allergies",
    "Assessment - Discussion",
    "Assessment - Plan",
    "Assessment - Plan - Treatment",
    "Assessment - Plan - Preventative Medicine",
]

# Define the prompt
prompt = "Put this transcription into a medical note. Note that this transcription is a conversation between a doctor and the patient, thus any mention of \"my, me, or I\" should not be ascribed to the patient's case. It should have the following categories, if they are discussed:\n\n" + "\n".join(categories) + "\n\n"

# Get the output of the previous script
input_text = sys.stdin.read().strip()

# Add the transcription text to the prompt
prompt += input_text

# Send the prompt to the GPT-4 API
response = openai.ChatCompletion.create(
    model="gpt-4",  # This might change when GPT-4 is released
    messages=[{
        "role":"user", "content":prompt
    }]
)

print(response['choices'][0]['message']['content'].strip())
