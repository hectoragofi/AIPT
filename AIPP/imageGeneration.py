import replicate
import os
import requests
import main


#os.environ["REPLICATE_API_TOKEN"] = "10d9d61cb2b4b2faab1ed3a6b535eee528ec845e"

#client = replicate.Client(api_token = "fd5d4806200325409ff7c9a4057f8d4923d798de")
def generateImage(prompptAi, token):

    os.environ["REPLICATE_API_TOKEN"] = token

    model = replicate.models.get("stability-ai/stable-diffusion")
    version = model.versions.get("db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf")
    # https://replicate.com/stability-ai/stable-diffusion/versions/db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf#input

    prompt = prompptAi
    inputs = {
        # Input prompt
        'prompt': prompt,

        # pixel dimensions of output image
        'image_dimensions': "768x768",

        # Specify things to not see in the output
        # 'negative_prompt': ...,

        # Number of images to output.
        # Range: 1 to 4
        'num_outputs': 1,

        # Number of denoising steps
        # Range: 1 to 500
        'num_inference_steps': 50,

        # Scale for classifier-free guidance
        # Range: 1 to 20
        'guidance_scale': 7.5,

        # Choose a scheduler.
        'scheduler': "DPMSolverMultistep",

        # Random seed. Leave blank to randomize the seed
        # 'seed': ...,
    }

    # https://replicate.com/stability-ai/stable-diffusion/versions/db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf#output-schema
    output = version.predict(**inputs)

    print(output)

    def imageDownload():
        url = output[0]
        #filename = url.split("/")[-1]
        filename = prompt.strip("")
        filename = filename[0] + ".png"# get the filename from the url
        r = requests.get(url, allow_redirects=True)
        open(filename, "wb").write(r.content)

    imageDownload()

#generateImage()