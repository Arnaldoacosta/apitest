
CREATE SEQUENCE notamateria_notamateria_id_seq;
CREATE TABLE notamateria (
    notamateria_id integer NOT NULL DEFAULT nextval('notamateria_notamateria_id_seq'),
    alumno_fk integer,
    nombremateria varchar(100),
    notafinal integer
    
);


ALTER TABLE notamateria
  ADD CONSTRAINT notamateria_notamateria_id_pk 
    PRIMARY KEY (notamateria_id);


ALTER SEQUENCE notamateria_notamateria_id_seq OWNED BY notamateria.notamateria_id;
