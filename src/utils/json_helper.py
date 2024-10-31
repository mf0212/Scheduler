import json
from typing import Dict, Any

class JsonHelper:
    @staticmethod
    def clean_json_response(response_text: str) -> str:
        """Clean the response text to ensure it's valid JSON"""
        cleaned = response_text.strip()
        
        # Remove markdown code block markers if present
        if cleaned.startswith("```json"):
            cleaned = cleaned[7:]  # Remove ```json
        if cleaned.endswith("```"):
            cleaned = cleaned[:-3]  # Remove ```
            
        return cleaned.strip()

    @staticmethod
    def parse_json(text: str) -> Dict[str, Any]:
        """Parse JSON with error handling"""
        try:
            return json.loads(text)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format: {e}")
        
    @staticmethod
    def read_meeting_json(file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
            return None
        except json.JSONDecodeError:
            print("Error: Invalid JSON format")
            return None