import frappe

@frappe.whitelist(allow_guest=True)
def get_all_articles():
    # Example of get_all
    articles = frappe.get_all("Article", fields=["name", "article_name", "status"])
    return articles

@frappe.whitelist()
def get_available_articles():
    # Example of get_list
    articles = frappe.get_list("Article", filters={"status": "Available"}, fields=["name", "article_name"])
    return articles

@frappe.whitelist()
def issue_article(article_name, member_name):
    # Enqueue a background job for processing
    frappe.enqueue(
        'library_management.tasks.process_issue',
        queue='default',
        article=article_name,
        member=member_name
    )
    return {"status": "Job Enqueued"}
