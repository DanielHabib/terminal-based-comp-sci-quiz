def solutionFileName(id):
    return 'solution_template_' + str(prompt.id) + '.py'

def strInput(prompt):
    return str(input(prompt + "\n"))

def handlePrompt(prompt, promptList):
    if prompt.type == TYPE_QUESTION:
        prompt.userAnswer = strInput(prompt.prompt)
    elif prompt.type == TYPE_IMPLEMENTATION:
        solutionTemplate = solutionFileName(prompt.id)
        val = subprocess.check_output(["cat", "implementation_template.py"]).decode('ascii')
        val = val.replace("func_name", prompt.funcName)
        val = val.replace("func_args", ", ".join(prompt.arguments))
        with open(solutionTemplate, 'w') as out:
            out.writelines(val)
        os.system("vim " + solutionTemplate)
    promptList.append(prompt)


if __name__ == '__main__':
    from prompts import prompts, TYPE_QUESTION, TYPE_IMPLEMENTATION
    from entry import Entry
    from pprint import pprint
    import random
    import subprocess
    import os
    import importlib

    promptList = []
    """Ask some Questions"""
    random.shuffle(prompts)
    for rawPrompt in prompts:
        prompt = Entry(**rawPrompt)
        handlePrompt(prompt,promptList)

    pprint("********************************************")
    pprint("Congrats you finished all of the questions! Now it is time to grade your answers!")
    pprint("********************************************")

    for prompt in promptList:
        pprint("My Answer: {0}      Exepected Answer:{1}".format(prompt.userAnswer, prompt.answer))
        grade = strInput("Did you get it right?")
        prompt.grade = grade


    """Build Report"""
    total = 0
    correct = 0
    importlib.invalidate_caches()
    for prompt in promptList:
        if prompt.type == TYPE_QUESTION:
            if prompt.grade == "y":
                correct += 1
        elif prompt.type == TYPE_IMPLEMENTATION:
            """Run the testcase and confirm result equals expected"""
            filename = solutionFileName(prompt.id)
            prompt_module = importlib.import_module(filename[:-3])
            
            result = prompt_module.evaluate(*prompt.test["input"])
            if result == prompt.test["output"]:
                correct += 1
        total += 1
    pprint("")
    pprint("GRADE : {0}".format((correct/total) * 100))
    
