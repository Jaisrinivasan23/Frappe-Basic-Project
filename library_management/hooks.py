
app_name = "library_management"
app_title = "Library Management"
app_publisher = "Aerele"
app_description = "A sample library management system."
app_email = "test@example.com"
app_license = "mit"

scheduler_events = {
    "daily": [
        "library_management.tasks.send_due_reminders"
    ]
}
