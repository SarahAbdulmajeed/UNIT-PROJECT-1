import os 
import json
import questionary 
from datetime import datetime
from openai import OpenAI
from speech_to_text.user_speech_text import record_audio,transcript_audio


client = OpenAI(api_key="")  
NUMBER_OF_QUESTIONS:int = 4
INTERVIEW_FILE:str = "Interview/interviews.json"

#========================================================================================
def start_interview(user, jobtitle):
    """
    This function: 
    - Sends a prompt to GPT-4 to generate interview questions. 
    - Records user's audio answers and transcribes them using Whisper.
    - Analyzes each answer with GPT-4 to extract a score, strengths, and weaknesses. 
    - Saves the final interview session to a JSON file under the username.
    """
    
    #This text will be send to GPT-4 later
    prompt = f"""
    Generate {NUMBER_OF_QUESTIONS} professional interview questions for the job title: '{jobtitle}'.
    Return the result as a JSON list of objects.
    Each object should have: "question" (string), "skills" (array of strings).
    Return ONLY the JSON, no explanations or formatting.
    """

    #Sending prompt to GPT-4 using OpenAI library 
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7 
    )

    #The 'GPT response' will be stored in 'output'
    output = response.choices[0].message.content
    
    try:
        #convert JSON string to python object  
        raw = json.loads(output)
        
        #prepare empty list for dictionary
        questions:list  = []
        
        for item in raw:
            questions.append({
                "question": item["question"],
                "Answer":"",
                "skills": item["skills"],
                "strengths": "",
                "weaknesses":"",
                "score":""
                })
            
        #
        user["interview"] = {
            "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "jobtitle": jobtitle,
            "questions": questions
        }
        
        #start the interview 
        counter:int = 1
        for question in questions:
            #Question to user
            print(f"Question {counter}. {question['question']}")
            counter += 1
            choice = questionary.select(
                "Do you want to answer or exit the interview?",
                choices=["Answer", "Exit"]
                ).ask()
            
            #Record the user answer and show it as text
            if choice == "Answer":
                record_audio()
                user_answer = transcript_audio()
                question['Answer'] = user_answer
                print(f"Your answer: {user_answer}")
            else:
                break
        
        #Analysis each of the user answers using GPT-4
        for question in questions:
            if question['Answer']: #check only questions that the user answered
                analysis_prompt = f"""
                The user was asked the interview question: "{question['question']}"
                Their answer was: "{question['Answer']}"

                Please analyze the answer and return:
                - A score from 1 to 10
                - List of strengths
                - List of weaknesses
                
                Important:
                - The user's answer was limited to around 20 seconds, so brevity and lack of detail should not be overly penalized.
                - Focus on the relevance and clarity of the answer rather than its length.
                - Be forgiving of missing depth due to the time constraint.


                Return the result in this JSON format ONLY:
                {{
                    "score": 7,
                    "strengths": ["...", "..."],
                    "weaknesses": ["...", "..."]
                }}
                """
                try:
                    response = client.chat.completions.create(
                        model="gpt-4",
                        messages=[{"role": "user", "content": analysis_prompt}],
                        temperature=0.5
                        )
                    analysis = json.loads(response.choices[0].message.content)
                    
                    question['score'] = analysis.get("score", "")
                    question['strengths'] = analysis.get("strengths", [])
                    question['weaknesses'] = analysis.get("weaknesses", [])    
                except Exception as e:
                    print(e)    
        save_interview_to_file(user)           
    except Exception as e:
        print(e)
#========================================================================================
#========================================================================================
def save_interview_to_file(user:dict[str | dict]) -> None:
    """
    This function save the interview to the interviews.json file
    the interview will be saved under the username
    
    Args:
        user: dict 
            - username: str
            - interview:
                - datetime: str
                - jobtitle: str
                - questions: list[dict]
    """
    
    username:str = user["username"]
    interview:dict = user["interview"]

    # check if the file already exist and load the data
    if os.path.exists(INTERVIEW_FILE):
        with open(INTERVIEW_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {}

    # add new interview list for username if he has no interviews before
    if username not in data:
        data[username] = []

    #add interview information to the username 
    data[username].append(interview)

    # Save data after changes to interview,json file
    with open(INTERVIEW_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
#========================================================================================