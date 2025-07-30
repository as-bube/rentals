import frappe

def throw_error(doc, event):
    frappe.throw("This is a custom error message from the rentals app.")

def send_payment_reminders():
    pass