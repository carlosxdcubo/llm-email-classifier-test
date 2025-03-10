# Standard Library Imports
import os
import json
import logging
from datetime import datetime
from typing import Dict, Optional

# Third-Party Imports
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI

# Local Imports
from prompts_samples import classification_prompt, response_prompt
from sample_emails import load_sample_emails
from metrics_utils import calculate_metrics

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Load environment variables (Moved to `run_demonstration`)
load_dotenv()

sample_emails=load_sample_emails()

class EmailProcessor:
    """Handles email classification and response generation using OpenAI's LLM."""

    MODEL_NAME = "gpt-4o-mini"
    TEMPERATURE = 0.1

    def __init__(self):
        """Initialize the email processor with OpenAI API key."""
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is missing!")
        
        self.client = OpenAI(api_key=api_key)

        # Define valid categories
        self.valid_categories = {"complaint", "inquiry", "feedback", "support_request", "other"}

    def classify_email(self, email: Dict) -> Optional[str]:
        """Classify an email using OpenAI's API."""
        email_body = email.get("body", "")
        prompt = classification_prompt(email_body, self.valid_categories)

        try:
            response = self.client.chat.completions.create(
                model=self.MODEL_NAME,
                temperature=self.TEMPERATURE,
                messages=[{"role": "user", "content": prompt}]
            )

            if response.choices:
                return response.choices[0].message.content.strip()

            logger.warning(f"Classification failed for email {email['id']}")
            return None

        except Exception as e:
            logger.exception(f"Error classifying email {email['id']}: {e}")
            return None

    def generate_response(self, email: Dict, classification: str) -> Optional[str]:
        """Generate a response based on email classification."""
        email_body = email.get("body", "")
        prompt = response_prompt(email_body, classification)

        try:
            response = self.client.chat.completions.create(
                model=self.MODEL_NAME,
                temperature=self.TEMPERATURE,
                messages=[{"role": "user", "content": prompt}]
            )

            if response.choices:
                return response.choices[0].message.content.strip()

            logger.warning(f"Response generation failed for email {email['id']}")
            return None

        except Exception as e:
            logger.exception(f"Error generating response for email {email['id']}: {e}")
            return None


class EmailAutomationSystem:
    """Handles email classification and response dispatching."""

    def __init__(self, processor: EmailProcessor):
        """Initialize the automation system with an EmailProcessor."""
        self.processor = processor
        self.response_handlers = {
            "complaint": self._handle_complaint,
            "inquiry": self._handle_inquiry,
            "feedback": self._handle_feedback,
            "support_request": self._handle_support_request,
            "other": self._handle_other
        }

    def process_email(self, email: Dict) -> Dict:
        """Process a single email through classification and response generation."""
        try:
            email_class = self.processor.classify_email(email)
            if not email_class:
                return {"email_id": email["id"], "status": "FAIL", "classification": None,"groundtruth": email.get("class",None), "response_sent": None}

            response = self.processor.generate_response(email, email_class)
            handler = self.response_handlers.get(email_class, self._handle_other)

            handler(email, response)
            return {"email_id": email["id"], "status": "SUCCEEDED", "classification": email_class, "groundtruth": email.get("class",None),"response_sent": response}

        except Exception as e:
            logger.exception(f"Error processing email {email['id']}: {e}")
            return {"email_id": email["id"], "status": "FAIL", "classification": None,"groundtruth": email.get("class",None), "response_sent": None}

    # Handling functions
    def _handle_complaint(self, email: Dict, response: str):
        send_complaint_response(email["id"], response)

    def _handle_inquiry(self, email: Dict, response: str):
        send_standard_response(email["id"], response)

    def _handle_feedback(self, email: Dict, response: str):
        log_customer_feedback(email["id"], email["body"])

    def _handle_support_request(self, email: Dict, response: str):
        create_support_ticket(email["id"], email["body"])

    def _handle_other(self, email: Dict, response: str):
        send_standard_response(email["id"], response)
        send_to_human_review(email["id"], email["body"])


# Mock service functions (kept for demonstration)
def send_complaint_response(email_id: str, response: str):
    logger.info(f"Sending complaint response for email {email_id}")


def send_standard_response(email_id: str, response: str):
    logger.info(f"Sending standard response for email {email_id}")


def create_support_ticket(email_id: str, context: str):
    logger.info(f"Creating support ticket for email {email_id}")


def log_customer_feedback(email_id: str, feedback: str):
    logger.info(f"Logging feedback for email {email_id}")


def send_to_human_review(email_id: str, email_body: str):
    logger.info(f"Sending email {email_id} for human review")


def run_demonstration():
    """Run a demonstration of the email processing system."""
    processor = EmailProcessor()
    automation_system = EmailAutomationSystem(processor)

    results = []
    for email in sample_emails:
        logger.info(f"Processing email {email['id']}...")
        results.append(automation_system.process_email(email))

    # Create summary DataFrame
    df = pd.DataFrame(results)
    df.columns = ["email_id", "status", "classification","groundtruth", "response_sent"]

    print("\nProcessing Summary:")
    print(df[["email_id", "status", "classification","groundtruth", "response_sent"]])
    calculate_metrics(df)
    df.to_csv("data.csv", index=False)
    return df

# Run script if executed directly
if __name__ == "__main__":
    run_demonstration()
