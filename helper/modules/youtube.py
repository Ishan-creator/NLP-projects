from youtubesearchpython import VideosSearch
import webbrowser

search_keyword = ""

class utube_play():

    videosSearch = VideosSearch(search_keyword, limit = 1)
    results = videosSearch.result()

    if results["result"]:
        video_url = results["result"][0]["link"]
        # print("Video URL:", video_url)
        webbrowser.open(video_url)
    else:
        print("No videos found for the search query:", search_keyword)
