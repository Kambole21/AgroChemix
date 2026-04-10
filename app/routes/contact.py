from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from flask_mail import Message

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

        # Basic validation
        if not name or not phone or not message_body or not enquiry_type:
            flash('Please fill in all required fields.', 'danger')
            return redirect(url_for('contact.contact_page'))

        # Build the email body
        email_body = f"""
New Contact Form Submission — AgroChemix Website
=================================================

Name:         {name}
Phone:        {phone}
Email:        {email or 'Not provided'}
Province:     {province}
Enquiry Type: {enquiry_type}
Farm Size:    {farm_size}

Message:
{message_body}
        """.strip()

        try:
            # Get the mail instance from current_app extensions
            mail = current_app.extensions.get('mail')
            if not mail:
                # Fallback: create a new mail instance (though this shouldn't happen)
                from flask_mail import Mail
                mail = Mail()
                mail.init_app(current_app)
            
            # Verify configuration is present
            if not current_app.config.get('MAIL_USERNAME') or not current_app.config.get('MAIL_PASSWORD'):
                flash('Mail configuration is incomplete. Please contact support.', 'danger')
                return redirect(url_for('contact.contact_page'))
            
            msg = Message(
                subject=f"[AgroChemix Enquiry] {enquiry_type} — {name}",
                sender=current_app.config['MAIL_DEFAULT_SENDER'],
                recipients=[current_app.config['MAIL_RECIPIENT']],  
                body=email_body,
                reply_to=email if email else None,
            )
            mail.send(msg)
            flash('Thank you! Your message has been sent. We will get back to you within 24 hours.', 'success')
        except Exception as e:
            current_app.logger.error(f"Mail send error: {e}")
            # Provide a user-friendly message instead of debug info
            flash('Sorry, there was an error sending your message. Please try again later or contact us directly via phone.', 'danger')
            if current_app.debug:
                # Only show debug info in development
                flash(f'Debug: {str(e)}', 'warning')

    return render_template('contact.html')