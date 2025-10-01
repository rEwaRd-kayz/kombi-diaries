# Transform for fullscreen background images
# Start and arrival screen images
image start_screen = "start.jpg"
image arrival_screen = "arrival.jpg"
# Transform to scale character images to normal size
transform normal_size:
    size (1600, 1200) # Much wider character images

# The script of the game goes in this file.


# Image definitions (add your image files to the 'game' folder)
image bg street = "street.jpg"
image bg kombi_inside = "kombi_inside.jpg"
image conductor = "conductor.png"
image driver = "driver.png"
image passenger = "passenger.png"

# Sound definitions (add your sound files to the 'game' folder)
# Example usage: play sound "door_open.ogg"
# Example usage: play music "city.mp3"


define p = Character("Passenger")
define d = Character("Driver")
define c = Character("Conductor")


# The game starts here.

label start:


    scene start_screen

    play music "city.mp3"


    show conductor at normal_size
    "Conductor: Hey there! Ready to get on the kombi?"

    menu:
        "Yes, I'm in!":
            jump kombi_inside
        "No, not today":
            "You decide to walk instead. Game Over."
            return

label kombi_inside:

    scene bg kombi_inside

    show driver at normal_size
    "Driver: Fare is 1.50. Please pay before we go."

    menu:
        "Pay with EcoCash":
            jump payment_ecocash
        "Pay with Bank Transfer":
            jump payment_bank

label payment_ecocash:

    "You paid using EcoCash."
    jump end_trip

label payment_bank:


    "Please enter bank details."
    $ account_name = "John Kombi"
    $ account_number = "123456789"
    $ bank = "ZB Bank"

    "Bank Name: {bank}"
    "Account Name: {account_name}"
    "Account Number: {account_number}"

    "Payment done successfully."
    jump end_trip

label end_trip:


    "The kombi drives off through the bustling city..."

    c "Where are you headed today?"
    menu:
        "Mbare Market":
            jump mbare_route
        "Avondale Shopping Centre":
            jump avondale_route
        "University of Zimbabwe":
            jump uz_route

label mbare_route:
    scene bg kombi_inside
    "You chose to go to Mbare Market. The kombi is lively with vendors."
    jump random_event

label avondale_route:
    scene bg kombi_inside
    "You chose Avondale Shopping Centre. The ride is calm and you see the city pass by."
    jump random_event

label uz_route:
    scene bg kombi_inside
    "You chose University of Zimbabwe. A student sits next to you."
    show passenger at normal_size
    p "Hi! Are you also going to campus?"
    menu:
        "Yes, I am a student there.":
            p "Awesome! Maybe we have a class together."
        "No, just visiting.":
            p "Cool! Hope you enjoy your visit."
    jump random_event

label random_event:
    $ import random
    $ event = random.choice(["police", "smooth"])
    if event == "police":
        scene bg street
        "Suddenly, the kombi is stopped at a police roadblock."
        d "Everyone, please stay calm."
        "After a quick check, the kombi is allowed to proceed."
    else:
        "The ride continues smoothly with music playing."
    jump game_end

label game_end:
    scene arrival_screen
    "You arrive safely at your destination."
    "Thanks for playing Kombi Tales!"
    return


