#!/usr/bin/env python
# coding: utf-8

# In[1]:

#----------------------------------------------------------------------
#  eliza.py
#----------------------------------------------------------------------

import string
import re
import random

class Eliza:
    def __init__(self):
        self.keys = [re.compile(x[0], re.IGNORECASE) for x in gPats]
        self.values = [x[1] for x in gPats]
  #----------------------------------------------------------------------
  # translate: take a string, replace any words found in dict.keys()
  #  with the corresponding dict.values()
  #----------------------------------------------------------------------
  
    def translate(self, text, dictionary):
        words = text.lower().split()
        keys = dictionary.keys()
        for i in range(len(words)):
            if words[i] in keys:
                words[i] = dictionary[words[i]]
        return ' '.join(words)
  #----------------------------------------------------------------------
  #  respond: take a string, a set of regexps, and a corresponding
  #    set of response lists; find a match, and return a randomly
  #    chosen response from the corresponding list.
  #----------------------------------------------------------------------
  
    def respond(self, text):
        for i in range(len(self.keys)):
            match = self.keys[i].match(text)
            if match:
                resp = random.choice(self.values[i])
                pos = resp.find('%')
                while pos > -1:
                    num = int(resp[pos + 1:pos + 2])
                    resp = resp[:pos] +                         self.translate(match.group(num), gReflections) +                         resp[pos + 2:]
                    pos = resp.find('%')
                if resp[-2:] == '?.': resp = resp[:-2] + '.'
                if resp[-2:] == '??': resp = resp[:-2] + '?'
                return resp
#----------------------------------------------------------------------
# gReflections, a translation table used to convert things you say
#    into things the computer says back, e.g. "I am" --> "you are"
#----------------------------------------------------------------------

gReflections = {
    "am": "are",
    "was": "were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

#----------------------------------------------------------------------
# gPats, the main response table.  Each element of the list is a
#  two-element list; the first is a regexp, and the second is a
#  list of possible responses, with group-macros labelled as
#  %1, %2, etc.  
#----------------------------------------------------------------------
# Define a new list of patterns and responses related to touristical monuments

gPats = [
    [r'Tell me about (.*)',
    [  "What can you tell me about %1?",
       "Why are you interested in %1?",
       "Have you visited %1 before?"]],
    
    [r'What is (.*)',
    [  "Can you provide information about %1?",
       "Tell me more about %1.",
       "Why is %1 known for?",
    "Hello. which countary you waht talk about it"]],
    
    [r'Have you been to (.*)',
    [  "Unfortunately, I haven't been to %1. Tell me about your experience.",
       "How was your visit to %1?",
       "I'd love to hear about your time at %1."]],
    
    [r'(.*) monument(.*)',
    [  "Monuments are fascinating. What specifically about monuments are you interested in?",
       "Do you have a favorite monument?",
       "Tell me more about your interest in monuments."]],
    
    [r'What are some famous monuments',
    [  "There are many famous monuments around the world. Some include the Eiffel Tower, Taj Mahal, and Statue of Liberty. Which one would you like to know more about?",
       "Famous monuments include the Great Wall of China, Machu Picchu, and Christ the Redeemer. Is there a specific one you're curious about?"]],
    
    [r'Tell me a story about (.*)',
    [  "Once upon a time, there was a remarkable monument called %1. People from all over the world came to marvel at its beauty. What else would you like to know about %1?",
       "Legend has it that %1 holds a special significance in the history of its region. Would you like to hear more stories about monuments?"]],
    
    [r'(.*) historical significance(.*)',
    [  "%1 has a rich historical significance. It played a key role in shaping the cultural heritage of its region. What specific aspect of its history are you interested in?",
       "The historical significance of %1 dates back centuries. What part of its history intrigues you the most?",
       "Exploring the historical significance of %1 can provide valuable insights into the past. What particular aspect are you curious about?"]],
    
    [r'What is unique about (.*)',
    [  "What sets %1 apart from other monuments?",
       "In what way is %1 distinctive?",
       "Tell me about the unique features of %1."]],
    
    [r'(.*) architecture(.*)',
    [  "The architecture of %1 is renowned for its unique style. What aspects of its architecture are you interested in?",
       "How would you describe the architectural beauty of %1?",
       "Tell me more about the design and architecture of %1."]],
    
    [r'(.*) famous landmark(.*)',
    [  "Yes, %1 is indeed a famous landmark. What drew your attention to this particular landmark?",
       "Many people recognize %1 as a famous landmark. What made it famous in your view?",
       "How does %1 contribute to the cultural identity of its region as a famous landmark?"]],
    
    [r'(.*) must-visit(.*)',
    [  "Would you recommend %1 as a must-visit destination?",
       "What makes %1 a must-visit according to you?",
       "Tell me about the attractions that make %1 a must-visit place."]],
       [r'What is the history of (.*)',
    [  "The history of %1 is quite fascinating. It dates back to...",
       "Tell me more about the historical background of %1.",
       "Exploring the history of %1 can provide insights into its cultural significance."]],
    
    [r'(.*) famous for(.*)',
    [  "What is %1 most famous for?",
       "Tell me about the aspects that make %1 famous.",
       "When people think of %1, what usually comes to mind?"]],
    
    [r'(.*) best time to visit(.*)',
    [  "When is the best time to visit %1?",
       "What season do you recommend for a visit to %1?",
       "Tell me about the ideal time to experience %1."]],
    
    [r'(.*) interesting facts(.*)',
    [  "I love interesting facts! What are some lesser-known facts about %1?",
       "Share some intriguing facts about %1.",
       "Tell me something about %1 that most people might not know."]],
    
    [r'(.*) local cuisine(.*)',
    [  "Exploring local cuisine is a delightful part of visiting a place. What are the must-try dishes near %1?",
       "Tell me about the local culinary delights around %1.",
       "Any specific recommendations for trying local food near %1?"]],
    
    [r'(.*) nearby attractions(.*)',
    [  "In addition to %1, what other attractions are worth visiting nearby?",
       "Are there any other interesting places to explore around %1?",
       "Tell me about the nearby attractions that complement a visit to %1."]],
    
    [r'(.*) fun activities(.*)',
    [  "What fun activities can visitors engage in near %1?",
       "Tell me about recreational activities and entertainment options around %1.",
       "Any recommendations for enjoyable experiences near %1?"]],
    
    [r'(.*) travel tips(.*)',
    [  "For travelers heading to %1, what tips do you have for a memorable visit?",
       "Share some travel tips for those planning to explore %1.",
       "Any advice for first-time visitors to %1?"]],
    
    [r'(.*) cultural events(.*)',
    [  "What cultural events take place around %1?",
       "Tell me about festivals and cultural celebrations near %1.",
       "Any recommendations for experiencing the local culture around %1?"]],
    
    [r'(.*) best view(.*)',
    [  "Where can one find the best view of %1?",
       "Tell me about the viewpoints that offer a stunning panorama of %1.",
       "For photography enthusiasts, where is the best vantage point for capturing %1?"]],

  [r'quit',
  [  "Thank you for talking with me.",
    "Good-bye.",
    "Thank you, Have a good day!"]],
 ] 
  
#----------------------------------------------------------------------
#  command_interface
#----------------------------------------------------------------------

def command_interface():
    print("Therapist\n---------")
    print("Talk to the program by typing in plain English, using normal upper-")
    print('and lower-case letters and punctuation.  Enter "quit" when done.')
    print('=' * 72)
    print("Hello. which countary you waht talk about it")
    s = ""
    therapist = Eliza()
    while s != "quit":
        try:
            s = input(">")
        except EOFError:
            s = "quit"
            print(s)
        while s[-1] in "!.": s = s[:-1]
        print(therapist.respond(s))

if __name__ == "__main__":
    command_interface()






