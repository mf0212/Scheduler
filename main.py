from src.core.scheduler import MeetingScheduler
from src.utils.json_helper import JsonHelper
import json

def main():
    scheduler = MeetingScheduler()
    
    # Test messages
    file_path = "data/meeting_1.json"
    test_messages = JsonHelper.read_meeting_json(file_path)
    # Add users
    for user_id, message in test_messages.items():
        print(f"\nProcessing {user_id}'s availability...")
        scheduler.add_user(user_id, message)
        print(f"Analyzed availability for {user_id}:")
        print(json.dumps(scheduler.users[user_id]['availability'], indent=2))
    
    # Get suggestion
    print("\nFinding suitable meeting time...")
    suggestion = scheduler.find_suitable_time()
    print("\nSuggested Meeting Time:")
    print(suggestion)

if __name__ == "__main__":
  main()