from google.oauth2 import service_account
from googleapiclient.discovery import build
import io
from googleapiclient.http import MediaIoBaseDownload
import config

def get_drive_service():
    credentials = service_account.Credentials.from_service_account_file(config.DRIVE_CREDENTIALS_JSON)
    return build('drive', 'v3', credentials=credentials)

def download_file(file_id):
    service = get_drive_service()
    request = service.files().get_media(fileId=file_id)
    file = io.BytesIO()
    downloader = MediaIoBaseDownload(file, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
    file.seek(0)
    return file.read().decode('utf-8')
