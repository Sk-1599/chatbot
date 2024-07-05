# youtube_service.py
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
import config

def get_youtube_service():
    return build('youtube', 'v3', developerKey=config.YOUTUBE_API_KEY)

def search_youtube_videos(query, max_results=5):
    youtube = get_youtube_service()
    request = youtube.search().list(
        q=query,
        part='snippet',
        type='video',
        maxResults=max_results
    )
    response = request.execute()
    return response['items']

def get_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return ' '.join([item['text'] for item in transcript])
