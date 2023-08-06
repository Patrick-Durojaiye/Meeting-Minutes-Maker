from abc import ABC, abstractmethod

class Audio(ABC):
    """
    Abstract class for meeting recordings
    """
    def __init__(self, atype, name, date):
        """

        :param atype: Audio Type
        :param name: Name of Audio Recording
        :param date: Date of Meeting
        """
        self.audio_type = atype
        self.audio_name = name
        self.recording_date = date

    @abstractmethod
    def convert(self):
        """
        Abstract method for converting audio to text
        :return: returns nothing
        """
        pass
