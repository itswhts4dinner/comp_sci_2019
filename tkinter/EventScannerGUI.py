
from tkinter import *


class sportsButtons:
        def __init__(self, master):
                #create a frame in the main window "master"
                frame = Frame(master)
                frame.pack()




                #fall season
                self.FootballButton = Button(fallframe, text="Football", fg="blue")
                self.FootballButton.config( height = 10, width = 20 )
                self.FootballButton.pack(side=LEFT)


                self.VolleyballButton = Button(fallframe, text="Volleyball", fg="red")
                self.VolleyballButton.config( height = 10, width = 20 )
                self.VolleyballButton.pack(side=LEFT)

                #uncomment to make the soccer button with the soccer ball icon
                #self.GirlsSoccerButton = Button(fallframe, image=soccericon, text="Girls Soccer", fg="red")
                self.GirlsSoccerButton = Button(fallframe, text="Girls Soccer", fg="red")
                self.GirlsSoccerButton.config( height = 10, width = 20 )
                self.GirlsSoccerButton.pack(side=LEFT)

                self.CrossCountryButton = Button(fallframe, text="Cross Country", fg="green")
                self.CrossCountryButton.config( height = 10, width = 20 )
                self.CrossCountryButton.pack(side=LEFT)

                #winter season

                self.BoysBasketballButton = Button(winterframe, text="Boys Basketball", fg="blue")
                self.BoysBasketballButton.config( height = 10, width = 20 )
                self.BoysBasketballButton.pack(side=LEFT)

                self.GirlsBasketballButton = Button(winterframe, text="Girls Basketball", fg="red")
                self.GirlsBasketballButton.config( height = 10, width = 20 )
                self.GirlsBasketballButton.pack(side=LEFT)

                self.SwimmingButton = Button(winterframe, text="Swimming", fg="green")
                self.SwimmingButton.config( height = 10, width = 20 )
                self.SwimmingButton.pack(side=LEFT)

                #spring season

                self.SoftballButton = Button(springframe, text="Softball", fg="red")
                self.SoftballButton.config( height = 10, width = 20 )
                self.SoftballButton.pack(side=LEFT)

                self.BaseballButton = Button(springframe, text="Baseball", fg="blue")
                self.BaseballButton.config( height = 10, width = 20 )
                self.BaseballButton.pack(side=LEFT)

                self.BoysSoccerButton = Button(springframe, text="Boys Soccer", fg="blue")
                self.BoysSoccerButton.config( height = 10, width = 20 )
                self.BoysSoccerButton.pack(side=LEFT)

                self.TennisButton = Button(springframe, text="Tennis", fg="green")
                self.TennisButton.config( height = 10, width = 20 )
                self.TennisButton.pack(side=LEFT)


                self.TrackButton = Button(springframe, text="Track", fg="green")
                self.TrackButton.config( height = 10, width = 20 )
                self.TrackButton.pack(side=LEFT)







                #the quit button
                self.quitButton = Button(bottomFrame, text="Quit", command = frame.quit)
                self.quitButton.pack(side=LEFT)

        def printMessage(self):
            print("Wow, this actually worked")




#make a blank window
root = Tk()

#this is where I think I'd call the image
#soccericon=PhotoImage('/Users/jeremy/Desktop/gui/soccer.jpg')


#setup the frames
fallframe = Frame(root)
#pack the frame in the window
fallframe.pack()
winterframe = Frame(root)
winterframe.pack()
springframe = Frame(root)
springframe.pack()
bottomFrame =Frame(root)
bottomFrame.pack(side=BOTTOM)




#this variable calls the class "sportsButtons"
v = sportsButtons(root)
#keep the "root" window open until you press the close button or something
root.mainloop()
