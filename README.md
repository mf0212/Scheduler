# AI Meeting Scheduler

An intelligent meeting scheduling system powered by Google's Gemini AI that analyzes user availability messages and suggests optimal meeting times.

## Features

- Natural language processing of availability messages
- Intelligent analysis of preferences and constraints
- Smart meeting time suggestions considering all participants
- Handles multiple users and complex scheduling scenarios
- Provides detailed reasoning for suggested meeting times

## Installation

1. Clone the repository:
bash
git clone https://github.com/mf0212/Scheduler.git
cd meeting-scheduler


2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```


3. Install dependencies:
```bash
pip install -r requirements.txt
```


4. Set up your Google API key:
   - Create a `.env` file in the project root
   - Add your Google API key:
```bash
 GOOGLE_API_KEY=your_api_key_here
```
 

## Usage Example


```bash
python main.py
```


## Example Input - Output

### Input
```json
{
    "User A": "I am available every morning from 9 to 11 AM, except on Wednesdays.", 
    "User B": "I am free on Tuesdays, but if possible, I prefer an early morning slot.",
    "User C": "I already have a meeting booked on Friday from 2 to 4 PM."
}
```

### Output
```
Processing User A's availability...
Analyzed availability for User A:
{
  "preference": [
    "mornings"
  ],
  "constraints": [
    "not available on Wednesdays",
    "available from 9 to 11 AM"
  ]
}

Processing User B's availability...
Analyzed availability for User B:
{
  "preference": [
    "early morning slot"
  ],
  "constraints": [
    "free on Tuesdays"
  ]
}

Processing User C's availability...
Analyzed availability for User C:
{
  "preference": [],
  "constraints": [
    "booked on Friday from 2 to 4 PM"
  ]
}

Finding suitable meeting time...

Suggested Meeting Time:
SUGGESTED TIME: Tuesday at 9 AM
REASON: This time falls within User A's preferred morning slot and their available window (9-11 AM). It also aligns with User B's preference for an early morning slot and their availability on Tuesdays. User C has no constraints at this time. 
```