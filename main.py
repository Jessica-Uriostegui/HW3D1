
# import file mood_responses where functions for mood inputs are located
# create main() funtion  where user can be asked to input mood

import mood_responses

def main():
    mood = input("How are you feeling today? happy,sad or excited \n").lower()
    try:
        if mood == "happy":
            print(mood_responses.happy(mood))
            
        elif mood == "sad":
            print(mood_responses.sad(mood))

        elif mood == "excited":
            print(mood_responses.excited(mood))
        else:
            print("Not a valid mood")
        
    except Exception as e:
        print(f"An error ocurred: {e}")
main()