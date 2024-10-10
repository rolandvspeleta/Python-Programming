from pytubefix import YouTube


def ytDownloader():
  
  running = True
  
  while running:
    
    link = input("Enter Youtube Link (e to exit): ")
    if link == "e" or link == "E":
      running = False
    else:
      yt = YouTube(link)
      print("Title: ", yt.title)
      yd = yt.streams.get_highest_resolution()
      yd.download('/Users/Rovic/Desktop/YT Downloads')
      
      play_again = input("Download another video? (y/n): ").lower()
      if not play_again == 'y':
        running = False
      else:
        continue
      continue

if __name__ == '__main__':
  ytDownloader()

