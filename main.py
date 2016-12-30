from prompts import prompts, Type, Topic
from entry import Entry
from functools import reduce
from ink import Ink
import random
import subprocess
import os
import importlib
import time


class ImplementationFailedException:
    """Implementation Script is busted """

def solutionFileName(idVal):
    return 'solution_template_' + str(idVal) + '.py'

def promptInput(prompt):
    return input(Ink.header(prompt + "\n"))

def strInput(prompt, clearScreen=False):
    val = str(promptInput(prompt))
    if clearScreen:
        os.system('clear') 
    return val

def intInput(prompt, clearScreen=False):
    val = int(promptInput(prompt))
    if clearScreen:
        os.system('clear')
    return val

def populateTemplate(prompt):
    solutionTemplate = solutionFileName(prompt.id)
    
    template = subprocess.check_output(["cat", "implementation_template.py"]).decode('ascii')

    replacementDict = {
            "func_name": prompt.funcName,
            "func_args": ", ".join(prompt.arguments),
            "func_description": prompt.description,
            "func_title": prompt.title
            }
    template = reduce(lambda template, y : template.replace(y, replacementDict[y]),  replacementDict.keys(), template)

    with open(solutionTemplate, 'w') as out:
        out.writelines(template)

    return solutionTemplate

def handlePrompt(prompt, promptList):
    if prompt.type == Type.QUESTION:
        prompt.userAnswer = strInput(prompt.prompt)
    elif prompt.type == Type.IMPLEMENTATION:
        solutionTemplate = populateTemplate(prompt)
        os.system("vim " + solutionTemplate)

    promptList.append(prompt)


if __name__ == '__main__':
   
    promptList = []
    """Ask some Questions"""
    random.shuffle(prompts)
    numberOfPrompts = intInput("How many questions would you like to solve today? (max: {0})".format(len(prompts)), clearScreen=True)
    
    prompts = [Entry(**x) for x in prompts[:numberOfPrompts]]

    for prompt in prompts: handlePrompt(prompt, promptList)

    os.system('clear')   
    print(Ink.good("Congrats you finished all of the questions! Now it is time to grade your answers! (Note: Code snippets will be evaluated at the end)\n\n"))

    questionPrompts = [prompt for prompt in promptList if prompt.type == Type.QUESTION] 
    implementationPrompts = [prompt for prompt in promptList if prompt.type == Type.IMPLEMENTATION]

    for prompt in questionPrompts:
        print(Ink.header("\n______________\nQuestion: {0}\n".format(prompt.prompt)), Ink.bold("My Answer: {0}\n".format(prompt.userAnswer)), Ink.good("Expected Answer:{0}".format(prompt.answer)))
        graded = False
        while True:
            grade = strInput("Did you get it right?(y/n)")
            if grade == 'y' or grade == 'n':
                prompt.grade = int(grade == 'y')
                break

    importlib.invalidate_caches()
    """Build Report"""
    total, correct = 0, 0
    
    def testImplementation(prompt):
        """Run the testcase and confirm result equals expected"""
        filename = solutionFileName(prompt.id)
        prompt_module = importlib.import_module(filename[:-3])
        try:
            result = prompt_module.evaluate(*prompt.test["input"])
            if result == prompt.test["output"]:
                return 1
            else:
                raise ImplementationFailedExeption()
        except:
            print(Ink.fail("Implementation of `{0}` failed\n".format(prompt.title)))
            return 0

    
    print(Ink.ok("Evaluating Scripts and building Report"))
    numberOfCorrectImplementations = sum(map(testImplementation, implementationPrompts))
    numberOfCorrectQuestions = sum([prompt.grade for prompt in questionPrompts])

    grade = ((numberOfCorrectImplementations + numberOfCorrectQuestions) / numberOfPrompts)*100
    
    print(Ink.underline("GRADE : {0}".format(grade)))
    with open('results.txt', 'a') as resultsFile:
        resultsFile.write("Grade:{0}\tNumber Of Questions:{1}\tTimestamp:{2}\n".format(grade, numberOfPrompts, time.time()))


