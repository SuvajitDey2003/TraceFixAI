def build_prompt(error_log: str, context: list) -> str:
    context_text = ""
    for i, item in enumerate(context, 1):
        context_text += (
            f"\nIssue {i}:\n"
            f"Error: {item['error']}\n"
            f"Cause: {item['cause']}\n"
            f"Fix: {item['fix']}\n"
            f"Prevention: {item['prevention']}\n"
        )

    return f"""
You are a senior software engineer.

Analyze the following error using similar past issues.

Error Log:
{error_log}

Similar Past Issues:
{context_text}

Tasks:
1. Identify the root cause
2. Explain it simply
3. Provide a clear fix
4. Suggest prevention steps
"""
