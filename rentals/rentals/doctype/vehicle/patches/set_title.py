import frappe

def execute():
    vehicles = frappe.get_all("Vehicle", fields=["name", "make", "model", "year"])
    for vehicle in vehicles:
        title = f"{vehicle.make} {vehicle.model} {vehicle.year}"
        frappe.db.set_value("Vehicle", vehicle.name, "title", title)
