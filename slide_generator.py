import openai
import os
from functools import reduce


# Set up the OpenAI API client
openai.api_key = os.environ["OPENAI_API_KEY"]
# Set up the model and prompt
model_engine = "text-davinci-003"
    

# Generate or modify HTML code based on prompt
def gen_html(prompt, start_html=None, chunks=1, temperature=0.25):
    prompt = prompt
    if start_html:
        prompt += f'''
        Original code:
        {start_html}

        Modified code (complete the below code):

        '''
    else:
        prompt += f'''
        Complete the code below:

        ''' 
    responses = ['<html>']
    last_response = '<html>'
    for chunk in range(chunks):
        prompt += last_response
        print(len(prompt))
        if last_response == '': 
            break
        else:
            completion = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                max_tokens=2500,
                n=1,
                temperature=temperature,
            )
        last_response = completion.choices[0].text
        responses.append(last_response)
    end_html = reduce(lambda x, y: ''.join([x, y]), responses)
    return end_html


def generate_scratch(topic, no_of_slides, colors, look_n_feel, approx_words_per_slide=100):

    # Prompt used to generate slides
    prompt = f'''
    I want you to create a {no_of_slides}-slide presentation deck in HTML/JS using the Reveal.js library by following the 18 steps below:
    1- Use the following JavaScript source <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.8.0/js/reveal.min.js">  and don't forget to run Reveal.initialize().
    2- Make sure to import <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.8.0/css/reveal.min.css">
    3- There should be {no_of_slides} <section> occurrences representing each slide.
    4- Ensure to add a <style> section for additional CSS changes requested below.
    5- The first slide is the title page and the last one is a conclusion.
    6- Include ACTUAL CONTENT on the topic of {topic}.
    7- Ensure there are examples provided.
    8- Ensure there are comparisons provided (for e.g. pros and cons).
    9- Ensure there are at least 2 tables with some content inside them.
    10- Ensure there is some data listed as bullet-points with a minimum of 3 entries per bullet-point list.
    11- Use all the following colors in the slides (adjust <style> element): {colors}
    12- Ensure there is sufficient contrast in the colors of overlapping HTML elements (adjust <style> element).
    13- Ensure every slide has content comprising of {approx_words_per_slide}*2 tokens.
    14- Ensure the content fits in each slide and there is no text overflow (adjust <style> element).
    15- Make sure the slides are very easy to read. Use bold, italic, and underlined fonts where applicable.
    16- Make the presentation css styling (in the <style> element) has a "{look_n_feel}" look and feel.
    17- Ensure there is sufficient contrast and use all the following colors in the slides: {colors}
    18- Make sure all the slide content (adjust <style> element) is centered and every slide has content comprising of {approx_words_per_slide}*2 tokens.
    '''

    html = gen_html(prompt=prompt)

    return html

