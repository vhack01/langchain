from typing import Literal
from typing import Optional
from typing import TypedDict, Annotated
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model = "gpt-4.1-mini")

# schema

schema = {
    "title": "Review", 
    "type": "object",
    "properties": {
        "summary" : {
            "description": "A short summary of the review",
            "type": "string",
        },
        "sentiment" : {
            "description": "The sentiment of the review",
            "type": "string",
            "enum": ["positive", "negative", "neutral"]
        },
        "author" : {
            "description": "The name of the reviewer",
            "type": ["string", "null"]
        },
        "rating" : {
            "type": ["number", "null"],
            "description": "The rating of the review from 1 to 5"
        },
        "pros" : {
            "type" : ["array", "null"],
            "items": {
                "type": "string",
            },
            "description" : "Pros of the review"
        },
        "cons" : {
            "type" : ["string", "null"],
            "description" : "Cons of the review"
        },
    },
    "required": ["summary", "sentiment", "rating"]
}

stuctured_model = model.with_structured_output(schema)

response = stuctured_model.invoke("""Apple iPhone 17 Pro Review Insights
Apple's major unibody redesign has drawn a lot of attention for its bold looks and daily practicality:

The "Camera Plateau" Design: The wide, body-spanning camera bar on the back is controversial visually but praised for practicality—it completely eliminates the annoying desktop wobble found on older iPhones when laying flat.

Performance and Thermal Mastery: The A19 Pro chip handles intense workflows like voice transcription and video rendering at lightning speeds. Thanks to the shift to an aluminum unibody paired with an improved vapor chamber, it handles heat dissipation much better than older titanium models. However, severe mobile gaming can still trigger some GPU thermal throttling.

Camera Innovation: Reviewers love the upgraded 18MP Center Stage front camera, which allows you to take ultra-wide group selfies in landscape mode while holding the phone vertically. The new 4x telephoto lens also utilizes a larger sensor, pulling in significantly better details in low-light environments compared to older 5x lenses.

Durability Warning: Because aluminum is softer than titanium, caseless users note that the frame is prone to minor scuffs and edge chips from drops. Putting a rugged case on it is highly recommended.

Head-to-Head Comparison
To help you decide between these two premium flagships, here is how they stack up directly across key attributes:""")

print('summary: ', response['summary'])
print('sentiment: ',response['sentiment'])
print('author: ',response['author'])
print('rating: ', response['rating'])
print('pros: ',response['pros'])
print('cons: ',response['cons'])

print(response)