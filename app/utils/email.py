import resend
import os
from dotenv import load_dotenv

load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")


def send_welcome_email(to_email: str, fullname: str):
    resend.Emails.send({
        "from": "Mosa <onboarding@resend.dev>",
        "to": "chalatsethabo@gmail.com",
        "subject": "Welcome to Mosa!",
        "html": f"""
            <h1>Welcome {fullname}!</h1>
            <p>Thank you for signing up to Mosa.</p>
            <p>You can now start donating to schools in need.</p>
        """
    })


def send_school_verification_email(email: str, name: str):
    try:
        print("Sending email to:", email)
        response = resend.Emails.send({
            "from": "Mosa <onboarding@resend.dev>",
            "to": "chalatsethabo@gmail.com",
            "subject": "Your school has been verified on Mosa",
            "html": f"""
                <h1>Congratulations {name}!</h1>
                <p>Your school has been successfully added and verified on Mosa.</p>
                <p>You can now start receiving donations.</p>
            """
        })
        print("Email response:", response)
    except Exception as e:
        print("Email error:", e)