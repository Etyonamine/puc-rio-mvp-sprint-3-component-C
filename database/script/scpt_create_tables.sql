CREATE TABLE MARCA(
cod_marca INTEGER PRIMARY KEY,
nom_marca VARCHAR(100) NOT NULL,
UNIQUE (nom_marca)

);

CREATE TABLE MODELO(
cod_modelo INTEGER PRIMARY KEY, 
des_modelo VARCHAR(100) NOT NULL,
cod_marca INT NOT NULL,
FOREIGN KEY (cod_marca) REFERENCES MARCA (cod_marca) ON DELETE CASCADE ON UPDATE CASCADE
); 

CREATE TABLE "cores" (
	"id_cor"	INTEGER,
	"nom_cor"	TEXT,
	PRIMARY KEY("id_cor")
)

CREATE TABLE "veiculo" (
	"pk_veiculo"	INTEGER NOT NULL,
	"des_placa"	VARCHAR(100),
	"cod_modelo"	INTEGER NOT NULL,
	"id_cor"	INTEGER,
	PRIMARY KEY("pk_veiculo"),
	UNIQUE("des_placa"),
	FOREIGN KEY("cod_modelo") REFERENCES "modelo"("pk_modelo"),
	FOREIGN KEY("id_cor") REFERENCES "cor"("id_cor")
);