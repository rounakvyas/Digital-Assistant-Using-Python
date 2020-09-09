#!/usr/bin/env python
# coding: utf-8


import wx
import wikipedia
import wolframalpha
import pyttsx3 
import speech_recognition as sr

engine = pyttsx3.init()
engine.say("Welcome to the Digital Assistant by Rounak Vyas")
engine.say("How can I help you?")
engine.runAndWait()
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, pos=wx.DefaultPosition, size=wx.Size(450,100), 
                          style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN,
                         title="Python Digital Assistant")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel, 
                           label="Hello, I'm PyDA, Python Digital Assistant. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()
    
    def OnEnter(self, event):
        ques_input = self.txt.GetValue()
        ques_input = ques_input.lower()
        if ques_input == '':
        	r = sr.Recognizer()
        	with sr.Microphone() as source:
        		audio = r.listen(source)
        	try:
        		self.txt.SetValue(r.recognize_google(audio))
        	except sr.UnknownValueError:
        		print("Google Speech Recognition could not understand audio.")
        	except sr.RequestError as e:
        		print("Could not request results from Google speech Recognition services: {0}".format(e))
        try:
            #wolframalpha
            app_id = "HRK3QL-PL3JWX8YGQ"
            client = wolframalpha.Client(app_id)
            res = client.query(ques_input)
            ans = next(res.results).text
            print(ans)
            engine.say("The answer is" + ans)
            engine.runAndWait()
        except:
            #wikipedia
            ques_input = ques_input.split(' ')
            ques_input = " ".join(ques_input[2:])
            engine.say("Searched for " + ques_input)
            engine.runAndWait()
            print(wikipedia.summary(ques_input, sentences=4))
        
if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
