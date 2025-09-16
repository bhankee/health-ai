
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv
import gradio as gr
import gspread
import os


load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")
sheet_id = os.getenv("GOOGLE_SHEET_ID")


# Code to get values from Google sheets
scopes = ['https://www.googleapis.com/auth/spreadsheets']
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)
sheet =client.open_by_key(sheet_id)

all_values = sheet.sheet1.get_all_values()

# Get last row
last_row = all_values[-1]

weight = last_row[1]
lean_weight = last_row[5]
fat_weight = last_row[3]




# Code for interacting with gemini LLM
system_prompt = f""""
You are a very experienced personal trainer.

I am a 44 year old male that is 205 pounds and 6 feet tall. I normally eat around 2500 calories and feel better with somewhat lower carbohydrates. 
today's total weight on the scale is {weight}, lean mass is {lean_weight} and fat mass is {fat_weight}.

You have experience with tailoring daily nutrition and activity to get to goals of the user.
You will give me a concise list of my current weight, lean mass and fat mass and one sentence how I am doing per my goal.
You will give me a daily recommendation for activity and nutrition to get to my goal weight.
Keep it pretty concise and give me a specific menu with 2 options for each meal being 4 meals a day and no snacks.
For the activity just giv ea one sentence plan if I should increase or decrease as I get 8000 to 12000 steps a day.
My goal weight is 195 pounds but my lean mass cannot lose more then 3 pounds to get to this goal.
"""


llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",google_api_key=gemini_key, temperature= 0.5)


prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    (MessagesPlaceholder(variable_name="history")),
    ("user", "{input}")])


chain = prompt | llm | StrOutputParser()

history = []

def chat(user_in, hist):

    langchain_history = []

    for item in hist:
        if item["role"] == "user":
            langchain_history.append(HumanMessage(content=item["content"]))
        elif item["role"] == "assistant":
            langchain_history.append(AIMessage(content=item["content"]))

    chat_response = chain.invoke({"input": user_in, "history": langchain_history})

    return "", hist + [{"role": "user", "content": user_in},
                       {"role": "assistant", "content": chat_response}]



while True:
    user_input = input("What are today's proteins I should use for the daily menu: ")

    if user_input == "exit":
        break

    response = chain.invoke({"input": user_input, "history": history})

    page = gr.Blocks(
        title="My Health AI",
        theme= gr.themes.Soft()
    )


# Simple web interface
    with page:
        gr.Markdown(
            """
            # My Health AI
            
            Your personal meal planner and activity monitor that pulls daily weight data from your smart scale and talks with Gemini LLM.        
                       
            """
        )

        chatbot = gr.Chatbot(type="messages")
        msg = gr.Textbox()
        msg.submit(chat, [msg, chatbot], [msg, chatbot])
        clear = gr.Button("Clear Chat")
    page.launch()





