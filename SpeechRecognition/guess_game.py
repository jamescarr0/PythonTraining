import random
import time

import speech_recognition as sr


def recognise_speech_from_mic(recogniser, mic, lang="en-GB") -> dict:
    """ Transcribe speech from a micrphone

    Args:
        recogniser (Recognizer): Recogniser object.
        mic (speech_recognition.Microphone): Recorded speech from a mic

    Returns:
        dict with three keys: 
            "success" : a bool indicating wether or not the API request was successful
            "error" : 'None' if no error otherwise a string containing the err msg.
    """

    # Check that recogniser and microphones are the correct type.
    if not isinstance(recogniser, sr.Recognizer):
        raise TypeError("recogniser must be a Recognizer instance")

    if not isinstance(mic, sr.Microphone):
        raise TypeError("mic must be a Microphone instance")

    # Adjust recogniser sensitivity to ambient noise and record audio from the mic.
    with mic as source:
        recogniser.adjust_for_ambient_noise(source, duration=0.5)
        audio = recogniser.listen(source, timeout=5)

    # Setup the response object
     #  Keys
    TRANS = "transcription"
    SUCC = "success"
    ERR = "error"

    res = {
        SUCC: True,
        ERR: None,
        TRANS: None
    }

    # Try recognising the speech in the recording.
    # If a RequestError or UnknownValueError exception is caught, update the
    # respsone object accordingly.
    try:
        res[TRANS] = recogniser.recognize_google(audio, language=lang)
    except sr.RequestError:
        # API unreachable or unresponsive
        res[SUCC] = False
        res[ERR] = "API unavailable."
    except sr.UnknownValueError:
        res[ERR] = "Unable to recognise speech"


    return res


def run():
    WORDS = ["apple", "banana", "grape", "orange", "mango", "lemon"]
    NUM_GUESSES = 3
    PROMPT_LIMIT = 5
    GAME_WON = False

    recogniser = sr.Recognizer()
    mic = sr.Microphone()
    
    instructions = (
        "I am thinking of one of these words:\n"
        f"{', '.join(WORDS)}\n"
        f"You have {NUM_GUESSES} tries to guess which one.\n"
        "Good luck!"
    )

    print(instructions)
    time.sleep(2)

    WORD = random.choice(WORDS)

    for i in range(NUM_GUESSES):

        for _ in range(PROMPT_LIMIT):
            print(f"Guess {i+1}: What word am i thinking?\nSpeak>")
            guess = recognise_speech_from_mic(recogniser, mic)
            
            if guess["error"] == "Unable to recognise speech":
                print(f"Error: {guess['error']} please try again..")
                continue

            if guess['error'] or not guess['success']:
                print(f"Error: {guess['error']}")
                return 

            if guess['success'] and guess["transcription"]:
                break
        
        print(f"You guessed: '{guess['transcription']}'")
        if guess['transcription'].lower() == WORD:
            GAME_WON = True
            break
        else:
            print(f"Incorrect.  {'Try again.' if i!=NUM_GUESSES-1 else 'GAME OVER'}")

    if GAME_WON:
        print("Correct! You Win!!")
    else:
        print(f"Sorry, you loose, i was thinking of the word '{WORD}'")

if __name__ == '__main__':
    run()
