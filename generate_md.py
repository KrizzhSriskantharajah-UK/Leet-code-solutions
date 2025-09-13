import os, json

BASE_DIR = "."
with open("solved_problems.json") as f:
    problems = json.load(f)

for problem in problems:
    difficulty = problem["difficulty"]
    os.makedirs(os.path.join(BASE_DIR, difficulty), exist_ok=True)
    md_path = os.path.join(BASE_DIR, difficulty, f"{problem['titleSlug']}.md")
    with open(md_path, "w", encoding="utf-8") as f_md:
        f_md.write(f"# {problem['title']}\n\n")
        f_md.write(f"**Difficulty:** {problem['difficulty']}\n")
        f_md.write(f"**Link:** [LeetCode](https://leetcode.com/problems/{problem['titleSlug']}/)\n\n")
        f_md.write("## Solution\n```python\n")
        f_md.write(problem.get("solutionCode",""))
        f_md.write("\n```\n")
        f_md.write(f"## Stats\n- Runtime: {problem.get('runtime','N/A')}\n- Memory: {problem.get('memory','N/A')}\n")
