import asyncio
from dedalus_labs import AsyncDedalus, DedalusRunner
from dotenv import load_dotenv

load_dotenv()

async def curate_gallery(theme: str):
    client = AsyncDedalus()
    runner = DedalusRunner(client)

    prompt = f"""
    You are an AI Curator. Curate a small gallery inspired by the theme "{theme}".
    - Pick 3 works of art (real or imagined).
    - Give each: a title, artist (real or plausible), and a 2-sentence poetic caption.
    - Present it as a clean markdown list with an emoji matching the mood.
    """

    response = await runner.run(
        input=prompt,
        model="openai/gpt-4o-mini"
    )

    print(response.final_output)
    return response.final_output

if __name__ == "__main__":
    theme = input("Enter a mood or theme for the gallery: ")
    asyncio.run(curate_gallery(theme))
