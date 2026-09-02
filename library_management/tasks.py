import frappe
from frappe.utils import today, add_days

def process_issue(article, member):
    # Example task run via enqueue
    frappe.logger().info(f"Processing issue of {article} for {member}")
    doc = frappe.get_doc({
        "doctype": "Library Transaction",
        "article": article,
        "library_member": member,
        "type": "Issue",
        "date": today()
    })
    doc.insert(ignore_permissions=True)
    doc.submit()

def send_due_reminders():
    # Example scheduler task using frappe.sendmail
    transactions = frappe.get_list("Library Transaction", filters={
        "type": "Issue",
        "docstatus": 1
    }, fields=["name", "library_member", "article", "date"])
    
    for t in transactions:
        member_email = frappe.db.get_value("Library Member", t.library_member, "email_address")
        if member_email:
            frappe.sendmail(
                recipients=[member_email],
                subject="Reminder: Article Return Due",
                message=f"Please return the article {t.article}."
            )
