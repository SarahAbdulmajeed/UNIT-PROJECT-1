import whisper

model = whisper.load_model("base")

result = model.transcribe("test/output.wav")
print("Transcript:", result["text"])
