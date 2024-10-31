from src.core.scheduler import MeetingScheduler

def main():
    scheduler = MeetingScheduler()
    
    # Test messages
    test_messages = {
        "User1": "I'm available Monday and Tuesday mornings",
        "User2": "I prefer afternoons, except Wednesdays",
        "User3": "I can meet any day before 2 PM"
        }
    
    # Add users
    for user_id, message in test_messages.items():
        print(f"\nProcessing {user_id}'s availability...")
        scheduler.add_user(user_id, message)
        print(f"Analyzed availability for {user_id}:")
        print(scheduler.users[user_id]['availability'])
    
    # Get suggestion
    print("\nFinding suitable meeting time...")
    suggestion = scheduler.find_suitable_time()
    print("\nSuggested Meeting Time:")
    print(suggestion)

if __name__ == "__main__":
    main()