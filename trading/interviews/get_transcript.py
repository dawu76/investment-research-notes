from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled

def get_youtube_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = ""
        for segment in transcript_list:
            transcript_text += segment['text'] + " "
        return transcript_text.strip()
    except NoTranscriptFound:
        return f"No transcript found for video ID: {video_id}. It might not have subtitles or they are not available in English."
    except TranscriptsDisabled:
        return f"Transcripts are disabled for video ID: {video_id}."
    except Exception as e:
        return f"An error occurred: {e}"

video_id = 'iu2gdI1cO88'
transcript = get_youtube_transcript(video_id)
print(transcript)
