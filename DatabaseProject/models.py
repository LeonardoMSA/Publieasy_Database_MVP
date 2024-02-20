from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum

db = SQLAlchemy()

class Cliente(db.Model):
    __tablename__ = "Cliente"
    cnpj = db.Column(db.String(30), primary_key=True)
    nomeResponsavel = db.Column(db.String(50))
    telefoneContato = db.Column(db.String(40))
    emailContato = db.Column(db.String(50))
    nomeFantasia = db.Column(db.String(50))
    setor = db.Column(db.String(50), nullable=False)
    porte = db.Column(Enum('Micro', 'Pequena', 'Media', 'Grande'))
    origemLead = db.Column(db.String(100))
    zipCode = db.Column(db.String(40))
    descricao = db.Column(db.String(200))
    infoImportante = db.Column(db.String(100))
    comentarios = db.Column(db.String(200), nullable=False)
    situacao = db.Column(Enum('Não prospectado', 'Prospectado', 'Reunião marcada', 'Proposta enviada', 
                              'Proposta aceita', 'Proposta recusada', 'Sem retorno', 'Descartado', 
                              'Entrar em contato novamente', 'Contrato expirado', 'Fim de contrato'))

class Contrato(db.Model):
    __tablename__ = "Contrato"
    id_contrato = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tempoContrato = db.Column(db.Integer)
    dataInicio = db.Column(db.Date)
    qtdMotoristas = db.Column(db.Integer)
    descontoValor = db.Column(db.Numeric(4,2))
    formaPagamento = db.Column(db.String(30), nullable=False)
    parcelas = db.Column(db.Integer)
    descontoPercent = db.Column(db.Numeric(4,2))
    dataAssinado = db.Column(db.Date)
    qtdTrocaAnuncios = db.Column(db.Integer)
    contratoAtivo = db.Column(db.Boolean)
    valor = db.Column(db.Numeric(9,2))
    cnpj_cliente = db.Column(db.String(30), db.ForeignKey('Cliente.cnpj'))

class Anuncio(db.Model):
    __tablename__ = "Anuncio"
    id_anuncio = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(200))
    dataCriacao = db.Column(db.Date)
    dataUpdate = db.Column(db.Date)
    tipoProduto = db.Column(db.String(100), nullable=False)
    campoProduto = db.Column(db.String(100))
    promocao = db.Column(db.Boolean)
    promocaoExclusiva = db.Column(db.Boolean)
    cnpj_cliente = db.Column(db.String(30), db.ForeignKey('Cliente.cnpj'))
    id_contrato = db.Column(db.Integer, db.ForeignKey('Contrato.id_contrato'))

class Motorista(db.Model):
    __tablename__ = "Motorista"
    id_motoristas = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    placa = db.Column(db.String(20), nullable=False)
    meioPagamento = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50))
    telefoneContato = db.Column(db.String(40))
    nota = db.Column(db.Numeric(6,4))
    horasTrabalho = db.Column(db.Integer)
    turnos = db.Column(db.String(100), nullable=False)
    viagensDia = db.Column(db.Integer)
    modeloCarro = db.Column(db.String(40), nullable=False)
    corridas = db.Column(db.Integer)
    anosDeMotorista = db.Column(db.Numeric(4,2))
    ocupacaoUnica = db.Column(db.Boolean)
    dataNascimento = db.Column(db.Date)
    kilometragem = db.Column(db.Integer)
    categoriaApp = db.Column(Enum('black', 'comfort'))
    carroAlugado = db.Column(db.Boolean)
    observacao = db.Column(db.String(200))
    id_contrato = db.Column(db.Integer, db.ForeignKey('Contrato.id_contrato'))
    id_anuncio = db.Column(db.Integer, db.ForeignKey('Anuncio.id_anuncio'))

class Administrador(db.Model):
    __tablename__ = "Administrador"
    id_adm = db.Column(db.Integer, primary_key=True, autoincrement=True)
    senha = db.Column(db.String(50))
    usuario = db.Column(db.String(50))

class QRCode(db.Model):
    __tablename__ = "QRCode"
    id_qrcode = db.Column(db.Integer, primary_key=True, autoincrement=True)
    acessos_total = db.Column(db.Integer)
    acesso_unico = db.Column(db.Integer)
    id_anuncio = db.Column(db.Integer, db.ForeignKey('Anuncio.id_anuncio'))

class QrCode_Motorista(db.Model):
    __tablename__ = "QrCode_Motorista"
    id_qrcode_motorista = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_qrcode = db.Column(db.Integer, db.ForeignKey('QRCode.id_qrcode'))
    id_motorista = db.Column(db.Integer, db.ForeignKey('Motorista.id_motoristas'))

class Gastos(db.Model):
    __tablename__ = "Gastos"
    id_gastos = db.Column(db.Integer, primary_key=True, autoincrement=True)
    custoFixo = db.Column(db.Numeric(10,2))
    custoVariavel = db.Column(db.Numeric(10,2))
    despesaFixa = db.Column(db.Numeric(10,2))
    despesaVariavel = db.Column(db.Numeric(10,2))
    investimento = db.Column(db.Numeric(10,2))
    perda = db.Column(db.Numeric(10,2))
    extraordinario = db.Column(db.Numeric(10,2))
    impostos = db.Column(db.Numeric(10,2))

class Faturamento(db.Model):
    __tablename__ = "Faturamento"
    id_faturamento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    recebimentoFixo = db.Column(db.Numeric(10,2))
    recebimentoVariavel = db.Column(db.Numeric(10,2))
    doacao = db.Column(db.Numeric(10,2))
    aceleracao = db.Column(db.Numeric(10,2))
    investimentos = db.Column(db.Numeric(10,2))
    premios = db.Column(db.Numeric(10,2))
    extraordinarios = db.Column(db.Numeric(10,2))
    poupanca = db.Column(db.Numeric(10,2))

class Count(db.Model):

    __tablename__ = 'Count'

    id_count = db.Column(db.Integer, primary_key=True)
    accessCount = db.Column(db.Integer)

    def __init__(self, accessCount):
        self.id_count = 1
        self.accessCount = accessCount