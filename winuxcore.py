import tkinter as tk
from tkinter import messagebox as msgbox
from PIL import Image, ImageTk
import time, pygame, random, sys

# no song and message = 0
# song only = 1
# message only = 2
# both song and message = 3

class Troll:
    def __init__(self):
        self.parent = tk.Tk()
        pygame.init()
        pygame.mixer.init()

        self.parent.attributes('-topmost', True)
        self.root_winwidth = 347
        self.root_winheight = 288
        
        self.screen_width = self.parent.winfo_screenwidth()
        self.screen_height = self.parent.winfo_screenheight()
        self.center_x = int((self.screen_width/2) - (self.root_winwidth/2))
        self.center_y = int((self.screen_height/2) - (self.root_winheight/2))
        self.parent.geometry(str(self.root_winwidth)+"x"+str(self.root_winheight)+"+"+str(self.center_x)+"+"+str(self.center_y))
        
        self.image = Image.open('assets/Trollface.png')
        self.image = ImageTk.PhotoImage(self.image)
        self.parent.overrideredirect(True)
        self.image_label = tk.Label(self.parent, image=self.image, bg=random.choice(['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']))
        self.image_label.pack()
        
    def change_colors(self):
        self.color_FPS=60
        x = self.center_x
        y = self.center_y
        c = 0
        colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
        last_color = colors[0]
        left = True
        down = True
        right = False
        up = False
        self.speed = random.choice(range(3,20))
        hidden = False
        while (pygame.mixer.music.get_busy()):
            current_color = random.choice(colors)
            if (current_color == last_color):
                try:
                    current_color = colors[colors.index(current_color)+1]
                except IndexError:
                    current_color = colors[0]

            if (c>100):
                if (c%random.choice(range(100,201))==0 and not hidden):
                    self.parent.withdraw()
                    hidden = True
                elif (hidden and c%random.choice(range(100,201))==0):
                    self.parent.deiconify()
                    hidden = False

            self.image_label.configure(bg = current_color)
            last_color = current_color
            if (x<=0):
                x=0
                right = True
                left = False
            if (x>=(self.parent.winfo_screenwidth()-self.root_winwidth)):
                x=(self.parent.winfo_screenwidth()-self.root_winwidth)
                left = True
                right = False
            if (y>=(self.parent.winfo_screenheight()-self.root_winheight)):
                y=(self.parent.winfo_screenheight()-self.root_winheight)
                up = True
                down = False
                
            if (y<=0):
                y=0
                up = False
                down = True
            if (left and down):
                x-=self.speed
                y+=self.speed
            if (right and up):
                x+=self.speed
                y-=self.speed
            if (left and up):
                x-=self.speed
                y-=self.speed
            if (right and down):
                x+=self.speed
                y+=self.speed
            self.parent.geometry(str(self.root_winwidth)+"x"+str(self.root_winheight)+"+"+str(x)+"+"+str(y))
            self.image_label.update()
            c+=1
            time.sleep(1/self.color_FPS)
        self.parent.deiconify()
        self.parent.update()
        
    def make_sound(self):
        pygame.mixer.Sound('assets/Trollsound.wav').play()
        
    def play_song(self):
        pygame.mixer.music.load('assets/Trollsong.wav')
        pygame.mixer.music.play()
        
    def exit(self):
        self.parent.destroy()
        pygame.quit()
    

def run(song=True, mbox=True):      
    troll = Troll()
    troll.parent.update()
    troll.make_sound()
    time.sleep(2)
    troll.play_song()
    if (not song):
        pygame.mixer.music.set_volume(0.0)
    troll.change_colors()
    troll.make_sound()
    time.sleep(2)
    if (mbox):
        while (pygame.mixer.music.get_busy()):
            pass
        import zlib, base64, tempfile
        icon=zlib.decompress(base64.b64decode('eJxjYGAEQgEBBiDJwZDBy'
                                              'sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc='))
        icon_path = tempfile.mkstemp()[1]
        with open(icon_path, 'wb') as icon_file:
            icon_file.write(icon)
        root = tk.Tk()
        root.iconbitmap(default=icon_path)
        root.withdraw()
        msgbox.showinfo(title="LOVE YOU MY DARLING!!!", message="Made with PURE LOVE only for YOU ( ＾3＾ )")
        root.destroy()
    troll.exit()

if __name__ == "__main__":
    try:
        if (sys.argv[1] == '0'):
            song=False
            mbox=False
        elif (sys.argv[1] == '1'):
            song=True
            mbox=False
        elif (sys.argv[1] == '2'):
            song=False
            mbox=True
        elif (sys.argv[1] == '3'):
            song=True
            mbox=True
        else:
            raise
    except:
        song=True
        mbox=True
    finally:
        run(song, mbox)
