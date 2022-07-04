#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on juni 27, 2022, at 10:09
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

import numpy as np







# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.3'
expName = 'SelectiveAttentionTest'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\psychoPy\\SelectiveAttention\\SelectiveAttentionTest_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 720], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "Intro"
IntroClock = core.Clock()
IntroText = visual.TextStim(win=win, name='IntroText',
    text='Velkommen til Opmærksomheds testen. \n\nDu vil blive præsenteret for bogstaver\nhold øje med b og p. \nEn af dem vil være i højre eller venstre side af skærmen. \nHvis du ser p klik til venstre på musen\nHvis du ser b klik til højre på musen\nKlik når skærmen bliver sort\n\ngod fornøjelse ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
next_screen1 = keyboard.Keyboard()

# Initialize components for Routine "FixationCross"
FixationCrossClock = core.Clock()
FixationCrossText = visual.TextStim(win=win, name='FixationCrossText',
    text='X',
    font='Open Sans ExtraBold',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "VisualDistractorStimuli"
VisualDistractorStimuliClock = core.Clock()
# setup variables to control the experiment
distractorPos = (0.0,0.3)
filler_up_left_pos = (-0.15,0.1)
filler_low_left_pos = (-0.15,-0.1)
filler_low_right_pos = (0.15,-0.1)
filler_up_right_pos = (0.15,0.1)
allowedBNeutral = 2; 
allowedBIncongruence = 2; 
allowedBCongruence = 2;
allowedPNeutral = 2; 
allowedPIncongruence = 2; 
allowedPCongruence = 2; 
targetletter = 'g';


#Default positions
p_targetpos = (1,1)
b_targetpos = (1,1)
p_distractorpos = (1,1)
b_distractorpos = (1,1)
g_distractorpos = (1,1)
h_fillerpos = (1,1)
l_fillerpos = (1,1)
y_fillerpos = (1,1)
p_Target_2 = visual.TextStim(win=win, name='p_Target_2',
    text='',
    font='Arial',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
b_Target_2 = visual.TextStim(win=win, name='b_Target_2',
    text='b',
    font='Arial',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
p_Distractor_2 = visual.TextStim(win=win, name='p_Distractor_2',
    text='p',
    font='Open Sans ExtraBold',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
b_Distractor_2 = visual.TextStim(win=win, name='b_Distractor_2',
    text='b',
    font='Open Sans ExtraBold',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
g_Distractor_2 = visual.TextStim(win=win, name='g_Distractor_2',
    text='g',
    font='Open Sans ExtraBold',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
h_Filler_2 = visual.TextStim(win=win, name='h_Filler_2',
    text='h',
    font='Open Sans ExtraBold',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
l_Filler_2 = visual.TextStim(win=win, name='l_Filler_2',
    text='l',
    font='Open Sans ExtraBold',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
y_filler_2 = visual.TextStim(win=win, name='y_filler_2',
    text='y',
    font='Open Sans ExtraBold',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
isItP = False;
isItB = False;
enableSadface = False;
enableHappyface = False;
enableFaster = False;
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
whiteimage_2 = visual.ImageStim(
    win=win,
    name='whiteimage_2', 
    image='graphic/black.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
Faster = visual.TextStim(win=win, name='Faster',
    text='Hurtigere',
    font='Open Sans ExtraBold',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
happy = visual.ImageStim(
    win=win,
    name='happy', 
    image='graphic/happyface.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
sad = visual.ImageStim(
    win=win,
    name='sad', 
    image='graphic/sadface.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# Initialize components for Routine "Pause"
PauseClock = core.Clock()
Pause_Text = visual.TextStim(win=win, name='Pause_Text',
    text='Pause\n\ntryk på en tast når du er klar til at fortsætte',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
next_screen1_2 = keyboard.Keyboard()

# Initialize components for Routine "FixationCross"
FixationCrossClock = core.Clock()
FixationCrossText = visual.TextStim(win=win, name='FixationCrossText',
    text='X',
    font='Open Sans ExtraBold',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "AudioVisualDistractorStimuli"
AudioVisualDistractorStimuliClock = core.Clock()
allowedBNeutralAV = 2; 
allowedBIncongruenceAV = 2; 
allowedBCongruenceAV = 2;
allowedPNeutralAV = 2; 
allowedPIncongruenceAV = 2; 
allowedPCongruenceAV = 2; 


#Default Distractor Volume 
p_dis_volume = 0.0
b_dis_volume = 0.0
g_dis_volume = 0.0
p_Target = visual.TextStim(win=win, name='p_Target',
    text='',
    font='Arial',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
b_Target = visual.TextStim(win=win, name='b_Target',
    text='b',
    font='Arial',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
p_Distractor = visual.TextStim(win=win, name='p_Distractor',
    text='p',
    font='Open Sans ExtraBold',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
b_Distractor = visual.TextStim(win=win, name='b_Distractor',
    text='b',
    font='Open Sans ExtraBold',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
g_Distractor = visual.TextStim(win=win, name='g_Distractor',
    text='g',
    font='Open Sans ExtraBold',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
h_Filler = visual.TextStim(win=win, name='h_Filler',
    text='h',
    font='Open Sans ExtraBold',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
l_Filler = visual.TextStim(win=win, name='l_Filler',
    text='l',
    font='Open Sans ExtraBold',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
y_filler = visual.TextStim(win=win, name='y_filler',
    text='y',
    font='Open Sans ExtraBold',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
p_Dis_Sound = sound.Sound('audio/p.wav', secs=0.2, stereo=True, hamming=False,
    name='p_Dis_Sound')
p_Dis_Sound.setVolume(1.0)
b_Dis_Sound = sound.Sound('audio/b.wav', secs=0.2, stereo=True, hamming=False,
    name='b_Dis_Sound')
b_Dis_Sound.setVolume(1.0)
g_Dis_Sound = sound.Sound('audio/g.wav', secs=0.2, stereo=True, hamming=False,
    name='g_Dis_Sound')
g_Dis_Sound.setVolume(1.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
whiteimage = visual.ImageStim(
    win=win,
    name='whiteimage', 
    image='graphic/black.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
Faster = visual.TextStim(win=win, name='Faster',
    text='Hurtigere',
    font='Open Sans ExtraBold',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
happy = visual.ImageStim(
    win=win,
    name='happy', 
    image='graphic/happyface.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
sad = visual.ImageStim(
    win=win,
    name='sad', 
    image='graphic/sadface.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# Initialize components for Routine "Pause"
PauseClock = core.Clock()
Pause_Text = visual.TextStim(win=win, name='Pause_Text',
    text='Pause\n\ntryk på en tast når du er klar til at fortsætte',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
next_screen1_2 = keyboard.Keyboard()

# Initialize components for Routine "FixationCross"
FixationCrossClock = core.Clock()
FixationCrossText = visual.TextStim(win=win, name='FixationCrossText',
    text='X',
    font='Open Sans ExtraBold',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "AudioDistractorStimuli"
AudioDistractorStimuliClock = core.Clock()
allowedBNeutralA = 2; 
allowedBIncongruenceA = 2; 
allowedBCongruenceA = 2;
allowedPNeutralA = 2; 
allowedPIncongruenceA = 2; 
allowedPCongruenceA = 2; 


#Default Distractor Volume 
p_dis_volume = 0.0
b_dis_volume = 0.0
g_dis_volume = 0.0
p_Target_3 = visual.TextStim(win=win, name='p_Target_3',
    text='',
    font='Arial',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
b_Target_3 = visual.TextStim(win=win, name='b_Target_3',
    text='b',
    font='Arial',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
h_Filler_3 = visual.TextStim(win=win, name='h_Filler_3',
    text='h',
    font='Open Sans ExtraBold',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
l_Filler_3 = visual.TextStim(win=win, name='l_Filler_3',
    text='l',
    font='Open Sans ExtraBold',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
y_filler_3 = visual.TextStim(win=win, name='y_filler_3',
    text='y',
    font='Open Sans ExtraBold',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
p_Dis_Sound_2 = sound.Sound('audio/p.wav', secs=0.2, stereo=True, hamming=False,
    name='p_Dis_Sound_2')
p_Dis_Sound_2.setVolume(1.0)
b_Dis_Sound_2 = sound.Sound('audio/b.wav', secs=0.2, stereo=True, hamming=False,
    name='b_Dis_Sound_2')
b_Dis_Sound_2.setVolume(1.0)
g_Dis_Sound_2 = sound.Sound('audio/g.wav', secs=0.2, stereo=True, hamming=False,
    name='g_Dis_Sound_2')
g_Dis_Sound_2.setVolume(1.0)
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()
whiteimage_3 = visual.ImageStim(
    win=win,
    name='whiteimage_3', 
    image='graphic/black.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
Faster = visual.TextStim(win=win, name='Faster',
    text='Hurtigere',
    font='Open Sans ExtraBold',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
happy = visual.ImageStim(
    win=win,
    name='happy', 
    image='graphic/happyface.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
sad = visual.ImageStim(
    win=win,
    name='sad', 
    image='graphic/sadface.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Intro"-------
continueRoutine = True
# update component parameters for each repeat
next_screen1.keys = []
next_screen1.rt = []
_next_screen1_allKeys = []
# keep track of which components have finished
IntroComponents = [IntroText, next_screen1]
for thisComponent in IntroComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
IntroClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Intro"-------
while continueRoutine:
    # get current time
    t = IntroClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=IntroClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *IntroText* updates
    if IntroText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IntroText.frameNStart = frameN  # exact frame index
        IntroText.tStart = t  # local t and not account for scr refresh
        IntroText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IntroText, 'tStartRefresh')  # time at next scr refresh
        IntroText.setAutoDraw(True)
    
    # *next_screen1* updates
    waitOnFlip = False
    if next_screen1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_screen1.frameNStart = frameN  # exact frame index
        next_screen1.tStart = t  # local t and not account for scr refresh
        next_screen1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_screen1, 'tStartRefresh')  # time at next scr refresh
        next_screen1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_screen1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_screen1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_screen1.status == STARTED and not waitOnFlip:
        theseKeys = next_screen1.getKeys(keyList=None, waitRelease=False)
        _next_screen1_allKeys.extend(theseKeys)
        if len(_next_screen1_allKeys):
            next_screen1.keys = _next_screen1_allKeys[-1].name  # just the last key pressed
            next_screen1.rt = _next_screen1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Intro"-------
for thisComponent in IntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('IntroText.started', IntroText.tStartRefresh)
thisExp.addData('IntroText.stopped', IntroText.tStopRefresh)
# check responses
if next_screen1.keys in ['', [], None]:  # No response was made
    next_screen1.keys = None
thisExp.addData('next_screen1.keys',next_screen1.keys)
if next_screen1.keys != None:  # we had a response
    thisExp.addData('next_screen1.rt', next_screen1.rt)
thisExp.addData('next_screen1.started', next_screen1.tStartRefresh)
thisExp.addData('next_screen1.stopped', next_screen1.tStopRefresh)
thisExp.nextEntry()
# the Routine "Intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
VisualDistractionTrials = data.TrialHandler(nReps=12.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='VisualDistractionTrials')
thisExp.addLoop(VisualDistractionTrials)  # add the loop to the experiment
thisVisualDistractionTrial = VisualDistractionTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisVisualDistractionTrial.rgb)
if thisVisualDistractionTrial != None:
    for paramName in thisVisualDistractionTrial:
        exec('{} = thisVisualDistractionTrial[paramName]'.format(paramName))

for thisVisualDistractionTrial in VisualDistractionTrials:
    currentLoop = VisualDistractionTrials
    # abbreviate parameter names if possible (e.g. rgb = thisVisualDistractionTrial.rgb)
    if thisVisualDistractionTrial != None:
        for paramName in thisVisualDistractionTrial:
            exec('{} = thisVisualDistractionTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "FixationCross"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    FixationCrossComponents = [FixationCrossText]
    for thisComponent in FixationCrossComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FixationCrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "FixationCross"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FixationCrossClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FixationCrossClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FixationCrossText* updates
        if FixationCrossText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FixationCrossText.frameNStart = frameN  # exact frame index
            FixationCrossText.tStart = t  # local t and not account for scr refresh
            FixationCrossText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FixationCrossText, 'tStartRefresh')  # time at next scr refresh
            FixationCrossText.setAutoDraw(True)
        if FixationCrossText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FixationCrossText.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                FixationCrossText.tStop = t  # not accounting for scr refresh
                FixationCrossText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FixationCrossText, 'tStopRefresh')  # time at next scr refresh
                FixationCrossText.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FixationCrossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FixationCross"-------
    for thisComponent in FixationCrossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    VisualDistractionTrials.addData('FixationCrossText.started', FixationCrossText.tStartRefresh)
    VisualDistractionTrials.addData('FixationCrossText.stopped', FixationCrossText.tStopRefresh)
    
    # ------Prepare to start Routine "VisualDistractorStimuli"-------
    continueRoutine = True
    routineTimer.add(0.700000)
    # update component parameters for each repeat
    p_targetpos = (1,1)
    b_targetpos = (1,1)
    p_distractorpos = (1,1)
    b_distractorpos = (1,1)
    g_distractorpos = (1,1)
    h_fillerpos = (1,1)
    l_fillerpos = (1,1)
    y_fillerpos = (1,1)
    p_dis_volume = 0.0
    b_dis_volume = 0.0
    g_dis_volume = 0.0
    
    def FindTargetAndDistractor(allowedPCongruence, allowedPIncongruence, allowedPNeutral, allowedBCongruence, allowedBIncongruence, allowedBNeutral):
        tar = np.random.choice(targets);
        tarAndDist = FindDistractor(tar, allowedPCongruence, allowedPIncongruence, allowedPNeutral, allowedBCongruence, allowedBIncongruence, allowedBNeutral);
        return tarAndDist; 
        
    def FindDistractor(target, allowedPCongruence, allowedPIncongruence, allowedPNeutral, allowedBCongruence, allowedBIncongruence, allowedBNeutral):
        
        dist = np.random.choice(distractors);
        if target == 'p' and dist == 'p' and allowedPCongruence > 0:
            allowedPCongruence = allowedPCongruence -1; 
            thisExp.addData('Condition', 'Congruent')
            return target, dist, allowedPCongruence, allowedPIncongruence, allowedPNeutral, allowedBCongruence, allowedBIncongruence, allowedBNeutral;
        elif target == 'p' and dist == 'b' and allowedPIncongruence > 0:
            allowedPIncongruence = allowedPIncongruence -1; 
            thisExp.addData('Condition', 'Incongruent')
            return target, dist, allowedPCongruence, allowedPIncongruence, allowedPNeutral, allowedBCongruence, allowedBIncongruence, allowedBNeutral;   
        elif target == 'p' and dist == 'g' and allowedPNeutral > 0:
            allowedPNeutral = allowedPNeutral -1; 
            thisExp.addData('Condition', 'Neutral')
            return target, dist, allowedPCongruence, allowedPIncongruence, allowedPNeutral, allowedBCongruence, allowedBIncongruence, allowedBNeutral;
        elif target == 'b' and dist == 'p' and allowedBIncongruence > 0:
            allowedBIncongruence = allowedBIncongruence -1; 
            thisExp.addData('Condition', 'Incongruent')
            return target, dist, allowedPCongruence, allowedPIncongruence, allowedPNeutral, allowedBCongruence, allowedBIncongruence, allowedBNeutral;
        elif target == 'b' and dist == 'b' and allowedBCongruence > 0:
            allowedBCongruence = allowedBCongruence -1; 
            thisExp.addData('Condition', 'Congruent')
            return target, dist, allowedPCongruence, allowedPIncongruence, allowedPNeutral, allowedBCongruence, allowedBIncongruence, allowedBNeutral;   
        elif target == 'b' and dist == 'g' and allowedBNeutral > 0:
            allowedBNeutral = allowedBNeutral -1; 
            thisExp.addData('Condition', 'Neutral')
            return target, dist, allowedPCongruence, allowedPIncongruence, allowedPNeutral, allowedBCongruence, allowedBIncongruence, allowedBNeutral;
        else: 
           return FindDistractor(np.random.choice(targets), allowedPCongruence, allowedPIncongruence, allowedPNeutral, allowedBCongruence, allowedBIncongruence, allowedBNeutral);
       
    # setup variables to control the experiment
    targets = ['p','b'];
    distractors = ['p','b','g'];
    fillers = ['h','l','y'];
    fillerposes = ['upLeft', 'lowLeft', 'upRight', 'lowRight'];
    targetpos = (1,1);
    
    # Setup scene
    # Find the target position 
    targetposName = np.random.choice(fillerposes)
    if targetposName == 'upLeft':
        targetpos = filler_up_left_pos;
    elif targetposName == 'lowLeft':
        targetpos = filler_low_left_pos;
    elif targetposName == 'upRight':
        targetpos = filler_up_right_pos;
    elif targetposName == 'lowRight':
        targetpos = filler_low_right_pos;       
    fillerposes.remove(targetposName);
    # find which will be the target and which will be the distractor
    targetAndDistractor = FindTargetAndDistractor(allowedPCongruence, allowedPIncongruence, allowedPNeutral, allowedBCongruence, allowedBIncongruence, allowedBNeutral)
    
    target = targetAndDistractor[0];
    distractor = targetAndDistractor[1];
    
    allowedPCongruence = targetAndDistractor[2]
    allowedPIncongruence = targetAndDistractor[3]
    allowedPNeutral = targetAndDistractor[4]
    allowedBCongruence = targetAndDistractor[5]
    allowedBIncongruence = targetAndDistractor[6]
    allowedBNeutral = targetAndDistractor[7]
    
    targetletter = target; 
    
    if target == 'p':
        p_targetpos = targetpos
    elif target == 'b':
        b_targetpos = targetpos
    
    if distractor == 'p':
        p_distractorpos = distractorPos
    elif distractor == 'b':
        b_distractorpos = distractorPos
    elif distractor == 'g':
        g_distractorpos = distractorPos
    # Randomly place the fillers 
    
    np.random.shuffle(fillerposes);
    np.random.shuffle(fillers);
    index = (0,1,2)
    
    for i in index:
            if fillerposes[i] == 'upLeft' and fillers[i] == 'h':
                h_fillerpos = filler_up_left_pos;
            if fillerposes[i] == 'upLeft' and fillers[i] == 'l':
                l_fillerpos = filler_up_left_pos;
            if fillerposes[i] == 'upLeft' and fillers[i] == 'y':
                y_fillerpos = filler_up_left_pos;
                
            if fillerposes[i] == 'lowLeft' and fillers[i] == 'h':
                h_fillerpos = filler_low_left_pos;
            if fillerposes[i] == 'lowLeft' and fillers[i] == 'l':
                l_fillerpos = filler_low_left_pos;
            if fillerposes[i] == 'lowLeft' and fillers[i] == 'y':
                y_fillerpos = filler_low_left_pos;
                
            if fillerposes[i] == 'lowRight' and fillers[i] == 'h':
                h_fillerpos = filler_low_right_pos;
            if fillerposes[i] == 'lowRight' and fillers[i] == 'l':
                l_fillerpos = filler_low_right_pos;
            if fillerposes[i] == 'lowRight' and fillers[i] == 'y':
                y_fillerpos = filler_low_right_pos;
                
            if fillerposes[i] == 'upRight' and fillers[i] == 'h':
                h_fillerpos = filler_up_right_pos;
            if fillerposes[i] == 'upRight' and fillers[i] == 'l':
                l_fillerpos = filler_up_right_pos;
            if fillerposes[i] == 'upRight' and fillers[i] == 'y':
                y_fillerpos = filler_up_right_pos;
        
    
    p_Target_2.setPos(p_targetpos)
    p_Target_2.setText('p')
    p_Target_2.setFont('Open Sans ExtraBold')
    b_Target_2.setPos(b_targetpos)
    b_Target_2.setFont('Open Sans ExtraBold')
    p_Distractor_2.setPos(p_distractorpos)
    b_Distractor_2.setPos(b_distractorpos)
    g_Distractor_2.setPos(g_distractorpos)
    h_Filler_2.setPos(h_fillerpos)
    l_Filler_2.setPos(l_fillerpos)
    y_filler_2.setPos(y_fillerpos)
    enableHappyface = False;
    enableSadface = False;
    enableFaster = False;
    
    if targetletter == 'p':
        isItP = True;
        isItB = False; 
        
    if targetletter == 'b':
        isItB = True;
        isItP = False; 
    # setup some python lists for storing info about the mouse_2
    mouse_2.x = []
    mouse_2.y = []
    mouse_2.leftButton = []
    mouse_2.midButton = []
    mouse_2.rightButton = []
    mouse_2.time = []
    gotValidClick = False  # until a click is received
    mouse_2.mouseClock.reset()
    # keep track of which components have finished
    VisualDistractorStimuliComponents = [p_Target_2, b_Target_2, p_Distractor_2, b_Distractor_2, g_Distractor_2, h_Filler_2, l_Filler_2, y_filler_2, mouse_2, whiteimage_2]
    for thisComponent in VisualDistractorStimuliComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    VisualDistractorStimuliClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "VisualDistractorStimuli"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = VisualDistractorStimuliClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=VisualDistractorStimuliClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *p_Target_2* updates
        if p_Target_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            p_Target_2.frameNStart = frameN  # exact frame index
            p_Target_2.tStart = t  # local t and not account for scr refresh
            p_Target_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_Target_2, 'tStartRefresh')  # time at next scr refresh
            p_Target_2.setAutoDraw(True)
        if p_Target_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > p_Target_2.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                p_Target_2.tStop = t  # not accounting for scr refresh
                p_Target_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(p_Target_2, 'tStopRefresh')  # time at next scr refresh
                p_Target_2.setAutoDraw(False)
        
        # *b_Target_2* updates
        if b_Target_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            b_Target_2.frameNStart = frameN  # exact frame index
            b_Target_2.tStart = t  # local t and not account for scr refresh
            b_Target_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(b_Target_2, 'tStartRefresh')  # time at next scr refresh
            b_Target_2.setAutoDraw(True)
        if b_Target_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > b_Target_2.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                b_Target_2.tStop = t  # not accounting for scr refresh
                b_Target_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(b_Target_2, 'tStopRefresh')  # time at next scr refresh
                b_Target_2.setAutoDraw(False)
        
        # *p_Distractor_2* updates
        if p_Distractor_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            p_Distractor_2.frameNStart = frameN  # exact frame index
            p_Distractor_2.tStart = t  # local t and not account for scr refresh
            p_Distractor_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_Distractor_2, 'tStartRefresh')  # time at next scr refresh
            p_Distractor_2.setAutoDraw(True)
        if p_Distractor_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > p_Distractor_2.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                p_Distractor_2.tStop = t  # not accounting for scr refresh
                p_Distractor_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(p_Distractor_2, 'tStopRefresh')  # time at next scr refresh
                p_Distractor_2.setAutoDraw(False)
        
        # *b_Distractor_2* updates
        if b_Distractor_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            b_Distractor_2.frameNStart = frameN  # exact frame index
            b_Distractor_2.tStart = t  # local t and not account for scr refresh
            b_Distractor_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(b_Distractor_2, 'tStartRefresh')  # time at next scr refresh
            b_Distractor_2.setAutoDraw(True)
        if b_Distractor_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > b_Distractor_2.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                b_Distractor_2.tStop = t  # not accounting for scr refresh
                b_Distractor_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(b_Distractor_2, 'tStopRefresh')  # time at next scr refresh
                b_Distractor_2.setAutoDraw(False)
        
        # *g_Distractor_2* updates
        if g_Distractor_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            g_Distractor_2.frameNStart = frameN  # exact frame index
            g_Distractor_2.tStart = t  # local t and not account for scr refresh
            g_Distractor_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(g_Distractor_2, 'tStartRefresh')  # time at next scr refresh
            g_Distractor_2.setAutoDraw(True)
        if g_Distractor_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > g_Distractor_2.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                g_Distractor_2.tStop = t  # not accounting for scr refresh
                g_Distractor_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(g_Distractor_2, 'tStopRefresh')  # time at next scr refresh
                g_Distractor_2.setAutoDraw(False)
        
        # *h_Filler_2* updates
        if h_Filler_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            h_Filler_2.frameNStart = frameN  # exact frame index
            h_Filler_2.tStart = t  # local t and not account for scr refresh
            h_Filler_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(h_Filler_2, 'tStartRefresh')  # time at next scr refresh
            h_Filler_2.setAutoDraw(True)
        if h_Filler_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > h_Filler_2.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                h_Filler_2.tStop = t  # not accounting for scr refresh
                h_Filler_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(h_Filler_2, 'tStopRefresh')  # time at next scr refresh
                h_Filler_2.setAutoDraw(False)
        
        # *l_Filler_2* updates
        if l_Filler_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            l_Filler_2.frameNStart = frameN  # exact frame index
            l_Filler_2.tStart = t  # local t and not account for scr refresh
            l_Filler_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l_Filler_2, 'tStartRefresh')  # time at next scr refresh
            l_Filler_2.setAutoDraw(True)
        if l_Filler_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l_Filler_2.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                l_Filler_2.tStop = t  # not accounting for scr refresh
                l_Filler_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(l_Filler_2, 'tStopRefresh')  # time at next scr refresh
                l_Filler_2.setAutoDraw(False)
        
        # *y_filler_2* updates
        if y_filler_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            y_filler_2.frameNStart = frameN  # exact frame index
            y_filler_2.tStart = t  # local t and not account for scr refresh
            y_filler_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(y_filler_2, 'tStartRefresh')  # time at next scr refresh
            y_filler_2.setAutoDraw(True)
        if y_filler_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > y_filler_2.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                y_filler_2.tStop = t  # not accounting for scr refresh
                y_filler_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(y_filler_2, 'tStopRefresh')  # time at next scr refresh
                y_filler_2.setAutoDraw(False)
        #button[0] = left click = P 
        #button[2] = right click = B
        
        buttons = mouse.getPressed()
        
        if isItP and buttons[0] == 1:
            enableHappyface = True;
            enableSadface = False;
            enableFaster = False; 
        elif isItB and buttons[2] == 1:
            enableHappyface = True;
            enableSadface = False;
            enableFaster = False;
        elif isItP and buttons[2] == 1:
            enableHappyface = False;
            enableSadface = True;
            enableFaster = False;  
        elif isItB and buttons[0] == 1:
            enableHappyface = False;
            enableSadface = True;
            enableFaster = False; 
        # *mouse_2* updates
        if mouse_2.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            mouse_2.frameNStart = frameN  # exact frame index
            mouse_2.tStart = t  # local t and not account for scr refresh
            mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
            mouse_2.status = STARTED
            prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
        if mouse_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_2.tStartRefresh + 0.7-frameTolerance:
                # keep track of stop time/frame for later
                mouse_2.tStop = t  # not accounting for scr refresh
                mouse_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mouse_2, 'tStopRefresh')  # time at next scr refresh
                mouse_2.status = FINISHED
        if mouse_2.status == STARTED:  # only update if started and not finished!
            buttons = mouse_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = mouse_2.getPos()
                    mouse_2.x.append(x)
                    mouse_2.y.append(y)
                    buttons = mouse_2.getPressed()
                    mouse_2.leftButton.append(buttons[0])
                    mouse_2.midButton.append(buttons[1])
                    mouse_2.rightButton.append(buttons[2])
                    mouse_2.time.append(mouse_2.mouseClock.getTime())
                    
                    continueRoutine = False  # abort routine on response
        
        # *whiteimage_2* updates
        if whiteimage_2.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            whiteimage_2.frameNStart = frameN  # exact frame index
            whiteimage_2.tStart = t  # local t and not account for scr refresh
            whiteimage_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(whiteimage_2, 'tStartRefresh')  # time at next scr refresh
            whiteimage_2.setAutoDraw(True)
        if whiteimage_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > whiteimage_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                whiteimage_2.tStop = t  # not accounting for scr refresh
                whiteimage_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(whiteimage_2, 'tStopRefresh')  # time at next scr refresh
                whiteimage_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in VisualDistractorStimuliComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "VisualDistractorStimuli"-------
    for thisComponent in VisualDistractorStimuliComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    VisualDistractionTrials.addData('p_Target_2.started', p_Target_2.tStartRefresh)
    VisualDistractionTrials.addData('p_Target_2.stopped', p_Target_2.tStopRefresh)
    VisualDistractionTrials.addData('b_Target_2.started', b_Target_2.tStartRefresh)
    VisualDistractionTrials.addData('b_Target_2.stopped', b_Target_2.tStopRefresh)
    VisualDistractionTrials.addData('p_Distractor_2.started', p_Distractor_2.tStartRefresh)
    VisualDistractionTrials.addData('p_Distractor_2.stopped', p_Distractor_2.tStopRefresh)
    VisualDistractionTrials.addData('b_Distractor_2.started', b_Distractor_2.tStartRefresh)
    VisualDistractionTrials.addData('b_Distractor_2.stopped', b_Distractor_2.tStopRefresh)
    VisualDistractionTrials.addData('g_Distractor_2.started', g_Distractor_2.tStartRefresh)
    VisualDistractionTrials.addData('g_Distractor_2.stopped', g_Distractor_2.tStopRefresh)
    VisualDistractionTrials.addData('h_Filler_2.started', h_Filler_2.tStartRefresh)
    VisualDistractionTrials.addData('h_Filler_2.stopped', h_Filler_2.tStopRefresh)
    VisualDistractionTrials.addData('l_Filler_2.started', l_Filler_2.tStartRefresh)
    VisualDistractionTrials.addData('l_Filler_2.stopped', l_Filler_2.tStopRefresh)
    VisualDistractionTrials.addData('y_filler_2.started', y_filler_2.tStartRefresh)
    VisualDistractionTrials.addData('y_filler_2.stopped', y_filler_2.tStopRefresh)
    if enableHappyface == False and enableSadface == False:
        enableFaster = True; 
        
    if enableHappyface == True:   
        thisExp.addData('Response', 'Correct')
        thisExp.addData('Response_code', 1.0)
        
    if enableSadface == True:   
        thisExp.addData('Response', 'Incorrect')
        thisExp.addData('Response_code', 2.0)
        
    if enableFaster == True:   
        thisExp.addData('Response', 'None')
        thisExp.addData('Response_code', 0.0)
        
    
    
    # store data for VisualDistractionTrials (TrialHandler)
    VisualDistractionTrials.addData('mouse_2.x', mouse_2.x)
    VisualDistractionTrials.addData('mouse_2.y', mouse_2.y)
    VisualDistractionTrials.addData('mouse_2.leftButton', mouse_2.leftButton)
    VisualDistractionTrials.addData('mouse_2.midButton', mouse_2.midButton)
    VisualDistractionTrials.addData('mouse_2.rightButton', mouse_2.rightButton)
    VisualDistractionTrials.addData('mouse_2.time', mouse_2.time)
    VisualDistractionTrials.addData('mouse_2.started', mouse_2.tStart)
    VisualDistractionTrials.addData('mouse_2.stopped', mouse_2.tStop)
    VisualDistractionTrials.addData('whiteimage_2.started', whiteimage_2.tStartRefresh)
    VisualDistractionTrials.addData('whiteimage_2.stopped', whiteimage_2.tStopRefresh)
    
    # ------Prepare to start Routine "Feedback"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    #from the previous routine feedback will be provided.
    if enableHappyface:
        fasterOpacity = 0.0;
        sadOpacity = 0.0;
        happyOpacity = 1.0; 
        
    if enableSadface:
        fasterOpacity = 0.0;
        sadOpacity = 1.0;
        happyOpacity = 0.0; 
        
    if enableFaster:
        fasterOpacity = 1.0;
        sadOpacity = 0.0;
        happyOpacity = 0.0; 
    Faster.setOpacity(fasterOpacity)
    happy.setOpacity(happyOpacity)
    sad.setOpacity(sadOpacity)
    # keep track of which components have finished
    FeedbackComponents = [Faster, happy, sad]
    for thisComponent in FeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Faster* updates
        if Faster.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Faster.frameNStart = frameN  # exact frame index
            Faster.tStart = t  # local t and not account for scr refresh
            Faster.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Faster, 'tStartRefresh')  # time at next scr refresh
            Faster.setAutoDraw(True)
        if Faster.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Faster.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Faster.tStop = t  # not accounting for scr refresh
                Faster.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Faster, 'tStopRefresh')  # time at next scr refresh
                Faster.setAutoDraw(False)
        
        # *happy* updates
        if happy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            happy.frameNStart = frameN  # exact frame index
            happy.tStart = t  # local t and not account for scr refresh
            happy.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(happy, 'tStartRefresh')  # time at next scr refresh
            happy.setAutoDraw(True)
        if happy.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > happy.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                happy.tStop = t  # not accounting for scr refresh
                happy.frameNStop = frameN  # exact frame index
                win.timeOnFlip(happy, 'tStopRefresh')  # time at next scr refresh
                happy.setAutoDraw(False)
        
        # *sad* updates
        if sad.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sad.frameNStart = frameN  # exact frame index
            sad.tStart = t  # local t and not account for scr refresh
            sad.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sad, 'tStartRefresh')  # time at next scr refresh
            sad.setAutoDraw(True)
        if sad.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sad.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                sad.tStop = t  # not accounting for scr refresh
                sad.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sad, 'tStopRefresh')  # time at next scr refresh
                sad.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback"-------
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    VisualDistractionTrials.addData('Faster.started', Faster.tStartRefresh)
    VisualDistractionTrials.addData('Faster.stopped', Faster.tStopRefresh)
    VisualDistractionTrials.addData('happy.started', happy.tStartRefresh)
    VisualDistractionTrials.addData('happy.stopped', happy.tStopRefresh)
    VisualDistractionTrials.addData('sad.started', sad.tStartRefresh)
    VisualDistractionTrials.addData('sad.stopped', sad.tStopRefresh)
    thisExp.nextEntry()
    
# completed 12.0 repeats of 'VisualDistractionTrials'


# ------Prepare to start Routine "Pause"-------
continueRoutine = True
# update component parameters for each repeat
next_screen1_2.keys = []
next_screen1_2.rt = []
_next_screen1_2_allKeys = []
# keep track of which components have finished
PauseComponents = [Pause_Text, next_screen1_2]
for thisComponent in PauseComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Pause"-------
while continueRoutine:
    # get current time
    t = PauseClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PauseClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Pause_Text* updates
    if Pause_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Pause_Text.frameNStart = frameN  # exact frame index
        Pause_Text.tStart = t  # local t and not account for scr refresh
        Pause_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Pause_Text, 'tStartRefresh')  # time at next scr refresh
        Pause_Text.setAutoDraw(True)
    
    # *next_screen1_2* updates
    waitOnFlip = False
    if next_screen1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_screen1_2.frameNStart = frameN  # exact frame index
        next_screen1_2.tStart = t  # local t and not account for scr refresh
        next_screen1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_screen1_2, 'tStartRefresh')  # time at next scr refresh
        next_screen1_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_screen1_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_screen1_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_screen1_2.status == STARTED and not waitOnFlip:
        theseKeys = next_screen1_2.getKeys(keyList=None, waitRelease=False)
        _next_screen1_2_allKeys.extend(theseKeys)
        if len(_next_screen1_2_allKeys):
            next_screen1_2.keys = _next_screen1_2_allKeys[-1].name  # just the last key pressed
            next_screen1_2.rt = _next_screen1_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PauseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Pause"-------
for thisComponent in PauseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Pause_Text.started', Pause_Text.tStartRefresh)
thisExp.addData('Pause_Text.stopped', Pause_Text.tStopRefresh)
# check responses
if next_screen1_2.keys in ['', [], None]:  # No response was made
    next_screen1_2.keys = None
thisExp.addData('next_screen1_2.keys',next_screen1_2.keys)
if next_screen1_2.keys != None:  # we had a response
    thisExp.addData('next_screen1_2.rt', next_screen1_2.rt)
thisExp.addData('next_screen1_2.started', next_screen1_2.tStartRefresh)
thisExp.addData('next_screen1_2.stopped', next_screen1_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "Pause" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
VisualAndAudioDistractor = data.TrialHandler(nReps=12.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='VisualAndAudioDistractor')
thisExp.addLoop(VisualAndAudioDistractor)  # add the loop to the experiment
thisVisualAndAudioDistractor = VisualAndAudioDistractor.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisVisualAndAudioDistractor.rgb)
if thisVisualAndAudioDistractor != None:
    for paramName in thisVisualAndAudioDistractor:
        exec('{} = thisVisualAndAudioDistractor[paramName]'.format(paramName))

for thisVisualAndAudioDistractor in VisualAndAudioDistractor:
    currentLoop = VisualAndAudioDistractor
    # abbreviate parameter names if possible (e.g. rgb = thisVisualAndAudioDistractor.rgb)
    if thisVisualAndAudioDistractor != None:
        for paramName in thisVisualAndAudioDistractor:
            exec('{} = thisVisualAndAudioDistractor[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "FixationCross"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    FixationCrossComponents = [FixationCrossText]
    for thisComponent in FixationCrossComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FixationCrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "FixationCross"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FixationCrossClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FixationCrossClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FixationCrossText* updates
        if FixationCrossText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FixationCrossText.frameNStart = frameN  # exact frame index
            FixationCrossText.tStart = t  # local t and not account for scr refresh
            FixationCrossText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FixationCrossText, 'tStartRefresh')  # time at next scr refresh
            FixationCrossText.setAutoDraw(True)
        if FixationCrossText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FixationCrossText.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                FixationCrossText.tStop = t  # not accounting for scr refresh
                FixationCrossText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FixationCrossText, 'tStopRefresh')  # time at next scr refresh
                FixationCrossText.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FixationCrossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FixationCross"-------
    for thisComponent in FixationCrossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    VisualAndAudioDistractor.addData('FixationCrossText.started', FixationCrossText.tStartRefresh)
    VisualAndAudioDistractor.addData('FixationCrossText.stopped', FixationCrossText.tStopRefresh)
    
    # ------Prepare to start Routine "AudioVisualDistractorStimuli"-------
    continueRoutine = True
    routineTimer.add(0.700000)
    # update component parameters for each repeat
    p_targetpos = (1,1)
    b_targetpos = (1,1)
    p_distractorpos = (1,1)
    b_distractorpos = (1,1)
    g_distractorpos = (1,1)
    h_fillerpos = (1,1)
    l_fillerpos = (1,1)
    y_fillerpos = (1,1)
    p_dis_volume = 0.0
    b_dis_volume = 0.0
    g_dis_volume = 0.0
    
    def FindTargetAndDistractor(allowedPCongruence, allowedPIncongruence, allowedPNeutral, allowedBCongruence, allowedBIncongruence, allowedBNeutral):
        tar = np.random.choice(targets);
        tarAndDist = FindDistractor(tar, allowedPCongruence, allowedPIncongruence, allowedPNeutral, allowedBCongruence, allowedBIncongruence, allowedBNeutral);
        return tarAndDist; 
        
    def FindDistractor(target, allowedPCongruence, allowedPIncongruence, allowedPNeutral, allowedBCongruence, allowedBIncongruence, allowedBNeutral):
        
        dist = np.random.choice(distractors);
        if target == 'p' and dist == 'p' and allowedPCongruence > 0:
            allowedPCongruence = allowedPCongruence -1; 
            thisExp.addData('Condition', 'Congruent')
            return target, dist, allowedPCongruence, allowedPIncongruence, allowedPNeutral, allowedBCongruence, allowedBIncongruence, allowedBNeutral;
        elif target == 'p' and dist == 'b' and allowedPIncongruence > 0:
            allowedPIncongruence = allowedPIncongruence -1; 
            thisExp.addData('Condition', 'Incongruent')
            return target, dist, allowedPCongruence, allowedPIncongruence, allowedPNeutral, allowedBCongruence, allowedBIncongruence, allowedBNeutral;   
        elif target == 'p' and dist == 'g' and allowedPNeutral > 0:
            allowedPNeutral = allowedPNeutral -1; 
            thisExp.addData('Condition', 'Neutral')
            return target, dist, allowedPCongruence, allowedPIncongruence, allowedPNeutral, allowedBCongruence, allowedBIncongruence, allowedBNeutral;
        elif target == 'b' and dist == 'p' and allowedBIncongruence > 0:
            allowedBIncongruence = allowedBIncongruence -1; 
            thisExp.addData('Condition', 'Incongruent')
            return target, dist, allowedPCongruence, allowedPIncongruence, allowedPNeutral, allowedBCongruence, allowedBIncongruence, allowedBNeutral;
        elif target == 'b' and dist == 'b' and allowedBCongruence > 0:
            allowedBCongruence = allowedBCongruence -1; 
            thisExp.addData('Condition', 'Congruent')
            return target, dist, allowedPCongruence, allowedPIncongruenceA, allowedPNeutral, allowedBCongruence, allowedBIncongruence, allowedBNeutral;   
        elif target == 'b' and dist == 'g' and allowedBNeutral > 0:
            allowedBNeutral = allowedBNeutral -1; 
            thisExp.addData('Condition', 'Neutral')
            return target, dist, allowedPCongruence, allowedPIncongruence, allowedPNeutral, allowedBCongruence, allowedBIncongruence, allowedBNeutral;
        else: 
           return FindDistractor(np.random.choice(targets), allowedPCongruence, allowedPIncongruence, allowedPNeutral, allowedBCongruence, allowedBIncongruence, allowedBNeutral);
       
    # setup variables to control the experiment
    targets = ['p','b'];
    distractors = ['p','b','g'];
    fillers = ['h','l','y'];
    fillerposes = ['upLeft', 'lowLeft', 'upRight', 'lowRight'];
    targetpos = (1,1);
    
    # Setup scene
    # Find the target position 
    targetposName = np.random.choice(fillerposes)
    if targetposName == 'upLeft':
        targetpos = filler_up_left_pos;
    elif targetposName == 'lowLeft':
        targetpos = filler_low_left_pos;
    elif targetposName == 'upRight':
        targetpos = filler_up_right_pos;
    elif targetposName == 'lowRight':
        targetpos = filler_low_right_pos;       
    fillerposes.remove(targetposName);
    # find which will be the target and which will be the distractor
    targetAndDistractor = FindTargetAndDistractor(allowedPCongruenceAV, allowedPIncongruenceAV, allowedPNeutralAV, allowedBCongruenceAV, allowedBIncongruenceAV, allowedBNeutralAV)
    
    target = targetAndDistractor[0];
    distractor = targetAndDistractor[1];
    
    allowedPCongruenceAV = targetAndDistractor[2]
    allowedPIncongruenceAV = targetAndDistractor[3]
    allowedPNeutralAV = targetAndDistractor[4]
    allowedBCongruenceAV = targetAndDistractor[5]
    allowedBIncongruenceAV = targetAndDistractor[6]
    allowedBNeutralAV = targetAndDistractor[7]
    
    targetletter = target; 
    
    if target == 'p':
        p_targetpos = targetpos
    elif target == 'b':
        b_targetpos = targetpos
    
    if distractor == 'p':
        p_distractorpos = distractorPos
        p_dis_volume = 1.0
    elif distractor == 'b':
        b_distractorpos = distractorPos
        b_dis_volume = 1.0
    elif distractor == 'g':
        g_distractorpos = distractorPos
        g_dis_volume = 1.0
    # Randomly place the fillers 
    
    np.random.shuffle(fillerposes);
    np.random.shuffle(fillers);
    index = (0,1,2)
    
    for i in index:
            if fillerposes[i] == 'upLeft' and fillers[i] == 'h':
                h_fillerpos = filler_up_left_pos;
            if fillerposes[i] == 'upLeft' and fillers[i] == 'l':
                l_fillerpos = filler_up_left_pos;
            if fillerposes[i] == 'upLeft' and fillers[i] == 'y':
                y_fillerpos = filler_up_left_pos;
                
            if fillerposes[i] == 'lowLeft' and fillers[i] == 'h':
                h_fillerpos = filler_low_left_pos;
            if fillerposes[i] == 'lowLeft' and fillers[i] == 'l':
                l_fillerpos = filler_low_left_pos;
            if fillerposes[i] == 'lowLeft' and fillers[i] == 'y':
                y_fillerpos = filler_low_left_pos;
                
            if fillerposes[i] == 'lowRight' and fillers[i] == 'h':
                h_fillerpos = filler_low_right_pos;
            if fillerposes[i] == 'lowRight' and fillers[i] == 'l':
                l_fillerpos = filler_low_right_pos;
            if fillerposes[i] == 'lowRight' and fillers[i] == 'y':
                y_fillerpos = filler_low_right_pos;
                
            if fillerposes[i] == 'upRight' and fillers[i] == 'h':
                h_fillerpos = filler_up_right_pos;
            if fillerposes[i] == 'upRight' and fillers[i] == 'l':
                l_fillerpos = filler_up_right_pos;
            if fillerposes[i] == 'upRight' and fillers[i] == 'y':
                y_fillerpos = filler_up_right_pos;
        
    
    p_Target.setPos(p_targetpos)
    p_Target.setText('p')
    p_Target.setFont('Open Sans ExtraBold')
    b_Target.setPos(b_targetpos)
    b_Target.setFont('Open Sans ExtraBold')
    p_Distractor.setPos(p_distractorpos)
    b_Distractor.setPos(b_distractorpos)
    g_Distractor.setPos(g_distractorpos)
    h_Filler.setPos(h_fillerpos)
    l_Filler.setPos(l_fillerpos)
    y_filler.setPos(y_fillerpos)
    p_Dis_Sound.setSound('audio/p.wav', secs=0.2, hamming=False)
    p_Dis_Sound.setVolume(p_dis_volume, log=False)
    b_Dis_Sound.setSound('audio/b.wav', secs=0.2, hamming=False)
    b_Dis_Sound.setVolume(b_dis_volume, log=False)
    g_Dis_Sound.setSound('audio/g.wav', secs=0.2, hamming=False)
    g_Dis_Sound.setVolume(g_dis_volume, log=False)
    enableHappyface = False;
    enableSadface = False;
    enableFaster = False;
    
    if targetletter == 'p':
        isItP = True;
        isItB = False; 
        
    if targetletter == 'b':
        isItB = True;
        isItP = False; 
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    gotValidClick = False  # until a click is received
    mouse.mouseClock.reset()
    # keep track of which components have finished
    AudioVisualDistractorStimuliComponents = [p_Target, b_Target, p_Distractor, b_Distractor, g_Distractor, h_Filler, l_Filler, y_filler, p_Dis_Sound, b_Dis_Sound, g_Dis_Sound, mouse, whiteimage]
    for thisComponent in AudioVisualDistractorStimuliComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    AudioVisualDistractorStimuliClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "AudioVisualDistractorStimuli"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AudioVisualDistractorStimuliClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AudioVisualDistractorStimuliClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *p_Target* updates
        if p_Target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            p_Target.frameNStart = frameN  # exact frame index
            p_Target.tStart = t  # local t and not account for scr refresh
            p_Target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_Target, 'tStartRefresh')  # time at next scr refresh
            p_Target.setAutoDraw(True)
        if p_Target.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > p_Target.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                p_Target.tStop = t  # not accounting for scr refresh
                p_Target.frameNStop = frameN  # exact frame index
                win.timeOnFlip(p_Target, 'tStopRefresh')  # time at next scr refresh
                p_Target.setAutoDraw(False)
        
        # *b_Target* updates
        if b_Target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            b_Target.frameNStart = frameN  # exact frame index
            b_Target.tStart = t  # local t and not account for scr refresh
            b_Target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(b_Target, 'tStartRefresh')  # time at next scr refresh
            b_Target.setAutoDraw(True)
        if b_Target.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > b_Target.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                b_Target.tStop = t  # not accounting for scr refresh
                b_Target.frameNStop = frameN  # exact frame index
                win.timeOnFlip(b_Target, 'tStopRefresh')  # time at next scr refresh
                b_Target.setAutoDraw(False)
        
        # *p_Distractor* updates
        if p_Distractor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            p_Distractor.frameNStart = frameN  # exact frame index
            p_Distractor.tStart = t  # local t and not account for scr refresh
            p_Distractor.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_Distractor, 'tStartRefresh')  # time at next scr refresh
            p_Distractor.setAutoDraw(True)
        if p_Distractor.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > p_Distractor.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                p_Distractor.tStop = t  # not accounting for scr refresh
                p_Distractor.frameNStop = frameN  # exact frame index
                win.timeOnFlip(p_Distractor, 'tStopRefresh')  # time at next scr refresh
                p_Distractor.setAutoDraw(False)
        
        # *b_Distractor* updates
        if b_Distractor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            b_Distractor.frameNStart = frameN  # exact frame index
            b_Distractor.tStart = t  # local t and not account for scr refresh
            b_Distractor.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(b_Distractor, 'tStartRefresh')  # time at next scr refresh
            b_Distractor.setAutoDraw(True)
        if b_Distractor.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > b_Distractor.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                b_Distractor.tStop = t  # not accounting for scr refresh
                b_Distractor.frameNStop = frameN  # exact frame index
                win.timeOnFlip(b_Distractor, 'tStopRefresh')  # time at next scr refresh
                b_Distractor.setAutoDraw(False)
        
        # *g_Distractor* updates
        if g_Distractor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            g_Distractor.frameNStart = frameN  # exact frame index
            g_Distractor.tStart = t  # local t and not account for scr refresh
            g_Distractor.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(g_Distractor, 'tStartRefresh')  # time at next scr refresh
            g_Distractor.setAutoDraw(True)
        if g_Distractor.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > g_Distractor.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                g_Distractor.tStop = t  # not accounting for scr refresh
                g_Distractor.frameNStop = frameN  # exact frame index
                win.timeOnFlip(g_Distractor, 'tStopRefresh')  # time at next scr refresh
                g_Distractor.setAutoDraw(False)
        
        # *h_Filler* updates
        if h_Filler.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            h_Filler.frameNStart = frameN  # exact frame index
            h_Filler.tStart = t  # local t and not account for scr refresh
            h_Filler.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(h_Filler, 'tStartRefresh')  # time at next scr refresh
            h_Filler.setAutoDraw(True)
        if h_Filler.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > h_Filler.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                h_Filler.tStop = t  # not accounting for scr refresh
                h_Filler.frameNStop = frameN  # exact frame index
                win.timeOnFlip(h_Filler, 'tStopRefresh')  # time at next scr refresh
                h_Filler.setAutoDraw(False)
        
        # *l_Filler* updates
        if l_Filler.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            l_Filler.frameNStart = frameN  # exact frame index
            l_Filler.tStart = t  # local t and not account for scr refresh
            l_Filler.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l_Filler, 'tStartRefresh')  # time at next scr refresh
            l_Filler.setAutoDraw(True)
        if l_Filler.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l_Filler.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                l_Filler.tStop = t  # not accounting for scr refresh
                l_Filler.frameNStop = frameN  # exact frame index
                win.timeOnFlip(l_Filler, 'tStopRefresh')  # time at next scr refresh
                l_Filler.setAutoDraw(False)
        
        # *y_filler* updates
        if y_filler.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            y_filler.frameNStart = frameN  # exact frame index
            y_filler.tStart = t  # local t and not account for scr refresh
            y_filler.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(y_filler, 'tStartRefresh')  # time at next scr refresh
            y_filler.setAutoDraw(True)
        if y_filler.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > y_filler.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                y_filler.tStop = t  # not accounting for scr refresh
                y_filler.frameNStop = frameN  # exact frame index
                win.timeOnFlip(y_filler, 'tStopRefresh')  # time at next scr refresh
                y_filler.setAutoDraw(False)
        # start/stop p_Dis_Sound
        if p_Dis_Sound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            p_Dis_Sound.frameNStart = frameN  # exact frame index
            p_Dis_Sound.tStart = t  # local t and not account for scr refresh
            p_Dis_Sound.tStartRefresh = tThisFlipGlobal  # on global time
            p_Dis_Sound.play(when=win)  # sync with win flip
        if p_Dis_Sound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > p_Dis_Sound.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                p_Dis_Sound.tStop = t  # not accounting for scr refresh
                p_Dis_Sound.frameNStop = frameN  # exact frame index
                win.timeOnFlip(p_Dis_Sound, 'tStopRefresh')  # time at next scr refresh
                p_Dis_Sound.stop()
        # start/stop b_Dis_Sound
        if b_Dis_Sound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            b_Dis_Sound.frameNStart = frameN  # exact frame index
            b_Dis_Sound.tStart = t  # local t and not account for scr refresh
            b_Dis_Sound.tStartRefresh = tThisFlipGlobal  # on global time
            b_Dis_Sound.play(when=win)  # sync with win flip
        if b_Dis_Sound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > b_Dis_Sound.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                b_Dis_Sound.tStop = t  # not accounting for scr refresh
                b_Dis_Sound.frameNStop = frameN  # exact frame index
                win.timeOnFlip(b_Dis_Sound, 'tStopRefresh')  # time at next scr refresh
                b_Dis_Sound.stop()
        # start/stop g_Dis_Sound
        if g_Dis_Sound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            g_Dis_Sound.frameNStart = frameN  # exact frame index
            g_Dis_Sound.tStart = t  # local t and not account for scr refresh
            g_Dis_Sound.tStartRefresh = tThisFlipGlobal  # on global time
            g_Dis_Sound.play(when=win)  # sync with win flip
        if g_Dis_Sound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > g_Dis_Sound.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                g_Dis_Sound.tStop = t  # not accounting for scr refresh
                g_Dis_Sound.frameNStop = frameN  # exact frame index
                win.timeOnFlip(g_Dis_Sound, 'tStopRefresh')  # time at next scr refresh
                g_Dis_Sound.stop()
        #button[0] = left click = P 
        #button[2] = right click = B
        
        buttons = mouse.getPressed()
        
        if isItP and buttons[0] == 1:
            enableHappyface = True;
            enableSadface = False;
            enableFaster = False; 
        elif isItB and buttons[2] == 1:
            enableHappyface = True;
            enableSadface = False;
            enableFaster = False;
        elif isItP and buttons[2] == 1:
            enableHappyface = False;
            enableSadface = True;
            enableFaster = False;  
        elif isItB and buttons[0] == 1:
            enableHappyface = False;
            enableSadface = True;
            enableFaster = False; 
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse.tStartRefresh + 0.7-frameTolerance:
                # keep track of stop time/frame for later
                mouse.tStop = t  # not accounting for scr refresh
                mouse.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mouse, 'tStopRefresh')  # time at next scr refresh
                mouse.status = FINISHED
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
                    
                    continueRoutine = False  # abort routine on response
        
        # *whiteimage* updates
        if whiteimage.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            whiteimage.frameNStart = frameN  # exact frame index
            whiteimage.tStart = t  # local t and not account for scr refresh
            whiteimage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(whiteimage, 'tStartRefresh')  # time at next scr refresh
            whiteimage.setAutoDraw(True)
        if whiteimage.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > whiteimage.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                whiteimage.tStop = t  # not accounting for scr refresh
                whiteimage.frameNStop = frameN  # exact frame index
                win.timeOnFlip(whiteimage, 'tStopRefresh')  # time at next scr refresh
                whiteimage.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AudioVisualDistractorStimuliComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AudioVisualDistractorStimuli"-------
    for thisComponent in AudioVisualDistractorStimuliComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    VisualAndAudioDistractor.addData('p_Target.started', p_Target.tStartRefresh)
    VisualAndAudioDistractor.addData('p_Target.stopped', p_Target.tStopRefresh)
    VisualAndAudioDistractor.addData('b_Target.started', b_Target.tStartRefresh)
    VisualAndAudioDistractor.addData('b_Target.stopped', b_Target.tStopRefresh)
    VisualAndAudioDistractor.addData('p_Distractor.started', p_Distractor.tStartRefresh)
    VisualAndAudioDistractor.addData('p_Distractor.stopped', p_Distractor.tStopRefresh)
    VisualAndAudioDistractor.addData('b_Distractor.started', b_Distractor.tStartRefresh)
    VisualAndAudioDistractor.addData('b_Distractor.stopped', b_Distractor.tStopRefresh)
    VisualAndAudioDistractor.addData('g_Distractor.started', g_Distractor.tStartRefresh)
    VisualAndAudioDistractor.addData('g_Distractor.stopped', g_Distractor.tStopRefresh)
    VisualAndAudioDistractor.addData('h_Filler.started', h_Filler.tStartRefresh)
    VisualAndAudioDistractor.addData('h_Filler.stopped', h_Filler.tStopRefresh)
    VisualAndAudioDistractor.addData('l_Filler.started', l_Filler.tStartRefresh)
    VisualAndAudioDistractor.addData('l_Filler.stopped', l_Filler.tStopRefresh)
    VisualAndAudioDistractor.addData('y_filler.started', y_filler.tStartRefresh)
    VisualAndAudioDistractor.addData('y_filler.stopped', y_filler.tStopRefresh)
    p_Dis_Sound.stop()  # ensure sound has stopped at end of routine
    VisualAndAudioDistractor.addData('p_Dis_Sound.started', p_Dis_Sound.tStartRefresh)
    VisualAndAudioDistractor.addData('p_Dis_Sound.stopped', p_Dis_Sound.tStopRefresh)
    b_Dis_Sound.stop()  # ensure sound has stopped at end of routine
    VisualAndAudioDistractor.addData('b_Dis_Sound.started', b_Dis_Sound.tStartRefresh)
    VisualAndAudioDistractor.addData('b_Dis_Sound.stopped', b_Dis_Sound.tStopRefresh)
    g_Dis_Sound.stop()  # ensure sound has stopped at end of routine
    VisualAndAudioDistractor.addData('g_Dis_Sound.started', g_Dis_Sound.tStartRefresh)
    VisualAndAudioDistractor.addData('g_Dis_Sound.stopped', g_Dis_Sound.tStopRefresh)
    if enableHappyface == False and enableSadface == False:
        enableFaster = True; 
        
    if enableHappyface == True:   
        thisExp.addData('Response', 'Correct')
        thisExp.addData('Response_code', 1.0)
        
    if enableSadface == True:   
        thisExp.addData('Response', 'Incorrect')
        thisExp.addData('Response_code', 2.0)
        
    if enableFaster == True:   
        thisExp.addData('Response', 'None')
        thisExp.addData('Response_code', 0.0)
        
    
    
    # store data for VisualAndAudioDistractor (TrialHandler)
    VisualAndAudioDistractor.addData('mouse.x', mouse.x)
    VisualAndAudioDistractor.addData('mouse.y', mouse.y)
    VisualAndAudioDistractor.addData('mouse.leftButton', mouse.leftButton)
    VisualAndAudioDistractor.addData('mouse.midButton', mouse.midButton)
    VisualAndAudioDistractor.addData('mouse.rightButton', mouse.rightButton)
    VisualAndAudioDistractor.addData('mouse.time', mouse.time)
    VisualAndAudioDistractor.addData('mouse.started', mouse.tStart)
    VisualAndAudioDistractor.addData('mouse.stopped', mouse.tStop)
    VisualAndAudioDistractor.addData('whiteimage.started', whiteimage.tStartRefresh)
    VisualAndAudioDistractor.addData('whiteimage.stopped', whiteimage.tStopRefresh)
    
    # ------Prepare to start Routine "Feedback"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    #from the previous routine feedback will be provided.
    if enableHappyface:
        fasterOpacity = 0.0;
        sadOpacity = 0.0;
        happyOpacity = 1.0; 
        
    if enableSadface:
        fasterOpacity = 0.0;
        sadOpacity = 1.0;
        happyOpacity = 0.0; 
        
    if enableFaster:
        fasterOpacity = 1.0;
        sadOpacity = 0.0;
        happyOpacity = 0.0; 
    Faster.setOpacity(fasterOpacity)
    happy.setOpacity(happyOpacity)
    sad.setOpacity(sadOpacity)
    # keep track of which components have finished
    FeedbackComponents = [Faster, happy, sad]
    for thisComponent in FeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Faster* updates
        if Faster.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Faster.frameNStart = frameN  # exact frame index
            Faster.tStart = t  # local t and not account for scr refresh
            Faster.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Faster, 'tStartRefresh')  # time at next scr refresh
            Faster.setAutoDraw(True)
        if Faster.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Faster.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Faster.tStop = t  # not accounting for scr refresh
                Faster.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Faster, 'tStopRefresh')  # time at next scr refresh
                Faster.setAutoDraw(False)
        
        # *happy* updates
        if happy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            happy.frameNStart = frameN  # exact frame index
            happy.tStart = t  # local t and not account for scr refresh
            happy.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(happy, 'tStartRefresh')  # time at next scr refresh
            happy.setAutoDraw(True)
        if happy.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > happy.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                happy.tStop = t  # not accounting for scr refresh
                happy.frameNStop = frameN  # exact frame index
                win.timeOnFlip(happy, 'tStopRefresh')  # time at next scr refresh
                happy.setAutoDraw(False)
        
        # *sad* updates
        if sad.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sad.frameNStart = frameN  # exact frame index
            sad.tStart = t  # local t and not account for scr refresh
            sad.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sad, 'tStartRefresh')  # time at next scr refresh
            sad.setAutoDraw(True)
        if sad.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sad.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                sad.tStop = t  # not accounting for scr refresh
                sad.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sad, 'tStopRefresh')  # time at next scr refresh
                sad.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback"-------
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    VisualAndAudioDistractor.addData('Faster.started', Faster.tStartRefresh)
    VisualAndAudioDistractor.addData('Faster.stopped', Faster.tStopRefresh)
    VisualAndAudioDistractor.addData('happy.started', happy.tStartRefresh)
    VisualAndAudioDistractor.addData('happy.stopped', happy.tStopRefresh)
    VisualAndAudioDistractor.addData('sad.started', sad.tStartRefresh)
    VisualAndAudioDistractor.addData('sad.stopped', sad.tStopRefresh)
    thisExp.nextEntry()
    
# completed 12.0 repeats of 'VisualAndAudioDistractor'


# ------Prepare to start Routine "Pause"-------
continueRoutine = True
# update component parameters for each repeat
next_screen1_2.keys = []
next_screen1_2.rt = []
_next_screen1_2_allKeys = []
# keep track of which components have finished
PauseComponents = [Pause_Text, next_screen1_2]
for thisComponent in PauseComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Pause"-------
while continueRoutine:
    # get current time
    t = PauseClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PauseClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Pause_Text* updates
    if Pause_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Pause_Text.frameNStart = frameN  # exact frame index
        Pause_Text.tStart = t  # local t and not account for scr refresh
        Pause_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Pause_Text, 'tStartRefresh')  # time at next scr refresh
        Pause_Text.setAutoDraw(True)
    
    # *next_screen1_2* updates
    waitOnFlip = False
    if next_screen1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_screen1_2.frameNStart = frameN  # exact frame index
        next_screen1_2.tStart = t  # local t and not account for scr refresh
        next_screen1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_screen1_2, 'tStartRefresh')  # time at next scr refresh
        next_screen1_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_screen1_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_screen1_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_screen1_2.status == STARTED and not waitOnFlip:
        theseKeys = next_screen1_2.getKeys(keyList=None, waitRelease=False)
        _next_screen1_2_allKeys.extend(theseKeys)
        if len(_next_screen1_2_allKeys):
            next_screen1_2.keys = _next_screen1_2_allKeys[-1].name  # just the last key pressed
            next_screen1_2.rt = _next_screen1_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PauseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Pause"-------
for thisComponent in PauseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Pause_Text.started', Pause_Text.tStartRefresh)
thisExp.addData('Pause_Text.stopped', Pause_Text.tStopRefresh)
# check responses
if next_screen1_2.keys in ['', [], None]:  # No response was made
    next_screen1_2.keys = None
thisExp.addData('next_screen1_2.keys',next_screen1_2.keys)
if next_screen1_2.keys != None:  # we had a response
    thisExp.addData('next_screen1_2.rt', next_screen1_2.rt)
thisExp.addData('next_screen1_2.started', next_screen1_2.tStartRefresh)
thisExp.addData('next_screen1_2.stopped', next_screen1_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "Pause" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
AudioDistractorFiles = data.TrialHandler(nReps=12.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='AudioDistractorFiles')
thisExp.addLoop(AudioDistractorFiles)  # add the loop to the experiment
thisAudioDistractorFile = AudioDistractorFiles.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisAudioDistractorFile.rgb)
if thisAudioDistractorFile != None:
    for paramName in thisAudioDistractorFile:
        exec('{} = thisAudioDistractorFile[paramName]'.format(paramName))

for thisAudioDistractorFile in AudioDistractorFiles:
    currentLoop = AudioDistractorFiles
    # abbreviate parameter names if possible (e.g. rgb = thisAudioDistractorFile.rgb)
    if thisAudioDistractorFile != None:
        for paramName in thisAudioDistractorFile:
            exec('{} = thisAudioDistractorFile[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "FixationCross"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    FixationCrossComponents = [FixationCrossText]
    for thisComponent in FixationCrossComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FixationCrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "FixationCross"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FixationCrossClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FixationCrossClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FixationCrossText* updates
        if FixationCrossText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FixationCrossText.frameNStart = frameN  # exact frame index
            FixationCrossText.tStart = t  # local t and not account for scr refresh
            FixationCrossText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FixationCrossText, 'tStartRefresh')  # time at next scr refresh
            FixationCrossText.setAutoDraw(True)
        if FixationCrossText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FixationCrossText.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                FixationCrossText.tStop = t  # not accounting for scr refresh
                FixationCrossText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FixationCrossText, 'tStopRefresh')  # time at next scr refresh
                FixationCrossText.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FixationCrossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FixationCross"-------
    for thisComponent in FixationCrossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    AudioDistractorFiles.addData('FixationCrossText.started', FixationCrossText.tStartRefresh)
    AudioDistractorFiles.addData('FixationCrossText.stopped', FixationCrossText.tStopRefresh)
    
    # ------Prepare to start Routine "AudioDistractorStimuli"-------
    continueRoutine = True
    routineTimer.add(0.700000)
    # update component parameters for each repeat
    p_targetpos = (1,1)
    b_targetpos = (1,1)
    h_fillerpos = (1,1)
    l_fillerpos = (1,1)
    y_fillerpos = (1,1)
    p_dis_volume = 0.0
    b_dis_volume = 0.0
    g_dis_volume = 0.0
    
    def FindTargetAndDistractor(allowedPCongruence, allowedPIncongruence, allowedPNeutral, allowedBCongruence, allowedBIncongruence, allowedBNeutral):
        tar = np.random.choice(targets);
        tarAndDist = FindDistractor(tar, allowedPCongruence, allowedPIncongruence, allowedPNeutral, allowedBCongruence, allowedBIncongruence, allowedBNeutral);
        return tarAndDist; 
        
    def FindDistractor(target, allowedPCongruence, allowedPIncongruence, allowedPNeutral, allowedBCongruence, allowedBIncongruence, allowedBNeutral):
        
        dist = np.random.choice(distractors);
        if target == 'p' and dist == 'p' and allowedPCongruence > 0:
            allowedPCongruence = allowedPCongruence -1; 
            thisExp.addData('Condition', 'Congruent')
            return target, dist, allowedPCongruence, allowedPIncongruence, allowedPNeutral, allowedBCongruence, allowedBIncongruence, allowedBNeutral;
        elif target == 'p' and dist == 'b' and allowedPIncongruence > 0:
            allowedPIncongruence = allowedPIncongruence -1; 
            thisExp.addData('Condition', 'Incongruent')
            return target, dist, allowedPCongruence, allowedPIncongruence, allowedPNeutral, allowedBCongruence, allowedBIncongruence, allowedBNeutral;   
        elif target == 'p' and dist == 'g' and allowedPNeutral > 0:
            allowedPNeutral = allowedPNeutral -1; 
            thisExp.addData('Condition', 'Neutral')
            return target, dist, allowedPCongruence, allowedPIncongruence, allowedPNeutral, allowedBCongruence, allowedBIncongruence, allowedBNeutral;
        elif target == 'b' and dist == 'p' and allowedBIncongruence > 0:
            allowedBIncongruence = allowedBIncongruence -1; 
            thisExp.addData('Condition', 'Incongruent')
            return target, dist, allowedPCongruence, allowedPIncongruence, allowedPNeutral, allowedBCongruence, allowedBIncongruence, allowedBNeutral;
        elif target == 'b' and dist == 'b' and allowedBCongruence > 0:
            allowedBCongruence = allowedBCongruence -1; 
            thisExp.addData('Condition', 'Congruent')
            return target, dist, allowedPCongruence, allowedPIncongruenceA, allowedPNeutral, allowedBCongruence, allowedBIncongruence, allowedBNeutral;   
        elif target == 'b' and dist == 'g' and allowedBNeutral > 0:
            allowedBNeutral = allowedBNeutral -1; 
            thisExp.addData('Condition', 'Neutral')
            return target, dist, allowedPCongruence, allowedPIncongruence, allowedPNeutral, allowedBCongruence, allowedBIncongruence, allowedBNeutral;
        else: 
           return FindDistractor(np.random.choice(targets), allowedPCongruence, allowedPIncongruence, allowedPNeutral, allowedBCongruence, allowedBIncongruence, allowedBNeutral);
       
    # setup variables to control the experiment
    targets = ['p','b'];
    distractors = ['p','b','g'];
    fillers = ['h','l','y'];
    fillerposes = ['upLeft', 'lowLeft', 'upRight', 'lowRight'];
    targetpos = (1,1);
    
    # Setup scene
    # Find the target position 
    targetposName = np.random.choice(fillerposes)
    if targetposName == 'upLeft':
        targetpos = filler_up_left_pos;
    elif targetposName == 'lowLeft':
        targetpos = filler_low_left_pos;
    elif targetposName == 'upRight':
        targetpos = filler_up_right_pos;
    elif targetposName == 'lowRight':
        targetpos = filler_low_right_pos;       
    fillerposes.remove(targetposName);
    # find which will be the target and which will be the distractor
    targetAndDistractor = FindTargetAndDistractor(allowedPCongruenceA, allowedPIncongruenceA, allowedPNeutralA, allowedBCongruenceA, allowedBIncongruenceA, allowedBNeutralA)
    
    target = targetAndDistractor[0];
    distractor = targetAndDistractor[1];
    
    allowedPCongruenceA = targetAndDistractor[2]
    allowedPIncongruenceA = targetAndDistractor[3]
    allowedPNeutralA = targetAndDistractor[4]
    allowedBCongruenceA = targetAndDistractor[5]
    allowedBIncongruenceA = targetAndDistractor[6]
    allowedBNeutralA = targetAndDistractor[7]
    
    targetletter = target; 
    
    if target == 'p':
        p_targetpos = targetpos
    elif target == 'b':
        b_targetpos = targetpos
    
    if distractor == 'p':
        p_dis_volume = 1.0
    elif distractor == 'b':
        b_dis_volume = 1.0
    elif distractor == 'g':
        g_dis_volume = 1.0
    # Randomly place the fillers 
    
    np.random.shuffle(fillerposes);
    np.random.shuffle(fillers);
    index = (0,1,2)
    
    for i in index:
            if fillerposes[i] == 'upLeft' and fillers[i] == 'h':
                h_fillerpos = filler_up_left_pos;
            if fillerposes[i] == 'upLeft' and fillers[i] == 'l':
                l_fillerpos = filler_up_left_pos;
            if fillerposes[i] == 'upLeft' and fillers[i] == 'y':
                y_fillerpos = filler_up_left_pos;
                
            if fillerposes[i] == 'lowLeft' and fillers[i] == 'h':
                h_fillerpos = filler_low_left_pos;
            if fillerposes[i] == 'lowLeft' and fillers[i] == 'l':
                l_fillerpos = filler_low_left_pos;
            if fillerposes[i] == 'lowLeft' and fillers[i] == 'y':
                y_fillerpos = filler_low_left_pos;
                
            if fillerposes[i] == 'lowRight' and fillers[i] == 'h':
                h_fillerpos = filler_low_right_pos;
            if fillerposes[i] == 'lowRight' and fillers[i] == 'l':
                l_fillerpos = filler_low_right_pos;
            if fillerposes[i] == 'lowRight' and fillers[i] == 'y':
                y_fillerpos = filler_low_right_pos;
                
            if fillerposes[i] == 'upRight' and fillers[i] == 'h':
                h_fillerpos = filler_up_right_pos;
            if fillerposes[i] == 'upRight' and fillers[i] == 'l':
                l_fillerpos = filler_up_right_pos;
            if fillerposes[i] == 'upRight' and fillers[i] == 'y':
                y_fillerpos = filler_up_right_pos;
        
    
    p_Target_3.setPos(p_targetpos)
    p_Target_3.setText('p')
    p_Target_3.setFont('Open Sans ExtraBold')
    b_Target_3.setPos(b_targetpos)
    b_Target_3.setFont('Open Sans ExtraBold')
    h_Filler_3.setPos(h_fillerpos)
    l_Filler_3.setPos(l_fillerpos)
    y_filler_3.setPos(y_fillerpos)
    p_Dis_Sound_2.setSound('audio/p.wav', secs=0.2, hamming=False)
    p_Dis_Sound_2.setVolume(p_dis_volume, log=False)
    b_Dis_Sound_2.setSound('audio/b.wav', secs=0.2, hamming=False)
    b_Dis_Sound_2.setVolume(b_dis_volume, log=False)
    g_Dis_Sound_2.setSound('audio/g.wav', secs=0.2, hamming=False)
    g_Dis_Sound_2.setVolume(g_dis_volume, log=False)
    enableHappyface = False;
    enableSadface = False;
    enableFaster = False;
    
    if targetletter == 'p':
        isItP = True;
        isItB = False; 
        
    if targetletter == 'b':
        isItB = True;
        isItP = False; 
    # setup some python lists for storing info about the mouse_3
    mouse_3.x = []
    mouse_3.y = []
    mouse_3.leftButton = []
    mouse_3.midButton = []
    mouse_3.rightButton = []
    mouse_3.time = []
    gotValidClick = False  # until a click is received
    mouse_3.mouseClock.reset()
    # keep track of which components have finished
    AudioDistractorStimuliComponents = [p_Target_3, b_Target_3, h_Filler_3, l_Filler_3, y_filler_3, p_Dis_Sound_2, b_Dis_Sound_2, g_Dis_Sound_2, mouse_3, whiteimage_3]
    for thisComponent in AudioDistractorStimuliComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    AudioDistractorStimuliClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "AudioDistractorStimuli"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AudioDistractorStimuliClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AudioDistractorStimuliClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *p_Target_3* updates
        if p_Target_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            p_Target_3.frameNStart = frameN  # exact frame index
            p_Target_3.tStart = t  # local t and not account for scr refresh
            p_Target_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_Target_3, 'tStartRefresh')  # time at next scr refresh
            p_Target_3.setAutoDraw(True)
        if p_Target_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > p_Target_3.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                p_Target_3.tStop = t  # not accounting for scr refresh
                p_Target_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(p_Target_3, 'tStopRefresh')  # time at next scr refresh
                p_Target_3.setAutoDraw(False)
        
        # *b_Target_3* updates
        if b_Target_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            b_Target_3.frameNStart = frameN  # exact frame index
            b_Target_3.tStart = t  # local t and not account for scr refresh
            b_Target_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(b_Target_3, 'tStartRefresh')  # time at next scr refresh
            b_Target_3.setAutoDraw(True)
        if b_Target_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > b_Target_3.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                b_Target_3.tStop = t  # not accounting for scr refresh
                b_Target_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(b_Target_3, 'tStopRefresh')  # time at next scr refresh
                b_Target_3.setAutoDraw(False)
        
        # *h_Filler_3* updates
        if h_Filler_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            h_Filler_3.frameNStart = frameN  # exact frame index
            h_Filler_3.tStart = t  # local t and not account for scr refresh
            h_Filler_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(h_Filler_3, 'tStartRefresh')  # time at next scr refresh
            h_Filler_3.setAutoDraw(True)
        if h_Filler_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > h_Filler_3.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                h_Filler_3.tStop = t  # not accounting for scr refresh
                h_Filler_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(h_Filler_3, 'tStopRefresh')  # time at next scr refresh
                h_Filler_3.setAutoDraw(False)
        
        # *l_Filler_3* updates
        if l_Filler_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            l_Filler_3.frameNStart = frameN  # exact frame index
            l_Filler_3.tStart = t  # local t and not account for scr refresh
            l_Filler_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l_Filler_3, 'tStartRefresh')  # time at next scr refresh
            l_Filler_3.setAutoDraw(True)
        if l_Filler_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l_Filler_3.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                l_Filler_3.tStop = t  # not accounting for scr refresh
                l_Filler_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(l_Filler_3, 'tStopRefresh')  # time at next scr refresh
                l_Filler_3.setAutoDraw(False)
        
        # *y_filler_3* updates
        if y_filler_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            y_filler_3.frameNStart = frameN  # exact frame index
            y_filler_3.tStart = t  # local t and not account for scr refresh
            y_filler_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(y_filler_3, 'tStartRefresh')  # time at next scr refresh
            y_filler_3.setAutoDraw(True)
        if y_filler_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > y_filler_3.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                y_filler_3.tStop = t  # not accounting for scr refresh
                y_filler_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(y_filler_3, 'tStopRefresh')  # time at next scr refresh
                y_filler_3.setAutoDraw(False)
        # start/stop p_Dis_Sound_2
        if p_Dis_Sound_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            p_Dis_Sound_2.frameNStart = frameN  # exact frame index
            p_Dis_Sound_2.tStart = t  # local t and not account for scr refresh
            p_Dis_Sound_2.tStartRefresh = tThisFlipGlobal  # on global time
            p_Dis_Sound_2.play(when=win)  # sync with win flip
        if p_Dis_Sound_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > p_Dis_Sound_2.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                p_Dis_Sound_2.tStop = t  # not accounting for scr refresh
                p_Dis_Sound_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(p_Dis_Sound_2, 'tStopRefresh')  # time at next scr refresh
                p_Dis_Sound_2.stop()
        # start/stop b_Dis_Sound_2
        if b_Dis_Sound_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            b_Dis_Sound_2.frameNStart = frameN  # exact frame index
            b_Dis_Sound_2.tStart = t  # local t and not account for scr refresh
            b_Dis_Sound_2.tStartRefresh = tThisFlipGlobal  # on global time
            b_Dis_Sound_2.play(when=win)  # sync with win flip
        if b_Dis_Sound_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > b_Dis_Sound_2.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                b_Dis_Sound_2.tStop = t  # not accounting for scr refresh
                b_Dis_Sound_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(b_Dis_Sound_2, 'tStopRefresh')  # time at next scr refresh
                b_Dis_Sound_2.stop()
        # start/stop g_Dis_Sound_2
        if g_Dis_Sound_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            g_Dis_Sound_2.frameNStart = frameN  # exact frame index
            g_Dis_Sound_2.tStart = t  # local t and not account for scr refresh
            g_Dis_Sound_2.tStartRefresh = tThisFlipGlobal  # on global time
            g_Dis_Sound_2.play(when=win)  # sync with win flip
        if g_Dis_Sound_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > g_Dis_Sound_2.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                g_Dis_Sound_2.tStop = t  # not accounting for scr refresh
                g_Dis_Sound_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(g_Dis_Sound_2, 'tStopRefresh')  # time at next scr refresh
                g_Dis_Sound_2.stop()
        #button[0] = left click = P 
        #button[2] = right click = B
        
        buttons = mouse.getPressed()
        
        if isItP and buttons[0] == 1:
            enableHappyface = True;
            enableSadface = False;
            enableFaster = False; 
        elif isItB and buttons[2] == 1:
            enableHappyface = True;
            enableSadface = False;
            enableFaster = False;
        elif isItP and buttons[2] == 1:
            enableHappyface = False;
            enableSadface = True;
            enableFaster = False;  
        elif isItB and buttons[0] == 1:
            enableHappyface = False;
            enableSadface = True;
            enableFaster = False; 
        # *mouse_3* updates
        if mouse_3.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            mouse_3.frameNStart = frameN  # exact frame index
            mouse_3.tStart = t  # local t and not account for scr refresh
            mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
            mouse_3.status = STARTED
            prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
        if mouse_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_3.tStartRefresh + 0.7-frameTolerance:
                # keep track of stop time/frame for later
                mouse_3.tStop = t  # not accounting for scr refresh
                mouse_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mouse_3, 'tStopRefresh')  # time at next scr refresh
                mouse_3.status = FINISHED
        if mouse_3.status == STARTED:  # only update if started and not finished!
            buttons = mouse_3.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = mouse_3.getPos()
                    mouse_3.x.append(x)
                    mouse_3.y.append(y)
                    buttons = mouse_3.getPressed()
                    mouse_3.leftButton.append(buttons[0])
                    mouse_3.midButton.append(buttons[1])
                    mouse_3.rightButton.append(buttons[2])
                    mouse_3.time.append(mouse_3.mouseClock.getTime())
                    
                    continueRoutine = False  # abort routine on response
        
        # *whiteimage_3* updates
        if whiteimage_3.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            whiteimage_3.frameNStart = frameN  # exact frame index
            whiteimage_3.tStart = t  # local t and not account for scr refresh
            whiteimage_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(whiteimage_3, 'tStartRefresh')  # time at next scr refresh
            whiteimage_3.setAutoDraw(True)
        if whiteimage_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > whiteimage_3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                whiteimage_3.tStop = t  # not accounting for scr refresh
                whiteimage_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(whiteimage_3, 'tStopRefresh')  # time at next scr refresh
                whiteimage_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AudioDistractorStimuliComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AudioDistractorStimuli"-------
    for thisComponent in AudioDistractorStimuliComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    AudioDistractorFiles.addData('p_Target_3.started', p_Target_3.tStartRefresh)
    AudioDistractorFiles.addData('p_Target_3.stopped', p_Target_3.tStopRefresh)
    AudioDistractorFiles.addData('b_Target_3.started', b_Target_3.tStartRefresh)
    AudioDistractorFiles.addData('b_Target_3.stopped', b_Target_3.tStopRefresh)
    AudioDistractorFiles.addData('h_Filler_3.started', h_Filler_3.tStartRefresh)
    AudioDistractorFiles.addData('h_Filler_3.stopped', h_Filler_3.tStopRefresh)
    AudioDistractorFiles.addData('l_Filler_3.started', l_Filler_3.tStartRefresh)
    AudioDistractorFiles.addData('l_Filler_3.stopped', l_Filler_3.tStopRefresh)
    AudioDistractorFiles.addData('y_filler_3.started', y_filler_3.tStartRefresh)
    AudioDistractorFiles.addData('y_filler_3.stopped', y_filler_3.tStopRefresh)
    p_Dis_Sound_2.stop()  # ensure sound has stopped at end of routine
    AudioDistractorFiles.addData('p_Dis_Sound_2.started', p_Dis_Sound_2.tStartRefresh)
    AudioDistractorFiles.addData('p_Dis_Sound_2.stopped', p_Dis_Sound_2.tStopRefresh)
    b_Dis_Sound_2.stop()  # ensure sound has stopped at end of routine
    AudioDistractorFiles.addData('b_Dis_Sound_2.started', b_Dis_Sound_2.tStartRefresh)
    AudioDistractorFiles.addData('b_Dis_Sound_2.stopped', b_Dis_Sound_2.tStopRefresh)
    g_Dis_Sound_2.stop()  # ensure sound has stopped at end of routine
    AudioDistractorFiles.addData('g_Dis_Sound_2.started', g_Dis_Sound_2.tStartRefresh)
    AudioDistractorFiles.addData('g_Dis_Sound_2.stopped', g_Dis_Sound_2.tStopRefresh)
    if enableHappyface == False and enableSadface == False:
        enableFaster = True; 
        
    if enableHappyface == True:   
        thisExp.addData('Response', 'Correct')
        thisExp.addData('Response_code', 1.0)
        
    if enableSadface == True:   
        thisExp.addData('Response', 'Incorrect')
        thisExp.addData('Response_code', 2.0)
        
    if enableFaster == True:   
        thisExp.addData('Response', 'None')
        thisExp.addData('Response_code', 0.0)
        
    
    
    # store data for AudioDistractorFiles (TrialHandler)
    AudioDistractorFiles.addData('mouse_3.x', mouse_3.x)
    AudioDistractorFiles.addData('mouse_3.y', mouse_3.y)
    AudioDistractorFiles.addData('mouse_3.leftButton', mouse_3.leftButton)
    AudioDistractorFiles.addData('mouse_3.midButton', mouse_3.midButton)
    AudioDistractorFiles.addData('mouse_3.rightButton', mouse_3.rightButton)
    AudioDistractorFiles.addData('mouse_3.time', mouse_3.time)
    AudioDistractorFiles.addData('mouse_3.started', mouse_3.tStart)
    AudioDistractorFiles.addData('mouse_3.stopped', mouse_3.tStop)
    AudioDistractorFiles.addData('whiteimage_3.started', whiteimage_3.tStartRefresh)
    AudioDistractorFiles.addData('whiteimage_3.stopped', whiteimage_3.tStopRefresh)
    
    # ------Prepare to start Routine "Feedback"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    #from the previous routine feedback will be provided.
    if enableHappyface:
        fasterOpacity = 0.0;
        sadOpacity = 0.0;
        happyOpacity = 1.0; 
        
    if enableSadface:
        fasterOpacity = 0.0;
        sadOpacity = 1.0;
        happyOpacity = 0.0; 
        
    if enableFaster:
        fasterOpacity = 1.0;
        sadOpacity = 0.0;
        happyOpacity = 0.0; 
    Faster.setOpacity(fasterOpacity)
    happy.setOpacity(happyOpacity)
    sad.setOpacity(sadOpacity)
    # keep track of which components have finished
    FeedbackComponents = [Faster, happy, sad]
    for thisComponent in FeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Faster* updates
        if Faster.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Faster.frameNStart = frameN  # exact frame index
            Faster.tStart = t  # local t and not account for scr refresh
            Faster.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Faster, 'tStartRefresh')  # time at next scr refresh
            Faster.setAutoDraw(True)
        if Faster.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Faster.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Faster.tStop = t  # not accounting for scr refresh
                Faster.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Faster, 'tStopRefresh')  # time at next scr refresh
                Faster.setAutoDraw(False)
        
        # *happy* updates
        if happy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            happy.frameNStart = frameN  # exact frame index
            happy.tStart = t  # local t and not account for scr refresh
            happy.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(happy, 'tStartRefresh')  # time at next scr refresh
            happy.setAutoDraw(True)
        if happy.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > happy.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                happy.tStop = t  # not accounting for scr refresh
                happy.frameNStop = frameN  # exact frame index
                win.timeOnFlip(happy, 'tStopRefresh')  # time at next scr refresh
                happy.setAutoDraw(False)
        
        # *sad* updates
        if sad.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sad.frameNStart = frameN  # exact frame index
            sad.tStart = t  # local t and not account for scr refresh
            sad.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sad, 'tStartRefresh')  # time at next scr refresh
            sad.setAutoDraw(True)
        if sad.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sad.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                sad.tStop = t  # not accounting for scr refresh
                sad.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sad, 'tStopRefresh')  # time at next scr refresh
                sad.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback"-------
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    AudioDistractorFiles.addData('Faster.started', Faster.tStartRefresh)
    AudioDistractorFiles.addData('Faster.stopped', Faster.tStopRefresh)
    AudioDistractorFiles.addData('happy.started', happy.tStartRefresh)
    AudioDistractorFiles.addData('happy.stopped', happy.tStopRefresh)
    AudioDistractorFiles.addData('sad.started', sad.tStartRefresh)
    AudioDistractorFiles.addData('sad.stopped', sad.tStopRefresh)
    thisExp.nextEntry()
    
# completed 12.0 repeats of 'AudioDistractorFiles'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
