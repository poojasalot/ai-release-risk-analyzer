import ollama


def assess_risk(pr: dict, risk: dict) -> str:

    prompt = f"""
You are an experienced software engineering reviewer.

Analyze the following pull request release risk.

Pull Request:
{pr['title']}

Files changed:
{pr['files_changed']}

Lines added:
{pr['lines_added']}

Lines deleted:
{pr['lines_deleted']}

Deterministic risk level:
{risk['level']}

Risk score:
{risk['score']}/10

Risk factors:
{risk['reasons']}

Provide:

1. A short explanation of the risk.
2. The most important concerns.
3. Recommended validation steps.
4. Recommended deployment strategy.

Be concise and practical.
"""

    response = ollama.chat(
        model="qwen-claude:latest",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response["message"]["content"]