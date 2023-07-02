# Caption Generator API

This is an Image Caption Generator, a Django REST API that generates captions for images.

## How it Works

1. The API accepts a POST request with a JSON payload containing the `img_url` of the image for which you want a caption.

2. The image is processed using a pre-trained Vision Encoder-Decoder model, which extracts visual features from the image.

3. The extracted features are passed through a pre-trained language model, specifically a ViT-GPT2 model, to generate a descriptive caption for the image.

4. The generated caption is then used as a prompt to an OpenAI API, which refines and generates a final Instagram caption.

5. The API returns the generated caption as a response in JSON format.
## Endpoint

The backend exposes a single endpoint:

### `/api/caption_generator`

This endpoint accepts a POST request and returns a JSON response containing the caption for the provided image.

**Request Parameters:**

- `img_url` (string): The link to the image to be processed.

**Example Request:**

```json
{
  "img_url": "image/url"
}
```

**Example Response:**

```json
{
  "caption": "Chasing My Dreams ⚽️🏃‍♂️"
}
```

## Setup

To set up the Caption Generator backend locally, follow the instructions below:

1. Clone the repository:

   ```bash
   git clone https://github.com/mbahraoui/CaptionGeneratorAPI.git
   ```
   

2. Navigate to the project directory:

   ```bash
   cd CaptionGeneratorAPI
   ```

3. Create a `.env` file in CaptionGenerator directory of the project and add the following line:

   ```plaintext
   API_KEY=your_api_key
   ```

   Replace `your_api_key` with your actual GPT-3 API key.

4. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

   The backend should now be running at `http://localhost:8000/`.
.
