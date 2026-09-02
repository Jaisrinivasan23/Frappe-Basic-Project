from frappe.model.document import Document
import frappe

class LibraryTransaction(Document):
    def validate(self):
        # Validate that the article is available before issuing
        if self.type == "Issue":
            article_status = frappe.db.get_value("Article", self.article, "status")
            if article_status == "Issued":
                frappe.throw(f"Article {self.article} is already issued.")
        
        # Validate return
        elif self.type == "Return":
            article_status = frappe.db.get_value("Article", self.article, "status")
            if article_status == "Available":
                frappe.throw(f"Article {self.article} is already available.")

    def on_submit(self):
        # Update the article status on submission
        if self.type == "Issue":
            frappe.db.set_value("Article", self.article, "status", "Issued")
        elif self.type == "Return":
            frappe.db.set_value("Article", self.article, "status", "Available")
            
    def before_cancel(self):
        # Revert the article status if transaction is cancelled
        if self.type == "Issue":
            frappe.db.set_value("Article", self.article, "status", "Available")
        elif self.type == "Return":
            frappe.db.set_value("Article", self.article, "status", "Issued")
