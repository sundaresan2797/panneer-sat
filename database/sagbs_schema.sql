-- SAGBS enquiry schema v1. Generated from app/services/sagbs_store.py.
-- Prefer python -m scripts.init_sagbs_db for repeatable initial setup.

CREATE TABLE sagbs_enquiries (
	id VARCHAR(36) NOT NULL, 
	submission_id VARCHAR(36) NOT NULL, 
	payload_hash VARCHAR(64) NOT NULL, 
	created_at TIMESTAMP WITH TIME ZONE NOT NULL, 
	kind VARCHAR(10) NOT NULL, 
	name VARCHAR(100) NOT NULL, 
	company_name VARCHAR(150) NOT NULL, 
	email VARCHAR(254) NOT NULL, 
	phone VARCHAR(25) NOT NULL, 
	country VARCHAR(100) NOT NULL, 
	service VARCHAR(100) NOT NULL, 
	engagement VARCHAR(20) NOT NULL, 
	budget VARCHAR(20) NOT NULL, 
	message TEXT NOT NULL, 
	consent_at TIMESTAMP WITH TIME ZONE NOT NULL, 
	notification_status VARCHAR(20) DEFAULT 'pending' NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (submission_id)
);

CREATE INDEX ix_sagbs_enquiries_created_at ON sagbs_enquiries (created_at);
