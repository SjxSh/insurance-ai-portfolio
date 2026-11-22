"""命令行保险条款问答 —— W1 交付物"""
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com",
)

MODEL = "deepseek-flash"
SYSTEM = "你是保险条款助手。回答简洁准确，不确定时明确说不确定。"


def ask(question: str) -> None:
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": question},
        ],
        temperature=2,
        stream=False,
        extra_body={"thinking": {"type": "disabled"}},
    )
    print(resp.choices[0].message.content)
    usage = resp.usage
    print(f"--- token: 输入 {usage.prompt_tokens} / 输出 {usage.completion_tokens}")


def main() -> None:
    print("保险条款问答（输入 exit 退出）\n")
    while True:
        question = input("你> ").strip()
        if question.lower() in {"exit", "quit", ""}:
            break
        try:
            ask(question)
        except Exception as exc:
            print(f"[错误] {exc}")


if __name__ == "__main__":
    main()