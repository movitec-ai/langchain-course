from dotenv import load_dotenv
import os
load_dotenv()

def main():
    print("Hello from langchain-course!")
    print(os.environ.get("OPENAI_API_KEY"))
    print("Hola")

if __name__ == "__main__":
    main()
