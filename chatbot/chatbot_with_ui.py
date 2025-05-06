from nltk.chat.util import Chat, reflections
import tkinter as tk
from tkinter import scrolledtext

# Define pet types and related information
pet_types = {
    'Dog': ['Labrador', 'Beagle', 'Bulldog', 'Poodle', 'German Shepherd'],
    'Cat': ['Persian', 'Siamese', 'Maine Coon', 'Bengal', 'British Shorthair'],
    'Bird': ['Parrot', 'Canary', 'Cockatiel', 'Lovebird', 'Macaw']
}

pet_care = {
    'Dog': ['Regular walks', 'Healthy diet', 'Training and socialization', 'Grooming'],
    'Cat': ['Litter box cleaning', 'Regular vet checkups', 'Nail trimming', 'Mental stimulation'],
    'Bird': ['Cage cleaning', 'Feeding nutritious seeds', 'Regular flying time', 'Mental enrichment']
}

pet_training = {
    'Dog': ['Sit', 'Stay', 'Roll over', 'Heel', 'Fetch'],
    'Cat': ['Litter box training', 'Come when called', 'Play fetch', 'High-five'],
    'Bird': ['Step up', 'Speak', 'Fetch', 'Wave', 'Dance']
}

# Main pet counseling information
pets = {
    'Dog': ['Loyal companion', 'Can live in apartments or houses', 'Requires daily exercise'],
    'Cat': ['Independent but affectionate', 'Perfect for smaller living spaces', 'Low maintenance'],
    'Bird': ['Colorful and fun', 'Requires large cage space', 'Loves social interaction']
}

patterns = [
    (r'hi|hello|hey',
     ['Hello! How can I help you with pet counseling today?', 'Hey there! Looking for information on pets?']),
    (r'how are you',
     ['I am just a bot, but I am always here to assist you with pet care!']),
    (r'(.*) pet(.*)',
     ['Here is a list of pets we can help with: ' + ', '.join(pets.keys()) + '. Which one interests you?',
      'Looking for information about pets? I can help with: ' + ', '.join(pets.keys()) + '.']),
    (r'(.*) (care|care tips)',
     ['Here are some care tips for each pet:' + ''.join([f"\n{pet}: {', '.join(care)}" for pet, care in pet_care.items()])]),
    (r'(.*) (training|training tips)',
     ['Here are some training tips for each pet:' + ''.join([f"\n{pet}: {', '.join(training)}" for pet, training in pet_training.items()])]),
    (r'(.*) (type|types)',
     ['I can help you with the following types of pets: ' + ', '.join(pets.keys()) + '. Which one would you like to learn more about?']),
    (r'(.*) dog(.*)',
     [f"The dog is a {', '.join(pets['Dog'])}. Would you like to know more about its care, training, or breeds?"]),
    (r'(.*) cat(.*)',
     [f"The cat is {', '.join(pets['Cat'])}. Would you like to know more about its care, training, or breeds?"]),
    (r'(.*) bird(.*)',
     [f"The bird is {', '.join(pets['Bird'])}. Would you like to know more about its care, training, or breeds?"]),
    (r'(.*) (dog|cat|bird) breed(.*)',
     ['Here are some breeds of {0}:\n'.format(pet) + ', '.join(pet_types[pet]) for pet in ['Dog', 'Cat', 'Bird']]),
    (r'(.*) (dog|cat|bird) care(.*)',
     ['Here is how to take care of a {0}:\n'.format(pet) + ', '.join(pet_care[pet]) for pet in ['Dog', 'Cat', 'Bird']]),
    (r'(.*) (dog|cat|bird) training(.*)',
     ['Here are some training tips for {0}:\n'.format(pet) + ', '.join(pet_training[pet]) for pet in ['Dog', 'Cat', 'Bird']]),
    (r'(.*) (price|cost)',
     ['The cost of adopting and caring for a pet depends on many factors, such as breed, age, and location. Would you like to know more about the expenses?']),
    (r'(.*) (adopt|adoption)',
     ['Would you like to know more about adopting a pet? I can help with that too!']),
    (r'(.*) bye|goodbye',
     ['Goodbye! Take care of your pet and see you soon!', 'Thanks for chatting! We hope your pet journey is amazing!'])
]

# Create the chatbot
pet_bot = Chat(patterns, reflections)

def main():
    root = tk.Tk()
    root.title("Pet Counseling ChatBot")

    chat_log = scrolledtext.ScrolledText(root, state='disabled', width=60, height=20, wrap='word', bg="#f0f0f0", fg="#333")
    chat_log.pack(padx=10, pady=10)

    entry_frame = tk.Frame(root)
    entry_frame.pack(fill='x', padx=10, pady=(0, 10))
    user_input = tk.Entry(entry_frame, width=50)
    user_input.pack(side='left', fill='x', expand=True)
    send_button = tk.Button(entry_frame, text="Send", width=10, command=lambda: send_message())
    send_button.pack(side='left', padx=(5, 0))

    def send_message():
        msg = user_input.get()
        if not msg.strip():
            return
        chat_log.config(state='normal')
        chat_log.insert('end', "You: " + msg + "\n")
        response = pet_bot.respond(msg)
        if response:
            chat_log.insert('end', "Pet Bot: " + response + "\n")
        else:
            chat_log.insert('end', "Pet Bot: I'm not sure how to respond to that. Can you rephrase?\n")
        chat_log.see('end')
        chat_log.config(state='disabled')
        user_input.delete(0, 'end')

    chat_log.config(state='normal')
    chat_log.insert('end', "Pet Bot: Hello! Welcome to the Pet Counseling ChatBot. How can I help you today?\n")
    chat_log.config(state='disabled')

    root.bind('<Return>', lambda event: send_message())
    root.mainloop()

main()
