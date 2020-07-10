import datetime
import pytz

a_list_of_choices = ["Learn Python", "Learn Java", "Go Swimming",
                     "Have Dinner", "Go to bed"]

while True:
    my_choice = int(input(":::The Menu:::\n"
                          "Please choose an option.\n"
                          "1. Learn Python\n"
                          "2. Learn Java\n"
                          "3. Go Swimming\n"
                          "4. Have Dinner\n"
                          "5. Go to bed\n"
                          "0. Exit\n"
                          "What is your choice:"))
    if my_choice == 0:
        print("Exiting now...")
        break
    elif 1 <= my_choice <= 5:
        print("The time is {}, and I am going to go {}".
            format(datetime.datetime.now(
            tz=pytz.timezone("Asia/Kolkata")),
            a_list_of_choices[my_choice - 1]))
    else:
        print("You entered the wrong choice, please try again...")

    print("*" * 50)
