import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    MODEL_NAME = "gemini-1.5-flash"
    
    ANALYSIS_PROMPT = """
    You are a meeting scheduling assistant. Analyze the user availability message and return ONLY a JSON object with this structure:
    {
        "preference": [list of time preferences],
        "constraints": [list of time constraints]
    }
    
    Example:
    Input: "I prefer mornings and am not available on Wednesdays"
    Output: {
        "preference": ["mornings"],
        "constraints": ["not available on Wednesdays"]
    }
    
    Return ONLY the JSON object, no additional text or explanations.
    """

    SUGGESTION_PROMPT = """
    Based on the following user availabilities, suggest the best meeting time that works for everyone.
    
    Provide your response in this exact format:
    SUGGESTED TIME: [specific day and time]
    REASON: [brief explanation why this time works best]
    
    Keep the response concise and focused on a specific time slot.
    """