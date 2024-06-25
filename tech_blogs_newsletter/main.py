import os
from typing import List

from tech_blogs_newsletter.domain import Newsletter
from tech_blogs_newsletter.notification.email import send_email
from tech_blogs_newsletter.tech_blogs.airbnb import Airbnb
from tech_blogs_newsletter.tech_blogs.mercado_livre import MercadoLivre
from tech_blogs_newsletter.tech_blogs.netflix import Netflix


TECH_BLOGS = [
    Airbnb(),
    MercadoLivre(),
    Netflix(),
]


def search_new_tech_blogs(max_days_since_publication: int = 7) -> Newsletter:

    newsletter = Newsletter()
    for tech_blog in TECH_BLOGS:
        newsletter.add_blog(
            blog_name=tech_blog.name,
            blog=tech_blog.get_blog()
        )

    newsletter.filter_by_publication_date(max_days_since_publication)

    send_email(
        receiver_emails=_get_receiver_emails(),
        html_message=newsletter.to_html(),
    )

    return newsletter


def _get_receiver_emails() -> List[str]:
    receiver_emails_str = os.environ.get("RECEIVER_EMAILS", "")
    receiver_emails = receiver_emails_str.split(",")
    receiver_emails = [email.strip() for email in receiver_emails]
    return receiver_emails


if __name__ == "__main__":
    search_new_tech_blogs()
