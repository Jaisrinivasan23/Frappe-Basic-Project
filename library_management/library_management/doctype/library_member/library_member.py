from frappe.model.document import Document
import frappe

class LibraryMember(Document):
    def validate(self):
        # Validate email address if provided
        if self.email_address:
            import re
            regex = r"^\S+@\S+\.\S+$"
            if not re.match(regex, self.email_address):
                frappe.throw("Invalid Email Address")
