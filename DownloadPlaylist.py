from pytube import Playlist
import re

from pytube import YouTube

def download_videos_from_playlist(video_ids):
    for video_id in video_ids:
        try:
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            yt = YouTube(video_url)
            stream = yt.streams.get_highest_resolution()
            print(f"Downloading: {yt.title}...")
            stream.download()  # Downloads the video to the current directory
            print(f"{yt.title} has been downloaded successfully.")
        except Exception as e:
            print(f"Error downloading video with ID {video_id}: {e}")

# Replace 'video_ids' with the list of video IDs you want to download
#video_ids = ['VIDEO_ID_1', 'VIDEO_ID_2', 'VIDEO_ID_3']  # Replace with your video IDs



def get_video_ids_from_playlist(playlist_url):
    try:
        playlist = Playlist(playlist_url)
        playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
        video_urls = playlist.video_urls
        video_ids = [url.split('v=')[1] for url in video_urls]
        return video_ids
    except Exception as e:
        print("Error:", e)
        return None

# Replace 'YOUR_PLAYLIST_URL' with the actual URL of the YouTube playlist
playlist_url = 'play_list_url'
'
video_ids = get_video_ids_from_playlist(playlist_url)

if video_ids:
    print("Video IDs in the Playlist:")
    print(video_ids)
    #download_videos_from_playlist(video_ids)
else:
    print("Error fetching video IDs. Please check the playlist URL.")
