# YouTube Top Comment API Test (Mock)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Status](https://img.shields.io/badge/Status-Completed-green)
![QA](https://img.shields.io/badge/Role-QA%20Automation-orange)

---

## 🎯 Project Overview
This project demonstrates a **QA Automation test** for retrieving the most liked comment from a YouTube video using a **mocked API response**.  

It includes:
- Parsing JSON data
- Identifying the comment with the **highest like count**
- Saving results to a text file
- QA assertions to ensure **data integrity**

> Note: Real YouTube API was not used — this is a fully **mock-based test**, safe to run without credentials.

---

## 📂 Project Structure

youtube_api_test/
│
├── get_top_comment_mock.py   # Python script: QA automation test
├── mock_response.json        # Mocked YouTube API response
├── top_comment.txt           # Output file with the top comment
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
└── .gitignore                # Files/folders to ignore in Git

---

## 🧪 Test Steps (QA Style)

1. Load mock JSON response from `mock_response.json`
2. Validate response:
   - `items` key exists
   - Items list is not empty
3. Identify **top liked comment**
4. Extract:
   - Author name
   - Like count
   - Comment text
5. Save data to `top_comment.txt`
6. Check assertions:
   - Correct parsing
   - Correct max likes

---

## ▶️ How to Run

1. Activate virtual environment:

```bash
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate    # Windows
	2.	Install dependencies (none needed for standard library, optional step):
pip install -r requirements.txt
   	3.	Run the test:
python get_top_comment_mock.py
	4.	Check top_comment.txt for the most liked comment.

✅ Example Output

Author: UserTwo
Likes: 245
Comment:
This is the best tutorial I've seen.



