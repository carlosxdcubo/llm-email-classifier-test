def classification_prompt(email_body, categories):
    prompt=f'''
Your task is to classify this email: "{email_body}" using this categories: "{categories}"
Responds only with the categorie without quotation marks or apostrophes'.
'''
    return prompt

def response_prompt(email_body, email_class):
    
    template= generate_email_response(email_class)
    prompt=f'''
Your task is to response this email: "{email_body}" using this template: "{template}". Try to give a personalized message.
Follow this instructions: 
- Do not give the subject, just the body.
- Always refer to the costumer as "Dear customer"
'''
    return prompt

def complaint_response():
    return ("Dear customer,\n\n"
            "Thank you for reaching out and sharing your concerns. I sincerely apologize for the inconvenience you have experienced. "
            "We take all complaints seriously and want to assure you that we are currently investigating the issue.\n\n"
            "Could you please provide more details about [specific problem mentioned]? This will help us expedite the resolution process. "
            "In the meantime, I have forwarded your case to our support team for further review.\n\n"
            "Once again, we apologize for the trouble and appreciate your patience. If you have any further questions, feel free to contact us.\n\n"
            "Best regards,CadreAI")


def inquiry_response():
    return (
            "Dear customer,\n\n"
            "Thank you for your inquiry regarding [specific product/service]. I’m happy to provide you with the information you need.\n\n"
            "[Provide specific details in response to the inquiry].\n\n"
            "If you need further clarification or have additional questions, don’t hesitate to reach out. We're here to assist!\n\n"
            "Best regards,CadreAI")


def feedback_response():
    return (
            "Dear customer,\n\n"
            "Thank you for taking the time to share your feedback with us. We greatly appreciate your insights and are glad to know that you had a positive experience with [product/service].\n\n"
            "We are constantly striving to improve, and your feedback helps us in our efforts. If there’s anything more we can do for you, or if you have additional suggestions, please let us know.\n\n"
            "Thanks again for your support!\n\n"
            "Best regards,CadreAI")


def support_request_response():
    return (
            "Dear customer,\n\n"
            "Thank you for reaching out to our support team. We have received your support request and are currently looking into the issue.\n\n"
            "To assist you better, could you please provide [details like error messages, system information, etc.]? This will help us address your concern more efficiently. "
            "Our team is dedicated to resolving your issue as soon as possible.\n\n"
            "We will keep you updated on the progress, and please don’t hesitate to contact us if you have any additional questions.\n\n"
            "Best regards,CadreAI")


def other_response():
    return ("Dear customer,\n\n"
            "Thank you for your email. We appreciate you reaching out to us with your query. "
            "It appears that your message is in regard to something outside our typical support areas, but we’re happy to help.\n\n"
            "Please let us know how we can further assist you or clarify any information you may need.\n\n"
            "We look forward to your response!\n\n"
            "Best regards,CadreAI")


def generate_email_response(category):
    responses = {
        "complaint": complaint_response,
        "inquiry": inquiry_response,
        "feedback": feedback_response,
        "support_request": support_request_response,
        "other": other_response,
    }
    
    return responses.get(category, other_response)()


