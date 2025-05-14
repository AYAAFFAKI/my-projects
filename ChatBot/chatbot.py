import customtkinter as ctk

#fonction de reponse du chatbot:
def chatbot_response(user_input):
    responses ={
        "bonjour":"Bonjour! comment puis-je vous aider?",
        "comment ça va?":"Je suis un programme, donc je suis toujours bien!",
        "quelle heure est-il?":"Je ne peux pas dire l'heure exacte, mais il est le temps de coder!",
        "au revoir":"Au revoir, passez une bonne journée!"
    }
    return responses.get(user_input.lower(), "Désolé je ne comprends pas votre question..")

#fonction pour  gérer l'envoie du message:
def send_message(event=None):
    user_message= user_input.get()
    #verfier si le message est vide:
    if user_message.strip() != "":   #strip(): eveter l'espace au debut et à la fin
        chat_history.configure(state= "normal")
        chat_history.insert("end",f"vous: {user_message}\n\n.","user")
        bot_response = chatbot_response(user_message)
        chat_history.insert("end",f"Chatbot: {bot_response}\n\n.","bot")
        chat_history.configure(state= "disabled")
        chat_history.see("end")
        user_input.delete(0,"end")

#config l'interface graphique:
app = ctk.CTk()
app.geometry("500x500")
app.title("chatbot1")

#creation de l'en-tete:
header = ctk.CTkLabel(app, text="Bienvenue sur le chatbot1",font=("Arial",18,"bold"),)
header.pack(pady =10) #pour affiche #pady =10: pour ajouter 10px ven haut

#zone d'afficheage les message:
chat_history = ctk.CTkTextbox(app, height=350, state = "disabled")#state = "disabled": modification diericte d'utilisation
#cnfig les coleur de mess d'utilisateur:
chat_history.tag_config("user", foreground="white")
#cnfig les coleur de mess de bot:
chat_history.tag_config("bot", foreground="green")
chat_history.pack(pady =10, padx =10,fill="both",expand =True)
chat_history.configure(font=("Arial",16))

#champ de saiser d'utilisateur:
user_input_frame = ctk.CTkFrame(app)
user_input_frame.pack(pady =10,padx=10,fill='x')

user_input=ctk.CTkEntry(user_input_frame,placeholder_text="Enter votre message ici....",width=330)
user_input.pack(side="left",padx=5)

send_button= ctk.CTkButton(user_input_frame, text="envoyer",command= send_message)
send_button.pack(side= 'left')

#associer la touche "Entree" au champ de saiser pour envoyer  le message:
app.bind("<Return>", send_message)

app.mainloop() #comme show