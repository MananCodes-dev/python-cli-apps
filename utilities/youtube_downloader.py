from pytube import Youtube 

def download_video(url, resolution = '720p'):
    try:
        yt = Youtube(url)
        stream = yt.streams.filter(res=resolution, progressive=True).first()
        if stream:
            print(f"Downloading {yt.title} at {resolution}...")
            stream.download()
            print("✅ Download completed!")
        else:
            print(f"❌ No stream found for {resolution} resolution.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

while True:
    link = input("\nEnter the YouTube video URL to download or type 'exit' to quit: ")
    if link.lower() =='exit':
        print("Exiting the video downloader. Goodbye!")
        break
    
    res = input("Enter the desired resolution (e.g., 720p, 1080p) or press Enter for default (720p): ")
    download_video(link, res if res else '720p')
