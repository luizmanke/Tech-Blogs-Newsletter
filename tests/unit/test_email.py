import os

import pytest

from tech_blogs_newsletter.notification import email


@pytest.fixture
def mock_sender_env_vars(mocker):
    mocker.patch.dict(
        os.environ,
        {
            "SENDER_EMAIL": "fake-sender@gmail.com",
            "SENDER_PASSWORD": "fake-password",
        },
    )


def test_send_email_should_send_message_to_the_receivers_list(
    mock_sender_env_vars,
    mocker,
):
    mocker.patch("smtplib.SMTP.login")
    sendmail_mock = mocker.patch("smtplib.SMTP.sendmail")

    email.send_email(
        receiver_emails=["fake-receiver@gmail.com"],
        html_message="fake message",
    )

    sendmail_mock.assert_called_once_with(
        "fake-sender@gmail.com",
        ["fake-receiver@gmail.com"],
        msg="""\
Content-Type: text/html; charset="us-ascii"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit

fake message\
"""
    )


def test_send_email_should_not_send_if_sender_email_and_password_are_not_defined(mocker):

    sendmail_mock = mocker.patch("smtplib.SMTP.sendmail")

    email.send_email(
        receiver_emails=[],
        html_message="fake message",
    )

    assert not sendmail_mock.called


def test_send_email_should_not_send_if_receivers_list_is_empty(
    mock_sender_env_vars,
    mocker,
):
    sendmail_mock = mocker.patch("smtplib.SMTP.sendmail")

    email.send_email(
        receiver_emails=[],
        html_message="fake message",
    )

    assert not sendmail_mock.called
