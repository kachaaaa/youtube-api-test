import json


with open("mock_response.json", "r", encoding="utf-8") as file:
    data = json.load(file)


assert "items" in data, "❌ 'items' key not found in response"
assert len(data["items"]) > 0, "❌ Comments list is empty"


top_comment = max(
    data["items"],
    key=lambda x: x["snippet"]["topLevelComment"]["snippet"]["likeCount"]
)


snippet = top_comment["snippet"]["topLevelComment"]["snippet"]
author = snippet["authorDisplayName"]
likes = snippet["likeCount"]
text = snippet["textDisplay"]


with open("top_comment.txt", "w", encoding="utf-8") as file:
    file.write(f"Author: {author}\n")
    file.write(f"Likes: {likes}\n")
    file.write("Comment:\n")
    file.write(text)

print("✅ Top comment saved (mock API)")