from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

bp = Blueprint('contact', __name__)


@bp.route('/contact', methods=['GET', 'POST'])
def contact_page():
    if request.method == 'POST':
        data = request.form

        name         = data.get('name', '').strip()
        phone        = data.get('phone', '').strip()
        email        = data.get('email', '').strip()
        province     = data.get('province', 'Not specified')
        enquiry_type = data.get('enquiry_type', 'Not specified')
        farm_size    = data.get('farm_size', 'Not specified')
        message_body = data.get('message', '').strip()

        if not name or not phone or not message_body or not enquiry_type:
            flash('Please fill in all required fields.', 'danger')
            return redirect(url_for('contact.contact_page'))

        email_body = f"""
New Contact Form Submission — AgroChemix Website

Name: {name}
Phone: {phone}
Email: {email or 'Not provided'}
Province: {province}
Enquiry Type: {enquiry_type}
Farm Size: {farm_size}

Message:
{message_body}
        """

        try:
            message = Mail(
                from_email=current_app.config['MAIL_DEFAULT_SENDER'],
                to_emails=current_app.config['MAIL_RECIPIENT'],
                subject=f"[AgroChemix Enquiry] {enquiry_type} — {name}",
                plain_text_content=email_body
            )

            if email:
                message.reply_to = email

            sg = SendGridAPIClient(current_app.config['SENDGRID_API_KEY'])
            response = sg.send(message)

            if response.status_code in [200, 202]:
                flash('Thank you! Your message has been sent successfully.', 'success')
            else:
                flash('Failed to send email. Please try again later.', 'danger')

        except Exception as e:
            current_app.logger.error(f"SendGrid Error: {e}")
            flash('Sorry, there was an error sending your message.', 'danger')

    return render_template('contact.html')
