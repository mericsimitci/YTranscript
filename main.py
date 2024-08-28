from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound
from urllib.parse import urlparse, parse_qs

video_url = input("Enter video link: ")
lang = input("Enter language (tr/en): ")

query = urlparse(video_url).query
video_id = parse_qs(query).get('v')

if video_id:
    video_id = video_id[0]
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang])
        transcript_text = "\n".join([x['text'] for x in transcript])

        print(transcript_text)
    except NoTranscriptFound:
        print("There is no transcript (Changing language may help).")
    except Exception as e:
        print(f"Error occured: {str(e)}")
else:
    print("No valid video for this url.")