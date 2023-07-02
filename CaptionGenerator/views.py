import io
from rest_framework import views
from rest_framework.response import Response
import numpy as np
import urllib3
from .serializers import CaptionGeneratorSerializer
from PIL import Image
from dotenv import load_dotenv
import os
import torch 
import re 
from transformers import AutoTokenizer, ViTFeatureExtractor, VisionEncoderDecoderModel 
import openai

class CaptionGeneratorView(views.APIView):
    def post(self, request):

        def predict(image,max_length=64, num_beams=4):
            image = image.convert('RGB')
            image = feature_extractor(image, return_tensors="pt").pixel_values.to(device)
            clean_text = lambda x: x.replace('<|endoftext|>','').split('\n')[0]
            caption_ids = model.generate(image, max_length = max_length)[0]
            caption_text = clean_text(tokenizer.decode(caption_ids))
            return caption_text         
        
        def generate_instagram_caption(image_description):
            prompt = f"This is an Instagram Caption generator. Instagram captions are short sentences that generally describe the image posted or what the post is about. The description for the Instagram caption is {image_description}. Give me only one caption."
            load_dotenv()
            API_KEY = os.environ.get("API_KEY")
            openai.api_key =API_KEY

            response = openai.Completion.create(
                engine='text-davinci-003',
                prompt=prompt,
                max_tokens=30,  
                n=1,  
                stop=None,
                temperature=0.7  
            )

            caption = response.choices[0].text.strip()

            return caption
                    
        
        def load_image_from_url(img_url):
            http = urllib3.PoolManager()
            response = http.request('GET', img_url)
            image_data = response.data
            image = Image.open(io.BytesIO(image_data))
            return image
        
        device='cpu'
        encoder_checkpoint = "nlpconnect/vit-gpt2-image-captioning"
        decoder_checkpoint = "nlpconnect/vit-gpt2-image-captioning"
        model_checkpoint = "nlpconnect/vit-gpt2-image-captioning"
        feature_extractor = ViTFeatureExtractor.from_pretrained(encoder_checkpoint)
        tokenizer = AutoTokenizer.from_pretrained(decoder_checkpoint)
        model = VisionEncoderDecoderModel.from_pretrained(model_checkpoint).to(device)

        img_url = request.data['img_url']

        image = load_image_from_url(img_url)

        image_description=predict(image,max_length=64, num_beams=4)
        generated_caption = generate_instagram_caption(image_description)

        data= [{"caption": generated_caption}]
        # print(data)
        results = CaptionGeneratorSerializer(data, many=True).data
        return Response(results)