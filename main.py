from smolagents import CodeAgent, UserInputTool
from model import callModel
from tools import read_pdf,image_to_text
from prompts import mainPrompt

prompt = mainPrompt.mainPrompt()

agent = CodeAgent(tools=[read_pdf,image_to_text,UserInputTool()], model=callModel(),instructions=prompt)

response = agent.run("Help me on understanding this subject. 'math.pdf' , 'multi.png' ")

print(response)
