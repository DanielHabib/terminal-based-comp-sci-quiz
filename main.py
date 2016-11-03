def solutionFileName(id):
    return 'solution_template_' + str(prompt.id) + '.py'

def strInput(prompt):
    return str(input(Ink.header(prompt + "\n")))

def intInput(prompt):
    return int(input(Ink.header(prompt + "\n")))

def handlePrompt(prompt, promptList):
    if prompt.type == TYPE_QUESTION:
        prompt.userAnswer = strInput(prompt.prompt)
    elif prompt.type == TYPE_IMPLEMENTATION:
        solutionTemplate = solutionFileName(prompt.id)
        
        val = subprocess.check_output(["cat", "implementation_template.py"]).decode('ascii')
        val = val.replace("func_name", prompt.funcName)
        val = val.replace("func_args", ", ".join(prompt.arguments))
        val = val.replace("func_description", prompt.description)

        with open(solutionTemplate, 'w') as out:
            out.writelines(val)
        os.system("vim " + solutionTemplate)
    promptList.append(prompt)


if __name__ == '__main__':
    from prompts import prompts, TYPE_QUESTION, TYPE_IMPLEMENTATION
    from entry import Entry
    from ink import Ink
    import random
    import subprocess
    import os
    import importlib
    import time
   
    promptList = []
    """Ask some Questions"""
    random.shuffle(prompts)
    numberOfQuestions = intInput(Ink.header("How many questions would you like to solve today? (max: {0})".format(len(prompts))))
    prompts = prompts[:numberOfQuestions]
    for rawPrompt in prompts:
        prompt = Entry(**rawPrompt)
        handlePrompt(prompt,promptList)
   
    print(Ink.good("Congrats you finished all of the questions! Now it is time to grade your answers! (Note: Code snippets will be evaluated at the end)\n\n"))

    for prompt in promptList:
        if prompt.type == TYPE_IMPLEMENTATION: continue

        print(Ink.bold("My Answer: {0}\n".format(prompt.userAnswer)), Ink.good("Expected Answer:{0}".format(prompt.answer)))
        graded = False
        while not graded:
            grade = strInput("Did you get it right?(y/n)")
            if grade == 'y' or grade == 'n':
                prompt.grade = grade
                graded=True


    """Build Report"""
    total, correct = 0, 0
    
    importlib.invalidate_caches()

    for prompt in promptList:
        if prompt.type == TYPE_QUESTION:
            if prompt.grade == "y": correct += 1
            
        elif prompt.type == TYPE_IMPLEMENTATION:
            """Run the testcase and confirm result equals expected"""
            filename = solutionFileName(prompt.id)
            prompt_module = importlib.import_module(filename[:-3])
            
            result = prompt_module.evaluate(*prompt.test["input"])
            if result == prompt.test["output"]:
                correct += 1
            else:
                print(Ink.fail("Implementation of `{0}` failed\n".format(prompt.title)))
        total += 1
    grade = (correct/total) * 100
    
    print(Ink.underline("GRADE : {0}".format(grade)))
    with open('results.txt', 'a') as resultsFile:
        resultsFile.write("Grade:{0}\tNumberOfQuestions:{1}\tTimestamp:{2}\n".format(grade,numberOfQuestions,time.time()))



