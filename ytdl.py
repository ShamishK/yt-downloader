import yt_dlp

# URL of the YouTube video
video_url = "https://www.youtube.com/your video url"

# Options to control video quality
try:
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    
    print("Download completed successfully!")

except Exception as e:
    print("An error occurred:", e)