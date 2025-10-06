from TTS.api import TTS

# Load a free pretrained model
# You can change this to any other model from https://tts.readthedocs.io/en/latest/models.html
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

# Read text from file
with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read().strip()

# Generate speech and save to a file
output_file = "output.wav"
tts.tts_to_file(text=text, file_path=output_file)

print(f"✅ Speech saved to {output_file}")
