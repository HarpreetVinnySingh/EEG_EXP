#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.3),
    on July 28, 2023, at 15:43
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '2'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
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

# Run 'Before Experiment' code from Record_CB_2
ERLloop = 0
Break_text = ''

import math
import random


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.3'
expName = 'SimpleWMEEG'  # from the Builder filename that created this script
expInfo = {
    'Sex assigned at birth': ['M','F'],
    'Age in years': '',
    'Highest level of education': ['GCSE','A-Levels','Undergraduate','Masters','PhD'],
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_' % (expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\harpr\\OneDrive\\Desktop\\SimpleWMEEG\\SimpleWMEEG.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=1, 
    winType='pyglet', allowStencil=True,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
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

# --- Initialize components for Routine "pre" ---
# Run 'Begin Experiment' code from code_44


TheWord = ""
Goodme = ''
Badme= ''
Goodother =''
Badother = ''
ShapeSelector = 0
POSFIRST = 0
POSSECOND = 0
TyperPosFirst = 0
TyperPosSecond = 0
TypeTaskFlip = 0
TyperCoinFlip = 0
G_me_RT_Matched = 0
G_me_RT_Mismatched = 0
B_me_RT_Matched = 0
B_me_RT_Mismatched = 0
G_other_RT_Matched = 0
G_other_RT_Mismatched = 0
B_other_RT_Matched = 0
B_other_RT_Mismatched = 0
G_me_TOTTER_Matched = 0
G_me_TOTTER_Mismatched = 0
B_me_TOTTER_Matched = 0
B_me_TOTTER_Mismatched = 0
G_other_TOTTER_Matched = 0
G_other_TOTTER_Mismatched = 0
B_other_TOTTER_Matched = 0
B_other_TOTTER_Mismatched = 0
G_me_CORR_Matched = 0
G_me_CORR_Mismatched = 0
B_me_CORR_Matched = 0
B_me_CORR_Mismatched = 0
G_other_CORR_Matched = 0
G_other_CORR_Mismatched = 0
B_other_CORR_Matched = 0
B_other_CORR_Mismatched = 0
score = 0
scale = 0
LoopnumJS2 = 0
ERLloop2 = 0
Left1 = ''
Right1 = ''
excel = 0
Aexcel = 0
HANDED2 = 0
BDIT = 0
Cognitive_Total = 0
Somatic_af_Total = 0
GADtot = 0
RRStot = 0
Instext2 = 0
score1 = 0

Xenia = 0
Prac = 0

meshape = ''

othershape = ''

shapes_images = ''

shape_label = ''

msg = ''

msgColor = ''

GMtotal_acc = 0

thepresentshape = ''

# --- Initialize components for Routine "Medicine" ---
Medicine_Q = visual.TextStim(win=win, name='Medicine_Q',
    text='If you are on any psychiatric medication or intervention for depression please write it below. If you prefer not to say, please just leave it blank\n\ne.g., 10 mg escitalopram daily, 1 CBT session weekly',
    font='Open Sans',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
textbox_6 = visual.TextBox2(
     win, text='Type here...', placeholder='Type here...', font='Open Sans',
     pos=(0, -.1),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0, speechPoint=None,
     padding=0.0, alignment='center',
     anchor='center', overflow='visible',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox_6',
     depth=-1, autoLog=True,
)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
Submit = visual.ImageStim(
    win=win,
    name='Submit', 
    image='submit.png', mask=None, anchor='center',
    ori=0.0, pos=(.4, -0.4), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "Initialiser" ---
# Run 'Begin Experiment' code from scale
scale = 0.1

# --- Initialize components for Routine "trial" ---
text = visual.TextStim(win=win, name='text',
    text='Thank you for agreeing to take part in this experiment.\n\nThere are two parts to the experiment\n\nThe first is a series of questionnaires about your mental health.\n\nThe second section is a task where you will be asked to indicate the direction of a tilted line.\n\n\nPress SPACE to continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "DorH" ---
cat_choice = visual.TextStim(win=win, name='cat_choice',
    text="If you have never had any pyschological disorder press 'H'\n\nIf you currently or previously have suffered from a psychological or neurological disorder please press 'D'",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
catresp = keyboard.Keyboard()

# --- Initialize components for Routine "Psychomet_Intro" ---
Qest_instruct = visual.TextStim(win=win, name='Qest_instruct',
    text='The first part of this experiment will be a series of questionnaires.\n\nPress the number key associated with the answer to respond.\n\n[Press space to continue]',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Qest_instruct_resp = keyboard.Keyboard()

# --- Initialize components for Routine "BDI" ---
Two_Week = visual.TextStim(win=win, name='Two_Week',
    text='In the last two weeks:',
    font='Open Sans',
    pos=(-0.65, 0.46), height=0.05, wrapWidth=None, ori=0.0, 
    color=[0.3804, 0.7569, 0.8039], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
BDIQ = visual.TextStim(win=win, name='BDIQ',
    text='',
    font='Open Sans',
    pos=(0,0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_20 = visual.TextStim(win=win, name='text_20',
    text='',
    font='Open Sans',
    pos=(0,0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_21 = visual.TextStim(win=win, name='text_21',
    text='',
    font='Open Sans',
    pos=(0, -.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_22 = visual.TextStim(win=win, name='text_22',
    text='',
    font='Open Sans',
    pos=(0,-0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
BDISCORE = keyboard.Keyboard()
# Run 'Begin Experiment' code from BDITotter
BDIT = 0
# Run 'Begin Experiment' code from SubscaleBDI
Cognitive_Total = 0
Somatic_af_Total = 0

# --- Initialize components for Routine "Now_GAD" ---
text_26 = visual.TextStim(win=win, name='text_26',
    text='The next set of questions will be about anxiety. Press SPACE to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
erespresp = keyboard.Keyboard()

# --- Initialize components for Routine "GAD7" ---
text_14 = visual.TextStim(win=win, name='text_14',
    text='Over the last two weeks how often have you been bothered by the following problems?',
    font='Open Sans',
    pos=(0,0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_15 = visual.TextStim(win=win, name='text_15',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_16 = visual.TextStim(win=win, name='text_16',
    text='0 - Not at all, 1 - several days, 2 - More than half the days, 3 - Nearly every day',
    font='Open Sans',
    pos=(0, -0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color=[1.0000, 0.8431, 0.6078], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
GAD7SCORE = keyboard.Keyboard()
# Run 'Begin Experiment' code from GADTotter
GADtot = 0

# --- Initialize components for Routine "Now_Rumination" ---
text_29 = visual.TextStim(win=win, name='text_29',
    text='The next set of questions will be about overthinking.\n\n(PRESS SPACE TO CONTINUE)',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "RSS" ---
text_17 = visual.TextStim(win=win, name='text_17',
    text='Please read the items below to see if and to what extent these thoughts and actions occur when you feel sad or depressed, and press the appropriate number.',
    font='Open Sans',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_18 = visual.TextStim(win=win, name='text_18',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[0.7412, 0.4431, 0.0588], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_19 = visual.TextStim(win=win, name='text_19',
    text='1 : never; 2 : sometimes; 3 : often; 4 : always\n\nRemember to answer according to your usual practice, rather than what you would like to do.',
    font='Open Sans',
    pos=(0, -.25), height=0.05, wrapWidth=None, ori=0.0, 
    color=[0.7412, 0.4431, 0.0588], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
RRSANSWER = keyboard.Keyboard()
# Run 'Begin Experiment' code from code_30
RRStot = 0

# --- Initialize components for Routine "Ethical_Text" ---
text_129 = visual.TextStim(win=win, name='text_129',
    text='You may have found some of the questions upsetting or be worried that you are experiencing symptoms of depression. You are encouraged to speak with your GP if you are concerned about your health.\n\nAlternatively you can call the Samiratans free 24/7/365 if you need someone to talk to. Just call 116 123 from any phone.\n\nUseful resources can also be found on Mind.org.uk\n\nIf you no longer wish to take part in the experiment press [ESC] to exit, otherwise press [SPACE] to continue.\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_54 = keyboard.Keyboard()

# --- Initialize components for Routine "GMBM_Explain" ---
GoodMeBadMeText = visual.TextStim(win=win, name='GoodMeBadMeText',
    text="You will learn to associate yourself 'You' with a shape\n\nYou will also now learn to associate an unknown stranger 'Other' as a different shape.\n\n\nSPACE TO CONTINUE",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[0.9608, 0.8824, 0.8039], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_17 = keyboard.Keyboard()

# --- Initialize components for Routine "NomenAssoc" ---
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, .2), size=(3*scale,3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_47 = visual.TextStim(win=win, name='text_47',
    text='',
    font='Open Sans',
    pos=(0.3, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_23 = keyboard.Keyboard()
text_49 = visual.TextStim(win=win, name='text_49',
    text='SPACE TO CONTINUE',
    font='Open Sans',
    pos=(0, -.38), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "MeAssoc" ---
image_13 = visual.ImageStim(
    win=win,
    name='image_13', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, .2), size=(3*scale,3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_50 = visual.TextStim(win=win, name='text_50',
    text='= You',
    font='Open Sans',
    pos=(0.3, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_24 = keyboard.Keyboard()
text_52 = visual.TextStim(win=win, name='text_52',
    text='SPACE TO CONTINUE',
    font='Open Sans',
    pos=(0, -.38), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "PracticeGoodText" ---
text_37 = visual.TextStim(win=win, name='text_37',
    text='Lets start with a practice to make sure you have learnt the right associations.\n\nThis practice loop will end when you get all possible matched and mismatched combinations correct.\n\nSPACE TO CONTINUE',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_25 = keyboard.Keyboard()

# --- Initialize components for Routine "MeAssoc" ---
image_13 = visual.ImageStim(
    win=win,
    name='image_13', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, .2), size=(3*scale,3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_50 = visual.TextStim(win=win, name='text_50',
    text='= You',
    font='Open Sans',
    pos=(0.3, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_24 = keyboard.Keyboard()
text_52 = visual.TextStim(win=win, name='text_52',
    text='SPACE TO CONTINUE',
    font='Open Sans',
    pos=(0, -.38), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "NomenAssoc" ---
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, .2), size=(3*scale,3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_47 = visual.TextStim(win=win, name='text_47',
    text='',
    font='Open Sans',
    pos=(0.3, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_23 = keyboard.Keyboard()
text_49 = visual.TextStim(win=win, name='text_49',
    text='SPACE TO CONTINUE',
    font='Open Sans',
    pos=(0, -.38), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "MeAssoc" ---
image_13 = visual.ImageStim(
    win=win,
    name='image_13', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, .2), size=(3*scale,3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_50 = visual.TextStim(win=win, name='text_50',
    text='= You',
    font='Open Sans',
    pos=(0.3, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_24 = keyboard.Keyboard()
text_52 = visual.TextStim(win=win, name='text_52',
    text='SPACE TO CONTINUE',
    font='Open Sans',
    pos=(0, -.38), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "NomenAssoc" ---
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, .2), size=(3*scale,3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_47 = visual.TextStim(win=win, name='text_47',
    text='',
    font='Open Sans',
    pos=(0.3, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_23 = keyboard.Keyboard()
text_49 = visual.TextStim(win=win, name='text_49',
    text='SPACE TO CONTINUE',
    font='Open Sans',
    pos=(0, -.38), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "MeAssoc" ---
image_13 = visual.ImageStim(
    win=win,
    name='image_13', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, .2), size=(3*scale,3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_50 = visual.TextStim(win=win, name='text_50',
    text='= You',
    font='Open Sans',
    pos=(0.3, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_24 = keyboard.Keyboard()
text_52 = visual.TextStim(win=win, name='text_52',
    text='SPACE TO CONTINUE',
    font='Open Sans',
    pos=(0, -.38), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "NomenAssoc" ---
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, .2), size=(3*scale,3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_47 = visual.TextStim(win=win, name='text_47',
    text='',
    font='Open Sans',
    pos=(0.3, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_23 = keyboard.Keyboard()
text_49 = visual.TextStim(win=win, name='text_49',
    text='SPACE TO CONTINUE',
    font='Open Sans',
    pos=(0, -.38), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "TASK_INSTRUCTIONS9" ---
text_100 = visual.TextStim(win=win, name='text_100',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_40 = keyboard.Keyboard()

# --- Initialize components for Routine "New_prac" ---
TheShape = visual.ImageStim(
    win=win,
    name='TheShape', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.2), size=(3*scale, 3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
Person = visual.TextStim(win=win, name='Person',
    text='',
    font='Open Sans',
    pos=(0,-.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Praccross = visual.TextStim(win=win, name='Praccross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Left_button = visual.TextStim(win=win, name='Left_button',
    text='',
    font='Open Sans',
    pos=(-.4, -.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
Right_button = visual.TextStim(win=win, name='Right_button',
    text='',
    font='Open Sans',
    pos=(0.4, -.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
Prac_resp = keyboard.Keyboard()

# --- Initialize components for Routine "New_feedback" ---
text_56 = visual.TextStim(win=win, name='text_56',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "DONE_GMBM" ---
text_126 = visual.TextStim(win=win, name='text_126',
    text='Congratulations, you have completed this part of the experiment.\n\nPress SPACE to continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_51 = keyboard.Keyboard()

# --- Initialize components for Routine "Learning_intro" ---
text_34 = visual.TextStim(win=win, name='text_34',
    text='You will now learn how the task works through a training version which is slower than the actual task so you can get used to it.\n\nYour goal is to indicate if the tilted line is tilted to the left or the right.\n\nIf it is tilted to the LEFT press X.\n\nIf it is tilted to the RIGHT press Y.\n\n\nThe lines will be superimposed onto some of the shapes from the previous task.\n\nYou will be asked to remember a meaningful shape, and occasionally quizzed on what that shape represented to ensure you are keeping it in your memory.\n\n\nThese shapes are task irrelevant. \n\nPress SPACE to continue.\n',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()
LeftTiltEx = visual.ImageStim(
    win=win,
    name='LeftTiltEx', 
    image='images/L_tilt.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.64, 0), size=(3*scale,3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
RightTiltEx = visual.ImageStim(
    win=win,
    name='RightTiltEx', 
    image='images/R_tilt.png', mask=None, anchor='center',
    ori=0.0, pos=(0.64, 0), size=(3*scale,3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
A_text = visual.TextStim(win=win, name='A_text',
    text='(X)',
    font='Open Sans',
    pos=(-.64, -.1), height=0.05, wrapWidth=None, ori=0.0, 
    color=[0.0902, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
L_text = visual.TextStim(win=win, name='L_text',
    text='(Y)',
    font='Open Sans',
    pos=(0.64, -0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color=[0.0902, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "MeAssoc" ---
image_13 = visual.ImageStim(
    win=win,
    name='image_13', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, .2), size=(3*scale,3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_50 = visual.TextStim(win=win, name='text_50',
    text='= You',
    font='Open Sans',
    pos=(0.3, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_24 = keyboard.Keyboard()
text_52 = visual.TextStim(win=win, name='text_52',
    text='SPACE TO CONTINUE',
    font='Open Sans',
    pos=(0, -.38), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "NomenAssoc" ---
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, .2), size=(3*scale,3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_47 = visual.TextStim(win=win, name='text_47',
    text='',
    font='Open Sans',
    pos=(0.3, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_23 = keyboard.Keyboard()
text_49 = visual.TextStim(win=win, name='text_49',
    text='SPACE TO CONTINUE',
    font='Open Sans',
    pos=(0, -.38), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "MeAssoc" ---
image_13 = visual.ImageStim(
    win=win,
    name='image_13', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, .2), size=(3*scale,3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_50 = visual.TextStim(win=win, name='text_50',
    text='= You',
    font='Open Sans',
    pos=(0.3, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_24 = keyboard.Keyboard()
text_52 = visual.TextStim(win=win, name='text_52',
    text='SPACE TO CONTINUE',
    font='Open Sans',
    pos=(0, -.38), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "NomenAssoc" ---
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, .2), size=(3*scale,3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_47 = visual.TextStim(win=win, name='text_47',
    text='',
    font='Open Sans',
    pos=(0.3, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_23 = keyboard.Keyboard()
text_49 = visual.TextStim(win=win, name='text_49',
    text='SPACE TO CONTINUE',
    font='Open Sans',
    pos=(0, -.38), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "Count_down" ---
text_72 = visual.TextStim(win=win, name='text_72',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Cue_WM_2" ---
image_5 = visual.ImageStim(
    win=win,
    name='image_5', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.2), size=(3*scale, 3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
Crux_5 = visual.TextStim(win=win, name='Crux_5',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_42 = visual.TextStim(win=win, name='text_42',
    text='Remember this shape',
    font='Open Sans',
    pos=(0, -.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "Crucem_WM" ---
text_41 = visual.TextStim(win=win, name='text_41',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
polygon_2 = visual.ShapeStim(
    win=win, name='polygon_2',
    size=[1.0, 1.0], vertices='circle',
    ori=0.0, pos=(0,0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.7333, 0.0902, -0.7333], fillColor=[-0.7333, 0.0902, -0.7333],
    opacity=0.3, depth=-4.0, interpolate=True)

# --- Initialize components for Routine "ERL_3" ---
Left_shape_3 = visual.ImageStim(
    win=win,
    name='Left_shape_3', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.5, 0), size=(3*scale, 3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
Right_shape_3 = visual.ImageStim(
    win=win,
    name='Right_shape_3', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(.5, 0), size=(3*scale, 3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Tilted_line_3 = visual.ImageStim(
    win=win,
    name='Tilted_line_3', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.5*scale, 0.5*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Horizontal_line_3 = visual.ImageStim(
    win=win,
    name='Horizontal_line_3', 
    image='images/V_line.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.5*scale, 0.5*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
Answer_3 = keyboard.Keyboard()
Crux_6 = visual.TextStim(win=win, name='Crux_6',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "Feedback_ERL_3" ---
Fodeback_3 = visual.TextStim(win=win, name='Fodeback_3',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "Test_3" ---
Test_answer_3 = keyboard.Keyboard()
text_43 = visual.TextStim(win=win, name='text_43',
    text='(X) = Yes',
    font='Open Sans',
    pos=(-.4, -.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_44 = visual.TextStim(win=win, name='text_44',
    text='The shape in the cue represented was:',
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_45 = visual.TextStim(win=win, name='text_45',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
text_46 = visual.TextStim(win=win, name='text_46',
    text='(Y) = No',
    font='Open Sans',
    pos=(.4, -.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "Test_feedback_3" ---
text_54 = visual.TextStim(win=win, name='text_54',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "Now_it_real" ---
text_55 = visual.TextStim(win=win, name='text_55',
    text='Now you will start the actual task\n\nIt will be the same as training but faster\n\n[Press SPACE to continue]',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_11 = keyboard.Keyboard()

# --- Initialize components for Routine "MeAssoc" ---
image_13 = visual.ImageStim(
    win=win,
    name='image_13', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, .2), size=(3*scale,3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_50 = visual.TextStim(win=win, name='text_50',
    text='= You',
    font='Open Sans',
    pos=(0.3, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_24 = keyboard.Keyboard()
text_52 = visual.TextStim(win=win, name='text_52',
    text='SPACE TO CONTINUE',
    font='Open Sans',
    pos=(0, -.38), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "NomenAssoc" ---
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, .2), size=(3*scale,3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_47 = visual.TextStim(win=win, name='text_47',
    text='',
    font='Open Sans',
    pos=(0.3, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_23 = keyboard.Keyboard()
text_49 = visual.TextStim(win=win, name='text_49',
    text='SPACE TO CONTINUE',
    font='Open Sans',
    pos=(0, -.38), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "MeAssoc" ---
image_13 = visual.ImageStim(
    win=win,
    name='image_13', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, .2), size=(3*scale,3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_50 = visual.TextStim(win=win, name='text_50',
    text='= You',
    font='Open Sans',
    pos=(0.3, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_24 = keyboard.Keyboard()
text_52 = visual.TextStim(win=win, name='text_52',
    text='SPACE TO CONTINUE',
    font='Open Sans',
    pos=(0, -.38), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "NomenAssoc" ---
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, .2), size=(3*scale,3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_47 = visual.TextStim(win=win, name='text_47',
    text='',
    font='Open Sans',
    pos=(0.3, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_23 = keyboard.Keyboard()
text_49 = visual.TextStim(win=win, name='text_49',
    text='SPACE TO CONTINUE',
    font='Open Sans',
    pos=(0, -.38), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "Count_down" ---
text_72 = visual.TextStim(win=win, name='text_72',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Cue_WM" ---
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.2), size=(3*scale, 3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
Crux_4 = visual.TextStim(win=win, name='Crux_4',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_40 = visual.TextStim(win=win, name='text_40',
    text='Remember this shape',
    font='Open Sans',
    pos=(0, -.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "Crucem_WM" ---
text_41 = visual.TextStim(win=win, name='text_41',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
polygon_2 = visual.ShapeStim(
    win=win, name='polygon_2',
    size=[1.0, 1.0], vertices='circle',
    ori=0.0, pos=(0,0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.7333, 0.0902, -0.7333], fillColor=[-0.7333, 0.0902, -0.7333],
    opacity=0.3, depth=-4.0, interpolate=True)

# --- Initialize components for Routine "ERL" ---
Left_shape = visual.ImageStim(
    win=win,
    name='Left_shape', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.5, 0), size=(3*scale, 3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
Right_shape = visual.ImageStim(
    win=win,
    name='Right_shape', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(.5, 0), size=(3*scale, 3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Tilted_line = visual.ImageStim(
    win=win,
    name='Tilted_line', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.5*scale, 0.5*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Horizontal_line = visual.ImageStim(
    win=win,
    name='Horizontal_line', 
    image='images/V_line.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.5*scale, 0.5*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
Answer = keyboard.Keyboard()
Crux = visual.TextStim(win=win, name='Crux',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "Feedback_ERL" ---
Fodeback = visual.TextStim(win=win, name='Fodeback',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "SAVER_WM" ---

# --- Initialize components for Routine "Test" ---
Test_answer = keyboard.Keyboard()
text_5 = visual.TextStim(win=win, name='text_5',
    text='(A) = Yes',
    font='Open Sans',
    pos=(-.4, -.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_12 = visual.TextStim(win=win, name='text_12',
    text='The shape in the cue represented was:',
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_13 = visual.TextStim(win=win, name='text_13',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
text_23 = visual.TextStim(win=win, name='text_23',
    text='(L) = No',
    font='Open Sans',
    pos=(.4, -.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "Test_feedback" ---
text_6 = visual.TextStim(win=win, name='text_6',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "ERL_Break_Text" ---
text_7 = visual.TextStim(win=win, name='text_7',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_5 = keyboard.Keyboard()

# --- Initialize components for Routine "ERL_Me_Assoc_2" ---
image_41 = visual.ImageStim(
    win=win,
    name='image_41', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, .2), size=(3*scale, 3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_42 = visual.ImageStim(
    win=win,
    name='image_42', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, -.2), size=(3*scale, 3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
text_127 = visual.TextStim(win=win, name='text_127',
    text="=" + "Good" +" "+ "Me",
    font='Open Sans',
    pos=(0.3, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_128 = visual.TextStim(win=win, name='text_128',
    text="=" + "Bad" +" "+ "Me",
    font='Open Sans',
    pos=(0.3, -.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
key_resp_52 = keyboard.Keyboard()
text_130 = visual.TextStim(win=win, name='text_130',
    text='SPACE TO CONTINUE',
    font='Open Sans',
    pos=(0, -.38), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "ERL_Nomen_Assoc_2" ---
image_43 = visual.ImageStim(
    win=win,
    name='image_43', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, .2), size=(3*scale, 3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_44 = visual.ImageStim(
    win=win,
    name='image_44', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, -.2), size=(3*scale, 3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
text_131 = visual.TextStim(win=win, name='text_131',
    text='',
    font='Open Sans',
    pos=(0.3, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_132 = visual.TextStim(win=win, name='text_132',
    text='',
    font='Open Sans',
    pos=(0.3, -.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
key_resp_53 = keyboard.Keyboard()
text_133 = visual.TextStim(win=win, name='text_133',
    text='SPACE TO CONTINUE',
    font='Open Sans',
    pos=(0, -.38), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "ERL_Me_Assoc_2" ---
image_41 = visual.ImageStim(
    win=win,
    name='image_41', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, .2), size=(3*scale, 3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_42 = visual.ImageStim(
    win=win,
    name='image_42', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, -.2), size=(3*scale, 3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
text_127 = visual.TextStim(win=win, name='text_127',
    text="=" + "Good" +" "+ "Me",
    font='Open Sans',
    pos=(0.3, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_128 = visual.TextStim(win=win, name='text_128',
    text="=" + "Bad" +" "+ "Me",
    font='Open Sans',
    pos=(0.3, -.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
key_resp_52 = keyboard.Keyboard()
text_130 = visual.TextStim(win=win, name='text_130',
    text='SPACE TO CONTINUE',
    font='Open Sans',
    pos=(0, -.38), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "ERL_Nomen_Assoc_2" ---
image_43 = visual.ImageStim(
    win=win,
    name='image_43', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, .2), size=(3*scale, 3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_44 = visual.ImageStim(
    win=win,
    name='image_44', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, -.2), size=(3*scale, 3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
text_131 = visual.TextStim(win=win, name='text_131',
    text='',
    font='Open Sans',
    pos=(0.3, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_132 = visual.TextStim(win=win, name='text_132',
    text='',
    font='Open Sans',
    pos=(0.3, -.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
key_resp_53 = keyboard.Keyboard()
text_133 = visual.TextStim(win=win, name='text_133',
    text='SPACE TO CONTINUE',
    font='Open Sans',
    pos=(0, -.38), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "ERL_CD" ---
text_134 = visual.TextStim(win=win, name='text_134',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "ERL_Break_Text_2" ---
text_8 = visual.TextStim(win=win, name='text_8',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_6 = keyboard.Keyboard()

# --- Initialize components for Routine "ERL_Me_Assoc_3" ---
image_45 = visual.ImageStim(
    win=win,
    name='image_45', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, .2), size=(3*scale, 3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_46 = visual.ImageStim(
    win=win,
    name='image_46', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, -.2), size=(3*scale, 3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
text_135 = visual.TextStim(win=win, name='text_135',
    text="=" + "Good" +" "+ "Me",
    font='Open Sans',
    pos=(0.3, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_136 = visual.TextStim(win=win, name='text_136',
    text="=" + "Bad" +" "+ "Me",
    font='Open Sans',
    pos=(0.3, -.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
key_resp_55 = keyboard.Keyboard()
text_137 = visual.TextStim(win=win, name='text_137',
    text='SPACE TO CONTINUE',
    font='Open Sans',
    pos=(0, -.38), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "ERL_Nomen_Assoc_3" ---
image_47 = visual.ImageStim(
    win=win,
    name='image_47', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, .2), size=(3*scale, 3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_48 = visual.ImageStim(
    win=win,
    name='image_48', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, -.2), size=(3*scale, 3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
text_138 = visual.TextStim(win=win, name='text_138',
    text='',
    font='Open Sans',
    pos=(0.3, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_139 = visual.TextStim(win=win, name='text_139',
    text='',
    font='Open Sans',
    pos=(0.3, -.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
key_resp_56 = keyboard.Keyboard()
text_140 = visual.TextStim(win=win, name='text_140',
    text='SPACE TO CONTINUE',
    font='Open Sans',
    pos=(0, -.38), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "ERL_Me_Assoc_3" ---
image_45 = visual.ImageStim(
    win=win,
    name='image_45', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, .2), size=(3*scale, 3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_46 = visual.ImageStim(
    win=win,
    name='image_46', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, -.2), size=(3*scale, 3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
text_135 = visual.TextStim(win=win, name='text_135',
    text="=" + "Good" +" "+ "Me",
    font='Open Sans',
    pos=(0.3, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_136 = visual.TextStim(win=win, name='text_136',
    text="=" + "Bad" +" "+ "Me",
    font='Open Sans',
    pos=(0.3, -.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
key_resp_55 = keyboard.Keyboard()
text_137 = visual.TextStim(win=win, name='text_137',
    text='SPACE TO CONTINUE',
    font='Open Sans',
    pos=(0, -.38), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "ERL_Nomen_Assoc_3" ---
image_47 = visual.ImageStim(
    win=win,
    name='image_47', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, .2), size=(3*scale, 3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_48 = visual.ImageStim(
    win=win,
    name='image_48', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, -.2), size=(3*scale, 3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
text_138 = visual.TextStim(win=win, name='text_138',
    text='',
    font='Open Sans',
    pos=(0.3, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_139 = visual.TextStim(win=win, name='text_139',
    text='',
    font='Open Sans',
    pos=(0.3, -.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
key_resp_56 = keyboard.Keyboard()
text_140 = visual.TextStim(win=win, name='text_140',
    text='SPACE TO CONTINUE',
    font='Open Sans',
    pos=(0, -.38), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "ERL_CD_2" ---
text_141 = visual.TextStim(win=win, name='text_141',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "ERL_Break_Text_3" ---
text_9 = visual.TextStim(win=win, name='text_9',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_7 = keyboard.Keyboard()

# --- Initialize components for Routine "ERL_Me_Assoc_4" ---
image_49 = visual.ImageStim(
    win=win,
    name='image_49', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, .2), size=(3*scale, 3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_50 = visual.ImageStim(
    win=win,
    name='image_50', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, -.2), size=(3*scale, 3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
text_142 = visual.TextStim(win=win, name='text_142',
    text="=" + "Good" +" "+ "Me",
    font='Open Sans',
    pos=(0.3, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_143 = visual.TextStim(win=win, name='text_143',
    text="=" + "Bad" +" "+ "Me",
    font='Open Sans',
    pos=(0.3, -.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
key_resp_57 = keyboard.Keyboard()
text_144 = visual.TextStim(win=win, name='text_144',
    text='SPACE TO CONTINUE',
    font='Open Sans',
    pos=(0, -.38), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "ERL_Nomen_Assoc_4" ---
image_51 = visual.ImageStim(
    win=win,
    name='image_51', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, .2), size=(3*scale, 3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_52 = visual.ImageStim(
    win=win,
    name='image_52', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, -.2), size=(3*scale, 3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
text_145 = visual.TextStim(win=win, name='text_145',
    text='',
    font='Open Sans',
    pos=(0.3, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_146 = visual.TextStim(win=win, name='text_146',
    text='',
    font='Open Sans',
    pos=(0.3, -.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
key_resp_58 = keyboard.Keyboard()
text_147 = visual.TextStim(win=win, name='text_147',
    text='SPACE TO CONTINUE',
    font='Open Sans',
    pos=(0, -.38), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "ERL_Me_Assoc_4" ---
image_49 = visual.ImageStim(
    win=win,
    name='image_49', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, .2), size=(3*scale, 3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_50 = visual.ImageStim(
    win=win,
    name='image_50', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, -.2), size=(3*scale, 3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
text_142 = visual.TextStim(win=win, name='text_142',
    text="=" + "Good" +" "+ "Me",
    font='Open Sans',
    pos=(0.3, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_143 = visual.TextStim(win=win, name='text_143',
    text="=" + "Bad" +" "+ "Me",
    font='Open Sans',
    pos=(0.3, -.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
key_resp_57 = keyboard.Keyboard()
text_144 = visual.TextStim(win=win, name='text_144',
    text='SPACE TO CONTINUE',
    font='Open Sans',
    pos=(0, -.38), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "ERL_Nomen_Assoc_4" ---
image_51 = visual.ImageStim(
    win=win,
    name='image_51', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, .2), size=(3*scale, 3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_52 = visual.ImageStim(
    win=win,
    name='image_52', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-.3, -.2), size=(3*scale, 3*scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
text_145 = visual.TextStim(win=win, name='text_145',
    text='',
    font='Open Sans',
    pos=(0.3, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_146 = visual.TextStim(win=win, name='text_146',
    text='',
    font='Open Sans',
    pos=(0.3, -.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
key_resp_58 = keyboard.Keyboard()
text_147 = visual.TextStim(win=win, name='text_147',
    text='SPACE TO CONTINUE',
    font='Open Sans',
    pos=(0, -.38), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "ERL_CD_3" ---
text_148 = visual.TextStim(win=win, name='text_148',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "END" ---
text_10 = visual.TextStim(win=win, name='text_10',
    text='Congratulation! you have completed the experiment.\n\nPLEASE make sure you press SPACE to finish.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_8 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "pre" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
preComponents = []
for thisComponent in preComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "pre" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in preComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "pre" ---
for thisComponent in preComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "pre" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Medicine" ---
continueRoutine = True
# update component parameters for each repeat
textbox_6.reset()
# setup some python lists for storing info about the mouse
mouse.x = []
mouse.y = []
mouse.leftButton = []
mouse.midButton = []
mouse.rightButton = []
mouse.time = []
mouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
MedicineComponents = [Medicine_Q, textbox_6, mouse, Submit]
for thisComponent in MedicineComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Medicine" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Medicine_Q* updates
    
    # if Medicine_Q is starting this frame...
    if Medicine_Q.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Medicine_Q.frameNStart = frameN  # exact frame index
        Medicine_Q.tStart = t  # local t and not account for scr refresh
        Medicine_Q.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Medicine_Q, 'tStartRefresh')  # time at next scr refresh
        # update status
        Medicine_Q.status = STARTED
        Medicine_Q.setAutoDraw(True)
    
    # if Medicine_Q is active this frame...
    if Medicine_Q.status == STARTED:
        # update params
        pass
    
    # *textbox_6* updates
    
    # if textbox_6 is starting this frame...
    if textbox_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox_6.frameNStart = frameN  # exact frame index
        textbox_6.tStart = t  # local t and not account for scr refresh
        textbox_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textbox_6.started')
        # update status
        textbox_6.status = STARTED
        textbox_6.setAutoDraw(True)
    
    # if textbox_6 is active this frame...
    if textbox_6.status == STARTED:
        # update params
        pass
    # *mouse* updates
    
    # if mouse is starting this frame...
    if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse.frameNStart = frameN  # exact frame index
        mouse.tStart = t  # local t and not account for scr refresh
        mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mouse.started', t)
        # update status
        mouse.status = STARTED
        mouse.mouseClock.reset()
        prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                clickableList = environmenttools.getFromNames(Submit, namespace=locals())
                for obj in clickableList:
                    # is this object clicked on?
                    if obj.contains(mouse):
                        gotValidClick = True
                        mouse.clicked_name.append(obj.name)
                x, y = mouse.getPos()
                mouse.x.append(x)
                mouse.y.append(y)
                buttons = mouse.getPressed()
                mouse.leftButton.append(buttons[0])
                mouse.midButton.append(buttons[1])
                mouse.rightButton.append(buttons[2])
                mouse.time.append(mouse.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # end routine on response
    
    # *Submit* updates
    
    # if Submit is starting this frame...
    if Submit.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Submit.frameNStart = frameN  # exact frame index
        Submit.tStart = t  # local t and not account for scr refresh
        Submit.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Submit, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Submit.started')
        # update status
        Submit.status = STARTED
        Submit.setAutoDraw(True)
    
    # if Submit is active this frame...
    if Submit.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MedicineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Medicine" ---
for thisComponent in MedicineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textbox_6.text',textbox_6.text)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse.x', mouse.x)
thisExp.addData('mouse.y', mouse.y)
thisExp.addData('mouse.leftButton', mouse.leftButton)
thisExp.addData('mouse.midButton', mouse.midButton)
thisExp.addData('mouse.rightButton', mouse.rightButton)
thisExp.addData('mouse.time', mouse.time)
thisExp.addData('mouse.clicked_name', mouse.clicked_name)
thisExp.nextEntry()
# the Routine "Medicine" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Initialiser" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
InitialiserComponents = []
for thisComponent in InitialiserComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Initialiser" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InitialiserComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Initialiser" ---
for thisComponent in InitialiserComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Initialiser" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "trial" ---
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
trialComponents = [text, key_resp]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "trial" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    
    # if text is starting this frame...
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # update status
        text.status = STARTED
        text.setAutoDraw(True)
    
    # if text is active this frame...
    if text.status == STARTED:
        # update params
        pass
    
    # *key_resp* updates
    waitOnFlip = False
    
    # if key_resp is starting this frame...
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        # update status
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            key_resp.duration = _key_resp_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "trial" ---
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
    thisExp.addData('key_resp.duration', key_resp.duration)
thisExp.nextEntry()
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "DorH" ---
continueRoutine = True
# update component parameters for each repeat
catresp.keys = []
catresp.rt = []
_catresp_allKeys = []
# keep track of which components have finished
DorHComponents = [cat_choice, catresp]
for thisComponent in DorHComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "DorH" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *cat_choice* updates
    
    # if cat_choice is starting this frame...
    if cat_choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cat_choice.frameNStart = frameN  # exact frame index
        cat_choice.tStart = t  # local t and not account for scr refresh
        cat_choice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cat_choice, 'tStartRefresh')  # time at next scr refresh
        # update status
        cat_choice.status = STARTED
        cat_choice.setAutoDraw(True)
    
    # if cat_choice is active this frame...
    if cat_choice.status == STARTED:
        # update params
        pass
    
    # *catresp* updates
    waitOnFlip = False
    
    # if catresp is starting this frame...
    if catresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        catresp.frameNStart = frameN  # exact frame index
        catresp.tStart = t  # local t and not account for scr refresh
        catresp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(catresp, 'tStartRefresh')  # time at next scr refresh
        # update status
        catresp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(catresp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(catresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if catresp.status == STARTED and not waitOnFlip:
        theseKeys = catresp.getKeys(keyList=['h','d'], waitRelease=False)
        _catresp_allKeys.extend(theseKeys)
        if len(_catresp_allKeys):
            catresp.keys = _catresp_allKeys[-1].name  # just the last key pressed
            catresp.rt = _catresp_allKeys[-1].rt
            catresp.duration = _catresp_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in DorHComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "DorH" ---
for thisComponent in DorHComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if catresp.keys in ['', [], None]:  # No response was made
    catresp.keys = None
thisExp.addData('catresp.keys',catresp.keys)
if catresp.keys != None:  # we had a response
    thisExp.addData('catresp.rt', catresp.rt)
    thisExp.addData('catresp.duration', catresp.duration)
thisExp.nextEntry()
# the Routine "DorH" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Psychomet_Intro" ---
continueRoutine = True
# update component parameters for each repeat
Qest_instruct_resp.keys = []
Qest_instruct_resp.rt = []
_Qest_instruct_resp_allKeys = []
# keep track of which components have finished
Psychomet_IntroComponents = [Qest_instruct, Qest_instruct_resp]
for thisComponent in Psychomet_IntroComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Psychomet_Intro" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Qest_instruct* updates
    
    # if Qest_instruct is starting this frame...
    if Qest_instruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Qest_instruct.frameNStart = frameN  # exact frame index
        Qest_instruct.tStart = t  # local t and not account for scr refresh
        Qest_instruct.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Qest_instruct, 'tStartRefresh')  # time at next scr refresh
        # update status
        Qest_instruct.status = STARTED
        Qest_instruct.setAutoDraw(True)
    
    # if Qest_instruct is active this frame...
    if Qest_instruct.status == STARTED:
        # update params
        pass
    
    # *Qest_instruct_resp* updates
    waitOnFlip = False
    
    # if Qest_instruct_resp is starting this frame...
    if Qest_instruct_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Qest_instruct_resp.frameNStart = frameN  # exact frame index
        Qest_instruct_resp.tStart = t  # local t and not account for scr refresh
        Qest_instruct_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Qest_instruct_resp, 'tStartRefresh')  # time at next scr refresh
        # update status
        Qest_instruct_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Qest_instruct_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Qest_instruct_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Qest_instruct_resp.status == STARTED and not waitOnFlip:
        theseKeys = Qest_instruct_resp.getKeys(keyList=['space'], waitRelease=False)
        _Qest_instruct_resp_allKeys.extend(theseKeys)
        if len(_Qest_instruct_resp_allKeys):
            Qest_instruct_resp.keys = _Qest_instruct_resp_allKeys[-1].name  # just the last key pressed
            Qest_instruct_resp.rt = _Qest_instruct_resp_allKeys[-1].rt
            Qest_instruct_resp.duration = _Qest_instruct_resp_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Psychomet_IntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Psychomet_Intro" ---
for thisComponent in Psychomet_IntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Psychomet_Intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
BDI_Loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BDI.xlsx'),
    seed=None, name='BDI_Loop')
thisExp.addLoop(BDI_Loop)  # add the loop to the experiment
thisBDI_Loop = BDI_Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBDI_Loop.rgb)
if thisBDI_Loop != None:
    for paramName in thisBDI_Loop:
        exec('{} = thisBDI_Loop[paramName]'.format(paramName))

for thisBDI_Loop in BDI_Loop:
    currentLoop = BDI_Loop
    # abbreviate parameter names if possible (e.g. rgb = thisBDI_Loop.rgb)
    if thisBDI_Loop != None:
        for paramName in thisBDI_Loop:
            exec('{} = thisBDI_Loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "BDI" ---
    continueRoutine = True
    # update component parameters for each repeat
    BDIQ.setText(BDI_Qest0)
    text_20.setText(BDI_Qest1)
    text_21.setText(BDI_Qest2)
    text_22.setText(BDI_Qest3)
    BDISCORE.keys = []
    BDISCORE.rt = []
    _BDISCORE_allKeys = []
    # keep track of which components have finished
    BDIComponents = [Two_Week, BDIQ, text_20, text_21, text_22, BDISCORE]
    for thisComponent in BDIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BDI" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Two_Week* updates
        
        # if Two_Week is starting this frame...
        if Two_Week.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Two_Week.frameNStart = frameN  # exact frame index
            Two_Week.tStart = t  # local t and not account for scr refresh
            Two_Week.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Two_Week, 'tStartRefresh')  # time at next scr refresh
            # update status
            Two_Week.status = STARTED
            Two_Week.setAutoDraw(True)
        
        # if Two_Week is active this frame...
        if Two_Week.status == STARTED:
            # update params
            pass
        
        # *BDIQ* updates
        
        # if BDIQ is starting this frame...
        if BDIQ.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            BDIQ.frameNStart = frameN  # exact frame index
            BDIQ.tStart = t  # local t and not account for scr refresh
            BDIQ.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BDIQ, 'tStartRefresh')  # time at next scr refresh
            # update status
            BDIQ.status = STARTED
            BDIQ.setAutoDraw(True)
        
        # if BDIQ is active this frame...
        if BDIQ.status == STARTED:
            # update params
            pass
        
        # *text_20* updates
        
        # if text_20 is starting this frame...
        if text_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_20.frameNStart = frameN  # exact frame index
            text_20.tStart = t  # local t and not account for scr refresh
            text_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_20, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_20.status = STARTED
            text_20.setAutoDraw(True)
        
        # if text_20 is active this frame...
        if text_20.status == STARTED:
            # update params
            pass
        
        # *text_21* updates
        
        # if text_21 is starting this frame...
        if text_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_21.frameNStart = frameN  # exact frame index
            text_21.tStart = t  # local t and not account for scr refresh
            text_21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_21, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_21.status = STARTED
            text_21.setAutoDraw(True)
        
        # if text_21 is active this frame...
        if text_21.status == STARTED:
            # update params
            pass
        
        # *text_22* updates
        
        # if text_22 is starting this frame...
        if text_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_22.frameNStart = frameN  # exact frame index
            text_22.tStart = t  # local t and not account for scr refresh
            text_22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_22, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_22.status = STARTED
            text_22.setAutoDraw(True)
        
        # if text_22 is active this frame...
        if text_22.status == STARTED:
            # update params
            pass
        
        # *BDISCORE* updates
        waitOnFlip = False
        
        # if BDISCORE is starting this frame...
        if BDISCORE.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            BDISCORE.frameNStart = frameN  # exact frame index
            BDISCORE.tStart = t  # local t and not account for scr refresh
            BDISCORE.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BDISCORE, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'BDISCORE.started')
            # update status
            BDISCORE.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(BDISCORE.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(BDISCORE.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if BDISCORE.status == STARTED and not waitOnFlip:
            theseKeys = BDISCORE.getKeys(keyList=['0','1','2','3'], waitRelease=False)
            _BDISCORE_allKeys.extend(theseKeys)
            if len(_BDISCORE_allKeys):
                BDISCORE.keys = _BDISCORE_allKeys[-1].name  # just the last key pressed
                BDISCORE.rt = _BDISCORE_allKeys[-1].rt
                BDISCORE.duration = _BDISCORE_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BDIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BDI" ---
    for thisComponent in BDIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_6
    if BDISCORE.keys == '0':
        thisExp.addData('BDIResult',0)
    if BDISCORE.keys == '1':
        thisExp.addData('BDIResult',1)
    if BDISCORE.keys == '2':
        thisExp.addData('BDIResult',2)
    if BDISCORE.keys == '3':
        thisExp.addData('BDIResult',3)
    # Run 'End Routine' code from BDITotter
    if BDISCORE.keys == '0':
        BDIT = (BDIT + 0)
    if BDISCORE.keys == '1':
        BDIT = (BDIT + 1)
    if BDISCORE.keys == '2':
        BDIT = (BDIT + 2)
    if BDISCORE.keys == '3':
        BDIT = (BDIT + 3)
    # Run 'End Routine' code from SubscaleBDI
    if BDISCORE.keys == '0' and factor == 'c':
        Cognitive_Total = (Cognitive_Total + 0)
    if BDISCORE.keys == '1' and factor == 'c':
        Cognitive_Total = (Cognitive_Total + 1)
    if BDISCORE.keys == '2' and factor == 'c':
        Cognitive_Total = (Cognitive_Total + 2)
    if BDISCORE.keys == '3' and factor == 'c':
        Cognitive_Total = (Cognitive_Total + 3)
    if BDISCORE.keys == '0' and factor == 's':
        Somatic_af_Total = (Somatic_af_Total + 0)
    if BDISCORE.keys == '1' and factor == 's':
        Somatic_af_Total = (Somatic_af_Total + 1)
    if BDISCORE.keys == '2' and factor == 's':
        Somatic_af_Total = (Somatic_af_Total + 2)
    if BDISCORE.keys == '3' and factor == 's':
        Somatic_af_Total = (Somatic_af_Total + 3)
    # the Routine "BDI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'BDI_Loop'


# --- Prepare to start Routine "Now_GAD" ---
continueRoutine = True
# update component parameters for each repeat
erespresp.keys = []
erespresp.rt = []
_erespresp_allKeys = []
# keep track of which components have finished
Now_GADComponents = [text_26, erespresp]
for thisComponent in Now_GADComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Now_GAD" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_26* updates
    
    # if text_26 is starting this frame...
    if text_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_26.frameNStart = frameN  # exact frame index
        text_26.tStart = t  # local t and not account for scr refresh
        text_26.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_26, 'tStartRefresh')  # time at next scr refresh
        # update status
        text_26.status = STARTED
        text_26.setAutoDraw(True)
    
    # if text_26 is active this frame...
    if text_26.status == STARTED:
        # update params
        pass
    
    # *erespresp* updates
    waitOnFlip = False
    
    # if erespresp is starting this frame...
    if erespresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        erespresp.frameNStart = frameN  # exact frame index
        erespresp.tStart = t  # local t and not account for scr refresh
        erespresp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(erespresp, 'tStartRefresh')  # time at next scr refresh
        # update status
        erespresp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(erespresp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(erespresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if erespresp.status == STARTED and not waitOnFlip:
        theseKeys = erespresp.getKeys(keyList=['space'], waitRelease=False)
        _erespresp_allKeys.extend(theseKeys)
        if len(_erespresp_allKeys):
            erespresp.keys = _erespresp_allKeys[-1].name  # just the last key pressed
            erespresp.rt = _erespresp_allKeys[-1].rt
            erespresp.duration = _erespresp_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Now_GADComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Now_GAD" ---
for thisComponent in Now_GADComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Now_GAD" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
GAD_Loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('GAD7.xlsx'),
    seed=None, name='GAD_Loop')
thisExp.addLoop(GAD_Loop)  # add the loop to the experiment
thisGAD_Loop = GAD_Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisGAD_Loop.rgb)
if thisGAD_Loop != None:
    for paramName in thisGAD_Loop:
        exec('{} = thisGAD_Loop[paramName]'.format(paramName))

for thisGAD_Loop in GAD_Loop:
    currentLoop = GAD_Loop
    # abbreviate parameter names if possible (e.g. rgb = thisGAD_Loop.rgb)
    if thisGAD_Loop != None:
        for paramName in thisGAD_Loop:
            exec('{} = thisGAD_Loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "GAD7" ---
    continueRoutine = True
    # update component parameters for each repeat
    text_15.setText(QuestionG)
    GAD7SCORE.keys = []
    GAD7SCORE.rt = []
    _GAD7SCORE_allKeys = []
    # keep track of which components have finished
    GAD7Components = [text_14, text_15, text_16, GAD7SCORE]
    for thisComponent in GAD7Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "GAD7" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_14* updates
        
        # if text_14 is starting this frame...
        if text_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_14.frameNStart = frameN  # exact frame index
            text_14.tStart = t  # local t and not account for scr refresh
            text_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_14.status = STARTED
            text_14.setAutoDraw(True)
        
        # if text_14 is active this frame...
        if text_14.status == STARTED:
            # update params
            pass
        
        # *text_15* updates
        
        # if text_15 is starting this frame...
        if text_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_15.frameNStart = frameN  # exact frame index
            text_15.tStart = t  # local t and not account for scr refresh
            text_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_15.status = STARTED
            text_15.setAutoDraw(True)
        
        # if text_15 is active this frame...
        if text_15.status == STARTED:
            # update params
            pass
        
        # *text_16* updates
        
        # if text_16 is starting this frame...
        if text_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_16.frameNStart = frameN  # exact frame index
            text_16.tStart = t  # local t and not account for scr refresh
            text_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_16.status = STARTED
            text_16.setAutoDraw(True)
        
        # if text_16 is active this frame...
        if text_16.status == STARTED:
            # update params
            pass
        
        # *GAD7SCORE* updates
        waitOnFlip = False
        
        # if GAD7SCORE is starting this frame...
        if GAD7SCORE.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            GAD7SCORE.frameNStart = frameN  # exact frame index
            GAD7SCORE.tStart = t  # local t and not account for scr refresh
            GAD7SCORE.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(GAD7SCORE, 'tStartRefresh')  # time at next scr refresh
            # update status
            GAD7SCORE.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(GAD7SCORE.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(GAD7SCORE.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if GAD7SCORE.status == STARTED and not waitOnFlip:
            theseKeys = GAD7SCORE.getKeys(keyList=['0','1','2','3'], waitRelease=False)
            _GAD7SCORE_allKeys.extend(theseKeys)
            if len(_GAD7SCORE_allKeys):
                GAD7SCORE.keys = _GAD7SCORE_allKeys[-1].name  # just the last key pressed
                GAD7SCORE.rt = _GAD7SCORE_allKeys[-1].rt
                GAD7SCORE.duration = _GAD7SCORE_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in GAD7Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "GAD7" ---
    for thisComponent in GAD7Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_7
    if GAD7SCORE.keys == '0':
        thisExp.addData('GAD7Result',0)
    if GAD7SCORE.keys == '1':
        thisExp.addData('GAD7Result',1)
    if GAD7SCORE.keys == '2':
        thisExp.addData('GAD7Result',2)
    if GAD7SCORE.keys == '3':
        thisExp.addData('GAD7Result',3)
    # Run 'End Routine' code from GADTotter
    if GAD7SCORE.keys == '0':
        GADtot = (GADtot + 0)
    if GAD7SCORE.keys == '1':
        GADtot = (GADtot + 1)
    if GAD7SCORE.keys == '2':
        GADtot = (GADtot + 2)
    if GAD7SCORE.keys == '3':
        GADtot = (GADtot + 3)
    # the Routine "GAD7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'GAD_Loop'


# --- Prepare to start Routine "Now_Rumination" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
Now_RuminationComponents = [text_29, key_resp_2]
for thisComponent in Now_RuminationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Now_Rumination" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_29* updates
    
    # if text_29 is starting this frame...
    if text_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_29.frameNStart = frameN  # exact frame index
        text_29.tStart = t  # local t and not account for scr refresh
        text_29.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_29, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_29.started')
        # update status
        text_29.status = STARTED
        text_29.setAutoDraw(True)
    
    # if text_29 is active this frame...
    if text_29.status == STARTED:
        # update params
        pass
    
    # *key_resp_2* updates
    waitOnFlip = False
    
    # if key_resp_2 is starting this frame...
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_2.started')
        # update status
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            key_resp_2.duration = _key_resp_2_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Now_RuminationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Now_Rumination" ---
for thisComponent in Now_RuminationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
    thisExp.addData('key_resp_2.duration', key_resp_2.duration)
thisExp.nextEntry()
# the Routine "Now_Rumination" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
RRS_Loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('RRS.xlsx'),
    seed=None, name='RRS_Loop')
thisExp.addLoop(RRS_Loop)  # add the loop to the experiment
thisRRS_Loop = RRS_Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRRS_Loop.rgb)
if thisRRS_Loop != None:
    for paramName in thisRRS_Loop:
        exec('{} = thisRRS_Loop[paramName]'.format(paramName))

for thisRRS_Loop in RRS_Loop:
    currentLoop = RRS_Loop
    # abbreviate parameter names if possible (e.g. rgb = thisRRS_Loop.rgb)
    if thisRRS_Loop != None:
        for paramName in thisRRS_Loop:
            exec('{} = thisRRS_Loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "RSS" ---
    continueRoutine = True
    # update component parameters for each repeat
    text_18.setText(RRSQ)
    RRSANSWER.keys = []
    RRSANSWER.rt = []
    _RRSANSWER_allKeys = []
    # keep track of which components have finished
    RSSComponents = [text_17, text_18, text_19, RRSANSWER]
    for thisComponent in RSSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "RSS" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_17* updates
        
        # if text_17 is starting this frame...
        if text_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_17.frameNStart = frameN  # exact frame index
            text_17.tStart = t  # local t and not account for scr refresh
            text_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_17.status = STARTED
            text_17.setAutoDraw(True)
        
        # if text_17 is active this frame...
        if text_17.status == STARTED:
            # update params
            pass
        
        # *text_18* updates
        
        # if text_18 is starting this frame...
        if text_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_18.frameNStart = frameN  # exact frame index
            text_18.tStart = t  # local t and not account for scr refresh
            text_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_18, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_18.status = STARTED
            text_18.setAutoDraw(True)
        
        # if text_18 is active this frame...
        if text_18.status == STARTED:
            # update params
            pass
        
        # *text_19* updates
        
        # if text_19 is starting this frame...
        if text_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_19.frameNStart = frameN  # exact frame index
            text_19.tStart = t  # local t and not account for scr refresh
            text_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_19, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_19.status = STARTED
            text_19.setAutoDraw(True)
        
        # if text_19 is active this frame...
        if text_19.status == STARTED:
            # update params
            pass
        
        # *RRSANSWER* updates
        waitOnFlip = False
        
        # if RRSANSWER is starting this frame...
        if RRSANSWER.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RRSANSWER.frameNStart = frameN  # exact frame index
            RRSANSWER.tStart = t  # local t and not account for scr refresh
            RRSANSWER.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RRSANSWER, 'tStartRefresh')  # time at next scr refresh
            # update status
            RRSANSWER.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(RRSANSWER.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(RRSANSWER.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if RRSANSWER.status == STARTED and not waitOnFlip:
            theseKeys = RRSANSWER.getKeys(keyList=['1','2','3','4'], waitRelease=False)
            _RRSANSWER_allKeys.extend(theseKeys)
            if len(_RRSANSWER_allKeys):
                RRSANSWER.keys = _RRSANSWER_allKeys[-1].name  # just the last key pressed
                RRSANSWER.rt = _RRSANSWER_allKeys[-1].rt
                RRSANSWER.duration = _RRSANSWER_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RSSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "RSS" ---
    for thisComponent in RSSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_8
    if RRSANSWER.keys == '1':
        thisExp.addData('RRSResult',1)
    if RRSANSWER.keys == '2':
        thisExp.addData('RRSResult',2)
    if RRSANSWER.keys == '3':
        thisExp.addData('RRSResult',3)
    if RRSANSWER.keys == '4':
        thisExp.addData('RRSResult',4)
    # Run 'End Routine' code from code_30
    if RRSANSWER.keys == '1':
        RRStot = (RRStot + 1)
    if RRSANSWER.keys == '2':
        RRStot = (RRStot + 2)
    if RRSANSWER.keys == '3':
        RRStot = (RRStot + 3)
    if RRSANSWER.keys == '4':
        RRStot = (RRStot + 4)
    # the Routine "RSS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'RRS_Loop'


# --- Prepare to start Routine "Ethical_Text" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_54.keys = []
key_resp_54.rt = []
_key_resp_54_allKeys = []
# keep track of which components have finished
Ethical_TextComponents = [text_129, key_resp_54]
for thisComponent in Ethical_TextComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Ethical_Text" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_129* updates
    
    # if text_129 is starting this frame...
    if text_129.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_129.frameNStart = frameN  # exact frame index
        text_129.tStart = t  # local t and not account for scr refresh
        text_129.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_129, 'tStartRefresh')  # time at next scr refresh
        # update status
        text_129.status = STARTED
        text_129.setAutoDraw(True)
    
    # if text_129 is active this frame...
    if text_129.status == STARTED:
        # update params
        pass
    
    # *key_resp_54* updates
    waitOnFlip = False
    
    # if key_resp_54 is starting this frame...
    if key_resp_54.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_54.frameNStart = frameN  # exact frame index
        key_resp_54.tStart = t  # local t and not account for scr refresh
        key_resp_54.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_54, 'tStartRefresh')  # time at next scr refresh
        # update status
        key_resp_54.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_54.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_54.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_54.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_54.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_54_allKeys.extend(theseKeys)
        if len(_key_resp_54_allKeys):
            key_resp_54.keys = _key_resp_54_allKeys[-1].name  # just the last key pressed
            key_resp_54.rt = _key_resp_54_allKeys[-1].rt
            key_resp_54.duration = _key_resp_54_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Ethical_TextComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Ethical_Text" ---
for thisComponent in Ethical_TextComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_54.keys in ['', [], None]:  # No response was made
    key_resp_54.keys = None
thisExp.addData('key_resp_54.keys',key_resp_54.keys)
if key_resp_54.keys != None:  # we had a response
    thisExp.addData('key_resp_54.rt', key_resp_54.rt)
    thisExp.addData('key_resp_54.duration', key_resp_54.duration)
thisExp.nextEntry()
# the Routine "Ethical_Text" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "GMBM_Explain" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_17.keys = []
key_resp_17.rt = []
_key_resp_17_allKeys = []
# Run 'Begin Routine' code from GMBM

ShapeSelector = random.randint(0, 23)




if ShapeSelector == 0:
    meshape = 'images/Circle.png'
    othershape = 'images/Diamond.png'
    Left1 = 'Match'
    Right1 = 'Mismatch'
    prac = 'Pracloop1.xlsx'
    Xenia = 'S1.csv'

if ShapeSelector == 1:
    meshape = 'images/Circle.png'
    othershape = 'images/Diamond.png'
    Left1 = 'Mismatch'
    Right1 = 'Match'
    prac = 'Pracloop2.xlsx'
    Xenia = 'S2.csv'

if ShapeSelector == 2:
    meshape = 'images/Circle.png'
    othershape = 'images/Star.png'
    Left1 = 'Match'
    Right1 = 'Mismatch'
    prac = 'Pracloop3.xlsx'
    Xenia = 'S3.csv'

if ShapeSelector == 3:
    meshape = 'images/Circle.png'
    othershape = 'images/Star.png'
    Left1 = 'Mismatch'
    Right1 = 'Match'
    prac = 'Pracloop4.xlsx'
    Xenia = 'S4.csv'

if ShapeSelector == 4:
    meshape = 'images/Circle.png'
    othershape = 'images/Triangle.png'
    Left1 = 'Match'
    Right1 = 'Mismatch'
    prac = 'Pracloop5.xlsx'
    Xenia = 'S5.csv'

if ShapeSelector == 5:
    meshape = 'images/Circle.png'
    othershape = 'images/Triangle.png'
    Left1 = 'Mismatch'
    Right1 = 'Match'
    prac = 'Pracloop6.xlsx'
    Xenia = 'S6.csv'

if ShapeSelector == 6:
    meshape = 'images/Diamond.png'
    othershape = 'images/Circle.png'
    Left1 = 'Match'
    Right1 = 'Mismatch'
    prac = 'Pracloop7.xlsx'
    Xenia = 'S7.csv'

if ShapeSelector == 7:
    meshape = 'images/Diamond.png'
    othershape = 'images/Circle.png'
    Left1 = 'Mismatch'
    Right1 = 'Match'
    prac = 'Pracloop8.xlsx'
    Xenia = 'S8.csv'

if ShapeSelector == 8:
    meshape = 'images/Diamond.png'
    othershape = 'images/Star.png'
    Left1 = 'Match'
    Right1 = 'Mismatch'
    prac = 'Pracloop9.xlsx'
    Xenia = 'S9.csv'

if ShapeSelector == 9:
    meshape = 'images/Diamond.png'
    othershape = 'images/Star.png'
    Left1 = 'Mismatch'
    Right1 = 'Match'
    prac = 'Pracloop10.xlsx'
    Xenia = 'S10.csv'

if ShapeSelector == 10:
    meshape = 'images/Diamond.png'
    othershape = 'images/Triangle.png'
    Left1 = 'Match'
    Right1 = 'Mismatch'
    prac = 'Pracloop11.xlsx'
    Xenia = 'S11.csv'

if ShapeSelector == 11:
    meshape = 'images/Diamond.png'
    othershape = 'images/Triangle.png'
    Left1 = 'Mismatch'
    Right1 = 'Match'
    prac = 'Pracloop12.xlsx'
    Xenia = 'S12.csv'

if ShapeSelector == 12:
    meshape = 'images/Star.png'
    othershape = 'images/Circle.png'
    Left1 = 'Match'
    Right1 = 'Mismatch'
    prac = 'Pracloop13.xlsx'
    Xenia = 'S13.csv'

if ShapeSelector == 13:
    meshape = 'images/Star.png'
    othershape = 'images/Circle.png'
    Left1 = 'Mismatch'
    Right1 = 'Match'
    prac = 'Pracloop14.xlsx'
    Xenia = 'S14.csv'

if ShapeSelector == 14:
    meshape = 'images/Star.png'
    othershape = 'images/Diamond.png'
    Left1 = 'Match'
    Right1 = 'Mismatch'
    prac = 'Pracloop15.xlsx'
    Xenia = 'S15.csv'

if ShapeSelector == 15:
    meshape = 'images/Star.png'
    othershape = 'images/Diamond.png'
    Left1 = 'Mismatch'
    Right1 = 'Match'
    prac = 'Pracloop16.xlsx'
    Xenia = 'S16.csv'

if ShapeSelector == 16:
    meshape = 'images/Star.png'
    othershape = 'images/Triangle.png'
    Left1 = 'Match'
    Right1 = 'Mismatch'
    prac = 'Pracloop17.xlsx'
    Xenia = 'S17.csv'

if ShapeSelector == 17:
    meshape = 'images/Star.png'
    othershape = 'images/Triangle.png'
    Left1 = 'Mismatch'
    Right1 = 'Match'
    prac = 'Pracloop18.xlsx'
    Xenia = 'S18.csv'

if ShapeSelector == 18:
    meshape = 'images/Triangle.png'
    othershape = 'images/Circle.png'
    Left1 = 'Match'
    Right1 = 'Mismatch'
    prac = 'Pracloop19.xlsx'
    Xenia = 'S19.csv'

if ShapeSelector == 19:
    meshape = 'images/Triangle.png'
    othershape = 'images/Circle.png'
    Left1 = 'Mismatch'
    Right1 = 'Match'
    prac = 'Pracloop20.xlsx'
    Xenia = 'S20.csv'

if ShapeSelector == 20:
    meshape = 'images/Triangle.png'
    othershape = 'images/Diamond.png'
    Left1 = 'Match'
    Right1 = 'Mismatch'
    prac = 'Pracloop21.xlsx'
    Xenia = 'S21.csv'

if ShapeSelector == 21:
    meshape = 'images/Triangle.png'
    othershape = 'images/Diamond.png'
    Left1 = 'Mismatch'
    Right1 = 'Match'
    prac = 'Pracloop22.xlsx'
    Xenia = 'S22.csv'

if ShapeSelector == 22:
    meshape = 'images/Triangle.png'
    othershape = 'images/Star.png'
    Left1 = 'Match'
    Right1 = 'Mismatch'
    prac = 'Pracloop23.xlsx'
    Xenia = 'S23.csv'

if ShapeSelector == 23:
    meshape = 'images/Triangle.png'
    othershape = 'images/Star.png'
    Left1 = 'Mismatch'
    Right1 = 'Match'
    prac = 'Pracloop24.xlsx'
    Xenia = 'S24.csv'

# keep track of which components have finished
GMBM_ExplainComponents = [GoodMeBadMeText, key_resp_17]
for thisComponent in GMBM_ExplainComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "GMBM_Explain" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *GoodMeBadMeText* updates
    
    # if GoodMeBadMeText is starting this frame...
    if GoodMeBadMeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        GoodMeBadMeText.frameNStart = frameN  # exact frame index
        GoodMeBadMeText.tStart = t  # local t and not account for scr refresh
        GoodMeBadMeText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GoodMeBadMeText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'GoodMeBadMeText.started')
        # update status
        GoodMeBadMeText.status = STARTED
        GoodMeBadMeText.setAutoDraw(True)
    
    # if GoodMeBadMeText is active this frame...
    if GoodMeBadMeText.status == STARTED:
        # update params
        pass
    
    # *key_resp_17* updates
    waitOnFlip = False
    
    # if key_resp_17 is starting this frame...
    if key_resp_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_17.frameNStart = frameN  # exact frame index
        key_resp_17.tStart = t  # local t and not account for scr refresh
        key_resp_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_17, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_17.started')
        # update status
        key_resp_17.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_17.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_17.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_17.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_17.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_17_allKeys.extend(theseKeys)
        if len(_key_resp_17_allKeys):
            key_resp_17.keys = _key_resp_17_allKeys[-1].name  # just the last key pressed
            key_resp_17.rt = _key_resp_17_allKeys[-1].rt
            key_resp_17.duration = _key_resp_17_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GMBM_ExplainComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "GMBM_Explain" ---
for thisComponent in GMBM_ExplainComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_17.keys in ['', [], None]:  # No response was made
    key_resp_17.keys = None
thisExp.addData('key_resp_17.keys',key_resp_17.keys)
if key_resp_17.keys != None:  # we had a response
    thisExp.addData('key_resp_17.rt', key_resp_17.rt)
    thisExp.addData('key_resp_17.duration', key_resp_17.duration)
thisExp.nextEntry()
# Run 'End Routine' code from CB_attrib
if Left1 == 'Match':
    HANDED2 = "Standard"

if Left1 == 'Mismatch':
    HANDED2 = "Flipped"

thisExp.addData('GMBM_Set',ShapeSelector)

thisExp.addData('Buttons',HANDED2)
# the Routine "GMBM_Explain" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "NomenAssoc" ---
continueRoutine = True
# update component parameters for each repeat
image_7.setImage(othershape)
text_47.setText('= Stranger')
key_resp_23.keys = []
key_resp_23.rt = []
_key_resp_23_allKeys = []
# keep track of which components have finished
NomenAssocComponents = [image_7, text_47, key_resp_23, text_49]
for thisComponent in NomenAssocComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "NomenAssoc" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_7* updates
    
    # if image_7 is starting this frame...
    if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_7.frameNStart = frameN  # exact frame index
        image_7.tStart = t  # local t and not account for scr refresh
        image_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_7.started')
        # update status
        image_7.status = STARTED
        image_7.setAutoDraw(True)
    
    # if image_7 is active this frame...
    if image_7.status == STARTED:
        # update params
        pass
    
    # *text_47* updates
    
    # if text_47 is starting this frame...
    if text_47.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_47.frameNStart = frameN  # exact frame index
        text_47.tStart = t  # local t and not account for scr refresh
        text_47.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_47, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_47.started')
        # update status
        text_47.status = STARTED
        text_47.setAutoDraw(True)
    
    # if text_47 is active this frame...
    if text_47.status == STARTED:
        # update params
        pass
    
    # *key_resp_23* updates
    waitOnFlip = False
    
    # if key_resp_23 is starting this frame...
    if key_resp_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_23.frameNStart = frameN  # exact frame index
        key_resp_23.tStart = t  # local t and not account for scr refresh
        key_resp_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_23, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_23.started')
        # update status
        key_resp_23.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_23.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_23.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_23.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_23.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_23_allKeys.extend(theseKeys)
        if len(_key_resp_23_allKeys):
            key_resp_23.keys = _key_resp_23_allKeys[-1].name  # just the last key pressed
            key_resp_23.rt = _key_resp_23_allKeys[-1].rt
            key_resp_23.duration = _key_resp_23_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # *text_49* updates
    
    # if text_49 is starting this frame...
    if text_49.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_49.frameNStart = frameN  # exact frame index
        text_49.tStart = t  # local t and not account for scr refresh
        text_49.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_49, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_49.started')
        # update status
        text_49.status = STARTED
        text_49.setAutoDraw(True)
    
    # if text_49 is active this frame...
    if text_49.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in NomenAssocComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "NomenAssoc" ---
for thisComponent in NomenAssocComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_23.keys in ['', [], None]:  # No response was made
    key_resp_23.keys = None
thisExp.addData('key_resp_23.keys',key_resp_23.keys)
if key_resp_23.keys != None:  # we had a response
    thisExp.addData('key_resp_23.rt', key_resp_23.rt)
    thisExp.addData('key_resp_23.duration', key_resp_23.duration)
thisExp.nextEntry()
# the Routine "NomenAssoc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "MeAssoc" ---
continueRoutine = True
# update component parameters for each repeat
image_13.setImage(meshape)
key_resp_24.keys = []
key_resp_24.rt = []
_key_resp_24_allKeys = []
# keep track of which components have finished
MeAssocComponents = [image_13, text_50, key_resp_24, text_52]
for thisComponent in MeAssocComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "MeAssoc" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_13* updates
    
    # if image_13 is starting this frame...
    if image_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_13.frameNStart = frameN  # exact frame index
        image_13.tStart = t  # local t and not account for scr refresh
        image_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_13.started')
        # update status
        image_13.status = STARTED
        image_13.setAutoDraw(True)
    
    # if image_13 is active this frame...
    if image_13.status == STARTED:
        # update params
        pass
    
    # *text_50* updates
    
    # if text_50 is starting this frame...
    if text_50.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_50.frameNStart = frameN  # exact frame index
        text_50.tStart = t  # local t and not account for scr refresh
        text_50.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_50, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_50.started')
        # update status
        text_50.status = STARTED
        text_50.setAutoDraw(True)
    
    # if text_50 is active this frame...
    if text_50.status == STARTED:
        # update params
        pass
    
    # *key_resp_24* updates
    waitOnFlip = False
    
    # if key_resp_24 is starting this frame...
    if key_resp_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_24.frameNStart = frameN  # exact frame index
        key_resp_24.tStart = t  # local t and not account for scr refresh
        key_resp_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_24, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_24.started')
        # update status
        key_resp_24.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_24.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_24.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_24.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_24.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_24_allKeys.extend(theseKeys)
        if len(_key_resp_24_allKeys):
            key_resp_24.keys = _key_resp_24_allKeys[-1].name  # just the last key pressed
            key_resp_24.rt = _key_resp_24_allKeys[-1].rt
            key_resp_24.duration = _key_resp_24_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # *text_52* updates
    
    # if text_52 is starting this frame...
    if text_52.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_52.frameNStart = frameN  # exact frame index
        text_52.tStart = t  # local t and not account for scr refresh
        text_52.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_52, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_52.started')
        # update status
        text_52.status = STARTED
        text_52.setAutoDraw(True)
    
    # if text_52 is active this frame...
    if text_52.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MeAssocComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "MeAssoc" ---
for thisComponent in MeAssocComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_24.keys in ['', [], None]:  # No response was made
    key_resp_24.keys = None
thisExp.addData('key_resp_24.keys',key_resp_24.keys)
if key_resp_24.keys != None:  # we had a response
    thisExp.addData('key_resp_24.rt', key_resp_24.rt)
    thisExp.addData('key_resp_24.duration', key_resp_24.duration)
thisExp.nextEntry()
# the Routine "MeAssoc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "PracticeGoodText" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_25.keys = []
key_resp_25.rt = []
_key_resp_25_allKeys = []
# keep track of which components have finished
PracticeGoodTextComponents = [text_37, key_resp_25]
for thisComponent in PracticeGoodTextComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "PracticeGoodText" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_37* updates
    
    # if text_37 is starting this frame...
    if text_37.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_37.frameNStart = frameN  # exact frame index
        text_37.tStart = t  # local t and not account for scr refresh
        text_37.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_37, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_37.started')
        # update status
        text_37.status = STARTED
        text_37.setAutoDraw(True)
    
    # if text_37 is active this frame...
    if text_37.status == STARTED:
        # update params
        pass
    
    # *key_resp_25* updates
    waitOnFlip = False
    
    # if key_resp_25 is starting this frame...
    if key_resp_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_25.frameNStart = frameN  # exact frame index
        key_resp_25.tStart = t  # local t and not account for scr refresh
        key_resp_25.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_25, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_25.started')
        # update status
        key_resp_25.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_25.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_25.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_25.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_25.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_25_allKeys.extend(theseKeys)
        if len(_key_resp_25_allKeys):
            key_resp_25.keys = _key_resp_25_allKeys[-1].name  # just the last key pressed
            key_resp_25.rt = _key_resp_25_allKeys[-1].rt
            key_resp_25.duration = _key_resp_25_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PracticeGoodTextComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "PracticeGoodText" ---
for thisComponent in PracticeGoodTextComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_25.keys in ['', [], None]:  # No response was made
    key_resp_25.keys = None
thisExp.addData('key_resp_25.keys',key_resp_25.keys)
if key_resp_25.keys != None:  # we had a response
    thisExp.addData('key_resp_25.rt', key_resp_25.rt)
    thisExp.addData('key_resp_25.duration', key_resp_25.duration)
thisExp.nextEntry()
# the Routine "PracticeGoodText" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "MeAssoc" ---
continueRoutine = True
# update component parameters for each repeat
image_13.setImage(meshape)
key_resp_24.keys = []
key_resp_24.rt = []
_key_resp_24_allKeys = []
# keep track of which components have finished
MeAssocComponents = [image_13, text_50, key_resp_24, text_52]
for thisComponent in MeAssocComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "MeAssoc" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_13* updates
    
    # if image_13 is starting this frame...
    if image_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_13.frameNStart = frameN  # exact frame index
        image_13.tStart = t  # local t and not account for scr refresh
        image_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_13.started')
        # update status
        image_13.status = STARTED
        image_13.setAutoDraw(True)
    
    # if image_13 is active this frame...
    if image_13.status == STARTED:
        # update params
        pass
    
    # *text_50* updates
    
    # if text_50 is starting this frame...
    if text_50.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_50.frameNStart = frameN  # exact frame index
        text_50.tStart = t  # local t and not account for scr refresh
        text_50.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_50, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_50.started')
        # update status
        text_50.status = STARTED
        text_50.setAutoDraw(True)
    
    # if text_50 is active this frame...
    if text_50.status == STARTED:
        # update params
        pass
    
    # *key_resp_24* updates
    waitOnFlip = False
    
    # if key_resp_24 is starting this frame...
    if key_resp_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_24.frameNStart = frameN  # exact frame index
        key_resp_24.tStart = t  # local t and not account for scr refresh
        key_resp_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_24, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_24.started')
        # update status
        key_resp_24.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_24.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_24.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_24.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_24.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_24_allKeys.extend(theseKeys)
        if len(_key_resp_24_allKeys):
            key_resp_24.keys = _key_resp_24_allKeys[-1].name  # just the last key pressed
            key_resp_24.rt = _key_resp_24_allKeys[-1].rt
            key_resp_24.duration = _key_resp_24_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # *text_52* updates
    
    # if text_52 is starting this frame...
    if text_52.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_52.frameNStart = frameN  # exact frame index
        text_52.tStart = t  # local t and not account for scr refresh
        text_52.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_52, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_52.started')
        # update status
        text_52.status = STARTED
        text_52.setAutoDraw(True)
    
    # if text_52 is active this frame...
    if text_52.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MeAssocComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "MeAssoc" ---
for thisComponent in MeAssocComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_24.keys in ['', [], None]:  # No response was made
    key_resp_24.keys = None
thisExp.addData('key_resp_24.keys',key_resp_24.keys)
if key_resp_24.keys != None:  # we had a response
    thisExp.addData('key_resp_24.rt', key_resp_24.rt)
    thisExp.addData('key_resp_24.duration', key_resp_24.duration)
thisExp.nextEntry()
# the Routine "MeAssoc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "NomenAssoc" ---
continueRoutine = True
# update component parameters for each repeat
image_7.setImage(othershape)
text_47.setText('= Stranger')
key_resp_23.keys = []
key_resp_23.rt = []
_key_resp_23_allKeys = []
# keep track of which components have finished
NomenAssocComponents = [image_7, text_47, key_resp_23, text_49]
for thisComponent in NomenAssocComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "NomenAssoc" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_7* updates
    
    # if image_7 is starting this frame...
    if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_7.frameNStart = frameN  # exact frame index
        image_7.tStart = t  # local t and not account for scr refresh
        image_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_7.started')
        # update status
        image_7.status = STARTED
        image_7.setAutoDraw(True)
    
    # if image_7 is active this frame...
    if image_7.status == STARTED:
        # update params
        pass
    
    # *text_47* updates
    
    # if text_47 is starting this frame...
    if text_47.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_47.frameNStart = frameN  # exact frame index
        text_47.tStart = t  # local t and not account for scr refresh
        text_47.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_47, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_47.started')
        # update status
        text_47.status = STARTED
        text_47.setAutoDraw(True)
    
    # if text_47 is active this frame...
    if text_47.status == STARTED:
        # update params
        pass
    
    # *key_resp_23* updates
    waitOnFlip = False
    
    # if key_resp_23 is starting this frame...
    if key_resp_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_23.frameNStart = frameN  # exact frame index
        key_resp_23.tStart = t  # local t and not account for scr refresh
        key_resp_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_23, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_23.started')
        # update status
        key_resp_23.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_23.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_23.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_23.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_23.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_23_allKeys.extend(theseKeys)
        if len(_key_resp_23_allKeys):
            key_resp_23.keys = _key_resp_23_allKeys[-1].name  # just the last key pressed
            key_resp_23.rt = _key_resp_23_allKeys[-1].rt
            key_resp_23.duration = _key_resp_23_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # *text_49* updates
    
    # if text_49 is starting this frame...
    if text_49.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_49.frameNStart = frameN  # exact frame index
        text_49.tStart = t  # local t and not account for scr refresh
        text_49.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_49, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_49.started')
        # update status
        text_49.status = STARTED
        text_49.setAutoDraw(True)
    
    # if text_49 is active this frame...
    if text_49.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in NomenAssocComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "NomenAssoc" ---
for thisComponent in NomenAssocComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_23.keys in ['', [], None]:  # No response was made
    key_resp_23.keys = None
thisExp.addData('key_resp_23.keys',key_resp_23.keys)
if key_resp_23.keys != None:  # we had a response
    thisExp.addData('key_resp_23.rt', key_resp_23.rt)
    thisExp.addData('key_resp_23.duration', key_resp_23.duration)
thisExp.nextEntry()
# the Routine "NomenAssoc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "MeAssoc" ---
continueRoutine = True
# update component parameters for each repeat
image_13.setImage(meshape)
key_resp_24.keys = []
key_resp_24.rt = []
_key_resp_24_allKeys = []
# keep track of which components have finished
MeAssocComponents = [image_13, text_50, key_resp_24, text_52]
for thisComponent in MeAssocComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "MeAssoc" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_13* updates
    
    # if image_13 is starting this frame...
    if image_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_13.frameNStart = frameN  # exact frame index
        image_13.tStart = t  # local t and not account for scr refresh
        image_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_13.started')
        # update status
        image_13.status = STARTED
        image_13.setAutoDraw(True)
    
    # if image_13 is active this frame...
    if image_13.status == STARTED:
        # update params
        pass
    
    # *text_50* updates
    
    # if text_50 is starting this frame...
    if text_50.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_50.frameNStart = frameN  # exact frame index
        text_50.tStart = t  # local t and not account for scr refresh
        text_50.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_50, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_50.started')
        # update status
        text_50.status = STARTED
        text_50.setAutoDraw(True)
    
    # if text_50 is active this frame...
    if text_50.status == STARTED:
        # update params
        pass
    
    # *key_resp_24* updates
    waitOnFlip = False
    
    # if key_resp_24 is starting this frame...
    if key_resp_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_24.frameNStart = frameN  # exact frame index
        key_resp_24.tStart = t  # local t and not account for scr refresh
        key_resp_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_24, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_24.started')
        # update status
        key_resp_24.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_24.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_24.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_24.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_24.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_24_allKeys.extend(theseKeys)
        if len(_key_resp_24_allKeys):
            key_resp_24.keys = _key_resp_24_allKeys[-1].name  # just the last key pressed
            key_resp_24.rt = _key_resp_24_allKeys[-1].rt
            key_resp_24.duration = _key_resp_24_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # *text_52* updates
    
    # if text_52 is starting this frame...
    if text_52.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_52.frameNStart = frameN  # exact frame index
        text_52.tStart = t  # local t and not account for scr refresh
        text_52.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_52, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_52.started')
        # update status
        text_52.status = STARTED
        text_52.setAutoDraw(True)
    
    # if text_52 is active this frame...
    if text_52.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MeAssocComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "MeAssoc" ---
for thisComponent in MeAssocComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_24.keys in ['', [], None]:  # No response was made
    key_resp_24.keys = None
thisExp.addData('key_resp_24.keys',key_resp_24.keys)
if key_resp_24.keys != None:  # we had a response
    thisExp.addData('key_resp_24.rt', key_resp_24.rt)
    thisExp.addData('key_resp_24.duration', key_resp_24.duration)
thisExp.nextEntry()
# the Routine "MeAssoc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "NomenAssoc" ---
continueRoutine = True
# update component parameters for each repeat
image_7.setImage(othershape)
text_47.setText('= Stranger')
key_resp_23.keys = []
key_resp_23.rt = []
_key_resp_23_allKeys = []
# keep track of which components have finished
NomenAssocComponents = [image_7, text_47, key_resp_23, text_49]
for thisComponent in NomenAssocComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "NomenAssoc" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_7* updates
    
    # if image_7 is starting this frame...
    if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_7.frameNStart = frameN  # exact frame index
        image_7.tStart = t  # local t and not account for scr refresh
        image_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_7.started')
        # update status
        image_7.status = STARTED
        image_7.setAutoDraw(True)
    
    # if image_7 is active this frame...
    if image_7.status == STARTED:
        # update params
        pass
    
    # *text_47* updates
    
    # if text_47 is starting this frame...
    if text_47.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_47.frameNStart = frameN  # exact frame index
        text_47.tStart = t  # local t and not account for scr refresh
        text_47.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_47, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_47.started')
        # update status
        text_47.status = STARTED
        text_47.setAutoDraw(True)
    
    # if text_47 is active this frame...
    if text_47.status == STARTED:
        # update params
        pass
    
    # *key_resp_23* updates
    waitOnFlip = False
    
    # if key_resp_23 is starting this frame...
    if key_resp_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_23.frameNStart = frameN  # exact frame index
        key_resp_23.tStart = t  # local t and not account for scr refresh
        key_resp_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_23, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_23.started')
        # update status
        key_resp_23.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_23.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_23.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_23.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_23.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_23_allKeys.extend(theseKeys)
        if len(_key_resp_23_allKeys):
            key_resp_23.keys = _key_resp_23_allKeys[-1].name  # just the last key pressed
            key_resp_23.rt = _key_resp_23_allKeys[-1].rt
            key_resp_23.duration = _key_resp_23_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # *text_49* updates
    
    # if text_49 is starting this frame...
    if text_49.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_49.frameNStart = frameN  # exact frame index
        text_49.tStart = t  # local t and not account for scr refresh
        text_49.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_49, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_49.started')
        # update status
        text_49.status = STARTED
        text_49.setAutoDraw(True)
    
    # if text_49 is active this frame...
    if text_49.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in NomenAssocComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "NomenAssoc" ---
for thisComponent in NomenAssocComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_23.keys in ['', [], None]:  # No response was made
    key_resp_23.keys = None
thisExp.addData('key_resp_23.keys',key_resp_23.keys)
if key_resp_23.keys != None:  # we had a response
    thisExp.addData('key_resp_23.rt', key_resp_23.rt)
    thisExp.addData('key_resp_23.duration', key_resp_23.duration)
thisExp.nextEntry()
# the Routine "NomenAssoc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "MeAssoc" ---
continueRoutine = True
# update component parameters for each repeat
image_13.setImage(meshape)
key_resp_24.keys = []
key_resp_24.rt = []
_key_resp_24_allKeys = []
# keep track of which components have finished
MeAssocComponents = [image_13, text_50, key_resp_24, text_52]
for thisComponent in MeAssocComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "MeAssoc" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_13* updates
    
    # if image_13 is starting this frame...
    if image_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_13.frameNStart = frameN  # exact frame index
        image_13.tStart = t  # local t and not account for scr refresh
        image_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_13.started')
        # update status
        image_13.status = STARTED
        image_13.setAutoDraw(True)
    
    # if image_13 is active this frame...
    if image_13.status == STARTED:
        # update params
        pass
    
    # *text_50* updates
    
    # if text_50 is starting this frame...
    if text_50.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_50.frameNStart = frameN  # exact frame index
        text_50.tStart = t  # local t and not account for scr refresh
        text_50.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_50, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_50.started')
        # update status
        text_50.status = STARTED
        text_50.setAutoDraw(True)
    
    # if text_50 is active this frame...
    if text_50.status == STARTED:
        # update params
        pass
    
    # *key_resp_24* updates
    waitOnFlip = False
    
    # if key_resp_24 is starting this frame...
    if key_resp_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_24.frameNStart = frameN  # exact frame index
        key_resp_24.tStart = t  # local t and not account for scr refresh
        key_resp_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_24, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_24.started')
        # update status
        key_resp_24.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_24.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_24.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_24.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_24.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_24_allKeys.extend(theseKeys)
        if len(_key_resp_24_allKeys):
            key_resp_24.keys = _key_resp_24_allKeys[-1].name  # just the last key pressed
            key_resp_24.rt = _key_resp_24_allKeys[-1].rt
            key_resp_24.duration = _key_resp_24_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # *text_52* updates
    
    # if text_52 is starting this frame...
    if text_52.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_52.frameNStart = frameN  # exact frame index
        text_52.tStart = t  # local t and not account for scr refresh
        text_52.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_52, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_52.started')
        # update status
        text_52.status = STARTED
        text_52.setAutoDraw(True)
    
    # if text_52 is active this frame...
    if text_52.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MeAssocComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "MeAssoc" ---
for thisComponent in MeAssocComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_24.keys in ['', [], None]:  # No response was made
    key_resp_24.keys = None
thisExp.addData('key_resp_24.keys',key_resp_24.keys)
if key_resp_24.keys != None:  # we had a response
    thisExp.addData('key_resp_24.rt', key_resp_24.rt)
    thisExp.addData('key_resp_24.duration', key_resp_24.duration)
thisExp.nextEntry()
# the Routine "MeAssoc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "NomenAssoc" ---
continueRoutine = True
# update component parameters for each repeat
image_7.setImage(othershape)
text_47.setText('= Stranger')
key_resp_23.keys = []
key_resp_23.rt = []
_key_resp_23_allKeys = []
# keep track of which components have finished
NomenAssocComponents = [image_7, text_47, key_resp_23, text_49]
for thisComponent in NomenAssocComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "NomenAssoc" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_7* updates
    
    # if image_7 is starting this frame...
    if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_7.frameNStart = frameN  # exact frame index
        image_7.tStart = t  # local t and not account for scr refresh
        image_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_7.started')
        # update status
        image_7.status = STARTED
        image_7.setAutoDraw(True)
    
    # if image_7 is active this frame...
    if image_7.status == STARTED:
        # update params
        pass
    
    # *text_47* updates
    
    # if text_47 is starting this frame...
    if text_47.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_47.frameNStart = frameN  # exact frame index
        text_47.tStart = t  # local t and not account for scr refresh
        text_47.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_47, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_47.started')
        # update status
        text_47.status = STARTED
        text_47.setAutoDraw(True)
    
    # if text_47 is active this frame...
    if text_47.status == STARTED:
        # update params
        pass
    
    # *key_resp_23* updates
    waitOnFlip = False
    
    # if key_resp_23 is starting this frame...
    if key_resp_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_23.frameNStart = frameN  # exact frame index
        key_resp_23.tStart = t  # local t and not account for scr refresh
        key_resp_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_23, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_23.started')
        # update status
        key_resp_23.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_23.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_23.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_23.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_23.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_23_allKeys.extend(theseKeys)
        if len(_key_resp_23_allKeys):
            key_resp_23.keys = _key_resp_23_allKeys[-1].name  # just the last key pressed
            key_resp_23.rt = _key_resp_23_allKeys[-1].rt
            key_resp_23.duration = _key_resp_23_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # *text_49* updates
    
    # if text_49 is starting this frame...
    if text_49.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_49.frameNStart = frameN  # exact frame index
        text_49.tStart = t  # local t and not account for scr refresh
        text_49.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_49, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_49.started')
        # update status
        text_49.status = STARTED
        text_49.setAutoDraw(True)
    
    # if text_49 is active this frame...
    if text_49.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in NomenAssocComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "NomenAssoc" ---
for thisComponent in NomenAssocComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_23.keys in ['', [], None]:  # No response was made
    key_resp_23.keys = None
thisExp.addData('key_resp_23.keys',key_resp_23.keys)
if key_resp_23.keys != None:  # we had a response
    thisExp.addData('key_resp_23.rt', key_resp_23.rt)
    thisExp.addData('key_resp_23.duration', key_resp_23.duration)
thisExp.nextEntry()
# the Routine "NomenAssoc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "TASK_INSTRUCTIONS9" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from code_35
if Left1 == 'Match':
    Instext2 = "Your task is to judge whether the shape and the person match in each display\n Press 'X' if the shape and person match\n Press 'Y' if the shape and the person do not match.\n Please respond AS QUICKLY AND ACCURATELY AS POSSIBLE\n SPACE to start"

if Left1 == 'Mismatch':
    Instext2 = "Your task is to judge whether the shape and the person match in each display\n Press 'Y' if the shape and person match\n Press 'X' if the shape and the person do not match.\n Please respond AS QUICKLY AND ACCURATELY AS POSSIBLE\n SPACE to start"
text_100.setText(Instext2)
key_resp_40.keys = []
key_resp_40.rt = []
_key_resp_40_allKeys = []
# keep track of which components have finished
TASK_INSTRUCTIONS9Components = [text_100, key_resp_40]
for thisComponent in TASK_INSTRUCTIONS9Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "TASK_INSTRUCTIONS9" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_100* updates
    
    # if text_100 is starting this frame...
    if text_100.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_100.frameNStart = frameN  # exact frame index
        text_100.tStart = t  # local t and not account for scr refresh
        text_100.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_100, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_100.started')
        # update status
        text_100.status = STARTED
        text_100.setAutoDraw(True)
    
    # if text_100 is active this frame...
    if text_100.status == STARTED:
        # update params
        pass
    
    # *key_resp_40* updates
    waitOnFlip = False
    
    # if key_resp_40 is starting this frame...
    if key_resp_40.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_40.frameNStart = frameN  # exact frame index
        key_resp_40.tStart = t  # local t and not account for scr refresh
        key_resp_40.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_40, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_40.started')
        # update status
        key_resp_40.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_40.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_40.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_40.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_40.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_40_allKeys.extend(theseKeys)
        if len(_key_resp_40_allKeys):
            key_resp_40.keys = _key_resp_40_allKeys[-1].name  # just the last key pressed
            key_resp_40.rt = _key_resp_40_allKeys[-1].rt
            key_resp_40.duration = _key_resp_40_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TASK_INSTRUCTIONS9Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "TASK_INSTRUCTIONS9" ---
for thisComponent in TASK_INSTRUCTIONS9Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_40.keys in ['', [], None]:  # No response was made
    key_resp_40.keys = None
thisExp.addData('key_resp_40.keys',key_resp_40.keys)
if key_resp_40.keys != None:  # we had a response
    thisExp.addData('key_resp_40.rt', key_resp_40.rt)
    thisExp.addData('key_resp_40.duration', key_resp_40.duration)
thisExp.nextEntry()
# the Routine "TASK_INSTRUCTIONS9" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_29 = data.TrialHandler(nReps=900.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(prac),
    seed=None, name='trials_29')
thisExp.addLoop(trials_29)  # add the loop to the experiment
thisTrial_29 = trials_29.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_29.rgb)
if thisTrial_29 != None:
    for paramName in thisTrial_29:
        exec('{} = thisTrial_29[paramName]'.format(paramName))

for thisTrial_29 in trials_29:
    currentLoop = trials_29
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_29.rgb)
    if thisTrial_29 != None:
        for paramName in thisTrial_29:
            exec('{} = thisTrial_29[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "New_prac" ---
    continueRoutine = True
    # update component parameters for each repeat
    TheShape.setImage(shapes_images)
    Person.setText(shape_label)
    Left_button.setText(Left1)
    Right_button.setText(Right1)
    Prac_resp.keys = []
    Prac_resp.rt = []
    _Prac_resp_allKeys = []
    # keep track of which components have finished
    New_pracComponents = [TheShape, Person, Praccross, Left_button, Right_button, Prac_resp]
    for thisComponent in New_pracComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "New_prac" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 2.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *TheShape* updates
        
        # if TheShape is starting this frame...
        if TheShape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TheShape.frameNStart = frameN  # exact frame index
            TheShape.tStart = t  # local t and not account for scr refresh
            TheShape.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TheShape, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TheShape.started')
            # update status
            TheShape.status = STARTED
            TheShape.setAutoDraw(True)
        
        # if TheShape is active this frame...
        if TheShape.status == STARTED:
            # update params
            pass
        
        # if TheShape is stopping this frame...
        if TheShape.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > TheShape.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                TheShape.tStop = t  # not accounting for scr refresh
                TheShape.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TheShape.stopped')
                # update status
                TheShape.status = FINISHED
                TheShape.setAutoDraw(False)
        
        # *Person* updates
        
        # if Person is starting this frame...
        if Person.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Person.frameNStart = frameN  # exact frame index
            Person.tStart = t  # local t and not account for scr refresh
            Person.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Person, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Person.started')
            # update status
            Person.status = STARTED
            Person.setAutoDraw(True)
        
        # if Person is active this frame...
        if Person.status == STARTED:
            # update params
            pass
        
        # if Person is stopping this frame...
        if Person.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Person.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                Person.tStop = t  # not accounting for scr refresh
                Person.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Person.stopped')
                # update status
                Person.status = FINISHED
                Person.setAutoDraw(False)
        
        # *Praccross* updates
        
        # if Praccross is starting this frame...
        if Praccross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Praccross.frameNStart = frameN  # exact frame index
            Praccross.tStart = t  # local t and not account for scr refresh
            Praccross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Praccross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Praccross.started')
            # update status
            Praccross.status = STARTED
            Praccross.setAutoDraw(True)
        
        # if Praccross is active this frame...
        if Praccross.status == STARTED:
            # update params
            pass
        
        # if Praccross is stopping this frame...
        if Praccross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Praccross.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                Praccross.tStop = t  # not accounting for scr refresh
                Praccross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Praccross.stopped')
                # update status
                Praccross.status = FINISHED
                Praccross.setAutoDraw(False)
        
        # *Left_button* updates
        
        # if Left_button is starting this frame...
        if Left_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Left_button.frameNStart = frameN  # exact frame index
            Left_button.tStart = t  # local t and not account for scr refresh
            Left_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Left_button, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Left_button.started')
            # update status
            Left_button.status = STARTED
            Left_button.setAutoDraw(True)
        
        # if Left_button is active this frame...
        if Left_button.status == STARTED:
            # update params
            pass
        
        # if Left_button is stopping this frame...
        if Left_button.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Left_button.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                Left_button.tStop = t  # not accounting for scr refresh
                Left_button.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Left_button.stopped')
                # update status
                Left_button.status = FINISHED
                Left_button.setAutoDraw(False)
        
        # *Right_button* updates
        
        # if Right_button is starting this frame...
        if Right_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Right_button.frameNStart = frameN  # exact frame index
            Right_button.tStart = t  # local t and not account for scr refresh
            Right_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Right_button, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Right_button.started')
            # update status
            Right_button.status = STARTED
            Right_button.setAutoDraw(True)
        
        # if Right_button is active this frame...
        if Right_button.status == STARTED:
            # update params
            pass
        
        # if Right_button is stopping this frame...
        if Right_button.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Right_button.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                Right_button.tStop = t  # not accounting for scr refresh
                Right_button.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Right_button.stopped')
                # update status
                Right_button.status = FINISHED
                Right_button.setAutoDraw(False)
        
        # *Prac_resp* updates
        waitOnFlip = False
        
        # if Prac_resp is starting this frame...
        if Prac_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Prac_resp.frameNStart = frameN  # exact frame index
            Prac_resp.tStart = t  # local t and not account for scr refresh
            Prac_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Prac_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Prac_resp.started')
            # update status
            Prac_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Prac_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Prac_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if Prac_resp is stopping this frame...
        if Prac_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Prac_resp.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                Prac_resp.tStop = t  # not accounting for scr refresh
                Prac_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Prac_resp.stopped')
                # update status
                Prac_resp.status = FINISHED
                Prac_resp.status = FINISHED
        if Prac_resp.status == STARTED and not waitOnFlip:
            theseKeys = Prac_resp.getKeys(keyList=['1','4',], waitRelease=False)
            _Prac_resp_allKeys.extend(theseKeys)
            if len(_Prac_resp_allKeys):
                Prac_resp.keys = _Prac_resp_allKeys[-1].name  # just the last key pressed
                Prac_resp.rt = _Prac_resp_allKeys[-1].rt
                Prac_resp.duration = _Prac_resp_allKeys[-1].duration
                # was this correct?
                if (Prac_resp.keys == str(corr_key)) or (Prac_resp.keys == corr_key):
                    Prac_resp.corr = 1
                else:
                    Prac_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in New_pracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "New_prac" ---
    for thisComponent in New_pracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Prac_resp.keys in ['', [], None]:  # No response was made
        Prac_resp.keys = None
        # was no response the correct answer?!
        if str(corr_key).lower() == 'none':
           Prac_resp.corr = 1;  # correct non-response
        else:
           Prac_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_29 (TrialHandler)
    trials_29.addData('Prac_resp.keys',Prac_resp.keys)
    trials_29.addData('Prac_resp.corr', Prac_resp.corr)
    if Prac_resp.keys != None:  # we had a response
        trials_29.addData('Prac_resp.rt', Prac_resp.rt)
        trials_29.addData('Prac_resp.duration', Prac_resp.duration)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.500000)
    
    # --- Prepare to start Routine "New_feedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_65
    if Prac_resp.corr == 1:
        msg = "Correct!"
        msgColor = "green"
    elif not Prac_resp.keys:
        msg = "Too slow"
        msgColor = "yellow"
    else:
        msg = "Incorrect"
        msgColor = "red"
    text_56.setColor(msgColor, colorSpace='rgb')
    text_56.setText(msg)
    # keep track of which components have finished
    New_feedbackComponents = [text_56]
    for thisComponent in New_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "New_feedback" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_56* updates
        
        # if text_56 is starting this frame...
        if text_56.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_56.frameNStart = frameN  # exact frame index
            text_56.tStart = t  # local t and not account for scr refresh
            text_56.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_56, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_56.started')
            # update status
            text_56.status = STARTED
            text_56.setAutoDraw(True)
        
        # if text_56 is active this frame...
        if text_56.status == STARTED:
            # update params
            pass
        
        # if text_56 is stopping this frame...
        if text_56.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_56.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_56.tStop = t  # not accounting for scr refresh
                text_56.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_56.stopped')
                # update status
                text_56.status = FINISHED
                text_56.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in New_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "New_feedback" ---
    for thisComponent in New_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_72
    if (Prac_resp.corr == 1):
        GMtotal_acc = GMtotal_acc + 1
    else:
        GMtotal_acc = 0
    
    if (GMtotal_acc >= 16):
        trials_29.finished = True; skipThisTrial = True; continueRoutine = False;
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 900.0 repeats of 'trials_29'


# --- Prepare to start Routine "DONE_GMBM" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_51.keys = []
key_resp_51.rt = []
_key_resp_51_allKeys = []
# keep track of which components have finished
DONE_GMBMComponents = [text_126, key_resp_51]
for thisComponent in DONE_GMBMComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "DONE_GMBM" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_126* updates
    
    # if text_126 is starting this frame...
    if text_126.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_126.frameNStart = frameN  # exact frame index
        text_126.tStart = t  # local t and not account for scr refresh
        text_126.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_126, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_126.started')
        # update status
        text_126.status = STARTED
        text_126.setAutoDraw(True)
    
    # if text_126 is active this frame...
    if text_126.status == STARTED:
        # update params
        pass
    
    # *key_resp_51* updates
    waitOnFlip = False
    
    # if key_resp_51 is starting this frame...
    if key_resp_51.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_51.frameNStart = frameN  # exact frame index
        key_resp_51.tStart = t  # local t and not account for scr refresh
        key_resp_51.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_51, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_51.started')
        # update status
        key_resp_51.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_51.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_51.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_51.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_51.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_51_allKeys.extend(theseKeys)
        if len(_key_resp_51_allKeys):
            key_resp_51.keys = _key_resp_51_allKeys[-1].name  # just the last key pressed
            key_resp_51.rt = _key_resp_51_allKeys[-1].rt
            key_resp_51.duration = _key_resp_51_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in DONE_GMBMComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "DONE_GMBM" ---
for thisComponent in DONE_GMBMComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_51.keys in ['', [], None]:  # No response was made
    key_resp_51.keys = None
thisExp.addData('key_resp_51.keys',key_resp_51.keys)
if key_resp_51.keys != None:  # we had a response
    thisExp.addData('key_resp_51.rt', key_resp_51.rt)
    thisExp.addData('key_resp_51.duration', key_resp_51.duration)
thisExp.nextEntry()
# the Routine "DONE_GMBM" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Learning_intro" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
Learning_introComponents = [text_34, key_resp_9, LeftTiltEx, RightTiltEx, A_text, L_text]
for thisComponent in Learning_introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Learning_intro" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_34* updates
    
    # if text_34 is starting this frame...
    if text_34.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_34.frameNStart = frameN  # exact frame index
        text_34.tStart = t  # local t and not account for scr refresh
        text_34.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_34, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_34.started')
        # update status
        text_34.status = STARTED
        text_34.setAutoDraw(True)
    
    # if text_34 is active this frame...
    if text_34.status == STARTED:
        # update params
        pass
    
    # *key_resp_9* updates
    waitOnFlip = False
    
    # if key_resp_9 is starting this frame...
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_9.started')
        # update status
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            key_resp_9.duration = _key_resp_9_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # *LeftTiltEx* updates
    
    # if LeftTiltEx is starting this frame...
    if LeftTiltEx.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        LeftTiltEx.frameNStart = frameN  # exact frame index
        LeftTiltEx.tStart = t  # local t and not account for scr refresh
        LeftTiltEx.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(LeftTiltEx, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'LeftTiltEx.started')
        # update status
        LeftTiltEx.status = STARTED
        LeftTiltEx.setAutoDraw(True)
    
    # if LeftTiltEx is active this frame...
    if LeftTiltEx.status == STARTED:
        # update params
        pass
    
    # *RightTiltEx* updates
    
    # if RightTiltEx is starting this frame...
    if RightTiltEx.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RightTiltEx.frameNStart = frameN  # exact frame index
        RightTiltEx.tStart = t  # local t and not account for scr refresh
        RightTiltEx.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RightTiltEx, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RightTiltEx.started')
        # update status
        RightTiltEx.status = STARTED
        RightTiltEx.setAutoDraw(True)
    
    # if RightTiltEx is active this frame...
    if RightTiltEx.status == STARTED:
        # update params
        pass
    
    # *A_text* updates
    
    # if A_text is starting this frame...
    if A_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        A_text.frameNStart = frameN  # exact frame index
        A_text.tStart = t  # local t and not account for scr refresh
        A_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(A_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'A_text.started')
        # update status
        A_text.status = STARTED
        A_text.setAutoDraw(True)
    
    # if A_text is active this frame...
    if A_text.status == STARTED:
        # update params
        pass
    
    # *L_text* updates
    
    # if L_text is starting this frame...
    if L_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        L_text.frameNStart = frameN  # exact frame index
        L_text.tStart = t  # local t and not account for scr refresh
        L_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L_text.started')
        # update status
        L_text.status = STARTED
        L_text.setAutoDraw(True)
    
    # if L_text is active this frame...
    if L_text.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Learning_introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Learning_intro" ---
for thisComponent in Learning_introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
    thisExp.addData('key_resp_9.duration', key_resp_9.duration)
thisExp.nextEntry()
# the Routine "Learning_intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "MeAssoc" ---
continueRoutine = True
# update component parameters for each repeat
image_13.setImage(meshape)
key_resp_24.keys = []
key_resp_24.rt = []
_key_resp_24_allKeys = []
# keep track of which components have finished
MeAssocComponents = [image_13, text_50, key_resp_24, text_52]
for thisComponent in MeAssocComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "MeAssoc" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_13* updates
    
    # if image_13 is starting this frame...
    if image_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_13.frameNStart = frameN  # exact frame index
        image_13.tStart = t  # local t and not account for scr refresh
        image_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_13.started')
        # update status
        image_13.status = STARTED
        image_13.setAutoDraw(True)
    
    # if image_13 is active this frame...
    if image_13.status == STARTED:
        # update params
        pass
    
    # *text_50* updates
    
    # if text_50 is starting this frame...
    if text_50.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_50.frameNStart = frameN  # exact frame index
        text_50.tStart = t  # local t and not account for scr refresh
        text_50.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_50, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_50.started')
        # update status
        text_50.status = STARTED
        text_50.setAutoDraw(True)
    
    # if text_50 is active this frame...
    if text_50.status == STARTED:
        # update params
        pass
    
    # *key_resp_24* updates
    waitOnFlip = False
    
    # if key_resp_24 is starting this frame...
    if key_resp_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_24.frameNStart = frameN  # exact frame index
        key_resp_24.tStart = t  # local t and not account for scr refresh
        key_resp_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_24, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_24.started')
        # update status
        key_resp_24.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_24.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_24.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_24.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_24.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_24_allKeys.extend(theseKeys)
        if len(_key_resp_24_allKeys):
            key_resp_24.keys = _key_resp_24_allKeys[-1].name  # just the last key pressed
            key_resp_24.rt = _key_resp_24_allKeys[-1].rt
            key_resp_24.duration = _key_resp_24_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # *text_52* updates
    
    # if text_52 is starting this frame...
    if text_52.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_52.frameNStart = frameN  # exact frame index
        text_52.tStart = t  # local t and not account for scr refresh
        text_52.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_52, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_52.started')
        # update status
        text_52.status = STARTED
        text_52.setAutoDraw(True)
    
    # if text_52 is active this frame...
    if text_52.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MeAssocComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "MeAssoc" ---
for thisComponent in MeAssocComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_24.keys in ['', [], None]:  # No response was made
    key_resp_24.keys = None
thisExp.addData('key_resp_24.keys',key_resp_24.keys)
if key_resp_24.keys != None:  # we had a response
    thisExp.addData('key_resp_24.rt', key_resp_24.rt)
    thisExp.addData('key_resp_24.duration', key_resp_24.duration)
thisExp.nextEntry()
# the Routine "MeAssoc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "NomenAssoc" ---
continueRoutine = True
# update component parameters for each repeat
image_7.setImage(othershape)
text_47.setText('= Stranger')
key_resp_23.keys = []
key_resp_23.rt = []
_key_resp_23_allKeys = []
# keep track of which components have finished
NomenAssocComponents = [image_7, text_47, key_resp_23, text_49]
for thisComponent in NomenAssocComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "NomenAssoc" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_7* updates
    
    # if image_7 is starting this frame...
    if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_7.frameNStart = frameN  # exact frame index
        image_7.tStart = t  # local t and not account for scr refresh
        image_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_7.started')
        # update status
        image_7.status = STARTED
        image_7.setAutoDraw(True)
    
    # if image_7 is active this frame...
    if image_7.status == STARTED:
        # update params
        pass
    
    # *text_47* updates
    
    # if text_47 is starting this frame...
    if text_47.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_47.frameNStart = frameN  # exact frame index
        text_47.tStart = t  # local t and not account for scr refresh
        text_47.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_47, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_47.started')
        # update status
        text_47.status = STARTED
        text_47.setAutoDraw(True)
    
    # if text_47 is active this frame...
    if text_47.status == STARTED:
        # update params
        pass
    
    # *key_resp_23* updates
    waitOnFlip = False
    
    # if key_resp_23 is starting this frame...
    if key_resp_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_23.frameNStart = frameN  # exact frame index
        key_resp_23.tStart = t  # local t and not account for scr refresh
        key_resp_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_23, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_23.started')
        # update status
        key_resp_23.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_23.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_23.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_23.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_23.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_23_allKeys.extend(theseKeys)
        if len(_key_resp_23_allKeys):
            key_resp_23.keys = _key_resp_23_allKeys[-1].name  # just the last key pressed
            key_resp_23.rt = _key_resp_23_allKeys[-1].rt
            key_resp_23.duration = _key_resp_23_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # *text_49* updates
    
    # if text_49 is starting this frame...
    if text_49.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_49.frameNStart = frameN  # exact frame index
        text_49.tStart = t  # local t and not account for scr refresh
        text_49.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_49, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_49.started')
        # update status
        text_49.status = STARTED
        text_49.setAutoDraw(True)
    
    # if text_49 is active this frame...
    if text_49.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in NomenAssocComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "NomenAssoc" ---
for thisComponent in NomenAssocComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_23.keys in ['', [], None]:  # No response was made
    key_resp_23.keys = None
thisExp.addData('key_resp_23.keys',key_resp_23.keys)
if key_resp_23.keys != None:  # we had a response
    thisExp.addData('key_resp_23.rt', key_resp_23.rt)
    thisExp.addData('key_resp_23.duration', key_resp_23.duration)
thisExp.nextEntry()
# the Routine "NomenAssoc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "MeAssoc" ---
continueRoutine = True
# update component parameters for each repeat
image_13.setImage(meshape)
key_resp_24.keys = []
key_resp_24.rt = []
_key_resp_24_allKeys = []
# keep track of which components have finished
MeAssocComponents = [image_13, text_50, key_resp_24, text_52]
for thisComponent in MeAssocComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "MeAssoc" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_13* updates
    
    # if image_13 is starting this frame...
    if image_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_13.frameNStart = frameN  # exact frame index
        image_13.tStart = t  # local t and not account for scr refresh
        image_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_13.started')
        # update status
        image_13.status = STARTED
        image_13.setAutoDraw(True)
    
    # if image_13 is active this frame...
    if image_13.status == STARTED:
        # update params
        pass
    
    # *text_50* updates
    
    # if text_50 is starting this frame...
    if text_50.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_50.frameNStart = frameN  # exact frame index
        text_50.tStart = t  # local t and not account for scr refresh
        text_50.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_50, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_50.started')
        # update status
        text_50.status = STARTED
        text_50.setAutoDraw(True)
    
    # if text_50 is active this frame...
    if text_50.status == STARTED:
        # update params
        pass
    
    # *key_resp_24* updates
    waitOnFlip = False
    
    # if key_resp_24 is starting this frame...
    if key_resp_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_24.frameNStart = frameN  # exact frame index
        key_resp_24.tStart = t  # local t and not account for scr refresh
        key_resp_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_24, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_24.started')
        # update status
        key_resp_24.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_24.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_24.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_24.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_24.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_24_allKeys.extend(theseKeys)
        if len(_key_resp_24_allKeys):
            key_resp_24.keys = _key_resp_24_allKeys[-1].name  # just the last key pressed
            key_resp_24.rt = _key_resp_24_allKeys[-1].rt
            key_resp_24.duration = _key_resp_24_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # *text_52* updates
    
    # if text_52 is starting this frame...
    if text_52.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_52.frameNStart = frameN  # exact frame index
        text_52.tStart = t  # local t and not account for scr refresh
        text_52.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_52, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_52.started')
        # update status
        text_52.status = STARTED
        text_52.setAutoDraw(True)
    
    # if text_52 is active this frame...
    if text_52.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MeAssocComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "MeAssoc" ---
for thisComponent in MeAssocComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_24.keys in ['', [], None]:  # No response was made
    key_resp_24.keys = None
thisExp.addData('key_resp_24.keys',key_resp_24.keys)
if key_resp_24.keys != None:  # we had a response
    thisExp.addData('key_resp_24.rt', key_resp_24.rt)
    thisExp.addData('key_resp_24.duration', key_resp_24.duration)
thisExp.nextEntry()
# the Routine "MeAssoc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "NomenAssoc" ---
continueRoutine = True
# update component parameters for each repeat
image_7.setImage(othershape)
text_47.setText('= Stranger')
key_resp_23.keys = []
key_resp_23.rt = []
_key_resp_23_allKeys = []
# keep track of which components have finished
NomenAssocComponents = [image_7, text_47, key_resp_23, text_49]
for thisComponent in NomenAssocComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "NomenAssoc" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_7* updates
    
    # if image_7 is starting this frame...
    if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_7.frameNStart = frameN  # exact frame index
        image_7.tStart = t  # local t and not account for scr refresh
        image_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_7.started')
        # update status
        image_7.status = STARTED
        image_7.setAutoDraw(True)
    
    # if image_7 is active this frame...
    if image_7.status == STARTED:
        # update params
        pass
    
    # *text_47* updates
    
    # if text_47 is starting this frame...
    if text_47.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_47.frameNStart = frameN  # exact frame index
        text_47.tStart = t  # local t and not account for scr refresh
        text_47.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_47, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_47.started')
        # update status
        text_47.status = STARTED
        text_47.setAutoDraw(True)
    
    # if text_47 is active this frame...
    if text_47.status == STARTED:
        # update params
        pass
    
    # *key_resp_23* updates
    waitOnFlip = False
    
    # if key_resp_23 is starting this frame...
    if key_resp_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_23.frameNStart = frameN  # exact frame index
        key_resp_23.tStart = t  # local t and not account for scr refresh
        key_resp_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_23, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_23.started')
        # update status
        key_resp_23.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_23.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_23.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_23.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_23.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_23_allKeys.extend(theseKeys)
        if len(_key_resp_23_allKeys):
            key_resp_23.keys = _key_resp_23_allKeys[-1].name  # just the last key pressed
            key_resp_23.rt = _key_resp_23_allKeys[-1].rt
            key_resp_23.duration = _key_resp_23_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # *text_49* updates
    
    # if text_49 is starting this frame...
    if text_49.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_49.frameNStart = frameN  # exact frame index
        text_49.tStart = t  # local t and not account for scr refresh
        text_49.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_49, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_49.started')
        # update status
        text_49.status = STARTED
        text_49.setAutoDraw(True)
    
    # if text_49 is active this frame...
    if text_49.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in NomenAssocComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "NomenAssoc" ---
for thisComponent in NomenAssocComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_23.keys in ['', [], None]:  # No response was made
    key_resp_23.keys = None
thisExp.addData('key_resp_23.keys',key_resp_23.keys)
if key_resp_23.keys != None:  # we had a response
    thisExp.addData('key_resp_23.rt', key_resp_23.rt)
    thisExp.addData('key_resp_23.duration', key_resp_23.duration)
thisExp.nextEntry()
# the Routine "NomenAssoc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_20 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('countdown.xlsx'),
    seed=None, name='trials_20')
thisExp.addLoop(trials_20)  # add the loop to the experiment
thisTrial_20 = trials_20.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_20.rgb)
if thisTrial_20 != None:
    for paramName in thisTrial_20:
        exec('{} = thisTrial_20[paramName]'.format(paramName))

for thisTrial_20 in trials_20:
    currentLoop = trials_20
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_20.rgb)
    if thisTrial_20 != None:
        for paramName in thisTrial_20:
            exec('{} = thisTrial_20[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Count_down" ---
    continueRoutine = True
    # update component parameters for each repeat
    text_72.setColor(ccolor, colorSpace='rgb')
    text_72.setText(numberC)
    # keep track of which components have finished
    Count_downComponents = [text_72]
    for thisComponent in Count_downComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Count_down" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_72* updates
        
        # if text_72 is starting this frame...
        if text_72.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_72.frameNStart = frameN  # exact frame index
            text_72.tStart = t  # local t and not account for scr refresh
            text_72.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_72, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_72.started')
            # update status
            text_72.status = STARTED
            text_72.setAutoDraw(True)
        
        # if text_72 is active this frame...
        if text_72.status == STARTED:
            # update params
            pass
        
        # if text_72 is stopping this frame...
        if text_72.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_72.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_72.tStop = t  # not accounting for scr refresh
                text_72.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_72.stopped')
                # update status
                text_72.status = FINISHED
                text_72.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Count_downComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Count_down" ---
    for thisComponent in Count_downComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
# completed 1.0 repeats of 'trials_20'


# set up handler to look after randomisation of conditions etc
trials_23 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(Xenia, selection='0:5, 20:25, 35:40, 50:55, 70:75, 90:95'),
    seed=None, name='trials_23')
thisExp.addLoop(trials_23)  # add the loop to the experiment
thisTrial_23 = trials_23.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_23.rgb)
if thisTrial_23 != None:
    for paramName in thisTrial_23:
        exec('{} = thisTrial_23[paramName]'.format(paramName))

for thisTrial_23 in trials_23:
    currentLoop = trials_23
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_23.rgb)
    if thisTrial_23 != None:
        for paramName in thisTrial_23:
            exec('{} = thisTrial_23[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Cue_WM_2" ---
    continueRoutine = True
    # update component parameters for each repeat
    image_5.setImage(thepresentshape)
    # keep track of which components have finished
    Cue_WM_2Components = [image_5, Crux_5, text_42]
    for thisComponent in Cue_WM_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Cue_WM_2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_5* updates
        
        # if image_5 is starting this frame...
        if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_5.frameNStart = frameN  # exact frame index
            image_5.tStart = t  # local t and not account for scr refresh
            image_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_5.started')
            # update status
            image_5.status = STARTED
            image_5.setAutoDraw(True)
        
        # if image_5 is active this frame...
        if image_5.status == STARTED:
            # update params
            pass
        
        # if image_5 is stopping this frame...
        if image_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_5.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                image_5.tStop = t  # not accounting for scr refresh
                image_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_5.stopped')
                # update status
                image_5.status = FINISHED
                image_5.setAutoDraw(False)
        
        # *Crux_5* updates
        
        # if Crux_5 is starting this frame...
        if Crux_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Crux_5.frameNStart = frameN  # exact frame index
            Crux_5.tStart = t  # local t and not account for scr refresh
            Crux_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Crux_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Crux_5.started')
            # update status
            Crux_5.status = STARTED
            Crux_5.setAutoDraw(True)
        
        # if Crux_5 is active this frame...
        if Crux_5.status == STARTED:
            # update params
            pass
        
        # if Crux_5 is stopping this frame...
        if Crux_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Crux_5.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Crux_5.tStop = t  # not accounting for scr refresh
                Crux_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Crux_5.stopped')
                # update status
                Crux_5.status = FINISHED
                Crux_5.setAutoDraw(False)
        
        # *text_42* updates
        
        # if text_42 is starting this frame...
        if text_42.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_42.frameNStart = frameN  # exact frame index
            text_42.tStart = t  # local t and not account for scr refresh
            text_42.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_42, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_42.started')
            # update status
            text_42.status = STARTED
            text_42.setAutoDraw(True)
        
        # if text_42 is active this frame...
        if text_42.status == STARTED:
            # update params
            pass
        
        # if text_42 is stopping this frame...
        if text_42.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_42.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                text_42.tStop = t  # not accounting for scr refresh
                text_42.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_42.stopped')
                # update status
                text_42.status = FINISHED
                text_42.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Cue_WM_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Cue_WM_2" ---
    for thisComponent in Cue_WM_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_56
    circleSize = 0.3
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "Crucem_WM" ---
    continueRoutine = True
    # update component parameters for each repeat
    text_41.setText('+')
    # Run 'Begin Routine' code from code_34
    SCTime = math.floor(random.random() * 201 + 500) / 1000
    # keep track of which components have finished
    Crucem_WMComponents = [text_41, polygon_2]
    for thisComponent in Crucem_WMComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Crucem_WM" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_55
        
        if polygon_2.size[0] > 0:
            circleSize -= 0.03333333333;
        
        # *text_41* updates
        
        # if text_41 is starting this frame...
        if text_41.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_41.frameNStart = frameN  # exact frame index
            text_41.tStart = t  # local t and not account for scr refresh
            text_41.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_41, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_41.started')
            # update status
            text_41.status = STARTED
            text_41.setAutoDraw(True)
        
        # if text_41 is active this frame...
        if text_41.status == STARTED:
            # update params
            pass
        
        # if text_41 is stopping this frame...
        if text_41.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_41.tStartRefresh + SCTime-frameTolerance:
                # keep track of stop time/frame for later
                text_41.tStop = t  # not accounting for scr refresh
                text_41.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_41.stopped')
                # update status
                text_41.status = FINISHED
                text_41.setAutoDraw(False)
        
        # *polygon_2* updates
        
        # if polygon_2 is starting this frame...
        if polygon_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            polygon_2.frameNStart = frameN  # exact frame index
            polygon_2.tStart = t  # local t and not account for scr refresh
            polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            polygon_2.status = STARTED
            polygon_2.setAutoDraw(True)
        
        # if polygon_2 is active this frame...
        if polygon_2.status == STARTED:
            # update params
            polygon_2.setSize((circleSize, circleSize), log=False)
        
        # if polygon_2 is stopping this frame...
        if polygon_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_2.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                polygon_2.tStop = t  # not accounting for scr refresh
                polygon_2.frameNStop = frameN  # exact frame index
                # update status
                polygon_2.status = FINISHED
                polygon_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Crucem_WMComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Crucem_WM" ---
    for thisComponent in Crucem_WMComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Crucem_WM" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ERL_3" ---
    continueRoutine = True
    # update component parameters for each repeat
    Left_shape_3.setImage(left)
    Right_shape_3.setImage(right)
    Tilted_line_3.setPos([tiltposx,tiltposy])
    Tilted_line_3.setImage(tilt)
    Horizontal_line_3.setPos([dposx,dposy])
    Answer_3.keys = []
    Answer_3.rt = []
    _Answer_3_allKeys = []
    # keep track of which components have finished
    ERL_3Components = [Left_shape_3, Right_shape_3, Tilted_line_3, Horizontal_line_3, Answer_3, Crux_6]
    for thisComponent in ERL_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ERL_3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Left_shape_3* updates
        
        # if Left_shape_3 is starting this frame...
        if Left_shape_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Left_shape_3.frameNStart = frameN  # exact frame index
            Left_shape_3.tStart = t  # local t and not account for scr refresh
            Left_shape_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Left_shape_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Left_shape_3.started')
            # update status
            Left_shape_3.status = STARTED
            Left_shape_3.setAutoDraw(True)
        
        # if Left_shape_3 is active this frame...
        if Left_shape_3.status == STARTED:
            # update params
            pass
        
        # if Left_shape_3 is stopping this frame...
        if Left_shape_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Left_shape_3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Left_shape_3.tStop = t  # not accounting for scr refresh
                Left_shape_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Left_shape_3.stopped')
                # update status
                Left_shape_3.status = FINISHED
                Left_shape_3.setAutoDraw(False)
        
        # *Right_shape_3* updates
        
        # if Right_shape_3 is starting this frame...
        if Right_shape_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Right_shape_3.frameNStart = frameN  # exact frame index
            Right_shape_3.tStart = t  # local t and not account for scr refresh
            Right_shape_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Right_shape_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Right_shape_3.started')
            # update status
            Right_shape_3.status = STARTED
            Right_shape_3.setAutoDraw(True)
        
        # if Right_shape_3 is active this frame...
        if Right_shape_3.status == STARTED:
            # update params
            pass
        
        # if Right_shape_3 is stopping this frame...
        if Right_shape_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Right_shape_3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Right_shape_3.tStop = t  # not accounting for scr refresh
                Right_shape_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Right_shape_3.stopped')
                # update status
                Right_shape_3.status = FINISHED
                Right_shape_3.setAutoDraw(False)
        
        # *Tilted_line_3* updates
        
        # if Tilted_line_3 is starting this frame...
        if Tilted_line_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Tilted_line_3.frameNStart = frameN  # exact frame index
            Tilted_line_3.tStart = t  # local t and not account for scr refresh
            Tilted_line_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Tilted_line_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Tilted_line_3.started')
            # update status
            Tilted_line_3.status = STARTED
            Tilted_line_3.setAutoDraw(True)
        
        # if Tilted_line_3 is active this frame...
        if Tilted_line_3.status == STARTED:
            # update params
            pass
        
        # if Tilted_line_3 is stopping this frame...
        if Tilted_line_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Tilted_line_3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Tilted_line_3.tStop = t  # not accounting for scr refresh
                Tilted_line_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Tilted_line_3.stopped')
                # update status
                Tilted_line_3.status = FINISHED
                Tilted_line_3.setAutoDraw(False)
        
        # *Horizontal_line_3* updates
        
        # if Horizontal_line_3 is starting this frame...
        if Horizontal_line_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Horizontal_line_3.frameNStart = frameN  # exact frame index
            Horizontal_line_3.tStart = t  # local t and not account for scr refresh
            Horizontal_line_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Horizontal_line_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Horizontal_line_3.started')
            # update status
            Horizontal_line_3.status = STARTED
            Horizontal_line_3.setAutoDraw(True)
        
        # if Horizontal_line_3 is active this frame...
        if Horizontal_line_3.status == STARTED:
            # update params
            pass
        
        # if Horizontal_line_3 is stopping this frame...
        if Horizontal_line_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Horizontal_line_3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Horizontal_line_3.tStop = t  # not accounting for scr refresh
                Horizontal_line_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Horizontal_line_3.stopped')
                # update status
                Horizontal_line_3.status = FINISHED
                Horizontal_line_3.setAutoDraw(False)
        
        # *Answer_3* updates
        waitOnFlip = False
        
        # if Answer_3 is starting this frame...
        if Answer_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Answer_3.frameNStart = frameN  # exact frame index
            Answer_3.tStart = t  # local t and not account for scr refresh
            Answer_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Answer_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Answer_3.started')
            # update status
            Answer_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Answer_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Answer_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if Answer_3 is stopping this frame...
        if Answer_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Answer_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Answer_3.tStop = t  # not accounting for scr refresh
                Answer_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Answer_3.stopped')
                # update status
                Answer_3.status = FINISHED
                Answer_3.status = FINISHED
        if Answer_3.status == STARTED and not waitOnFlip:
            theseKeys = Answer_3.getKeys(keyList=['1','4'], waitRelease=False)
            _Answer_3_allKeys.extend(theseKeys)
            if len(_Answer_3_allKeys):
                Answer_3.keys = _Answer_3_allKeys[-1].name  # just the last key pressed
                Answer_3.rt = _Answer_3_allKeys[-1].rt
                Answer_3.duration = _Answer_3_allKeys[-1].duration
                # was this correct?
                if (Answer_3.keys == str(corkey)) or (Answer_3.keys == corkey):
                    Answer_3.corr = 1
                else:
                    Answer_3.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *Crux_6* updates
        
        # if Crux_6 is starting this frame...
        if Crux_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Crux_6.frameNStart = frameN  # exact frame index
            Crux_6.tStart = t  # local t and not account for scr refresh
            Crux_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Crux_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Crux_6.started')
            # update status
            Crux_6.status = STARTED
            Crux_6.setAutoDraw(True)
        
        # if Crux_6 is active this frame...
        if Crux_6.status == STARTED:
            # update params
            pass
        
        # if Crux_6 is stopping this frame...
        if Crux_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Crux_6.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Crux_6.tStop = t  # not accounting for scr refresh
                Crux_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Crux_6.stopped')
                # update status
                Crux_6.status = FINISHED
                Crux_6.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ERL_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ERL_3" ---
    for thisComponent in ERL_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Answer_3.keys in ['', [], None]:  # No response was made
        Answer_3.keys = None
        # was no response the correct answer?!
        if str(corkey).lower() == 'none':
           Answer_3.corr = 1;  # correct non-response
        else:
           Answer_3.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_23 (TrialHandler)
    trials_23.addData('Answer_3.keys',Answer_3.keys)
    trials_23.addData('Answer_3.corr', Answer_3.corr)
    if Answer_3.keys != None:  # we had a response
        trials_23.addData('Answer_3.rt', Answer_3.rt)
        trials_23.addData('Answer_3.duration', Answer_3.duration)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "Feedback_ERL_3" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_58
    if Answer_3.corr:
        msg='Correct!'
        msgColor = "green"
    elif not Answer_3.keys:
        msg='Too slow'
        msgColor= "yellow"
    else:
        msg='Incorrect'
        msgColor = "red"
    Fodeback_3.setColor(msgColor, colorSpace='rgb')
    Fodeback_3.setText(msg)
    # keep track of which components have finished
    Feedback_ERL_3Components = [Fodeback_3]
    for thisComponent in Feedback_ERL_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Feedback_ERL_3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fodeback_3* updates
        
        # if Fodeback_3 is starting this frame...
        if Fodeback_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fodeback_3.frameNStart = frameN  # exact frame index
            Fodeback_3.tStart = t  # local t and not account for scr refresh
            Fodeback_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fodeback_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Fodeback_3.started')
            # update status
            Fodeback_3.status = STARTED
            Fodeback_3.setAutoDraw(True)
        
        # if Fodeback_3 is active this frame...
        if Fodeback_3.status == STARTED:
            # update params
            pass
        
        # if Fodeback_3 is stopping this frame...
        if Fodeback_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fodeback_3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Fodeback_3.tStop = t  # not accounting for scr refresh
                Fodeback_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fodeback_3.stopped')
                # update status
                Fodeback_3.status = FINISHED
                Fodeback_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Feedback_ERL_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Feedback_ERL_3" ---
    for thisComponent in Feedback_ERL_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "Test_3" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_59
    
    # Set the probability of running the routine (20%)
    probability_of_running = 0.2
    
    # Determine whether to run the routine on this trial
    run_task_routine = random.random() < probability_of_running
    
    if not run_task_routine:
        continueRoutine = False  # Skip the routine if the condition is false
    
    Test_answer_3.keys = []
    Test_answer_3.rt = []
    _Test_answer_3_allKeys = []
    text_45.setText(logos)
    # keep track of which components have finished
    Test_3Components = [Test_answer_3, text_43, text_44, text_45, text_46]
    for thisComponent in Test_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Test_3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Test_answer_3* updates
        waitOnFlip = False
        
        # if Test_answer_3 is starting this frame...
        if Test_answer_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Test_answer_3.frameNStart = frameN  # exact frame index
            Test_answer_3.tStart = t  # local t and not account for scr refresh
            Test_answer_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Test_answer_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Test_answer_3.started')
            # update status
            Test_answer_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Test_answer_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Test_answer_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if Test_answer_3 is stopping this frame...
        if Test_answer_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Test_answer_3.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                Test_answer_3.tStop = t  # not accounting for scr refresh
                Test_answer_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Test_answer_3.stopped')
                # update status
                Test_answer_3.status = FINISHED
                Test_answer_3.status = FINISHED
        if Test_answer_3.status == STARTED and not waitOnFlip:
            theseKeys = Test_answer_3.getKeys(keyList=['a','l'], waitRelease=False)
            _Test_answer_3_allKeys.extend(theseKeys)
            if len(_Test_answer_3_allKeys):
                Test_answer_3.keys = _Test_answer_3_allKeys[-1].name  # just the last key pressed
                Test_answer_3.rt = _Test_answer_3_allKeys[-1].rt
                Test_answer_3.duration = _Test_answer_3_allKeys[-1].duration
                # was this correct?
                if (Test_answer_3.keys == str(corkey2)) or (Test_answer_3.keys == corkey2):
                    Test_answer_3.corr = 1
                else:
                    Test_answer_3.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *text_43* updates
        
        # if text_43 is starting this frame...
        if text_43.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_43.frameNStart = frameN  # exact frame index
            text_43.tStart = t  # local t and not account for scr refresh
            text_43.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_43, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_43.started')
            # update status
            text_43.status = STARTED
            text_43.setAutoDraw(True)
        
        # if text_43 is active this frame...
        if text_43.status == STARTED:
            # update params
            pass
        
        # if text_43 is stopping this frame...
        if text_43.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_43.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_43.tStop = t  # not accounting for scr refresh
                text_43.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_43.stopped')
                # update status
                text_43.status = FINISHED
                text_43.setAutoDraw(False)
        
        # *text_44* updates
        
        # if text_44 is starting this frame...
        if text_44.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_44.frameNStart = frameN  # exact frame index
            text_44.tStart = t  # local t and not account for scr refresh
            text_44.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_44, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_44.started')
            # update status
            text_44.status = STARTED
            text_44.setAutoDraw(True)
        
        # if text_44 is active this frame...
        if text_44.status == STARTED:
            # update params
            pass
        
        # if text_44 is stopping this frame...
        if text_44.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_44.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_44.tStop = t  # not accounting for scr refresh
                text_44.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_44.stopped')
                # update status
                text_44.status = FINISHED
                text_44.setAutoDraw(False)
        
        # *text_45* updates
        
        # if text_45 is starting this frame...
        if text_45.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_45.frameNStart = frameN  # exact frame index
            text_45.tStart = t  # local t and not account for scr refresh
            text_45.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_45, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_45.started')
            # update status
            text_45.status = STARTED
            text_45.setAutoDraw(True)
        
        # if text_45 is active this frame...
        if text_45.status == STARTED:
            # update params
            pass
        
        # if text_45 is stopping this frame...
        if text_45.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_45.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_45.tStop = t  # not accounting for scr refresh
                text_45.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_45.stopped')
                # update status
                text_45.status = FINISHED
                text_45.setAutoDraw(False)
        
        # *text_46* updates
        
        # if text_46 is starting this frame...
        if text_46.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_46.frameNStart = frameN  # exact frame index
            text_46.tStart = t  # local t and not account for scr refresh
            text_46.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_46, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_46.started')
            # update status
            text_46.status = STARTED
            text_46.setAutoDraw(True)
        
        # if text_46 is active this frame...
        if text_46.status == STARTED:
            # update params
            pass
        
        # if text_46 is stopping this frame...
        if text_46.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_46.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_46.tStop = t  # not accounting for scr refresh
                text_46.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_46.stopped')
                # update status
                text_46.status = FINISHED
                text_46.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Test_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Test_3" ---
    for thisComponent in Test_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Test_answer_3.keys in ['', [], None]:  # No response was made
        Test_answer_3.keys = None
        # was no response the correct answer?!
        if str(corkey2).lower() == 'none':
           Test_answer_3.corr = 1;  # correct non-response
        else:
           Test_answer_3.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_23 (TrialHandler)
    trials_23.addData('Test_answer_3.keys',Test_answer_3.keys)
    trials_23.addData('Test_answer_3.corr', Test_answer_3.corr)
    if Test_answer_3.keys != None:  # we had a response
        trials_23.addData('Test_answer_3.rt', Test_answer_3.rt)
        trials_23.addData('Test_answer_3.duration', Test_answer_3.duration)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    
    # --- Prepare to start Routine "Test_feedback_3" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_61
    if Test_answer_3.corr:
        msg='Correct!'
        msgColor = "green"
    elif not Test_answer_3.keys:
        msg='Too slow'
        msgColor= "yellow"
    else:
        msg='Incorrect'
        msgColor = "red"
    text_54.setColor(msgColor, colorSpace='rgb')
    text_54.setText(msg)
    # Run 'Begin Routine' code from Rez_2
    if not run_task_routine:
        continueRoutine = False  # Skip the routine if the task routine was skipped
    
    # keep track of which components have finished
    Test_feedback_3Components = [text_54]
    for thisComponent in Test_feedback_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Test_feedback_3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_54* updates
        
        # if text_54 is starting this frame...
        if text_54.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_54.frameNStart = frameN  # exact frame index
            text_54.tStart = t  # local t and not account for scr refresh
            text_54.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_54, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_54.started')
            # update status
            text_54.status = STARTED
            text_54.setAutoDraw(True)
        
        # if text_54 is active this frame...
        if text_54.status == STARTED:
            # update params
            pass
        
        # if text_54 is stopping this frame...
        if text_54.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_54.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_54.tStop = t  # not accounting for scr refresh
                text_54.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_54.stopped')
                # update status
                text_54.status = FINISHED
                text_54.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Test_feedback_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Test_feedback_3" ---
    for thisComponent in Test_feedback_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from Rez_2
    thisExp.addData('Congruence',corkey2)
    thisExp.addData('Cor3',Test_answer.corr)
    thisExp.addData('RT3',Test_answer.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
# completed 1.0 repeats of 'trials_23'


# --- Prepare to start Routine "Now_it_real" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_11.keys = []
key_resp_11.rt = []
_key_resp_11_allKeys = []
# keep track of which components have finished
Now_it_realComponents = [text_55, key_resp_11]
for thisComponent in Now_it_realComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Now_it_real" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_55* updates
    
    # if text_55 is starting this frame...
    if text_55.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_55.frameNStart = frameN  # exact frame index
        text_55.tStart = t  # local t and not account for scr refresh
        text_55.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_55, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_55.started')
        # update status
        text_55.status = STARTED
        text_55.setAutoDraw(True)
    
    # if text_55 is active this frame...
    if text_55.status == STARTED:
        # update params
        pass
    
    # *key_resp_11* updates
    waitOnFlip = False
    
    # if key_resp_11 is starting this frame...
    if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.tStart = t  # local t and not account for scr refresh
        key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_11.started')
        # update status
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_11.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_11.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_11_allKeys.extend(theseKeys)
        if len(_key_resp_11_allKeys):
            key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
            key_resp_11.rt = _key_resp_11_allKeys[-1].rt
            key_resp_11.duration = _key_resp_11_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Now_it_realComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Now_it_real" ---
for thisComponent in Now_it_realComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_11.keys in ['', [], None]:  # No response was made
    key_resp_11.keys = None
thisExp.addData('key_resp_11.keys',key_resp_11.keys)
if key_resp_11.keys != None:  # we had a response
    thisExp.addData('key_resp_11.rt', key_resp_11.rt)
    thisExp.addData('key_resp_11.duration', key_resp_11.duration)
thisExp.nextEntry()
# the Routine "Now_it_real" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "MeAssoc" ---
continueRoutine = True
# update component parameters for each repeat
image_13.setImage(meshape)
key_resp_24.keys = []
key_resp_24.rt = []
_key_resp_24_allKeys = []
# keep track of which components have finished
MeAssocComponents = [image_13, text_50, key_resp_24, text_52]
for thisComponent in MeAssocComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "MeAssoc" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_13* updates
    
    # if image_13 is starting this frame...
    if image_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_13.frameNStart = frameN  # exact frame index
        image_13.tStart = t  # local t and not account for scr refresh
        image_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_13.started')
        # update status
        image_13.status = STARTED
        image_13.setAutoDraw(True)
    
    # if image_13 is active this frame...
    if image_13.status == STARTED:
        # update params
        pass
    
    # *text_50* updates
    
    # if text_50 is starting this frame...
    if text_50.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_50.frameNStart = frameN  # exact frame index
        text_50.tStart = t  # local t and not account for scr refresh
        text_50.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_50, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_50.started')
        # update status
        text_50.status = STARTED
        text_50.setAutoDraw(True)
    
    # if text_50 is active this frame...
    if text_50.status == STARTED:
        # update params
        pass
    
    # *key_resp_24* updates
    waitOnFlip = False
    
    # if key_resp_24 is starting this frame...
    if key_resp_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_24.frameNStart = frameN  # exact frame index
        key_resp_24.tStart = t  # local t and not account for scr refresh
        key_resp_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_24, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_24.started')
        # update status
        key_resp_24.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_24.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_24.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_24.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_24.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_24_allKeys.extend(theseKeys)
        if len(_key_resp_24_allKeys):
            key_resp_24.keys = _key_resp_24_allKeys[-1].name  # just the last key pressed
            key_resp_24.rt = _key_resp_24_allKeys[-1].rt
            key_resp_24.duration = _key_resp_24_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # *text_52* updates
    
    # if text_52 is starting this frame...
    if text_52.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_52.frameNStart = frameN  # exact frame index
        text_52.tStart = t  # local t and not account for scr refresh
        text_52.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_52, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_52.started')
        # update status
        text_52.status = STARTED
        text_52.setAutoDraw(True)
    
    # if text_52 is active this frame...
    if text_52.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MeAssocComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "MeAssoc" ---
for thisComponent in MeAssocComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_24.keys in ['', [], None]:  # No response was made
    key_resp_24.keys = None
thisExp.addData('key_resp_24.keys',key_resp_24.keys)
if key_resp_24.keys != None:  # we had a response
    thisExp.addData('key_resp_24.rt', key_resp_24.rt)
    thisExp.addData('key_resp_24.duration', key_resp_24.duration)
thisExp.nextEntry()
# the Routine "MeAssoc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "NomenAssoc" ---
continueRoutine = True
# update component parameters for each repeat
image_7.setImage(othershape)
text_47.setText('= Stranger')
key_resp_23.keys = []
key_resp_23.rt = []
_key_resp_23_allKeys = []
# keep track of which components have finished
NomenAssocComponents = [image_7, text_47, key_resp_23, text_49]
for thisComponent in NomenAssocComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "NomenAssoc" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_7* updates
    
    # if image_7 is starting this frame...
    if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_7.frameNStart = frameN  # exact frame index
        image_7.tStart = t  # local t and not account for scr refresh
        image_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_7.started')
        # update status
        image_7.status = STARTED
        image_7.setAutoDraw(True)
    
    # if image_7 is active this frame...
    if image_7.status == STARTED:
        # update params
        pass
    
    # *text_47* updates
    
    # if text_47 is starting this frame...
    if text_47.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_47.frameNStart = frameN  # exact frame index
        text_47.tStart = t  # local t and not account for scr refresh
        text_47.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_47, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_47.started')
        # update status
        text_47.status = STARTED
        text_47.setAutoDraw(True)
    
    # if text_47 is active this frame...
    if text_47.status == STARTED:
        # update params
        pass
    
    # *key_resp_23* updates
    waitOnFlip = False
    
    # if key_resp_23 is starting this frame...
    if key_resp_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_23.frameNStart = frameN  # exact frame index
        key_resp_23.tStart = t  # local t and not account for scr refresh
        key_resp_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_23, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_23.started')
        # update status
        key_resp_23.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_23.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_23.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_23.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_23.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_23_allKeys.extend(theseKeys)
        if len(_key_resp_23_allKeys):
            key_resp_23.keys = _key_resp_23_allKeys[-1].name  # just the last key pressed
            key_resp_23.rt = _key_resp_23_allKeys[-1].rt
            key_resp_23.duration = _key_resp_23_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # *text_49* updates
    
    # if text_49 is starting this frame...
    if text_49.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_49.frameNStart = frameN  # exact frame index
        text_49.tStart = t  # local t and not account for scr refresh
        text_49.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_49, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_49.started')
        # update status
        text_49.status = STARTED
        text_49.setAutoDraw(True)
    
    # if text_49 is active this frame...
    if text_49.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in NomenAssocComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "NomenAssoc" ---
for thisComponent in NomenAssocComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_23.keys in ['', [], None]:  # No response was made
    key_resp_23.keys = None
thisExp.addData('key_resp_23.keys',key_resp_23.keys)
if key_resp_23.keys != None:  # we had a response
    thisExp.addData('key_resp_23.rt', key_resp_23.rt)
    thisExp.addData('key_resp_23.duration', key_resp_23.duration)
thisExp.nextEntry()
# the Routine "NomenAssoc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "MeAssoc" ---
continueRoutine = True
# update component parameters for each repeat
image_13.setImage(meshape)
key_resp_24.keys = []
key_resp_24.rt = []
_key_resp_24_allKeys = []
# keep track of which components have finished
MeAssocComponents = [image_13, text_50, key_resp_24, text_52]
for thisComponent in MeAssocComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "MeAssoc" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_13* updates
    
    # if image_13 is starting this frame...
    if image_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_13.frameNStart = frameN  # exact frame index
        image_13.tStart = t  # local t and not account for scr refresh
        image_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_13.started')
        # update status
        image_13.status = STARTED
        image_13.setAutoDraw(True)
    
    # if image_13 is active this frame...
    if image_13.status == STARTED:
        # update params
        pass
    
    # *text_50* updates
    
    # if text_50 is starting this frame...
    if text_50.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_50.frameNStart = frameN  # exact frame index
        text_50.tStart = t  # local t and not account for scr refresh
        text_50.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_50, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_50.started')
        # update status
        text_50.status = STARTED
        text_50.setAutoDraw(True)
    
    # if text_50 is active this frame...
    if text_50.status == STARTED:
        # update params
        pass
    
    # *key_resp_24* updates
    waitOnFlip = False
    
    # if key_resp_24 is starting this frame...
    if key_resp_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_24.frameNStart = frameN  # exact frame index
        key_resp_24.tStart = t  # local t and not account for scr refresh
        key_resp_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_24, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_24.started')
        # update status
        key_resp_24.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_24.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_24.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_24.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_24.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_24_allKeys.extend(theseKeys)
        if len(_key_resp_24_allKeys):
            key_resp_24.keys = _key_resp_24_allKeys[-1].name  # just the last key pressed
            key_resp_24.rt = _key_resp_24_allKeys[-1].rt
            key_resp_24.duration = _key_resp_24_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # *text_52* updates
    
    # if text_52 is starting this frame...
    if text_52.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_52.frameNStart = frameN  # exact frame index
        text_52.tStart = t  # local t and not account for scr refresh
        text_52.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_52, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_52.started')
        # update status
        text_52.status = STARTED
        text_52.setAutoDraw(True)
    
    # if text_52 is active this frame...
    if text_52.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MeAssocComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "MeAssoc" ---
for thisComponent in MeAssocComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_24.keys in ['', [], None]:  # No response was made
    key_resp_24.keys = None
thisExp.addData('key_resp_24.keys',key_resp_24.keys)
if key_resp_24.keys != None:  # we had a response
    thisExp.addData('key_resp_24.rt', key_resp_24.rt)
    thisExp.addData('key_resp_24.duration', key_resp_24.duration)
thisExp.nextEntry()
# the Routine "MeAssoc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "NomenAssoc" ---
continueRoutine = True
# update component parameters for each repeat
image_7.setImage(othershape)
text_47.setText('= Stranger')
key_resp_23.keys = []
key_resp_23.rt = []
_key_resp_23_allKeys = []
# keep track of which components have finished
NomenAssocComponents = [image_7, text_47, key_resp_23, text_49]
for thisComponent in NomenAssocComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "NomenAssoc" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_7* updates
    
    # if image_7 is starting this frame...
    if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_7.frameNStart = frameN  # exact frame index
        image_7.tStart = t  # local t and not account for scr refresh
        image_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_7.started')
        # update status
        image_7.status = STARTED
        image_7.setAutoDraw(True)
    
    # if image_7 is active this frame...
    if image_7.status == STARTED:
        # update params
        pass
    
    # *text_47* updates
    
    # if text_47 is starting this frame...
    if text_47.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_47.frameNStart = frameN  # exact frame index
        text_47.tStart = t  # local t and not account for scr refresh
        text_47.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_47, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_47.started')
        # update status
        text_47.status = STARTED
        text_47.setAutoDraw(True)
    
    # if text_47 is active this frame...
    if text_47.status == STARTED:
        # update params
        pass
    
    # *key_resp_23* updates
    waitOnFlip = False
    
    # if key_resp_23 is starting this frame...
    if key_resp_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_23.frameNStart = frameN  # exact frame index
        key_resp_23.tStart = t  # local t and not account for scr refresh
        key_resp_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_23, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_23.started')
        # update status
        key_resp_23.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_23.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_23.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_23.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_23.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_23_allKeys.extend(theseKeys)
        if len(_key_resp_23_allKeys):
            key_resp_23.keys = _key_resp_23_allKeys[-1].name  # just the last key pressed
            key_resp_23.rt = _key_resp_23_allKeys[-1].rt
            key_resp_23.duration = _key_resp_23_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # *text_49* updates
    
    # if text_49 is starting this frame...
    if text_49.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_49.frameNStart = frameN  # exact frame index
        text_49.tStart = t  # local t and not account for scr refresh
        text_49.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_49, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_49.started')
        # update status
        text_49.status = STARTED
        text_49.setAutoDraw(True)
    
    # if text_49 is active this frame...
    if text_49.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in NomenAssocComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "NomenAssoc" ---
for thisComponent in NomenAssocComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_23.keys in ['', [], None]:  # No response was made
    key_resp_23.keys = None
thisExp.addData('key_resp_23.keys',key_resp_23.keys)
if key_resp_23.keys != None:  # we had a response
    thisExp.addData('key_resp_23.rt', key_resp_23.rt)
    thisExp.addData('key_resp_23.duration', key_resp_23.duration)
thisExp.nextEntry()
# the Routine "NomenAssoc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_24 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('countdown.xlsx'),
    seed=None, name='trials_24')
thisExp.addLoop(trials_24)  # add the loop to the experiment
thisTrial_24 = trials_24.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_24.rgb)
if thisTrial_24 != None:
    for paramName in thisTrial_24:
        exec('{} = thisTrial_24[paramName]'.format(paramName))

for thisTrial_24 in trials_24:
    currentLoop = trials_24
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_24.rgb)
    if thisTrial_24 != None:
        for paramName in thisTrial_24:
            exec('{} = thisTrial_24[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Count_down" ---
    continueRoutine = True
    # update component parameters for each repeat
    text_72.setColor(ccolor, colorSpace='rgb')
    text_72.setText(numberC)
    # keep track of which components have finished
    Count_downComponents = [text_72]
    for thisComponent in Count_downComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Count_down" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_72* updates
        
        # if text_72 is starting this frame...
        if text_72.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_72.frameNStart = frameN  # exact frame index
            text_72.tStart = t  # local t and not account for scr refresh
            text_72.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_72, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_72.started')
            # update status
            text_72.status = STARTED
            text_72.setAutoDraw(True)
        
        # if text_72 is active this frame...
        if text_72.status == STARTED:
            # update params
            pass
        
        # if text_72 is stopping this frame...
        if text_72.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_72.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_72.tStop = t  # not accounting for scr refresh
                text_72.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_72.stopped')
                # update status
                text_72.status = FINISHED
                text_72.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Count_downComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Count_down" ---
    for thisComponent in Count_downComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
# completed 1.0 repeats of 'trials_24'


# set up handler to look after randomisation of conditions etc
trials_22 = data.TrialHandler(nReps=5.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(Aexcel),
    seed=None, name='trials_22')
thisExp.addLoop(trials_22)  # add the loop to the experiment
thisTrial_22 = trials_22.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_22.rgb)
if thisTrial_22 != None:
    for paramName in thisTrial_22:
        exec('{} = thisTrial_22[paramName]'.format(paramName))

for thisTrial_22 in trials_22:
    currentLoop = trials_22
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_22.rgb)
    if thisTrial_22 != None:
        for paramName in thisTrial_22:
            exec('{} = thisTrial_22[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Cue_WM" ---
    continueRoutine = True
    # update component parameters for each repeat
    image_4.setImage(thepresentshape)
    # keep track of which components have finished
    Cue_WMComponents = [image_4, Crux_4, text_40]
    for thisComponent in Cue_WMComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Cue_WM" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_4* updates
        
        # if image_4 is starting this frame...
        if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_4.frameNStart = frameN  # exact frame index
            image_4.tStart = t  # local t and not account for scr refresh
            image_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_4.started')
            # update status
            image_4.status = STARTED
            image_4.setAutoDraw(True)
        
        # if image_4 is active this frame...
        if image_4.status == STARTED:
            # update params
            pass
        
        # if image_4 is stopping this frame...
        if image_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_4.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                image_4.tStop = t  # not accounting for scr refresh
                image_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_4.stopped')
                # update status
                image_4.status = FINISHED
                image_4.setAutoDraw(False)
        
        # *Crux_4* updates
        
        # if Crux_4 is starting this frame...
        if Crux_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Crux_4.frameNStart = frameN  # exact frame index
            Crux_4.tStart = t  # local t and not account for scr refresh
            Crux_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Crux_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Crux_4.started')
            # update status
            Crux_4.status = STARTED
            Crux_4.setAutoDraw(True)
        
        # if Crux_4 is active this frame...
        if Crux_4.status == STARTED:
            # update params
            pass
        
        # if Crux_4 is stopping this frame...
        if Crux_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Crux_4.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Crux_4.tStop = t  # not accounting for scr refresh
                Crux_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Crux_4.stopped')
                # update status
                Crux_4.status = FINISHED
                Crux_4.setAutoDraw(False)
        
        # *text_40* updates
        
        # if text_40 is starting this frame...
        if text_40.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_40.frameNStart = frameN  # exact frame index
            text_40.tStart = t  # local t and not account for scr refresh
            text_40.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_40, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_40.started')
            # update status
            text_40.status = STARTED
            text_40.setAutoDraw(True)
        
        # if text_40 is active this frame...
        if text_40.status == STARTED:
            # update params
            pass
        
        # if text_40 is stopping this frame...
        if text_40.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_40.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                text_40.tStop = t  # not accounting for scr refresh
                text_40.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_40.stopped')
                # update status
                text_40.status = FINISHED
                text_40.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Cue_WMComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Cue_WM" ---
    for thisComponent in Cue_WMComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_32
    circleSize = 0.3
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "Crucem_WM" ---
    continueRoutine = True
    # update component parameters for each repeat
    text_41.setText('+')
    # Run 'Begin Routine' code from code_34
    SCTime = math.floor(random.random() * 201 + 500) / 1000
    # keep track of which components have finished
    Crucem_WMComponents = [text_41, polygon_2]
    for thisComponent in Crucem_WMComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Crucem_WM" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_55
        
        if polygon_2.size[0] > 0:
            circleSize -= 0.03333333333;
        
        # *text_41* updates
        
        # if text_41 is starting this frame...
        if text_41.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_41.frameNStart = frameN  # exact frame index
            text_41.tStart = t  # local t and not account for scr refresh
            text_41.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_41, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_41.started')
            # update status
            text_41.status = STARTED
            text_41.setAutoDraw(True)
        
        # if text_41 is active this frame...
        if text_41.status == STARTED:
            # update params
            pass
        
        # if text_41 is stopping this frame...
        if text_41.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_41.tStartRefresh + SCTime-frameTolerance:
                # keep track of stop time/frame for later
                text_41.tStop = t  # not accounting for scr refresh
                text_41.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_41.stopped')
                # update status
                text_41.status = FINISHED
                text_41.setAutoDraw(False)
        
        # *polygon_2* updates
        
        # if polygon_2 is starting this frame...
        if polygon_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            polygon_2.frameNStart = frameN  # exact frame index
            polygon_2.tStart = t  # local t and not account for scr refresh
            polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            polygon_2.status = STARTED
            polygon_2.setAutoDraw(True)
        
        # if polygon_2 is active this frame...
        if polygon_2.status == STARTED:
            # update params
            polygon_2.setSize((circleSize, circleSize), log=False)
        
        # if polygon_2 is stopping this frame...
        if polygon_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_2.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                polygon_2.tStop = t  # not accounting for scr refresh
                polygon_2.frameNStop = frameN  # exact frame index
                # update status
                polygon_2.status = FINISHED
                polygon_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Crucem_WMComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Crucem_WM" ---
    for thisComponent in Crucem_WMComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Crucem_WM" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ERL" ---
    continueRoutine = True
    # update component parameters for each repeat
    Left_shape.setImage(left)
    Right_shape.setImage(right)
    Tilted_line.setPos([tiltposx,tiltposy])
    Tilted_line.setImage(tilt)
    Horizontal_line.setPos([dposx,dposy])
    Answer.keys = []
    Answer.rt = []
    _Answer_allKeys = []
    # keep track of which components have finished
    ERLComponents = [Left_shape, Right_shape, Tilted_line, Horizontal_line, Answer, Crux]
    for thisComponent in ERLComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ERL" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Left_shape* updates
        
        # if Left_shape is starting this frame...
        if Left_shape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Left_shape.frameNStart = frameN  # exact frame index
            Left_shape.tStart = t  # local t and not account for scr refresh
            Left_shape.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Left_shape, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Left_shape.started')
            # update status
            Left_shape.status = STARTED
            Left_shape.setAutoDraw(True)
        
        # if Left_shape is active this frame...
        if Left_shape.status == STARTED:
            # update params
            pass
        
        # if Left_shape is stopping this frame...
        if Left_shape.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Left_shape.tStartRefresh + 0.15-frameTolerance:
                # keep track of stop time/frame for later
                Left_shape.tStop = t  # not accounting for scr refresh
                Left_shape.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Left_shape.stopped')
                # update status
                Left_shape.status = FINISHED
                Left_shape.setAutoDraw(False)
        
        # *Right_shape* updates
        
        # if Right_shape is starting this frame...
        if Right_shape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Right_shape.frameNStart = frameN  # exact frame index
            Right_shape.tStart = t  # local t and not account for scr refresh
            Right_shape.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Right_shape, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Right_shape.started')
            # update status
            Right_shape.status = STARTED
            Right_shape.setAutoDraw(True)
        
        # if Right_shape is active this frame...
        if Right_shape.status == STARTED:
            # update params
            pass
        
        # if Right_shape is stopping this frame...
        if Right_shape.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Right_shape.tStartRefresh + 0.15-frameTolerance:
                # keep track of stop time/frame for later
                Right_shape.tStop = t  # not accounting for scr refresh
                Right_shape.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Right_shape.stopped')
                # update status
                Right_shape.status = FINISHED
                Right_shape.setAutoDraw(False)
        
        # *Tilted_line* updates
        
        # if Tilted_line is starting this frame...
        if Tilted_line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Tilted_line.frameNStart = frameN  # exact frame index
            Tilted_line.tStart = t  # local t and not account for scr refresh
            Tilted_line.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Tilted_line, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Tilted_line.started')
            # update status
            Tilted_line.status = STARTED
            Tilted_line.setAutoDraw(True)
        
        # if Tilted_line is active this frame...
        if Tilted_line.status == STARTED:
            # update params
            pass
        
        # if Tilted_line is stopping this frame...
        if Tilted_line.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Tilted_line.tStartRefresh + 0.15-frameTolerance:
                # keep track of stop time/frame for later
                Tilted_line.tStop = t  # not accounting for scr refresh
                Tilted_line.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Tilted_line.stopped')
                # update status
                Tilted_line.status = FINISHED
                Tilted_line.setAutoDraw(False)
        
        # *Horizontal_line* updates
        
        # if Horizontal_line is starting this frame...
        if Horizontal_line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Horizontal_line.frameNStart = frameN  # exact frame index
            Horizontal_line.tStart = t  # local t and not account for scr refresh
            Horizontal_line.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Horizontal_line, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Horizontal_line.started')
            # update status
            Horizontal_line.status = STARTED
            Horizontal_line.setAutoDraw(True)
        
        # if Horizontal_line is active this frame...
        if Horizontal_line.status == STARTED:
            # update params
            pass
        
        # if Horizontal_line is stopping this frame...
        if Horizontal_line.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Horizontal_line.tStartRefresh + 0.15-frameTolerance:
                # keep track of stop time/frame for later
                Horizontal_line.tStop = t  # not accounting for scr refresh
                Horizontal_line.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Horizontal_line.stopped')
                # update status
                Horizontal_line.status = FINISHED
                Horizontal_line.setAutoDraw(False)
        
        # *Answer* updates
        waitOnFlip = False
        
        # if Answer is starting this frame...
        if Answer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Answer.frameNStart = frameN  # exact frame index
            Answer.tStart = t  # local t and not account for scr refresh
            Answer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Answer, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Answer.started')
            # update status
            Answer.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Answer.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Answer.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if Answer is stopping this frame...
        if Answer.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Answer.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Answer.tStop = t  # not accounting for scr refresh
                Answer.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Answer.stopped')
                # update status
                Answer.status = FINISHED
                Answer.status = FINISHED
        if Answer.status == STARTED and not waitOnFlip:
            theseKeys = Answer.getKeys(keyList=['1','4'], waitRelease=False)
            _Answer_allKeys.extend(theseKeys)
            if len(_Answer_allKeys):
                Answer.keys = _Answer_allKeys[-1].name  # just the last key pressed
                Answer.rt = _Answer_allKeys[-1].rt
                Answer.duration = _Answer_allKeys[-1].duration
                # was this correct?
                if (Answer.keys == str(corkey)) or (Answer.keys == corkey):
                    Answer.corr = 1
                else:
                    Answer.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *Crux* updates
        
        # if Crux is starting this frame...
        if Crux.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Crux.frameNStart = frameN  # exact frame index
            Crux.tStart = t  # local t and not account for scr refresh
            Crux.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Crux, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Crux.started')
            # update status
            Crux.status = STARTED
            Crux.setAutoDraw(True)
        
        # if Crux is active this frame...
        if Crux.status == STARTED:
            # update params
            pass
        
        # if Crux is stopping this frame...
        if Crux.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Crux.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Crux.tStop = t  # not accounting for scr refresh
                Crux.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Crux.stopped')
                # update status
                Crux.status = FINISHED
                Crux.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ERLComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ERL" ---
    for thisComponent in ERLComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Answer.keys in ['', [], None]:  # No response was made
        Answer.keys = None
        # was no response the correct answer?!
        if str(corkey).lower() == 'none':
           Answer.corr = 1;  # correct non-response
        else:
           Answer.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_22 (TrialHandler)
    trials_22.addData('Answer.keys',Answer.keys)
    trials_22.addData('Answer.corr', Answer.corr)
    if Answer.keys != None:  # we had a response
        trials_22.addData('Answer.rt', Answer.rt)
        trials_22.addData('Answer.duration', Answer.duration)
    # Run 'End Routine' code from code_5
    if Answer.keys == "a":
        ERLloop = (ERLloop + 1)
    if Answer.keys == "l":
        ERLloop = (ERLloop + 1)
    
    
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "Feedback_ERL" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_2
    if Answer.corr:
        msg='Correct!'
        msgColor = "green"
    elif not Answer.keys:
        msg='Too slow'
        msgColor= "yellow"
    else:
        msg='Incorrect'
        msgColor = "red"
    Fodeback.setColor(msgColor, colorSpace='rgb')
    Fodeback.setText(msg)
    # keep track of which components have finished
    Feedback_ERLComponents = [Fodeback]
    for thisComponent in Feedback_ERLComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Feedback_ERL" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fodeback* updates
        
        # if Fodeback is starting this frame...
        if Fodeback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fodeback.frameNStart = frameN  # exact frame index
            Fodeback.tStart = t  # local t and not account for scr refresh
            Fodeback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fodeback, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Fodeback.started')
            # update status
            Fodeback.status = STARTED
            Fodeback.setAutoDraw(True)
        
        # if Fodeback is active this frame...
        if Fodeback.status == STARTED:
            # update params
            pass
        
        # if Fodeback is stopping this frame...
        if Fodeback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fodeback.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Fodeback.tStop = t  # not accounting for scr refresh
                Fodeback.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fodeback.stopped')
                # update status
                Fodeback.status = FINISHED
                Fodeback.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Feedback_ERLComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Feedback_ERL" ---
    for thisComponent in Feedback_ERLComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "SAVER_WM" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_36
    thisExp.addData('Task2',task)
    thisExp.addData('Validity2',validity)
    thisExp.addData('Cor2',Answer.corr)
    thisExp.addData('RT2',Answer.rt)
    # keep track of which components have finished
    SAVER_WMComponents = []
    for thisComponent in SAVER_WMComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "SAVER_WM" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SAVER_WMComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "SAVER_WM" ---
    for thisComponent in SAVER_WMComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "SAVER_WM" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Test" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_51
    
    # Set the probability of running the routine (20%)
    probability_of_running = 0.2
    
    # Determine whether to run the routine on this trial
    run_task_routine = random.random() < probability_of_running
    
    if not run_task_routine:
        continueRoutine = False  # Skip the routine if the condition is false
    
    
    Test_answer.keys = []
    Test_answer.rt = []
    _Test_answer_allKeys = []
    text_13.setText(logos)
    # keep track of which components have finished
    TestComponents = [Test_answer, text_5, text_12, text_13, text_23]
    for thisComponent in TestComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Test" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Test_answer* updates
        waitOnFlip = False
        
        # if Test_answer is starting this frame...
        if Test_answer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Test_answer.frameNStart = frameN  # exact frame index
            Test_answer.tStart = t  # local t and not account for scr refresh
            Test_answer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Test_answer, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Test_answer.started')
            # update status
            Test_answer.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Test_answer.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Test_answer.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if Test_answer is stopping this frame...
        if Test_answer.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Test_answer.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Test_answer.tStop = t  # not accounting for scr refresh
                Test_answer.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Test_answer.stopped')
                # update status
                Test_answer.status = FINISHED
                Test_answer.status = FINISHED
        if Test_answer.status == STARTED and not waitOnFlip:
            theseKeys = Test_answer.getKeys(keyList=['a','l'], waitRelease=False)
            _Test_answer_allKeys.extend(theseKeys)
            if len(_Test_answer_allKeys):
                Test_answer.keys = _Test_answer_allKeys[-1].name  # just the last key pressed
                Test_answer.rt = _Test_answer_allKeys[-1].rt
                Test_answer.duration = _Test_answer_allKeys[-1].duration
                # was this correct?
                if (Test_answer.keys == str(corkey2)) or (Test_answer.keys == corkey2):
                    Test_answer.corr = 1
                else:
                    Test_answer.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *text_5* updates
        
        # if text_5 is starting this frame...
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_5.started')
            # update status
            text_5.status = STARTED
            text_5.setAutoDraw(True)
        
        # if text_5 is active this frame...
        if text_5.status == STARTED:
            # update params
            pass
        
        # if text_5 is stopping this frame...
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_5.stopped')
                # update status
                text_5.status = FINISHED
                text_5.setAutoDraw(False)
        
        # *text_12* updates
        
        # if text_12 is starting this frame...
        if text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_12.frameNStart = frameN  # exact frame index
            text_12.tStart = t  # local t and not account for scr refresh
            text_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_12.started')
            # update status
            text_12.status = STARTED
            text_12.setAutoDraw(True)
        
        # if text_12 is active this frame...
        if text_12.status == STARTED:
            # update params
            pass
        
        # if text_12 is stopping this frame...
        if text_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_12.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_12.tStop = t  # not accounting for scr refresh
                text_12.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_12.stopped')
                # update status
                text_12.status = FINISHED
                text_12.setAutoDraw(False)
        
        # *text_13* updates
        
        # if text_13 is starting this frame...
        if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_13.frameNStart = frameN  # exact frame index
            text_13.tStart = t  # local t and not account for scr refresh
            text_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_13.started')
            # update status
            text_13.status = STARTED
            text_13.setAutoDraw(True)
        
        # if text_13 is active this frame...
        if text_13.status == STARTED:
            # update params
            pass
        
        # if text_13 is stopping this frame...
        if text_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_13.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_13.tStop = t  # not accounting for scr refresh
                text_13.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_13.stopped')
                # update status
                text_13.status = FINISHED
                text_13.setAutoDraw(False)
        
        # *text_23* updates
        
        # if text_23 is starting this frame...
        if text_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_23.frameNStart = frameN  # exact frame index
            text_23.tStart = t  # local t and not account for scr refresh
            text_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_23, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_23.started')
            # update status
            text_23.status = STARTED
            text_23.setAutoDraw(True)
        
        # if text_23 is active this frame...
        if text_23.status == STARTED:
            # update params
            pass
        
        # if text_23 is stopping this frame...
        if text_23.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_23.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_23.tStop = t  # not accounting for scr refresh
                text_23.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_23.stopped')
                # update status
                text_23.status = FINISHED
                text_23.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Test" ---
    for thisComponent in TestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Test_answer.keys in ['', [], None]:  # No response was made
        Test_answer.keys = None
        # was no response the correct answer?!
        if str(corkey2).lower() == 'none':
           Test_answer.corr = 1;  # correct non-response
        else:
           Test_answer.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_22 (TrialHandler)
    trials_22.addData('Test_answer.keys',Test_answer.keys)
    trials_22.addData('Test_answer.corr', Test_answer.corr)
    if Test_answer.keys != None:  # we had a response
        trials_22.addData('Test_answer.rt', Test_answer.rt)
        trials_22.addData('Test_answer.duration', Test_answer.duration)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "Test_feedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_3
    if Test_answer.corr:
        msg='Correct!'
        msgColor = "green"
    elif not Test_answer.keys:
        msg='Too slow'
        msgColor= "yellow"
    else:
        msg='Incorrect'
        msgColor = "red"
    text_6.setColor(msgColor, colorSpace='rgb')
    text_6.setText(msg)
    # Run 'Begin Routine' code from Rez
    if not run_task_routine:
        continueRoutine = False  # Skip the routine if the task routine was skipped
    
    # keep track of which components have finished
    Test_feedbackComponents = [text_6]
    for thisComponent in Test_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Test_feedback" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_6* updates
        
        # if text_6 is starting this frame...
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_6.started')
            # update status
            text_6.status = STARTED
            text_6.setAutoDraw(True)
        
        # if text_6 is active this frame...
        if text_6.status == STARTED:
            # update params
            pass
        
        # if text_6 is stopping this frame...
        if text_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_6.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_6.tStop = t  # not accounting for scr refresh
                text_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_6.stopped')
                # update status
                text_6.status = FINISHED
                text_6.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Test_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Test_feedback" ---
    for thisComponent in Test_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from Rez
    thisExp.addData('Congruence',corkey2)
    thisExp.addData('Cor3',Test_answer.corr)
    thisExp.addData('RT3',Test_answer.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "ERL_Break_Text" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_12
    if ERLloop == 214:
        Break_text = "You have completed approximately 10 minutes of this experiment.\n Take a break if you would like.\n You have 35 minutes left\n Press SPACE when you are ready to continue"
    text_7.setText(Break_text)
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    # keep track of which components have finished
    ERL_Break_TextComponents = [text_7, key_resp_5]
    for thisComponent in ERL_Break_TextComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ERL_Break_Text" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_4
        if ERLloop != 214:
            continueRoutine = False
        
        # *text_7* updates
        
        # if text_7 is starting this frame...
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_7.status = STARTED
            text_7.setAutoDraw(True)
        
        # if text_7 is active this frame...
        if text_7.status == STARTED:
            # update params
            pass
        
        # *key_resp_5* updates
        
        # if key_resp_5 is starting this frame...
        if key_resp_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            key_resp_5.clock.reset()  # now t=0
        if key_resp_5.status == STARTED:
            theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                key_resp_5.duration = _key_resp_5_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ERL_Break_TextComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ERL_Break_Text" ---
    for thisComponent in ERL_Break_TextComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    trials_22.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        trials_22.addData('key_resp_5.rt', key_resp_5.rt)
        trials_22.addData('key_resp_5.duration', key_resp_5.duration)
    # the Routine "ERL_Break_Text" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ERL_Me_Assoc_2" ---
    continueRoutine = True
    # update component parameters for each repeat
    image_41.setImage(Goodme)
    image_42.setImage(Badme)
    key_resp_52.keys = []
    key_resp_52.rt = []
    _key_resp_52_allKeys = []
    # keep track of which components have finished
    ERL_Me_Assoc_2Components = [image_41, image_42, text_127, text_128, key_resp_52, text_130]
    for thisComponent in ERL_Me_Assoc_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ERL_Me_Assoc_2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from B_Code_13
        if ERLloop != 214:
            continueRoutine = False
        
        # *image_41* updates
        
        # if image_41 is starting this frame...
        if image_41.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_41.frameNStart = frameN  # exact frame index
            image_41.tStart = t  # local t and not account for scr refresh
            image_41.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_41, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_41.status = STARTED
            image_41.setAutoDraw(True)
        
        # if image_41 is active this frame...
        if image_41.status == STARTED:
            # update params
            pass
        
        # *image_42* updates
        
        # if image_42 is starting this frame...
        if image_42.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_42.frameNStart = frameN  # exact frame index
            image_42.tStart = t  # local t and not account for scr refresh
            image_42.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_42, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_42.status = STARTED
            image_42.setAutoDraw(True)
        
        # if image_42 is active this frame...
        if image_42.status == STARTED:
            # update params
            pass
        
        # *text_127* updates
        
        # if text_127 is starting this frame...
        if text_127.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_127.frameNStart = frameN  # exact frame index
            text_127.tStart = t  # local t and not account for scr refresh
            text_127.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_127, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_127.status = STARTED
            text_127.setAutoDraw(True)
        
        # if text_127 is active this frame...
        if text_127.status == STARTED:
            # update params
            pass
        
        # *text_128* updates
        
        # if text_128 is starting this frame...
        if text_128.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_128.frameNStart = frameN  # exact frame index
            text_128.tStart = t  # local t and not account for scr refresh
            text_128.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_128, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_128.status = STARTED
            text_128.setAutoDraw(True)
        
        # if text_128 is active this frame...
        if text_128.status == STARTED:
            # update params
            pass
        
        # *key_resp_52* updates
        waitOnFlip = False
        
        # if key_resp_52 is starting this frame...
        if key_resp_52.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_52.frameNStart = frameN  # exact frame index
            key_resp_52.tStart = t  # local t and not account for scr refresh
            key_resp_52.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_52, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_52.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_52.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_52.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_52.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_52.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_52_allKeys.extend(theseKeys)
            if len(_key_resp_52_allKeys):
                key_resp_52.keys = _key_resp_52_allKeys[-1].name  # just the last key pressed
                key_resp_52.rt = _key_resp_52_allKeys[-1].rt
                key_resp_52.duration = _key_resp_52_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *text_130* updates
        
        # if text_130 is starting this frame...
        if text_130.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_130.frameNStart = frameN  # exact frame index
            text_130.tStart = t  # local t and not account for scr refresh
            text_130.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_130, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_130.status = STARTED
            text_130.setAutoDraw(True)
        
        # if text_130 is active this frame...
        if text_130.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ERL_Me_Assoc_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ERL_Me_Assoc_2" ---
    for thisComponent in ERL_Me_Assoc_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_52.keys in ['', [], None]:  # No response was made
        key_resp_52.keys = None
    trials_22.addData('key_resp_52.keys',key_resp_52.keys)
    if key_resp_52.keys != None:  # we had a response
        trials_22.addData('key_resp_52.rt', key_resp_52.rt)
        trials_22.addData('key_resp_52.duration', key_resp_52.duration)
    # the Routine "ERL_Me_Assoc_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ERL_Nomen_Assoc_2" ---
    continueRoutine = True
    # update component parameters for each repeat
    image_43.setImage(Goodother)
    image_44.setImage(Badother)
    text_131.setText("=" + " " + "Good" +" "+ Nomen)
    text_132.setText("=" + " " + "Bad" +" "+ Nomen)
    key_resp_53.keys = []
    key_resp_53.rt = []
    _key_resp_53_allKeys = []
    # keep track of which components have finished
    ERL_Nomen_Assoc_2Components = [image_43, image_44, text_131, text_132, key_resp_53, text_133]
    for thisComponent in ERL_Nomen_Assoc_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ERL_Nomen_Assoc_2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from B_Code_14
        if ERLloop != 214:
            continueRoutine = False
        
        # *image_43* updates
        
        # if image_43 is starting this frame...
        if image_43.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_43.frameNStart = frameN  # exact frame index
            image_43.tStart = t  # local t and not account for scr refresh
            image_43.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_43, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_43.status = STARTED
            image_43.setAutoDraw(True)
        
        # if image_43 is active this frame...
        if image_43.status == STARTED:
            # update params
            pass
        
        # *image_44* updates
        
        # if image_44 is starting this frame...
        if image_44.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_44.frameNStart = frameN  # exact frame index
            image_44.tStart = t  # local t and not account for scr refresh
            image_44.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_44, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_44.status = STARTED
            image_44.setAutoDraw(True)
        
        # if image_44 is active this frame...
        if image_44.status == STARTED:
            # update params
            pass
        
        # *text_131* updates
        
        # if text_131 is starting this frame...
        if text_131.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_131.frameNStart = frameN  # exact frame index
            text_131.tStart = t  # local t and not account for scr refresh
            text_131.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_131, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_131.status = STARTED
            text_131.setAutoDraw(True)
        
        # if text_131 is active this frame...
        if text_131.status == STARTED:
            # update params
            pass
        
        # *text_132* updates
        
        # if text_132 is starting this frame...
        if text_132.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_132.frameNStart = frameN  # exact frame index
            text_132.tStart = t  # local t and not account for scr refresh
            text_132.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_132, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_132.status = STARTED
            text_132.setAutoDraw(True)
        
        # if text_132 is active this frame...
        if text_132.status == STARTED:
            # update params
            pass
        
        # *key_resp_53* updates
        
        # if key_resp_53 is starting this frame...
        if key_resp_53.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_53.frameNStart = frameN  # exact frame index
            key_resp_53.tStart = t  # local t and not account for scr refresh
            key_resp_53.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_53, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_53.status = STARTED
            # keyboard checking is just starting
            key_resp_53.clock.reset()  # now t=0
        if key_resp_53.status == STARTED:
            theseKeys = key_resp_53.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_53_allKeys.extend(theseKeys)
            if len(_key_resp_53_allKeys):
                key_resp_53.keys = _key_resp_53_allKeys[-1].name  # just the last key pressed
                key_resp_53.rt = _key_resp_53_allKeys[-1].rt
                key_resp_53.duration = _key_resp_53_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *text_133* updates
        
        # if text_133 is starting this frame...
        if text_133.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_133.frameNStart = frameN  # exact frame index
            text_133.tStart = t  # local t and not account for scr refresh
            text_133.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_133, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_133.status = STARTED
            text_133.setAutoDraw(True)
        
        # if text_133 is active this frame...
        if text_133.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ERL_Nomen_Assoc_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ERL_Nomen_Assoc_2" ---
    for thisComponent in ERL_Nomen_Assoc_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_53.keys in ['', [], None]:  # No response was made
        key_resp_53.keys = None
    trials_22.addData('key_resp_53.keys',key_resp_53.keys)
    if key_resp_53.keys != None:  # we had a response
        trials_22.addData('key_resp_53.rt', key_resp_53.rt)
        trials_22.addData('key_resp_53.duration', key_resp_53.duration)
    # the Routine "ERL_Nomen_Assoc_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ERL_Me_Assoc_2" ---
    continueRoutine = True
    # update component parameters for each repeat
    image_41.setImage(Goodme)
    image_42.setImage(Badme)
    key_resp_52.keys = []
    key_resp_52.rt = []
    _key_resp_52_allKeys = []
    # keep track of which components have finished
    ERL_Me_Assoc_2Components = [image_41, image_42, text_127, text_128, key_resp_52, text_130]
    for thisComponent in ERL_Me_Assoc_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ERL_Me_Assoc_2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from B_Code_13
        if ERLloop != 214:
            continueRoutine = False
        
        # *image_41* updates
        
        # if image_41 is starting this frame...
        if image_41.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_41.frameNStart = frameN  # exact frame index
            image_41.tStart = t  # local t and not account for scr refresh
            image_41.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_41, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_41.status = STARTED
            image_41.setAutoDraw(True)
        
        # if image_41 is active this frame...
        if image_41.status == STARTED:
            # update params
            pass
        
        # *image_42* updates
        
        # if image_42 is starting this frame...
        if image_42.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_42.frameNStart = frameN  # exact frame index
            image_42.tStart = t  # local t and not account for scr refresh
            image_42.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_42, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_42.status = STARTED
            image_42.setAutoDraw(True)
        
        # if image_42 is active this frame...
        if image_42.status == STARTED:
            # update params
            pass
        
        # *text_127* updates
        
        # if text_127 is starting this frame...
        if text_127.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_127.frameNStart = frameN  # exact frame index
            text_127.tStart = t  # local t and not account for scr refresh
            text_127.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_127, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_127.status = STARTED
            text_127.setAutoDraw(True)
        
        # if text_127 is active this frame...
        if text_127.status == STARTED:
            # update params
            pass
        
        # *text_128* updates
        
        # if text_128 is starting this frame...
        if text_128.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_128.frameNStart = frameN  # exact frame index
            text_128.tStart = t  # local t and not account for scr refresh
            text_128.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_128, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_128.status = STARTED
            text_128.setAutoDraw(True)
        
        # if text_128 is active this frame...
        if text_128.status == STARTED:
            # update params
            pass
        
        # *key_resp_52* updates
        waitOnFlip = False
        
        # if key_resp_52 is starting this frame...
        if key_resp_52.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_52.frameNStart = frameN  # exact frame index
            key_resp_52.tStart = t  # local t and not account for scr refresh
            key_resp_52.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_52, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_52.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_52.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_52.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_52.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_52.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_52_allKeys.extend(theseKeys)
            if len(_key_resp_52_allKeys):
                key_resp_52.keys = _key_resp_52_allKeys[-1].name  # just the last key pressed
                key_resp_52.rt = _key_resp_52_allKeys[-1].rt
                key_resp_52.duration = _key_resp_52_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *text_130* updates
        
        # if text_130 is starting this frame...
        if text_130.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_130.frameNStart = frameN  # exact frame index
            text_130.tStart = t  # local t and not account for scr refresh
            text_130.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_130, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_130.status = STARTED
            text_130.setAutoDraw(True)
        
        # if text_130 is active this frame...
        if text_130.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ERL_Me_Assoc_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ERL_Me_Assoc_2" ---
    for thisComponent in ERL_Me_Assoc_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_52.keys in ['', [], None]:  # No response was made
        key_resp_52.keys = None
    trials_22.addData('key_resp_52.keys',key_resp_52.keys)
    if key_resp_52.keys != None:  # we had a response
        trials_22.addData('key_resp_52.rt', key_resp_52.rt)
        trials_22.addData('key_resp_52.duration', key_resp_52.duration)
    # the Routine "ERL_Me_Assoc_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ERL_Nomen_Assoc_2" ---
    continueRoutine = True
    # update component parameters for each repeat
    image_43.setImage(Goodother)
    image_44.setImage(Badother)
    text_131.setText("=" + " " + "Good" +" "+ Nomen)
    text_132.setText("=" + " " + "Bad" +" "+ Nomen)
    key_resp_53.keys = []
    key_resp_53.rt = []
    _key_resp_53_allKeys = []
    # keep track of which components have finished
    ERL_Nomen_Assoc_2Components = [image_43, image_44, text_131, text_132, key_resp_53, text_133]
    for thisComponent in ERL_Nomen_Assoc_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ERL_Nomen_Assoc_2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from B_Code_14
        if ERLloop != 214:
            continueRoutine = False
        
        # *image_43* updates
        
        # if image_43 is starting this frame...
        if image_43.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_43.frameNStart = frameN  # exact frame index
            image_43.tStart = t  # local t and not account for scr refresh
            image_43.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_43, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_43.status = STARTED
            image_43.setAutoDraw(True)
        
        # if image_43 is active this frame...
        if image_43.status == STARTED:
            # update params
            pass
        
        # *image_44* updates
        
        # if image_44 is starting this frame...
        if image_44.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_44.frameNStart = frameN  # exact frame index
            image_44.tStart = t  # local t and not account for scr refresh
            image_44.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_44, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_44.status = STARTED
            image_44.setAutoDraw(True)
        
        # if image_44 is active this frame...
        if image_44.status == STARTED:
            # update params
            pass
        
        # *text_131* updates
        
        # if text_131 is starting this frame...
        if text_131.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_131.frameNStart = frameN  # exact frame index
            text_131.tStart = t  # local t and not account for scr refresh
            text_131.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_131, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_131.status = STARTED
            text_131.setAutoDraw(True)
        
        # if text_131 is active this frame...
        if text_131.status == STARTED:
            # update params
            pass
        
        # *text_132* updates
        
        # if text_132 is starting this frame...
        if text_132.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_132.frameNStart = frameN  # exact frame index
            text_132.tStart = t  # local t and not account for scr refresh
            text_132.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_132, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_132.status = STARTED
            text_132.setAutoDraw(True)
        
        # if text_132 is active this frame...
        if text_132.status == STARTED:
            # update params
            pass
        
        # *key_resp_53* updates
        
        # if key_resp_53 is starting this frame...
        if key_resp_53.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_53.frameNStart = frameN  # exact frame index
            key_resp_53.tStart = t  # local t and not account for scr refresh
            key_resp_53.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_53, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_53.status = STARTED
            # keyboard checking is just starting
            key_resp_53.clock.reset()  # now t=0
        if key_resp_53.status == STARTED:
            theseKeys = key_resp_53.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_53_allKeys.extend(theseKeys)
            if len(_key_resp_53_allKeys):
                key_resp_53.keys = _key_resp_53_allKeys[-1].name  # just the last key pressed
                key_resp_53.rt = _key_resp_53_allKeys[-1].rt
                key_resp_53.duration = _key_resp_53_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *text_133* updates
        
        # if text_133 is starting this frame...
        if text_133.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_133.frameNStart = frameN  # exact frame index
            text_133.tStart = t  # local t and not account for scr refresh
            text_133.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_133, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_133.status = STARTED
            text_133.setAutoDraw(True)
        
        # if text_133 is active this frame...
        if text_133.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ERL_Nomen_Assoc_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ERL_Nomen_Assoc_2" ---
    for thisComponent in ERL_Nomen_Assoc_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_53.keys in ['', [], None]:  # No response was made
        key_resp_53.keys = None
    trials_22.addData('key_resp_53.keys',key_resp_53.keys)
    if key_resp_53.keys != None:  # we had a response
        trials_22.addData('key_resp_53.rt', key_resp_53.rt)
        trials_22.addData('key_resp_53.duration', key_resp_53.duration)
    # the Routine "ERL_Nomen_Assoc_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_19 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('countdown.xlsx'),
        seed=None, name='trials_19')
    thisExp.addLoop(trials_19)  # add the loop to the experiment
    thisTrial_19 = trials_19.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_19.rgb)
    if thisTrial_19 != None:
        for paramName in thisTrial_19:
            exec('{} = thisTrial_19[paramName]'.format(paramName))
    
    for thisTrial_19 in trials_19:
        currentLoop = trials_19
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_19.rgb)
        if thisTrial_19 != None:
            for paramName in thisTrial_19:
                exec('{} = thisTrial_19[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "ERL_CD" ---
        continueRoutine = True
        # update component parameters for each repeat
        text_134.setColor(ccolor, colorSpace='rgb')
        text_134.setText(numberC)
        # keep track of which components have finished
        ERL_CDComponents = [text_134]
        for thisComponent in ERL_CDComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ERL_CD" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from B_Code_15
            if ERLloop != 214:
                continueRoutine = False
            
            # *text_134* updates
            
            # if text_134 is starting this frame...
            if text_134.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_134.frameNStart = frameN  # exact frame index
                text_134.tStart = t  # local t and not account for scr refresh
                text_134.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_134, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_134.status = STARTED
                text_134.setAutoDraw(True)
            
            # if text_134 is active this frame...
            if text_134.status == STARTED:
                # update params
                pass
            
            # if text_134 is stopping this frame...
            if text_134.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_134.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_134.tStop = t  # not accounting for scr refresh
                    text_134.frameNStop = frameN  # exact frame index
                    # update status
                    text_134.status = FINISHED
                    text_134.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ERL_CDComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ERL_CD" ---
        for thisComponent in ERL_CDComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
    # completed 1.0 repeats of 'trials_19'
    
    
    # --- Prepare to start Routine "ERL_Break_Text_2" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_14
    
    if ERLloop == 429:
        Break_text = "You have completed approximately 20 minutes of this experiment.\n Take a break if you would like.\n You have 25 minutes left\n Press SPACE when you are ready to continue"
    text_8.setText(Break_text)
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    # keep track of which components have finished
    ERL_Break_Text_2Components = [text_8, key_resp_6]
    for thisComponent in ERL_Break_Text_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ERL_Break_Text_2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_13
        if ERLloop != 429:
            continueRoutine = False
        
        # *text_8* updates
        
        # if text_8 is starting this frame...
        if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_8.status = STARTED
            text_8.setAutoDraw(True)
        
        # if text_8 is active this frame...
        if text_8.status == STARTED:
            # update params
            pass
        
        # *key_resp_6* updates
        
        # if key_resp_6 is starting this frame...
        if key_resp_6.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            key_resp_6.clock.reset()  # now t=0
        if key_resp_6.status == STARTED:
            theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                key_resp_6.duration = _key_resp_6_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ERL_Break_Text_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ERL_Break_Text_2" ---
    for thisComponent in ERL_Break_Text_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    trials_22.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        trials_22.addData('key_resp_6.rt', key_resp_6.rt)
        trials_22.addData('key_resp_6.duration', key_resp_6.duration)
    # the Routine "ERL_Break_Text_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ERL_Me_Assoc_3" ---
    continueRoutine = True
    # update component parameters for each repeat
    image_45.setImage(Goodme)
    image_46.setImage(Badme)
    key_resp_55.keys = []
    key_resp_55.rt = []
    _key_resp_55_allKeys = []
    # keep track of which components have finished
    ERL_Me_Assoc_3Components = [image_45, image_46, text_135, text_136, key_resp_55, text_137]
    for thisComponent in ERL_Me_Assoc_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ERL_Me_Assoc_3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from B_Code_16
        if ERLloop != 429:
            continueRoutine = False
        
        # *image_45* updates
        
        # if image_45 is starting this frame...
        if image_45.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_45.frameNStart = frameN  # exact frame index
            image_45.tStart = t  # local t and not account for scr refresh
            image_45.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_45, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_45.status = STARTED
            image_45.setAutoDraw(True)
        
        # if image_45 is active this frame...
        if image_45.status == STARTED:
            # update params
            pass
        
        # *image_46* updates
        
        # if image_46 is starting this frame...
        if image_46.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_46.frameNStart = frameN  # exact frame index
            image_46.tStart = t  # local t and not account for scr refresh
            image_46.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_46, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_46.status = STARTED
            image_46.setAutoDraw(True)
        
        # if image_46 is active this frame...
        if image_46.status == STARTED:
            # update params
            pass
        
        # *text_135* updates
        
        # if text_135 is starting this frame...
        if text_135.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_135.frameNStart = frameN  # exact frame index
            text_135.tStart = t  # local t and not account for scr refresh
            text_135.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_135, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_135.status = STARTED
            text_135.setAutoDraw(True)
        
        # if text_135 is active this frame...
        if text_135.status == STARTED:
            # update params
            pass
        
        # *text_136* updates
        
        # if text_136 is starting this frame...
        if text_136.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_136.frameNStart = frameN  # exact frame index
            text_136.tStart = t  # local t and not account for scr refresh
            text_136.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_136, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_136.status = STARTED
            text_136.setAutoDraw(True)
        
        # if text_136 is active this frame...
        if text_136.status == STARTED:
            # update params
            pass
        
        # *key_resp_55* updates
        waitOnFlip = False
        
        # if key_resp_55 is starting this frame...
        if key_resp_55.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_55.frameNStart = frameN  # exact frame index
            key_resp_55.tStart = t  # local t and not account for scr refresh
            key_resp_55.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_55, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_55.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_55.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_55.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_55.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_55.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_55_allKeys.extend(theseKeys)
            if len(_key_resp_55_allKeys):
                key_resp_55.keys = _key_resp_55_allKeys[-1].name  # just the last key pressed
                key_resp_55.rt = _key_resp_55_allKeys[-1].rt
                key_resp_55.duration = _key_resp_55_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *text_137* updates
        
        # if text_137 is starting this frame...
        if text_137.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_137.frameNStart = frameN  # exact frame index
            text_137.tStart = t  # local t and not account for scr refresh
            text_137.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_137, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_137.status = STARTED
            text_137.setAutoDraw(True)
        
        # if text_137 is active this frame...
        if text_137.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ERL_Me_Assoc_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ERL_Me_Assoc_3" ---
    for thisComponent in ERL_Me_Assoc_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_55.keys in ['', [], None]:  # No response was made
        key_resp_55.keys = None
    trials_22.addData('key_resp_55.keys',key_resp_55.keys)
    if key_resp_55.keys != None:  # we had a response
        trials_22.addData('key_resp_55.rt', key_resp_55.rt)
        trials_22.addData('key_resp_55.duration', key_resp_55.duration)
    # the Routine "ERL_Me_Assoc_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ERL_Nomen_Assoc_3" ---
    continueRoutine = True
    # update component parameters for each repeat
    image_47.setImage(Goodother)
    image_48.setImage(Badother)
    text_138.setText("=" + " " + "Good" +" "+ Nomen)
    text_139.setText("=" + " " + "Bad" +" "+ Nomen)
    key_resp_56.keys = []
    key_resp_56.rt = []
    _key_resp_56_allKeys = []
    # keep track of which components have finished
    ERL_Nomen_Assoc_3Components = [image_47, image_48, text_138, text_139, key_resp_56, text_140]
    for thisComponent in ERL_Nomen_Assoc_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ERL_Nomen_Assoc_3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from B_Code_17
        if ERLloop != 429:
            continueRoutine = False
        
        # *image_47* updates
        
        # if image_47 is starting this frame...
        if image_47.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_47.frameNStart = frameN  # exact frame index
            image_47.tStart = t  # local t and not account for scr refresh
            image_47.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_47, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_47.status = STARTED
            image_47.setAutoDraw(True)
        
        # if image_47 is active this frame...
        if image_47.status == STARTED:
            # update params
            pass
        
        # *image_48* updates
        
        # if image_48 is starting this frame...
        if image_48.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_48.frameNStart = frameN  # exact frame index
            image_48.tStart = t  # local t and not account for scr refresh
            image_48.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_48, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_48.status = STARTED
            image_48.setAutoDraw(True)
        
        # if image_48 is active this frame...
        if image_48.status == STARTED:
            # update params
            pass
        
        # *text_138* updates
        
        # if text_138 is starting this frame...
        if text_138.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_138.frameNStart = frameN  # exact frame index
            text_138.tStart = t  # local t and not account for scr refresh
            text_138.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_138, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_138.status = STARTED
            text_138.setAutoDraw(True)
        
        # if text_138 is active this frame...
        if text_138.status == STARTED:
            # update params
            pass
        
        # *text_139* updates
        
        # if text_139 is starting this frame...
        if text_139.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_139.frameNStart = frameN  # exact frame index
            text_139.tStart = t  # local t and not account for scr refresh
            text_139.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_139, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_139.status = STARTED
            text_139.setAutoDraw(True)
        
        # if text_139 is active this frame...
        if text_139.status == STARTED:
            # update params
            pass
        
        # *key_resp_56* updates
        
        # if key_resp_56 is starting this frame...
        if key_resp_56.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_56.frameNStart = frameN  # exact frame index
            key_resp_56.tStart = t  # local t and not account for scr refresh
            key_resp_56.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_56, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_56.status = STARTED
            # keyboard checking is just starting
            key_resp_56.clock.reset()  # now t=0
        if key_resp_56.status == STARTED:
            theseKeys = key_resp_56.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_56_allKeys.extend(theseKeys)
            if len(_key_resp_56_allKeys):
                key_resp_56.keys = _key_resp_56_allKeys[-1].name  # just the last key pressed
                key_resp_56.rt = _key_resp_56_allKeys[-1].rt
                key_resp_56.duration = _key_resp_56_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *text_140* updates
        
        # if text_140 is starting this frame...
        if text_140.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_140.frameNStart = frameN  # exact frame index
            text_140.tStart = t  # local t and not account for scr refresh
            text_140.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_140, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_140.status = STARTED
            text_140.setAutoDraw(True)
        
        # if text_140 is active this frame...
        if text_140.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ERL_Nomen_Assoc_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ERL_Nomen_Assoc_3" ---
    for thisComponent in ERL_Nomen_Assoc_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_56.keys in ['', [], None]:  # No response was made
        key_resp_56.keys = None
    trials_22.addData('key_resp_56.keys',key_resp_56.keys)
    if key_resp_56.keys != None:  # we had a response
        trials_22.addData('key_resp_56.rt', key_resp_56.rt)
        trials_22.addData('key_resp_56.duration', key_resp_56.duration)
    # the Routine "ERL_Nomen_Assoc_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ERL_Me_Assoc_3" ---
    continueRoutine = True
    # update component parameters for each repeat
    image_45.setImage(Goodme)
    image_46.setImage(Badme)
    key_resp_55.keys = []
    key_resp_55.rt = []
    _key_resp_55_allKeys = []
    # keep track of which components have finished
    ERL_Me_Assoc_3Components = [image_45, image_46, text_135, text_136, key_resp_55, text_137]
    for thisComponent in ERL_Me_Assoc_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ERL_Me_Assoc_3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from B_Code_16
        if ERLloop != 429:
            continueRoutine = False
        
        # *image_45* updates
        
        # if image_45 is starting this frame...
        if image_45.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_45.frameNStart = frameN  # exact frame index
            image_45.tStart = t  # local t and not account for scr refresh
            image_45.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_45, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_45.status = STARTED
            image_45.setAutoDraw(True)
        
        # if image_45 is active this frame...
        if image_45.status == STARTED:
            # update params
            pass
        
        # *image_46* updates
        
        # if image_46 is starting this frame...
        if image_46.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_46.frameNStart = frameN  # exact frame index
            image_46.tStart = t  # local t and not account for scr refresh
            image_46.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_46, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_46.status = STARTED
            image_46.setAutoDraw(True)
        
        # if image_46 is active this frame...
        if image_46.status == STARTED:
            # update params
            pass
        
        # *text_135* updates
        
        # if text_135 is starting this frame...
        if text_135.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_135.frameNStart = frameN  # exact frame index
            text_135.tStart = t  # local t and not account for scr refresh
            text_135.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_135, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_135.status = STARTED
            text_135.setAutoDraw(True)
        
        # if text_135 is active this frame...
        if text_135.status == STARTED:
            # update params
            pass
        
        # *text_136* updates
        
        # if text_136 is starting this frame...
        if text_136.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_136.frameNStart = frameN  # exact frame index
            text_136.tStart = t  # local t and not account for scr refresh
            text_136.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_136, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_136.status = STARTED
            text_136.setAutoDraw(True)
        
        # if text_136 is active this frame...
        if text_136.status == STARTED:
            # update params
            pass
        
        # *key_resp_55* updates
        waitOnFlip = False
        
        # if key_resp_55 is starting this frame...
        if key_resp_55.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_55.frameNStart = frameN  # exact frame index
            key_resp_55.tStart = t  # local t and not account for scr refresh
            key_resp_55.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_55, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_55.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_55.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_55.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_55.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_55.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_55_allKeys.extend(theseKeys)
            if len(_key_resp_55_allKeys):
                key_resp_55.keys = _key_resp_55_allKeys[-1].name  # just the last key pressed
                key_resp_55.rt = _key_resp_55_allKeys[-1].rt
                key_resp_55.duration = _key_resp_55_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *text_137* updates
        
        # if text_137 is starting this frame...
        if text_137.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_137.frameNStart = frameN  # exact frame index
            text_137.tStart = t  # local t and not account for scr refresh
            text_137.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_137, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_137.status = STARTED
            text_137.setAutoDraw(True)
        
        # if text_137 is active this frame...
        if text_137.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ERL_Me_Assoc_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ERL_Me_Assoc_3" ---
    for thisComponent in ERL_Me_Assoc_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_55.keys in ['', [], None]:  # No response was made
        key_resp_55.keys = None
    trials_22.addData('key_resp_55.keys',key_resp_55.keys)
    if key_resp_55.keys != None:  # we had a response
        trials_22.addData('key_resp_55.rt', key_resp_55.rt)
        trials_22.addData('key_resp_55.duration', key_resp_55.duration)
    # the Routine "ERL_Me_Assoc_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ERL_Nomen_Assoc_3" ---
    continueRoutine = True
    # update component parameters for each repeat
    image_47.setImage(Goodother)
    image_48.setImage(Badother)
    text_138.setText("=" + " " + "Good" +" "+ Nomen)
    text_139.setText("=" + " " + "Bad" +" "+ Nomen)
    key_resp_56.keys = []
    key_resp_56.rt = []
    _key_resp_56_allKeys = []
    # keep track of which components have finished
    ERL_Nomen_Assoc_3Components = [image_47, image_48, text_138, text_139, key_resp_56, text_140]
    for thisComponent in ERL_Nomen_Assoc_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ERL_Nomen_Assoc_3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from B_Code_17
        if ERLloop != 429:
            continueRoutine = False
        
        # *image_47* updates
        
        # if image_47 is starting this frame...
        if image_47.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_47.frameNStart = frameN  # exact frame index
            image_47.tStart = t  # local t and not account for scr refresh
            image_47.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_47, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_47.status = STARTED
            image_47.setAutoDraw(True)
        
        # if image_47 is active this frame...
        if image_47.status == STARTED:
            # update params
            pass
        
        # *image_48* updates
        
        # if image_48 is starting this frame...
        if image_48.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_48.frameNStart = frameN  # exact frame index
            image_48.tStart = t  # local t and not account for scr refresh
            image_48.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_48, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_48.status = STARTED
            image_48.setAutoDraw(True)
        
        # if image_48 is active this frame...
        if image_48.status == STARTED:
            # update params
            pass
        
        # *text_138* updates
        
        # if text_138 is starting this frame...
        if text_138.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_138.frameNStart = frameN  # exact frame index
            text_138.tStart = t  # local t and not account for scr refresh
            text_138.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_138, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_138.status = STARTED
            text_138.setAutoDraw(True)
        
        # if text_138 is active this frame...
        if text_138.status == STARTED:
            # update params
            pass
        
        # *text_139* updates
        
        # if text_139 is starting this frame...
        if text_139.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_139.frameNStart = frameN  # exact frame index
            text_139.tStart = t  # local t and not account for scr refresh
            text_139.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_139, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_139.status = STARTED
            text_139.setAutoDraw(True)
        
        # if text_139 is active this frame...
        if text_139.status == STARTED:
            # update params
            pass
        
        # *key_resp_56* updates
        
        # if key_resp_56 is starting this frame...
        if key_resp_56.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_56.frameNStart = frameN  # exact frame index
            key_resp_56.tStart = t  # local t and not account for scr refresh
            key_resp_56.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_56, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_56.status = STARTED
            # keyboard checking is just starting
            key_resp_56.clock.reset()  # now t=0
        if key_resp_56.status == STARTED:
            theseKeys = key_resp_56.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_56_allKeys.extend(theseKeys)
            if len(_key_resp_56_allKeys):
                key_resp_56.keys = _key_resp_56_allKeys[-1].name  # just the last key pressed
                key_resp_56.rt = _key_resp_56_allKeys[-1].rt
                key_resp_56.duration = _key_resp_56_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *text_140* updates
        
        # if text_140 is starting this frame...
        if text_140.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_140.frameNStart = frameN  # exact frame index
            text_140.tStart = t  # local t and not account for scr refresh
            text_140.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_140, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_140.status = STARTED
            text_140.setAutoDraw(True)
        
        # if text_140 is active this frame...
        if text_140.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ERL_Nomen_Assoc_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ERL_Nomen_Assoc_3" ---
    for thisComponent in ERL_Nomen_Assoc_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_56.keys in ['', [], None]:  # No response was made
        key_resp_56.keys = None
    trials_22.addData('key_resp_56.keys',key_resp_56.keys)
    if key_resp_56.keys != None:  # we had a response
        trials_22.addData('key_resp_56.rt', key_resp_56.rt)
        trials_22.addData('key_resp_56.duration', key_resp_56.duration)
    # the Routine "ERL_Nomen_Assoc_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_21 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('countdown.xlsx'),
        seed=None, name='trials_21')
    thisExp.addLoop(trials_21)  # add the loop to the experiment
    thisTrial_21 = trials_21.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_21.rgb)
    if thisTrial_21 != None:
        for paramName in thisTrial_21:
            exec('{} = thisTrial_21[paramName]'.format(paramName))
    
    for thisTrial_21 in trials_21:
        currentLoop = trials_21
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_21.rgb)
        if thisTrial_21 != None:
            for paramName in thisTrial_21:
                exec('{} = thisTrial_21[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "ERL_CD_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        text_141.setColor(ccolor, colorSpace='rgb')
        text_141.setText(numberC)
        # keep track of which components have finished
        ERL_CD_2Components = [text_141]
        for thisComponent in ERL_CD_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ERL_CD_2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from B_Code_18
            if ERLloop != 429:
                continueRoutine = False
            
            # *text_141* updates
            
            # if text_141 is starting this frame...
            if text_141.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_141.frameNStart = frameN  # exact frame index
                text_141.tStart = t  # local t and not account for scr refresh
                text_141.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_141, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_141.status = STARTED
                text_141.setAutoDraw(True)
            
            # if text_141 is active this frame...
            if text_141.status == STARTED:
                # update params
                pass
            
            # if text_141 is stopping this frame...
            if text_141.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_141.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_141.tStop = t  # not accounting for scr refresh
                    text_141.frameNStop = frameN  # exact frame index
                    # update status
                    text_141.status = FINISHED
                    text_141.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ERL_CD_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ERL_CD_2" ---
        for thisComponent in ERL_CD_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
    # completed 1.0 repeats of 'trials_21'
    
    
    # --- Prepare to start Routine "ERL_Break_Text_3" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_16
    if ERLloop == 643:
        Break_text = "You have completed approximately 30 minutes of this experiment.\n Take a break if you would like.\n You have 15 minutes left\n Press SPACE when you are ready to continue"
    text_9.setText(Break_text)
    key_resp_7.keys = []
    key_resp_7.rt = []
    _key_resp_7_allKeys = []
    # keep track of which components have finished
    ERL_Break_Text_3Components = [text_9, key_resp_7]
    for thisComponent in ERL_Break_Text_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ERL_Break_Text_3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_15
        if ERLloop != 643:
            continueRoutine = False
        
        # *text_9* updates
        
        # if text_9 is starting this frame...
        if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_9.frameNStart = frameN  # exact frame index
            text_9.tStart = t  # local t and not account for scr refresh
            text_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_9.status = STARTED
            text_9.setAutoDraw(True)
        
        # if text_9 is active this frame...
        if text_9.status == STARTED:
            # update params
            pass
        
        # *key_resp_7* updates
        
        # if key_resp_7 is starting this frame...
        if key_resp_7.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.tStart = t  # local t and not account for scr refresh
            key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            key_resp_7.clock.reset()  # now t=0
        if key_resp_7.status == STARTED:
            theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_7_allKeys.extend(theseKeys)
            if len(_key_resp_7_allKeys):
                key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                key_resp_7.duration = _key_resp_7_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ERL_Break_Text_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ERL_Break_Text_3" ---
    for thisComponent in ERL_Break_Text_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys = None
    trials_22.addData('key_resp_7.keys',key_resp_7.keys)
    if key_resp_7.keys != None:  # we had a response
        trials_22.addData('key_resp_7.rt', key_resp_7.rt)
        trials_22.addData('key_resp_7.duration', key_resp_7.duration)
    # the Routine "ERL_Break_Text_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ERL_Me_Assoc_4" ---
    continueRoutine = True
    # update component parameters for each repeat
    image_49.setImage(Goodme)
    image_50.setImage(Badme)
    key_resp_57.keys = []
    key_resp_57.rt = []
    _key_resp_57_allKeys = []
    # keep track of which components have finished
    ERL_Me_Assoc_4Components = [image_49, image_50, text_142, text_143, key_resp_57, text_144]
    for thisComponent in ERL_Me_Assoc_4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ERL_Me_Assoc_4" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from B_Code_19
        if ERLloop != 643:
            continueRoutine = False
        
        # *image_49* updates
        
        # if image_49 is starting this frame...
        if image_49.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_49.frameNStart = frameN  # exact frame index
            image_49.tStart = t  # local t and not account for scr refresh
            image_49.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_49, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_49.status = STARTED
            image_49.setAutoDraw(True)
        
        # if image_49 is active this frame...
        if image_49.status == STARTED:
            # update params
            pass
        
        # *image_50* updates
        
        # if image_50 is starting this frame...
        if image_50.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_50.frameNStart = frameN  # exact frame index
            image_50.tStart = t  # local t and not account for scr refresh
            image_50.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_50, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_50.status = STARTED
            image_50.setAutoDraw(True)
        
        # if image_50 is active this frame...
        if image_50.status == STARTED:
            # update params
            pass
        
        # *text_142* updates
        
        # if text_142 is starting this frame...
        if text_142.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_142.frameNStart = frameN  # exact frame index
            text_142.tStart = t  # local t and not account for scr refresh
            text_142.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_142, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_142.status = STARTED
            text_142.setAutoDraw(True)
        
        # if text_142 is active this frame...
        if text_142.status == STARTED:
            # update params
            pass
        
        # *text_143* updates
        
        # if text_143 is starting this frame...
        if text_143.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_143.frameNStart = frameN  # exact frame index
            text_143.tStart = t  # local t and not account for scr refresh
            text_143.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_143, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_143.status = STARTED
            text_143.setAutoDraw(True)
        
        # if text_143 is active this frame...
        if text_143.status == STARTED:
            # update params
            pass
        
        # *key_resp_57* updates
        waitOnFlip = False
        
        # if key_resp_57 is starting this frame...
        if key_resp_57.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_57.frameNStart = frameN  # exact frame index
            key_resp_57.tStart = t  # local t and not account for scr refresh
            key_resp_57.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_57, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_57.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_57.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_57.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_57.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_57.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_57_allKeys.extend(theseKeys)
            if len(_key_resp_57_allKeys):
                key_resp_57.keys = _key_resp_57_allKeys[-1].name  # just the last key pressed
                key_resp_57.rt = _key_resp_57_allKeys[-1].rt
                key_resp_57.duration = _key_resp_57_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *text_144* updates
        
        # if text_144 is starting this frame...
        if text_144.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_144.frameNStart = frameN  # exact frame index
            text_144.tStart = t  # local t and not account for scr refresh
            text_144.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_144, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_144.status = STARTED
            text_144.setAutoDraw(True)
        
        # if text_144 is active this frame...
        if text_144.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ERL_Me_Assoc_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ERL_Me_Assoc_4" ---
    for thisComponent in ERL_Me_Assoc_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_57.keys in ['', [], None]:  # No response was made
        key_resp_57.keys = None
    trials_22.addData('key_resp_57.keys',key_resp_57.keys)
    if key_resp_57.keys != None:  # we had a response
        trials_22.addData('key_resp_57.rt', key_resp_57.rt)
        trials_22.addData('key_resp_57.duration', key_resp_57.duration)
    # the Routine "ERL_Me_Assoc_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ERL_Nomen_Assoc_4" ---
    continueRoutine = True
    # update component parameters for each repeat
    image_51.setImage(Goodother)
    image_52.setImage(Badother)
    text_145.setText("=" + " " + "Good" +" "+ Nomen)
    text_146.setText("=" + " " + "Bad" +" "+ Nomen)
    key_resp_58.keys = []
    key_resp_58.rt = []
    _key_resp_58_allKeys = []
    # keep track of which components have finished
    ERL_Nomen_Assoc_4Components = [image_51, image_52, text_145, text_146, key_resp_58, text_147]
    for thisComponent in ERL_Nomen_Assoc_4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ERL_Nomen_Assoc_4" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from B_Code_20
        if ERLloop != 643:
            continueRoutine = False
        
        # *image_51* updates
        
        # if image_51 is starting this frame...
        if image_51.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_51.frameNStart = frameN  # exact frame index
            image_51.tStart = t  # local t and not account for scr refresh
            image_51.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_51, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_51.status = STARTED
            image_51.setAutoDraw(True)
        
        # if image_51 is active this frame...
        if image_51.status == STARTED:
            # update params
            pass
        
        # *image_52* updates
        
        # if image_52 is starting this frame...
        if image_52.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_52.frameNStart = frameN  # exact frame index
            image_52.tStart = t  # local t and not account for scr refresh
            image_52.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_52, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_52.status = STARTED
            image_52.setAutoDraw(True)
        
        # if image_52 is active this frame...
        if image_52.status == STARTED:
            # update params
            pass
        
        # *text_145* updates
        
        # if text_145 is starting this frame...
        if text_145.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_145.frameNStart = frameN  # exact frame index
            text_145.tStart = t  # local t and not account for scr refresh
            text_145.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_145, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_145.status = STARTED
            text_145.setAutoDraw(True)
        
        # if text_145 is active this frame...
        if text_145.status == STARTED:
            # update params
            pass
        
        # *text_146* updates
        
        # if text_146 is starting this frame...
        if text_146.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_146.frameNStart = frameN  # exact frame index
            text_146.tStart = t  # local t and not account for scr refresh
            text_146.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_146, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_146.status = STARTED
            text_146.setAutoDraw(True)
        
        # if text_146 is active this frame...
        if text_146.status == STARTED:
            # update params
            pass
        
        # *key_resp_58* updates
        
        # if key_resp_58 is starting this frame...
        if key_resp_58.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_58.frameNStart = frameN  # exact frame index
            key_resp_58.tStart = t  # local t and not account for scr refresh
            key_resp_58.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_58, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_58.status = STARTED
            # keyboard checking is just starting
            key_resp_58.clock.reset()  # now t=0
        if key_resp_58.status == STARTED:
            theseKeys = key_resp_58.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_58_allKeys.extend(theseKeys)
            if len(_key_resp_58_allKeys):
                key_resp_58.keys = _key_resp_58_allKeys[-1].name  # just the last key pressed
                key_resp_58.rt = _key_resp_58_allKeys[-1].rt
                key_resp_58.duration = _key_resp_58_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *text_147* updates
        
        # if text_147 is starting this frame...
        if text_147.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_147.frameNStart = frameN  # exact frame index
            text_147.tStart = t  # local t and not account for scr refresh
            text_147.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_147, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_147.status = STARTED
            text_147.setAutoDraw(True)
        
        # if text_147 is active this frame...
        if text_147.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ERL_Nomen_Assoc_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ERL_Nomen_Assoc_4" ---
    for thisComponent in ERL_Nomen_Assoc_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_58.keys in ['', [], None]:  # No response was made
        key_resp_58.keys = None
    trials_22.addData('key_resp_58.keys',key_resp_58.keys)
    if key_resp_58.keys != None:  # we had a response
        trials_22.addData('key_resp_58.rt', key_resp_58.rt)
        trials_22.addData('key_resp_58.duration', key_resp_58.duration)
    # the Routine "ERL_Nomen_Assoc_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ERL_Me_Assoc_4" ---
    continueRoutine = True
    # update component parameters for each repeat
    image_49.setImage(Goodme)
    image_50.setImage(Badme)
    key_resp_57.keys = []
    key_resp_57.rt = []
    _key_resp_57_allKeys = []
    # keep track of which components have finished
    ERL_Me_Assoc_4Components = [image_49, image_50, text_142, text_143, key_resp_57, text_144]
    for thisComponent in ERL_Me_Assoc_4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ERL_Me_Assoc_4" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from B_Code_19
        if ERLloop != 643:
            continueRoutine = False
        
        # *image_49* updates
        
        # if image_49 is starting this frame...
        if image_49.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_49.frameNStart = frameN  # exact frame index
            image_49.tStart = t  # local t and not account for scr refresh
            image_49.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_49, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_49.status = STARTED
            image_49.setAutoDraw(True)
        
        # if image_49 is active this frame...
        if image_49.status == STARTED:
            # update params
            pass
        
        # *image_50* updates
        
        # if image_50 is starting this frame...
        if image_50.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_50.frameNStart = frameN  # exact frame index
            image_50.tStart = t  # local t and not account for scr refresh
            image_50.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_50, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_50.status = STARTED
            image_50.setAutoDraw(True)
        
        # if image_50 is active this frame...
        if image_50.status == STARTED:
            # update params
            pass
        
        # *text_142* updates
        
        # if text_142 is starting this frame...
        if text_142.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_142.frameNStart = frameN  # exact frame index
            text_142.tStart = t  # local t and not account for scr refresh
            text_142.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_142, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_142.status = STARTED
            text_142.setAutoDraw(True)
        
        # if text_142 is active this frame...
        if text_142.status == STARTED:
            # update params
            pass
        
        # *text_143* updates
        
        # if text_143 is starting this frame...
        if text_143.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_143.frameNStart = frameN  # exact frame index
            text_143.tStart = t  # local t and not account for scr refresh
            text_143.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_143, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_143.status = STARTED
            text_143.setAutoDraw(True)
        
        # if text_143 is active this frame...
        if text_143.status == STARTED:
            # update params
            pass
        
        # *key_resp_57* updates
        waitOnFlip = False
        
        # if key_resp_57 is starting this frame...
        if key_resp_57.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_57.frameNStart = frameN  # exact frame index
            key_resp_57.tStart = t  # local t and not account for scr refresh
            key_resp_57.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_57, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_57.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_57.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_57.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_57.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_57.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_57_allKeys.extend(theseKeys)
            if len(_key_resp_57_allKeys):
                key_resp_57.keys = _key_resp_57_allKeys[-1].name  # just the last key pressed
                key_resp_57.rt = _key_resp_57_allKeys[-1].rt
                key_resp_57.duration = _key_resp_57_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *text_144* updates
        
        # if text_144 is starting this frame...
        if text_144.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_144.frameNStart = frameN  # exact frame index
            text_144.tStart = t  # local t and not account for scr refresh
            text_144.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_144, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_144.status = STARTED
            text_144.setAutoDraw(True)
        
        # if text_144 is active this frame...
        if text_144.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ERL_Me_Assoc_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ERL_Me_Assoc_4" ---
    for thisComponent in ERL_Me_Assoc_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_57.keys in ['', [], None]:  # No response was made
        key_resp_57.keys = None
    trials_22.addData('key_resp_57.keys',key_resp_57.keys)
    if key_resp_57.keys != None:  # we had a response
        trials_22.addData('key_resp_57.rt', key_resp_57.rt)
        trials_22.addData('key_resp_57.duration', key_resp_57.duration)
    # the Routine "ERL_Me_Assoc_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ERL_Nomen_Assoc_4" ---
    continueRoutine = True
    # update component parameters for each repeat
    image_51.setImage(Goodother)
    image_52.setImage(Badother)
    text_145.setText("=" + " " + "Good" +" "+ Nomen)
    text_146.setText("=" + " " + "Bad" +" "+ Nomen)
    key_resp_58.keys = []
    key_resp_58.rt = []
    _key_resp_58_allKeys = []
    # keep track of which components have finished
    ERL_Nomen_Assoc_4Components = [image_51, image_52, text_145, text_146, key_resp_58, text_147]
    for thisComponent in ERL_Nomen_Assoc_4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ERL_Nomen_Assoc_4" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from B_Code_20
        if ERLloop != 643:
            continueRoutine = False
        
        # *image_51* updates
        
        # if image_51 is starting this frame...
        if image_51.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_51.frameNStart = frameN  # exact frame index
            image_51.tStart = t  # local t and not account for scr refresh
            image_51.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_51, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_51.status = STARTED
            image_51.setAutoDraw(True)
        
        # if image_51 is active this frame...
        if image_51.status == STARTED:
            # update params
            pass
        
        # *image_52* updates
        
        # if image_52 is starting this frame...
        if image_52.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_52.frameNStart = frameN  # exact frame index
            image_52.tStart = t  # local t and not account for scr refresh
            image_52.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_52, 'tStartRefresh')  # time at next scr refresh
            # update status
            image_52.status = STARTED
            image_52.setAutoDraw(True)
        
        # if image_52 is active this frame...
        if image_52.status == STARTED:
            # update params
            pass
        
        # *text_145* updates
        
        # if text_145 is starting this frame...
        if text_145.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_145.frameNStart = frameN  # exact frame index
            text_145.tStart = t  # local t and not account for scr refresh
            text_145.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_145, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_145.status = STARTED
            text_145.setAutoDraw(True)
        
        # if text_145 is active this frame...
        if text_145.status == STARTED:
            # update params
            pass
        
        # *text_146* updates
        
        # if text_146 is starting this frame...
        if text_146.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_146.frameNStart = frameN  # exact frame index
            text_146.tStart = t  # local t and not account for scr refresh
            text_146.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_146, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_146.status = STARTED
            text_146.setAutoDraw(True)
        
        # if text_146 is active this frame...
        if text_146.status == STARTED:
            # update params
            pass
        
        # *key_resp_58* updates
        
        # if key_resp_58 is starting this frame...
        if key_resp_58.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_58.frameNStart = frameN  # exact frame index
            key_resp_58.tStart = t  # local t and not account for scr refresh
            key_resp_58.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_58, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_58.status = STARTED
            # keyboard checking is just starting
            key_resp_58.clock.reset()  # now t=0
        if key_resp_58.status == STARTED:
            theseKeys = key_resp_58.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_58_allKeys.extend(theseKeys)
            if len(_key_resp_58_allKeys):
                key_resp_58.keys = _key_resp_58_allKeys[-1].name  # just the last key pressed
                key_resp_58.rt = _key_resp_58_allKeys[-1].rt
                key_resp_58.duration = _key_resp_58_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *text_147* updates
        
        # if text_147 is starting this frame...
        if text_147.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_147.frameNStart = frameN  # exact frame index
            text_147.tStart = t  # local t and not account for scr refresh
            text_147.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_147, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_147.status = STARTED
            text_147.setAutoDraw(True)
        
        # if text_147 is active this frame...
        if text_147.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ERL_Nomen_Assoc_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ERL_Nomen_Assoc_4" ---
    for thisComponent in ERL_Nomen_Assoc_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_58.keys in ['', [], None]:  # No response was made
        key_resp_58.keys = None
    trials_22.addData('key_resp_58.keys',key_resp_58.keys)
    if key_resp_58.keys != None:  # we had a response
        trials_22.addData('key_resp_58.rt', key_resp_58.rt)
        trials_22.addData('key_resp_58.duration', key_resp_58.duration)
    # the Routine "ERL_Nomen_Assoc_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_25 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('countdown.xlsx'),
        seed=None, name='trials_25')
    thisExp.addLoop(trials_25)  # add the loop to the experiment
    thisTrial_25 = trials_25.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_25.rgb)
    if thisTrial_25 != None:
        for paramName in thisTrial_25:
            exec('{} = thisTrial_25[paramName]'.format(paramName))
    
    for thisTrial_25 in trials_25:
        currentLoop = trials_25
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_25.rgb)
        if thisTrial_25 != None:
            for paramName in thisTrial_25:
                exec('{} = thisTrial_25[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "ERL_CD_3" ---
        continueRoutine = True
        # update component parameters for each repeat
        text_148.setColor(ccolor, colorSpace='rgb')
        text_148.setText(numberC)
        # keep track of which components have finished
        ERL_CD_3Components = [text_148]
        for thisComponent in ERL_CD_3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ERL_CD_3" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from B_Code_21
            if ERLloop != 643:
                continueRoutine = False
            
            # *text_148* updates
            
            # if text_148 is starting this frame...
            if text_148.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_148.frameNStart = frameN  # exact frame index
                text_148.tStart = t  # local t and not account for scr refresh
                text_148.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_148, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_148.status = STARTED
                text_148.setAutoDraw(True)
            
            # if text_148 is active this frame...
            if text_148.status == STARTED:
                # update params
                pass
            
            # if text_148 is stopping this frame...
            if text_148.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_148.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_148.tStop = t  # not accounting for scr refresh
                    text_148.frameNStop = frameN  # exact frame index
                    # update status
                    text_148.status = FINISHED
                    text_148.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ERL_CD_3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ERL_CD_3" ---
        for thisComponent in ERL_CD_3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
    # completed 1.0 repeats of 'trials_25'
    
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'trials_22'


# --- Prepare to start Routine "END" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
ENDComponents = [text_10, key_resp_8]
for thisComponent in ENDComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "END" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_10* updates
    
    # if text_10 is starting this frame...
    if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_10.frameNStart = frameN  # exact frame index
        text_10.tStart = t  # local t and not account for scr refresh
        text_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_10.started')
        # update status
        text_10.status = STARTED
        text_10.setAutoDraw(True)
    
    # if text_10 is active this frame...
    if text_10.status == STARTED:
        # update params
        pass
    
    # *key_resp_8* updates
    waitOnFlip = False
    
    # if key_resp_8 is starting this frame...
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_8.started')
        # update status
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            key_resp_8.duration = _key_resp_8_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ENDComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "END" ---
for thisComponent in ENDComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
    thisExp.addData('key_resp_8.duration', key_resp_8.duration)
thisExp.nextEntry()
# the Routine "END" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
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
