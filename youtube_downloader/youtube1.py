# in this file we are using get_videos() method

import tkinter as tk

from pytube import YouTube
def downloadVid():
    global E1
    string =E1.get()
    yt = YouTube(str(string))
    videos = yt.get_videos()
    s=1
    for v in videos:
        print(str(s) + '.' + str(v))
        s +=1
    n=int(input("Enter your choice"))
    vid=videos[n-1]
    destination=str(input("Enter your destination"))
    vid.download(destination)
    print(yt.filename+"\n Has downloaded")
root=tk.Tk()

w=tk.Label(root,text="Downloader")
w.pack()


E1=tk.Entry(root,bd=5)
E1.pack(side=tk.TOP)


button=tk.Button(root,text="Download",fg="red",command=downloadVid   )
button.pack(side=tk.BOTTOM)

root.mainloop()
