create table if not exists chronic_diseases
(
	icd_10 varchar,
	pathology_name varchar,
	is_chronic boolean,
	id serial not null
		constraint chronic_diseases_pk
			primary key
);

alter table chronic_diseases owner to gloth;

create unique index if not exists chronic_diseases_id_uindex
	on chronic_diseases (id);

create table if not exists classes
(
	name varchar,
	id serial not null
		constraint classes_pk
			primary key
);

alter table classes owner to gloth;

create unique index if not exists classes_id_uindex
	on classes (id);

create table if not exists classes_families
(
	molecule_id integer,
	class_id integer,
	family_name varchar,
	atc varchar
);

alter table classes_families owner to gloth;

create table if not exists dermocorticoids
(
	cis integer,
	medication_name varchar,
	potency varchar,
	id serial not null
		constraint dermocorticoids_pk
			primary key
);

alter table dermocorticoids owner to gloth;

create unique index if not exists dermocorticoids_id_uindex
	on dermocorticoids (id);

create table if not exists forms
(
	name varchar,
	id serial not null
		constraint forms_pk
			primary key
);

alter table forms owner to gloth;

create unique index if not exists forms_id_uindex
	on forms (id);

create table if not exists medication
(
	cis integer not null,
	name varchar,
	molecule_id integer
);

alter table medication owner to gloth;

create table if not exists medications_forms
(
	cis integer,
	medication_name varchar,
	form_name varchar,
	form_id integer
);

alter table medications_forms owner to gloth;

create table if not exists molecules
(
	name varchar,
	rcp varchar,
	rcp_sum varchar,
	id serial not null
		constraint molecules_pk
			primary key
);

alter table molecules owner to gloth;

create unique index if not exists molecules_id_uindex
	on molecules (id);

create table if not exists opiates
(
	potency varchar,
	id serial not null
		constraint opiates_pk
			primary key,
	molecule_id integer
);

alter table opiates owner to gloth;

create unique index if not exists opiates_id_uindex
	on opiates (id);

create table if not exists pathology
(
	id serial not null,
	name varchar not null,
	info varchar not null,
	has varchar,
	age_min integer not null,
	age_max integer not null,
	sex varchar not null,
	symptoms varchar not null,
	other_name varchar,
	norm_name varchar not null,
	rec_tests_string varchar,
	rec_tests bytea not null,
	created_on timestamp default now(),
	updated_by integer,
	updated_on timestamp default now(),
	user_id integer not null,
	treatment varchar,
	description varchar,
	icd_10 varchar,
	medic varchar
);

alter table pathology owner to gloth;

create table if not exists pathology_specialty
(
	id serial not null,
	pathology_id integer,
	specialty_id integer
);

alter table pathology_specialty owner to gloth;

create table if not exists patient
(
	id serial not null
		constraint patient_pk
			primary key,
	age integer,
	sex varchar,
	weight integer,
	height integer,
	symptoms varchar,
	bmi double precision,
	tests varchar,
	rec_tests bytea,
	user_id integer not null,
	created_on timestamp default now(),
	pathology_id integer not null,
	pathology_name varchar not null,
	updated_on timestamp default now(),
	updated_by integer,
	icd_10 varchar
);

alter table patient owner to gloth;

create unique index if not exists patient_user_id_uindex
	on patient (user_id);

create unique index if not exists patient_icd_10_uindex
	on patient (icd_10);

create table if not exists roles
(
	id serial not null,
	name varchar(50)
);

alter table roles owner to gloth;

create table if not exists specialty
(
	id serial not null,
	name varchar(50)
);

alter table specialty owner to gloth;

create table if not exists thesaurus
(
	molecule_id_1 integer,
	molecule_id_2 integer,
	remark varchar,
	interaction_level varchar,
	cis integer
);

alter table thesaurus owner to gloth;

create table if not exists treatment_cis
(
	icd_10 varchar,
	pathology_name varchar,
	cis integer
);

alter table treatment_cis owner to gloth;

create table if not exists treatment_class
(
	icd_10 varchar,
	pathology_name varchar,
	class_id integer
);

alter table treatment_class owner to gloth;

create table if not exists treatment_molecule
(
	icd_10 varchar,
	pathology_name varchar,
	molecule_id integer
);

alter table treatment_molecule owner to gloth;

create table if not exists "user"
(
	id serial not null,
	email varchar(50),
	rpps bigint,
	password varchar(100),
	name varchar(50) not null,
	forename varchar(50) not null,
	registered_on timestamp default now(),
	confirmed boolean not null,
	confirmed_on timestamp,
	entry_count_patient integer not null,
	entry_count_pathology integer not null,
	modify_count_patient integer not null,
	modify_count_pathology integer not null,
	phone varchar not null,
	zip_code varchar not null
);

alter table "user" owner to gloth;

create table if not exists user_roles
(
	id serial not null,
	user_id integer,
	role_id integer
);

alter table user_roles owner to gloth;

create table if not exists prescription
(
	id_prescription serial not null
		constraint prescription_pk
			primary key,
	cis_fk integer,
	id_patient_fk integer
		constraint prescription_patient_user_id_fk
			references patient (user_id),
	icd10_fk varchar
		constraint prescription_patient_icd_10_fk
			references patient (icd_10),
	nb_medicaments integer
);

alter table prescription owner to gloth;

create unique index if not exists prescription_id_prescription_uindex
	on prescription (id_prescription);

