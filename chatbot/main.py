from nltk.chat.util import Chat, reflections

# Define movies, showtimes, and seat types for booking
movies = {
    'Avatar 2': ['3:00 PM', '6:00 PM', '9:00 PM'],
    'The Flash': ['1:00 PM', '4:00 PM', '7:00 PM'],
    'Spider-Man: No Way Home': ['2:30 PM', '5:30 PM', '8:30 PM']
}

seat_types = ['Regular', 'VIP', 'IMAX']

# Main movie information
movie_details = {
    'Avatar 2': ['Sci-Fi, Action', 'Directed by James Cameron', 'Duration: 3 hours 10 minutes'],
    'The Flash': ['Superhero, Action', 'Directed by Andy Muschietti', 'Duration: 2 hours 30 minutes'],
    'Spider-Man: No Way Home': ['Action, Superhero', 'Directed by Jon Watts', 'Duration: 2 hours 28 minutes']
}

patterns = [
    (r'hi|hello|hey',
     ['Hello! How can I assist you with movie ticket booking today?', 'Hey there! Looking to book a movie ticket?',
      'Hi! Ready to book your movie tickets?']),
    (r'how are you',
     ['I am just a bot, but I am always ready to help you book your movie tickets!',
      'I am doing well, thanks for asking. How can I assist you with movie booking today?']),
    (r'(.*) movie(.*)',
     ['Here are the movies currently available for booking: ' + ', '.join(movies.keys()) + '. Which movie interests you?',
      'Sure! Here are the movies you can book tickets for: ' + ', '.join(movies.keys()) + '.']),
    (r'(.*) (showtime|show times)',
     ['Here are the showtimes for each movie: ' + ''.join([f"\n{movie}: {', '.join(showtimes)}" for movie, showtimes in movies.items()])]),
    (r'(.*) (details|info|information)',
     ['Here are the movie details for each film:' + ''.join([f"\n{movie}: {', '.join(details)}" for movie, details in movie_details.items()])]),
    (r'(.*) (seat|seats)',
     ['Here are the seat types available for booking: ' + ', '.join(seat_types) + '. Which seat type would you like to select?']),
    (r'(.*) (book|schedule|appointment)',
     ['I can help you with booking your movie tickets. Please provide the following details.']),
    (r'(.*) (bye|goodbye)',
     ['Thank you for booking with us. Have a great time at the movies!', 'Goodbye! Enjoy your movie experience!', 'Bye! We hope to see you again soon!']),
]

# Create a chatbot
movie_bot = Chat(patterns, reflections)


def schedule_booking(movie_name, showtime, seat_type, name, contact):
    return f"Booking confirmed! Your tickets for '{movie_name}' at {showtime} with {seat_type} seats are booked.\nWe have your details as: {name}, {contact}."


def main():
    print("\nHello! Welcome to the Movie Ticket Booking ChatBot. How can I assist you today?")

    while True:
        user_input = input("You: ")
        response = movie_bot.respond(user_input)
        print("Movie Bot:", response)

        # Extract information for booking movie tickets
        if any(word in user_input.lower() for word in ['book', 'schedule', 'appointment']):
            movie_name = input("Which movie would you like to book tickets for? (Avatar 2/The Flash/Spider-Man: No Way Home): ")

            # Display showtimes for selected movie
            if movie_name in movies:
                print(f"Available showtimes for {movie_name}: {', '.join(movies[movie_name])}")
                showtime = input(f"Which showtime for {movie_name} interests you? : ")
            else:
                showtime = "3:00 PM"

            # Select seat type
            print(f"Available seat types: {', '.join(seat_types)}")
            seat_type = input("Which seat type would you like to choose? : ")

            name = input("Could you please provide your name? : ")
            contact = input("And your contact number or email? : ")
            booking_response = schedule_booking(movie_name, showtime, seat_type, name, contact)
            print("Movie Bot:", booking_response)

        # Check if the user wants to end the conversation
        if any(word in user_input.lower() for word in ['bye', 'goodbye']):
            break


main()
