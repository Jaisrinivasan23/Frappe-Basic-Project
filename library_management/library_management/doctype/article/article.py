from frappe.model.document import Document
import frappe

class Article(Document):
    def before_save(self):
        # Example before_save hook: strip trailing whitespaces
        if self.article_name:
            self.article_name = self.article_name.strip()
