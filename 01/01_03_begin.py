
import random
from string import punctuation
from collections import defaultdict


class MarkovChain:
    def __init__(self):
        self.graph = defaultdict(list)

    def _tokenize(self, text):
        return (
            text.translate(str.maketrans("", "", punctuation + "1234567890"))
            .replace("\n", " ")
            .split(" ")
        )

    def train(self, text):
        tokens = self._tokenize(text)
        for i, token in enumerate(tokens):
            if (len(tokens) - 1)  == i:
                break
            self.graph[token].append(tokens[i + 1])
                    

    def generate(self, prompt, length=20):
        # get the lask token from the prompt
        current = self._tokenize(prompt)[-1]
        # initialize the output
        output = prompt
        for i in range(length):
            # look up the options in the graph dictionary
            options = self.graph.get(current, self.graph[i])
            if not options:
                continue
            # use random.choice method to pick a current option
            current = random.choice(options)
            
            # add the random choice to the output string
            output += f" {current}"
    
        return output
    
text = """
Goals is about what you want to achieve.System is about the process that led you to that results.
Results usually not related to the goals you first set.
Goals give a direction but system first mentality makes you progress.
Goals can led to a yo-yo (new -> old habits).
Purpose of goals is to win the game.
Purpose of systems is continually playing the game.
You don’t raise to the level of your goals but you fall to the level of your system.
Atomic - small, marginal, regular practices that are not only easy to do but source of great power.
Getting 1% better everyday counts a lot.
"""

chain = MarkovChain()
chain.train(text)
sample_prompt = "Atomic is"
print(chain.generate(sample_prompt))
