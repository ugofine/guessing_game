#GUESSING GAME- Is about guessing a number betwween 1 to 100.
#define a function for the game
def number_guessing_games_for_students ():
    
#We will print the isntructions or explanation  of the game
  print("Welcome to my brain teaser game!")
  print("Tell us the number you are thinking of right now......!")
  print("Rememeber ypou have only 5 attempts to guess the number correctly!")
  
#We will set our secret number
  my_secret_number = 33
#Ww set the number of attempts the student will make, this is the maximum number of guesses by each player
  num_of_attempts = 5  
  guessed_correctly = False # tracks if the student guessed the number correctly
    
#We are going to create the loop for the game
  while num_of_attempts > 0:
    try:
      
        your_guess = int(input("Can you enter your({num_of_attempts}) num_of_attempts):    ")) # we are asking a student to enter a number, convert it to an integer
        num_of_attempts -=1 # the attempts is reducing by one after each guess
#Logical check on the gueesed number        
        if  your_guess < my_secret_number:
            print("YOUR NUMNBER IS TOO LOW")
        elif your_guess > my_secret_number:
            print("PLEASE YOUR NUMBER IS TOO HIGH!!!!!")   
        else:
            print(f"Congratualtions you have guessed it right, and the number is {my_secret_number} ") 
            guessed_correctly = True
            break
    except ValueError:
      num_of_attempts -= 1
      print("Your guess is invalid!!!!!!!!") # the students guessed a letter insted of a numnber
    if not guessed_correctly:      
            print ("THE GAME IS OVER FOR YOU, TRY AGAIN")
                #print(f"this is the answer {my_secret_number}")
        
number_guessing_games_for_students() # it calls the function again to start afresh                
        
        #the conditiion to terminate the error and a statement to print the end of the game
        
          









