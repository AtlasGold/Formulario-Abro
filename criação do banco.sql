
drop schema abro;

create schema abro;
use abro;
create table cadastro( 
`ID Paciente` int NOT NULL AUTO_INCREMENT,
`Nome` varchar(500) not null,
`Telefone` varchar(15) not null,
`CPF` varchar(14) null,
primary key (`ID Paciente`));

drop table `sociais`; 

CREATE TABLE IF NOT EXISTS `sociais` (
  `ID Paciente` INT NOT NULL AUTO_INCREMENT,
  `Qual sua profissão ?` VARCHAR(500) ,
  `Gosta de Futebol ?` VARCHAR(4),
  `Times que torce` VARCHAR(500) ,
  `Tem algum animal de estimação` VARCHAR(4),
  `Qual animal?` VARCHAR(500) ,
  `Tem filhos ?` VARCHAR(4),
  `Como se chamam ?` VARCHAR(500) ,
  `Tem medo de dentista ?` VARCHAR(4) ,
  `Esta Satisfeito Com Sua Estética Facil e de Sorriso ?` VARCHAR(4) ,
  `Tem Facebook` VARCHAR(4) ,
  `Tem Instagram ?` VARCHAR(4) ,
  `Qual instagram ?` VARCHAR(500) ,
  `Tem algum Hobby ?` VARCHAR(4) ,
  `Quais hobbies?` VARCHAR(500) ,
  `Gosta de música ambiente ?` VARCHAR(3) ,
  `Qual Gênero/Ritmo Gosta de Ouvir ?` VARCHAR(500) ,
  `Qual Tipo De Programa De Televisão Gosta De Assistir ?` VARCHAR(500) ,
  `Qual Gênero De Filme Gosta ?` VARCHAR(500) ,
  `CPF` VARCHAR(14) ,
  `Nome` VARCHAR(500) ,
  PRIMARY KEY (`ID Paciente`));
  
  drop table `anamnese1`;
  CREATE TABLE `anamnese1` (
  `Id Paciente` INT NOT NULL AUTO_INCREMENT,
  `Qual O Motivo Da Consulta` VARCHAR(500) NOT NULL,
  `Tratamento ou Problema de Saude` VARCHAR(4) NOT NULL,
  `Está Tomando Algum Medicamento` VARCHAR(4) NOT NULL,
  `Quais Medicamentos` VARCHAR(500),
  `Tem alergia a algum medicamento` VARCHAR(4) NOT NULL,
  `Apresenta Alergia a Quais Medicamentos` VARCHAR(500),
  `Teve Alguma Reação a Anestesia Local` VARCHAR(4) NOT NULL,
  `Quando Foi o Seu Ultimo Tratamento Odontologico` date NOT NULL,
  `Tratamento de Canal Protese Implante Perdeu um Dente` VARCHAR(4) NOT NULL,
  `Sua Gengiva Sangra Com Frequência` VARCHAR(4) NOT NULL,
  `Voce Fuma` VARCHAR(4) NOT NULL,
  `Quando Você se Corta Sangra Muito` VARCHAR(4) NOT NULL,
  `Dores de Dente Cabeça Face Ouvido Articulações` VARCHAR(4) NOT NULL,
  `Teve Algum Desmaio Ataques Nervoso Epilepsia ou Convulsoes` VARCHAR(4) NOT NULL,
  `Pode Estar Gravida` VARCHAR(3) NOT NULL,
  `Procedimento Facial Botox Preenchimento Hialurônico PMA` VARCHAR(4) NOT NULL,
  `CPF` VARCHAR(14) NOT NULL,
  `Nome` VARCHAR(500) NOT NULL,
  PRIMARY KEY (`ID Paciente`))

;
select * from cadastro, sociais, anamnese1;


select idpaciente,nome from cadastro;
use abro

