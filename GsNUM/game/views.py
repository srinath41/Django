from django.shortcuts import render
import random

def index(request):
    if request.method == 'POST':
        # Extract the user's guess from the form submission
        user_guess = int(request.POST['guess'])
        # Retrieve the randomly generated number from the session
        random_number = request.session.get('random_number')
        if user_guess == random_number:
            # If the guess is correct, display a success message
            message = "Congratulations! You guessed the number correctly."
        elif user_guess > random_number:
            # If the guess is too high, provide a hint
            message = "You are close a bit! But it's Greater than the number. Try again."
        else:
            # If the guess is too low, provide a hint
            message = "You are close a bit! But it's Lesser than the number. Try again."
    else:
        # If it's a GET request (initial load), generate a random number and store it in the session
        random_number = random.randint(1, 10)
        request.session['random_number'] = random_number
        # Display the initial message
        message = "The number is locked! Now guess it..."
    # Render the template with the message
    return render(request, 'game/index.html', {'message': message})
