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

        html_content = f"""
        <html>
        <body style="font-family: Arial, sans-serif; background:#f4f6f8; padding:20px;">
            <div style="max-width:800px; margin:auto; background:white; padding:20px; border-radius:8px;">

                <div><img src="https://agrochemix.net/static/icons/agro_logo.jpeg" alt="AgroChemix Logo" style="width:120px; height:130px; display:block; margin:auto;"></div>
                
                <h2 style="color:#2e7d32;" class"border-bottom">New Customer Enquiry</h2>
                
                <p><strong>Name:</strong> {name}</p>
                <p><strong>Phone:</strong> {phone}</p>
                <p><strong>Email:</strong> {email or 'Not provided'}</p>
                <p><strong>Province:</strong> {province}</p>
                <p><strong>Enquiry Type:</strong> {enquiry_type}</p>
                <p><strong>Farm Size:</strong> {farm_size}</p>

                <hr>

                <h3 style="color:#444;" class"bg-gray text-muted">Message</h3>
                <p style="line-height:1.6; font-size:400;">{message_body}</p>

                <hr>

                <p style="font-size:12px; color:#888;">
                    This message was sent from the https://agrochemix.net/contact.
                </p>
            </div>
        </body>
        </html>
        """


        try:
            message = Mail(
                from_email=current_app.config['MAIL_DEFAULT_SENDER'],
                to_emails=current_app.config['MAIL_RECIPIENT'],
                subject=f"[AgroChemix Enquiry] {enquiry_type} — {name}",
                html_content=html_content
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
