# in this file we are using streams.first() to get the videos

import tkinter as tk
import pytube
def downloadVid():
    yt = pytube.YouTube('https://www.youtube.com/watch?v=IOxTTrsCw_E')
    fn = yt.title
    print(fn)
    stream = yt.streams.first()
    path = 'C:/Users/DIKSHIT/Videos'
    stream.download(path)
    print(yt.filename+"\n Has downloaded")
root=tk.Tk()

w=tk.Label(root,text="Youtube Downloader")
w.pack()


E1=tk.Entry(root,bd=5)
E1.pack(side=tk.TOP)


button=tk.Button(root,text="Download",fg="red",command=downloadVid   )
button.pack(side=tk.BOTTOM)

root.mainloop()
