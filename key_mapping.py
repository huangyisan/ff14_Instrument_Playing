import pyautogui

shift = 't'
ctrl = 'b'
# Bass
_note_Bass_Do = [ctrl,'q']
_note_Bass_Re = [ctrl,'w']
_note_Bass_Mi = [ctrl,'e']
_note_Bass_Fa = [ctrl,'r']
_note_Bass_So = [ctrl,'t']
_note_Bass_La = [ctrl,'y']
_note_Bass_Si = [ctrl,'u']

# Normal
_note_Normal_Do = ['n','q']
_note_Normal_Re = ['n','w']
_note_Normal_Mi = ['n','e']
_note_Normal_Fa = ['n','r']
_note_Normal_So = ['n','t']
_note_Normal_La = ['n','y']
_note_Normal_Si = ['n','u']

# Treble
_note_Treble_Do = [shift,'q']
_note_Treble_Re = [shift,'w']
_note_Treble_Mi = [shift,'e']
_note_Treble_Fa = [shift,'r']
_note_Treble_So = [shift,'t']
_note_Treble_La = [shift,'y']
_note_Treble_Si = [shift,'u']

def press_a_key(note, ptime):
    if note[0] == ctrl:
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown(note[1],pause=ptime)
        pyautogui.keyUp(note[1])
        pyautogui.keyUp('ctrl')
    elif note[0] == 'n':
        pyautogui.keyDown(note[1],pause=ptime)
        pyautogui.keyUp(note[1])
    elif note[0] == shift:
        pyautogui.keyDown('shift')
        pyautogui.keyDown(note[1],pause=ptime)
        pyautogui.keyUp(note[1])
        pyautogui.keyUp('shift')


def Bass_Do(ptime):
    press_a_key(_note_Bass_Do, ptime)
def Bass_Re(ptime):
    press_a_key(_note_Bass_Re, ptime)
def Bass_Mi(ptime):
    press_a_key(_note_Bass_Mi, ptime)
def Bass_Fa(ptime):
    press_a_key(_note_Bass_Fa, ptime)
def Bass_So(ptime):
    press_a_key(_note_Bass_So, ptime)
def Bass_La(ptime):
    press_a_key(_note_Bass_La, ptime)
def Bass_Si(ptime):
    press_a_key(_note_Bass_Si, ptime)


def Normal_Do(ptime):
    press_a_key(_note_Normal_Do, ptime)
def Normal_Re(ptime):
    press_a_key(_note_Normal_Re, ptime)
def Normal_Mi(ptime):
    press_a_key(_note_Normal_Mi, ptime)
def Normal_Fa(ptime):
    press_a_key(_note_Normal_Fa, ptime)
def Normal_So(ptime):
    press_a_key(_note_Normal_So, ptime)
def Normal_La(ptime):
    press_a_key(_note_Normal_La, ptime)
def Normal_Si(ptime):
    press_a_key(_note_Normal_Si, ptime)


def Treble_Do(ptime):
    press_a_key(_note_Treble_Do, ptime)
def Treble_Re(ptime):
    press_a_key(_note_Treble_Re, ptime)
def Treble_Mi(ptime):
    press_a_key(_note_Treble_Mi, ptime)
def Treble_Fa(ptime):
    press_a_key(_note_Treble_Fa, ptime)
def Treble_So(ptime):
    press_a_key(_note_Treble_So, ptime)
def Treble_La(ptime):
    press_a_key(_note_Treble_La, ptime)
def Treble_Si(ptime):
    press_a_key(_note_Treble_Si, ptime)





