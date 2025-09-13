import os
import subprocess
import json

BASE_DIR = "."

# Fetch solved problems
result = subprocess.run(
    ["leetcode", "list", "-s", "ac", "-x", "--json"],
    capture_output=True,
    text=True,
    env={**os.environ, "LC_SESSION": os.environ["LC_SESSION"]}
)
problems_json = result.stdout

try:
    problems = json.loads(problems_json)
except json.JSONDecodeError:
    print("Error: solved.json is not valid JSON")
    print(problems_json)
    exit(1)

for problem in problems:
    title_slug = problem['titleSlug']
    difficulty = problem['difficulty'].capitalize()
    os.makedirs(os.path.join(BASE_DIR, difficulty), exist_ok=True)
    
    # Fetch Python solution code
    code_result = subprocess.run(
        ["leetcode", "show", title_slug, "-l", "python3"],
        capture_output=True,
        text=True,
        env={**os.environ, "LC_SESSION": os.environ["LC_SESSION"]}
    )
    code = code_result.stdout
    
    md_path = os.path.join(BASE_DIR, difficulty, f"{title_slug}.md")
    with open(md_path, "w", encoding="utf-8") as f_md:
        f_md.write(f"# {problem['title']}\n\n")
        f_md.write(f"**Difficulty:** {difficulty}\n")
        f_md.write(f"**Link:** [LeetCode](https://leetcode.com/problems/{title_slug}/)\n\n")
        f_md.write("## Solution (Python)\n```python\n")
        f_md.write(code)
        f_md.write("\n```\n")
