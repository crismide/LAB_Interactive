from time import sleep
from furhat_remote_api import FurhatRemoteAPI
from numpy.random import randint

FURHAT_IP = "localhost"

furhat = FurhatRemoteAPI(FURHAT_IP)
furhat.set_led(red=100, green=50, blue=50)


FACES = {
    'Loo'    : 'Patricia',
    'Amany'  : 'Nazar'
}

VOICES_EN = {
    'Loo'    : 'BellaNeural',
    'Amany'  : 'CoraNeural'
}

def idle_animation():
    furhat.gesture(name="GazeAway")
    gesture = {"frames" : 
        [{
            "time" : [0.33],
            "persist" : True,
            "params": {
                "NECK_PAN"  : randint(-4,4),
                "NECK_TILT" : randint(-4,4),
                "NECK_ROLL" : randint(-4,4),
            }
        }],

    "class": "furhatos.gestures.Gesture"
    }
    furhat.gesture(body=gesture, blocking=True)

def LOOK_BACK(speed):
    return {
    "frames": [
        {
            "time": [
                0.33 / speed
            ],
            "persist": True,
            "params": {
                'LOOK_DOWN' : 0,
                'LOOK_UP' : 0,
                'NECK_TILT' : 0
            }
        }, {
            "time": [
                1 / speed
            ],
            "params": {
                "NECK_PAN": 0,
                'LOOK_DOWN' : 0,
                'LOOK_UP' : 0,
                'NECK_TILT' : 0
            }
        }
    ],
    "class": "furhatos.gestures.Gesture"
    }

# DO NOT CHANGE
def LOOK_DOWN(speed=1):
    return {
    "frames": [
        {
            "time": [
                0.33 / speed
            ],
            "persist": True,
            "params": {
#                'LOOK_DOWN' : 1.0
            }
        }, {
            "time": [
                1 / speed
            ],
            "persist": True,
            "params": {
                "NECK_TILT": 20
            }
        }
    ],
    "class": "furhatos.gestures.Gesture"
    }

def set_persona(persona):
    furhat.gesture(name="CloseEyes")
    furhat.gesture(body=LOOK_DOWN(speed=1), blocking=True)
    sleep(0.3)
    furhat.set_face(character=FACES[persona], mask="Adult")
    furhat.set_voice(name=VOICES_EN[persona])
    sleep(2)
    furhat.gesture(body=LOOK_BACK(speed=1), blocking=True)

# Say with blocking (blocking say, bsay for short)
def bsay(line):
    furhat.say(text=line, blocking=True)

def demo_personas():
    set_persona("Loo")
    

    furhat.gesture(name='Smile')
    bsay("Hi!")
    bsay("How are you?")
    result = furhat.listen()
    print(result.message)
    if result.message == "fine" or result.message == "good":
        bsay("That's nice")
        furhat.gesture(name='BigSmile')
        bsay("Do you want to hear a joke?")
        result_joke = furhat.listen()
        if result_joke.message == "yes":
            bsay("I love when the earth do the rotation, it makes my day")
            furhat.gesture(name='BigSmile')
            sleep(2)
            bsay("Do you want to hear a pickup line?")
            result_pickup = furhat.listen()
            if result_pickup.message == "yes":
                bsay("Are your pants a compressed file? Cause I want to unzip them")
                furhat.gesture(name='Wink')
            else:
                bsay("Okay, I will not flirt with you")
                furhat.gesture(name='ExpressDisgust')
        elif result_joke.message == "no":
            bsay("Okay, I will leave you alone")
            furhat.gesture(name='ExpressAnger')
    elif result.message == "bad": 
        bsay("Thats is so sad")
        furhat.gesture(name='ExpressSad')
        bsay("What happened?")
        furhat.gesture(name='Surprise')
        sleep(5)
        bsay("That is too bad")

    else: 
        furhat.gesture(name='Shake')
        bsay("Sorry, I could not understand you")

if __name__ == '__main__':
    demo_personas()
    idle_animation()
