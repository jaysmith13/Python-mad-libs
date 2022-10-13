from importlib.resources import path
import json
import os
from re import template
from typing_extensions import Self

class MadLibs:
    path = "./templates"
    def_init_(self, word_descriptions, template);
        self.template = template
        self.word_description = word_descriptions
        self.user_input = []
        self.story = None

@classmethod
def from_json