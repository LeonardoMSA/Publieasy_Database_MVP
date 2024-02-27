USE Publieasy;

CREATE TABLE Cliente(
cnpj varchar(30) NOT NULL,
nomeResponsavel varchar(50),
telefoneContato varchar(40),
emailContato varchar(50),
nomeFantasia varchar(50),
setor varchar(50) NOT NULL,
porte ENUM('Micro', 'Pequena', 'Media', 'Grande'),
origemLead varchar(100),
zipCode varchar(40),
descricao varchar(200),
infoImportante varchar(100),
comentarios varchar(200) NOT NULL,
situacao ENUM('Não prospectado', 'Prospectado', 'Reunião marcada', 'Proposta enviada', 'Proposta aceita', 
'Proposta recusada', 'Sem retorno', 'Descartado', 'Entrar em contato novamente', 'Contrato expirado', 'Fim de contrato'),
CONSTRAINT cliente_pk PRIMARY KEY (cnpj)
);

CREATE TABLE Contrato(
id_contrato int AUTO_INCREMENT,
tempoContrato int,
dataInicio date,
qtdMotoristas int,
descontoValor decimal(4,2),
formaPagamento varchar(30) NOT NULL,
parcelas int,
descontoPercent decimal(4,2),
dataAssinado date,
qtdTrocaAnuncios int,
contratoAtivo Boolean,
valor decimal(9,2),
cnpj_cliente varchar(30) NOT NULL,
CONSTRAINT contrato_pk PRIMARY KEY (id_contrato),
CONSTRAINT cnpj_fk_contrato FOREIGN KEY (cnpj_cliente) REFERENCES Cliente (cnpj)
);

CREATE TABLE Anuncio(
id_anuncio int AUTO_INCREMENT,
url varchar(200),
dataCriacao date,
dataUpdate date,
tipoProduto varchar(100) NOT NULL,
campoProduto varchar(100),
promocao boolean,
promocaoExclusiva boolean,
cnpj_cliente varchar(30) NOT NULL,
id_contrato int,
CONSTRAINT anuncio_pk PRIMARY KEY (id_anuncio),
CONSTRAINT id_contrato_fk FOREIGN KEY (id_contrato) REFERENCES Contrato (id_contrato),
CONSTRAINT cnpj_fk_anuncio FOREIGN KEY (cnpj_cliente) REFERENCES Cliente (cnpj)
);


CREATE TABLE Motorista(
id_motoristas int AUTO_INCREMENT,
nome varchar(50) NOT NULL,
placa varchar(20) NOT NULL,
meioPagamento varchar(20) NOT NULL,
email varchar(50),
telefoneContato varchar(40),
nota decimal(6,4),
horasTrabalho int,
turnos varchar(100) NOT NULL,
viagensDia int,
modeloCarro varchar(40) NOT NULL,
corridas int,
anosDeMotorista decimal(4,2),
ocupacaoUnica boolean,
dataNascimento DATE,
kilometragem int,
categoriaApp ENUM('black', 'comfort'),
carroAlugado boolean,
observacao varchar(200),
id_contrato int,
id_anuncio int,
CONSTRAINT motorista_pk PRIMARY KEY (id_motoristas),
CONSTRAINT id_contrato_fk_motoristas FOREIGN KEY (id_contrato) REFERENCES Contrato (id_contrato),
CONSTRAINT id_anuncio_fk_motoristas FOREIGN KEY (id_anuncio) REFERENCES Anuncio (id_anuncio)
);


CREATE TABLE Administrador(
id_adm int AUTO_INCREMENT,
senha varchar(50),
usuario varchar(50),
CONSTRAINT administrador_pk PRIMARY KEY (id_adm)
);


CREATE TABLE QRCode(
id_qrcode int AUTO_INCREMENT,
acessos_total int,
acesso_unico int,
id_anuncio int,
CONSTRAINT qrcode_pk PRIMARY KEY (id_qrcode),
CONSTRAINT id_anuncio_fk_qr FOREIGN KEY (id_anuncio) REFERENCES Anuncio (id_anuncio)
);

CREATE TABLE QrCode_Motorista(
id_qrcode_motorista int AUTO_INCREMENT,
id_qrcode int,
id_motorista int,
CONSTRAINT qrcode_motorista_pk PRIMARY KEY (id_qrcode_motorista),
CONSTRAINT id_qrcode_fk_qrcode_motorista FOREIGN KEY (id_qrcode) REFERENCES QRCode (id_qrcode),
CONSTRAINT id_motorista_fk_qrcode_motorista FOREIGN KEY (id_motorista) REFERENCES Motorista (id_motoristas)
);

CREATE TABLE Gastos(
id_gastos int AUTO_INCREMENT,
custoFixo decimal (10,2),
custoVariavel decimal (10,2),
despesaFixa decimal (10,2),
despesaVariavel decimal (10,2),
investimento decimal (10,2),
perda decimal (10,2),
extraordinario  decimal(10,2),
impostos decimal (10,2),
CONSTRAINT gastos_pk PRIMARY KEY (id_gastos)
);

CREATE TABLE Faturamento(
id_faturamento int AUTO_INCREMENT,
recebimentoFixo decimal (10,2),
recebimentoVariavel decimal (10,2),
doacao decimal (10,2),
aceleracao decimal (10,2),
investimentos decimal (10,2),
premios decimal (10,2), 
extraordinarios decimal (10,2),
poupanca decimal (10,2),
CONSTRAINT faturamento_pk PRIMARY KEY (id_faturamento)
);

CREATE TABLE `Count`(
  id_count int,
  accessCount int,
  CONSTRAINT count_pk PRIMARY KEY (id_count)
);

CREATE TABLE users(
    username varchar(15) NOT NULL PRIMARY KEY,
    email varchar(30),
    password varchar(30) NOT NULL
);