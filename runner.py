from mp3audio import mp3
from gpthandler import gptDataProcesser
from datetime import date
from pdfmaker import save_minutes

if __name__ == "__main__":

    meeting_mp3 = mp3(atype="mp3", name="Swiss RE 2014 AGM", adate=date.fromisoformat('2014-04-24'), file='recordings/agm-conf-call-2014-hi.mp3')
    meeting_transcript = meeting_mp3.convert()

    gpt = gptDataProcesser(prompt="Please create meeting minutes with regards to the following text below.", meetings_text=meeting_transcript)
    key = gpt.get_keys()
    minutes = gpt.ask_gpt(api_key=key)

    save_minutes(text=minutes)
