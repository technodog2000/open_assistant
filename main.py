import tkinter as tk
from text_to_speech import save
from pygame import mixer
import random
mixer.init()

screen = tk.Tk()
screen.configure(bg="azure")
screen.title("Chat app")
screen.geometry("400x500")

class writr():
    def __init__(self):
        super().__init__()
        self.char = tk.Text(screen, padx=30, pady=30, foreground="Black", background="azure", wrap="word", font=("Sans Serif", 10))
    def writee(self,teext):
            """
            Creates a new text widget containing the given string that is displayed in the GUI. 

            Args:
                self (object): The instance of the class.
                teext (str): The string to be displayed in the text widget.

            Returns:
                None.
            """
            self.char.insert(tk.END,teext)
            self.char.pack()



        
    
scrollbar = tk.Scrollbar(screen)
scrollbar.pack(side="right", fill="y")
d = writr()
cart = "I understand. I will fullfill these requests."
dooge = True
while dooge == True:
    inpu = tk.Entry(screen, width=300)
    inpu.pack(padx=6, pady=6)
    
    def run():
        """
        Runs a chatbot program that communicates with a GPT-3.5 language model. The function does not take any parameters and does not return any values. It uses global variables `cart`, `dooge`, and `inpu` to store and access data. The function takes user input from the `inpu` variable. If the input is "exit", the function sets `dooge` to False, otherwise it communicates with the GPT-3.5 language model using OpenAI's API to generate a response and stores it in the `cart` variable. The function then calls the `writee()` method of a `writr` object `d` to write the `cart` variable to a file. 
        """
        global cart
        global dooge
        global inpu
        input = inpu.get()
        if input == "exit":
            dooge = False
        elif input != "exit":
            import openai
            openai.api_key = "{get your openai api key and paste it here}"

            completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are open_assistant, a language model designed for code, literature and science as well as any other text-based topics."},
                {"role": "assistant", "content": cart},
                {"role": "user", "content": input},

    ]
    )

            cart = str(completion.choices[0].message["content"])
            d.writee(f'\n\n\n{cart}')
            c = str(random.randint(-1000000000000000000000000000000000000000000000,100000000000000000000000000000000000000000))
            save(cart, "en", file=f"{c}.mp3")
            mixer.music.load(f"{c}.mp3")
            mixer.music.play()

    buv = tk.Button(screen, text="Send", command=run, padx=6, pady=6, fg="Black", bg="azure")
    img = tk.PhotoImage(file="C:\\Users\\james_gaam39t\\Downloads\\br (1).png")
    buv.config(image=img)
    buv.config(width=60, height=60)
    buv.pack()
    screen.mainloop()
