def strInput(prompt):
    return str(input(prompt + "\n"))

def handlePrompt(prompt, promptList):
    if prompt.type == TYPE_QUESTION:
        prompt.userAnswer = strInput(prompt.prompt)
        promptList.append(prompt)
    elif prompt.type == TYPE_IMPLEMENTATION:
        solutionTemplate = 'solution_template_'+str(prompt.id)+'.py'

        val = subprocess.check_output(["cat", "implementation_template.py"]).decode('ascii')
        val = val.replace("func_name", prompt.funcName)

        with open(solutionTemplate, 'w') as out:
            out.writelines(val)

        # command = 'touch ' + solutionTemplate + '; val="${$(cat implementation_template.py)/func_name/' + prompt.funcName + '}";echo $val >> ' + solutionTemplate
        # os.system('touch ' + solutionTemplate+ ';')
        #print(command)
        #os.system(command)
        os.system("vim " + solutionTemplate)



if __name__ == '__main__':
    from prompts import prompts, TYPE_QUESTION, TYPE_IMPLEMENTATION
    from entry import Entry
    from pprint import pprint
    import subprocess
    import os


    promptList = []

    for rawPrompt in prompts:
        prompt = Entry(**rawPrompt)
        handlePrompt(prompt,promptList)

    pprint("********************************************")
    pprint("Congrats you finished all of the questions! Now it is time to grade your answers!")
    pprint("********************************************")

    for prompt in promptList:
        pprint("My Answer: {0}    Exepected Answer:{1}".format(prompt.userAnswer, prompt.answer))
        grade = strInput("Did you get it right?")
        prompt.grade = grade


    """Build Report"""
    total = 0
    correct = 0
    for prompt in promptList:
        if prompt.userAnswer.lower() in ("y", "yes"):
            correct += 1
        total += 1
    pprint("")
    pprint("GRADE : {0}".format((correct/total) * 100))
    
