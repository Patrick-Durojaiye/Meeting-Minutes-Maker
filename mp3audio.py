from audio import Audio
import whisper

class mp3(Audio):
    def __init__(self, atype, name, adate, file):
        """
        Constructs a new object 'mp3'

        :param atype: Audio Type
        :param name: Name of Audio Recording
        :param adate: Date of Meeting
        :param file: Mp3 file of meeting
        """
        super().__init__(atype, name, adate)
        self.audio_file = file

    def convert(self):
        """
        Transcribes mp3 audio file using Open AI's Whisper model
        :return: The transcription of meeting recording in string format
        """
        model = whisper.load_model("base")
        result = model.transcribe(self.audio_file, fp16=False)
        return str(result['text'])
