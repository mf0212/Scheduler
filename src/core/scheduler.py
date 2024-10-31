from typing import Dict
from .analyzer import AvailabilityAnalyzer
from ..config.settings import Settings

class MeetingScheduler:
    def __init__(self):
        self.users: Dict = {}
        self.analyzer = AvailabilityAnalyzer()
        self.settings = Settings()

    def add_user(self, user_id: str, message: str) -> None:
        """Add a user and their availability message"""
        availability = self.analyzer.analyze_availability(message)
        self.users[user_id] = {
            "message": message,
            "availability": availability
        }

    def find_suitable_time(self) -> str:
        """Find suitable meeting time based on all users' availability"""
        if not self.users:
            return "No users added to schedule"

        # Create a structured context for the AI
        context = "Current user availabilities:\n\n"
        for user_id, data in self.users.items():
            avail = data['availability']
            context += f"{user_id}:\n"
            if avail['preference']:
                context += f"Preferences: {', '.join(avail['preference'])}\n"
            if avail['constraints']:
                context += f"Constraints: {', '.join(avail['constraints'])}\n"
            context += "\n"

        try:
            prompt = f"{context}\n{self.settings.SUGGESTION_PROMPT}"
            response = self.analyzer.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error finding suitable time: {e}"