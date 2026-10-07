from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_ollama import ChatOllama

model = ChatOllama(
    model="qwen2.5:0.5b",
    temperature = 0,
    num_predict=50,
)

parser = StrOutputParser()


prompt = ChatPromptTemplate.from_messages([
    ("system",
     """You are a concise assistant.
        Answer in 1-3 sentences.
        Do not provide unnecessary explanations."""),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])
chain = prompt | model | parser

store = {}

def get_session_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

chain_with_memory = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key='input',
    history_messages_key='history'
)

session_key = {
        '1' : 'create session',
        '2' : 'show all session',
        '3' : 'current session',
        '4' : 'switch session'
    }
print(session_key)

session_id = "user1"

while True:

    user_input = input("You: ")

    if user_input == '1':
        new_session = input('enter an new session_id: ')
        if new_session not in store:
            store [new_session] = InMemoryChatMessageHistory()
            session_id = new_session
        continue

    
    if user_input.lower() == '2':
        for session in store:
            print (session )
        continue
    elif user_input.lower() == '3':
        print(session_id)
        continue


    if user_input.lower() == '4':
        target_session = input("give the session_id to change: ")
        if target_session in store:
            session_id = target_session
            print(f"session changed {session_id} ")
        continue


    if user_input.lower() == 'break':
        print("Goodbye!")
        break

    response = chain_with_memory.invoke(
        {"input": user_input},
        config={"configurable": {"session_id": session_id}}
    )
    print(f"Bot: {response}")
