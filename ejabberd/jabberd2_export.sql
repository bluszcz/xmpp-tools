-- PostgreSQL 
COPY "authreg" TO '/tmp/jabberd2-export-authreg.csv' DELIMITER ',' CSV HEADER;
COPY "vcard" TO '/tmp/jabberd2-export-vcard.csv' DELIMITER ',' CSV HEADER;
COPY "roster-groups" TO '/tmp/jabberd2-export-roster-groups.csv' DELIMITER ',' CSV HEADER;
COPY "roster-items" TO '/tmp/jabberd2-export-roster-items.csv' DELIMITER ',' CSV HEADER;
