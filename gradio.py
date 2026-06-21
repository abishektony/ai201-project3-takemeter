#Code to paste at the end to call and use the model in your notebook

import gradio as gr
import torch

def classify_user_post(text):
    if not text.strip():
        return "Please enter valid text."
        
    # Tokenize input text
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=256).to(model.device)
    
    # Run inference
    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=-1).squeeze().tolist()
    
    # Format the output scores for both classes
    response = "=== TakeMeter Analysis ===\n"
    for label_str, class_id in LABEL_MAP.items():
        response += f"{label_str}: {probs[class_id]:.2%}\n"
        
    return response

# Launch the interactive UI
demo = gr.Interface(
    fn=classify_user_post,
    inputs=gr.Textbox(lines=5, placeholder="Paste an r/TrueFilm post here to test..."),
    outputs="text",
    title="TakeMeter Deployed Interface",
    description="Test your fine-tuned DistilBERT model live on new movie discourse!"
)

# Setting share=True gives you a temporary public link for your video demo
demo.launch(share=True)