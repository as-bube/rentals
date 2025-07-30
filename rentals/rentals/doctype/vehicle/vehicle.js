// Copyright (c) 2025, bube.dev and contributors
// For license information, please see license.txt

frappe.ui.form.on("Vehicle", {
	refresh(frm) {
        

	},
    getsummary(frm) {
        frm.get_field("summary").$wrapper.append(
            `
                <p class="alert alert-warning"> Your library membership is about to expire !    </p>`)
    }

});
