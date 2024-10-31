import google.generativeai as genai
from typing import Dict, Any

from ..config.settings import Settings
from ..utils.json_helper import JsonHelper
from ..exceptions.scheduler_exceptions import AnalysisError

class AvailabilityAnalyzer:
  def __init__(self):
      self.settings = Settings()
      genai.configure(api_key=self.settings.GOOGLE_API_KEY)
      self.model = genai.GenerativeModel(self.settings.MODEL_NAME)

  def analyze_availability(self, message: str) -> Dict[str, Any]:
      """Analyze a user's availability message using Gemini"""
      try:
          prompt = f"{self.settings.ANALYSIS_PROMPT}\n\nAnalyze this message: {message}"
          response = self.model.generate_content(prompt)
          
          cleaned_json = JsonHelper.clean_json_response(response.text)
          availability_data = JsonHelper.parse_json(cleaned_json)
          
          return availability_data
          
      except Exception as e:
          print(f"Error analyzing message: {e}")
          # Return default structure with original message as constraint
          return {
              "preference": [],
              "constraints": [message]  # Include the original message as constraint
          }